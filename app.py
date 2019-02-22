#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('1NCFjtzWjkieeW0FPyF0DUzwLtJ+kfd+rtoqFRygSlPaN8NItmXbXLfXtcvIFfLGWOClsROt8sM12WF2MlKPi+5Au8r02oEYhfMst6i1/JD49uVUK3pvyjgymAHKp5nK6rrBaGoyPeyLPTzr3yR22AdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('b3e87cdfd2933b788e37630eb79c7949')



@app.route("/", methods=['POST'])
def index():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text==u"==":
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(u"2017年底終於有人知道==不要加空格"))
    else:
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(text=event.message.text))

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
