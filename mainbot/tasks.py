import logging
import asyncio
import aiohttp
from celery import shared_task
from django.conf import settings
from linebot import LineBotApi
from linebot.models import FlexSendMessage
from account.models import Account
from mainbot.utils.message_template import vocabulary_card
from mainbot.utils.chatgpt_processor import generate_response

logger = logging.getLogger(settings.LOG_VERSION)

def request_vocabulary_api(session):
    url = f"{settings.VOCABULARY_HOST}/api/vocabulary/"
    return session.get(url)

async def get_vocabularies():
    async with aiohttp.ClientSession() as session:
        tasks = []
        vocabulary_list = []
        en_words = ""

        for _ in range(3):
            tasks.append(request_vocabulary_api(session))

        results = await asyncio.gather(*tasks)

        for result in results:
            res_json = await result.json()

            en_words += f"'{res_json[0]['en_word']}',"

            vocabulary_list.append((
                res_json[0]["en_word"],
                res_json[0]["cn_word"],
                res_json[0]["example"]
            ))

        en_words = en_words.rstrip(",")

    return vocabulary_list, en_words

@shared_task
def send_vocabulary():
    try:
        line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

        vocabulary_list, en_words = asyncio.run(get_vocabularies())

        example = generate_response(f"{settings.CHATGPT_PROMPT_EXAMPLE} : {en_words}")
        translation = generate_response(f"{settings.CHATGPT_PROMPT_TRANSLATION} : {example}")

        message_card = FlexSendMessage(
            alt_text="New Vocabulary",
            contents=vocabulary_card(vocabulary_list, example, translation)
        )

        users_id = Account.objects.all().values_list("user_id", flat=True)

        for user_id in users_id:
            logger.debug(f"USER ID : {user_id}")
            line_bot_api.push_message(user_id, message_card)

    except Exception as exception_message:
        logger.exception(exception_message)