import logging
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseBadRequest
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import FollowEvent, UnfollowEvent, MessageEvent, TextMessage
from account.models import Account

logger = logging.getLogger(settings.LOG_VERSION)
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(settings.LINE_CHANNEL_SECRET)

@csrf_exempt
def callback(request):
    if request.method == "POST":
        signature = request.META["HTTP_X_LINE_SIGNATURE"]
        body = request.body.decode("utf-8")
        logger.info(body)
        try:
            handler.handle(body, signature)

        except InvalidSignatureError:
            logger.exception("Invalid signature.\nPlease check your channel access token/channel secret.")
            return HttpResponseBadRequest()
        
    return HttpResponse('OK')

@handler.add(FollowEvent)
def handleFollow(event):
    try:
        user_profile = line_bot_api.get_profile(event.source.user_id)
        account, created = Account.objects.get_or_create(user_id=event.source.user_id)

        if created:
            account.username = user_profile.display_name
            account.user_profile_pic = user_profile.picture_url
            account.user_language = user_profile.language

        account.is_active = True
        account.save()

    except Exception as exception_message:
        logger.exception(exception_message)

@handler.add(UnfollowEvent)
def handleUnFollow(event):
    try:
        account = Account.objects.filter(user_id=event.source.user_id).first()
        account.is_active = False
        account.save()

    except Exception as exception_message:
        logger.exception(exception_message)

@handler.add(MessageEvent)
def handleMessage(event):
    try:
        line_bot_api.reply_message(event.reply_token, TextMessage(text="Shut Up !"))

    except Exception as exception_message:
        logger.exception(exception_message)