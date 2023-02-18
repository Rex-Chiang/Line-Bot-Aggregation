import logging
import requests
from celery import shared_task
from django.conf import settings
from linebot import LineBotApi
from linebot.models import FlexSendMessage
from account.models import Account
from mainbot.utils.message_template import vocabulary_card

logger = logging.getLogger(settings.LOG_VERSION)

@shared_task
def send_vocabulary():
    vocabulary_list = []
    url = f"{settings.VOCABULARY_HOST}/api/vocabulary/"

    for _ in range(3):
        res = requests.get(url).json()[0]

        logger.debug(f"RESULT : {res}")

        vocabulary_list.append((res["english_word"], res["chinese_word"], res["example"]))

    users_id = Account.objects.all().values_list("user_id", flat=True)
    logger.debug(f"USERS ID : {users_id}")

    message_card = FlexSendMessage(alt_text="New Vocabulary", contents=vocabulary_card(vocabulary_list))
    line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

    for user_id in users_id:
        line_bot_api.push_message(user_id, message_card)
