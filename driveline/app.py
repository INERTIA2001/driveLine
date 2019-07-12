import errno
import os
import tempfile
from mr import Morse
from tranlaste import Translate
from decouple import config
from flask import (Flask, request, abort)
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import InvalidSignatureError
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,AudioMessage,AudioSendMessage)
app = Flask(__name__)
line_bot_api = LineBotApi(config("LINE_CHANNEL_ACCESS_TOKEN",default=os.environ.get('LINE_ACCESS_TOKEN')))
handler = WebhookHandler(config("LINE_CHANNEL_SECRET",default=os.environ.get('LINE_CHANNEL_SECRET')))
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
def make_static_tmp_dir():
    try:
        os.makedirs(static_tmp_path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(static_tmp_path):
            pass
        else:
            raise
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']   
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    text = event.message.text
    if text.split()[0] == "/Trans":
        source = text.split()[1]
        to = text.split()[2]
        word = text[13:]
        word = Translate(target=to,string=word,source=source)
        try:
            res = word.getOutput()
            line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=res))
        except KeyError:
            line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="please try using the ISO lang code\nThank you!!"))
    elif text.split()[0] == "/Morse":
        string = text[7:]
        s = Morse(string=string)
        if s.string[0] == "." or s.string[0] == "_":
            result = s.translateFromMorse(string=string)
        else:
            result = s.translate(string=string)
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=result))
    elif text.split()[0] == "/help":
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="more features is coming soon!\ntry this!\n/Trans (from) (to) (input)\nfor ex:- /Trans en id hello!\n/Morse (input)"))
    else:
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="type /help my friend!"))
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
