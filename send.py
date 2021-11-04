#! /opt/alt/python37/bin/python3.7
# -*- coding: utf-8 -*-

import random
import requests
import cgi
import os
# from geolite2 import geolite2


# 参考サイト
# ・PythonでLINEにメッセージを送る：https://qiita.com/moriita/items/5b199ac6b14ceaa4f7c9
# ・Python CGIでアクセス情報取得：https://webings.net/python/referer/
# ・パラメータ一覧：https://www.futomi.com/lecture/env_var/index.html
# ・IPアドレスから位置情報取得：https://euniclus.com/article/get-location-information/


# LINEメッセージ送信（ここから）
class LINENotifyBot:
    API_URL = 'https://notify-api.line.me/api/notify'
    def __init__(self, access_token):
        self.__headers = {'Authorization': 'Bearer ' + access_token}

    def send(
            self, message,
            image=None, sticker_package_id=None, sticker_id=None,
            ):
        payload = {
            'message': message,
            'stickerPackageId': sticker_package_id,
            'stickerId': sticker_id,
            }
        files = {}
        if image != None:
            files = {'imageFile': open(image, 'rb')}
        r = requests.post(
            LINENotifyBot.API_URL,
            headers=self.__headers,
            data=payload,
            files=files,
            )


# 絵文字一覧：https://note.com/kawatyanlife/n/ndf5e32d8dcd6
emoji=["✨","😊","☺️","💦","‼️","😅","❗️","😭","💕","❤️","😂","⭐️","👍","♂","♀","🙇","😌","😆","▶️","👋","💖","😁","✅","🤔","🤣","⁉️","🔥","🥺","🍀","🙏","❣️","🌟","😢","☀️","🌈","🏻","✌️","🎵","💪","♥️","⬇️","🥰","🌸","👇","😃","🤗","🙌","😱","😄","😉","💓","❓","👏","😍","👀","🎉","😳","😋","💡","🎶","🌱","💛","✳️","🌙","✖️","➡️","😓","😇","🙆","💧","☕️","🍎","😀","🙄","✍️","💢","😎","✔️","🧡","✋️","🌻","🌷","🐶","💫","⚡️","⚠️","💗","🙋","🌞","🌼","◼️","🍇","💁","🐾","®","💨","💭","📚","☝️","👌","✴️","✏️","😥","😣","🎯","😏","😪","😤","🍰","✂️","🤤","🥳","🌿","📝","🐰","😞","⏬","🍁","💙","😨","📖","✊️","💞","☔️","🎁","🏃","🙂","🏼","😝","😰","⤴️","🐈","❕","☁️","🐟","💰","🕊","👉","⚫️","💤","🧘","◾️","💐","😔","📷","🎊","😴","😵","©","🇺","㊗️","😫","🐥","👨","™","🎈","🍚","🌺","👊","🐕","👼","😡","🎂","📸","👩","🍓","⤵️","🥕","💌","😚","❌","😘","🍺","✈️","▪️","💚","👶","👆","🚶","💥","🐦","🍻","🙃","🌕","♨️","🍑","🍂","🐱","💮","🐚","🦀","☑️","🤦","🍃","⬆️","🍞","⭕️","🌊","💻","🙅","😲","🍋","🇦","🍜","🧐","🔸","🏇","🌹","🍙","◀️","📅","🌏","🍛","🎮","💜","💍","😩","♦️","🔬","📻","🎨","💎","🖐","🧸","😜","🍅","🌝","🍴","⚔️","🦙","😑","🌀","♻️","🧀","🐣","🌾","🍵","🎐","🚗","🍨","✉️","🌰","🤸","🥚","🔚","🍣","👗","🥀","🍒","🎃","🐴","🍊","😮","🐯","🤞","📣","🥣","🤍","🌠","😖","🎀","📕","🇵","💔","🎤","🥝","🚃","🉐","🍮","☘️","🐻","⚪️","🎸","⛩","🔁","🙈","🇸","🍏","👧","😸","🍽","😯","〰","😙","🍳","🍫","🍹","🍐","🌃","🇯","🔻","🍕","🥗","🍌","😷","😿","🕺","❔","🏫","💼","📺","🍩","🇹","💩","🍠","🐢","🍬","💯","⚽️","🦋","💝","👦","🍖","🧚","🌴","🤷","🍷","🐷","🍄","🤙","🌄","🇮","🤓","😺","🏋","🇳","📱","🥔","😠","🍈","🤳","🚲","👻","🇷","🦍","🍟","🏠","💟","🐤","🥴","😻","🐧","🍔","👑","🖤","🇫","😶","🖋","🐼","↔️","💃","💸","🇨","🥐","🏄","🐓","🐿","🐸","🐙","🧠","🐝","➕","☠️","☪️","🐔","🚤","🥶","🍱","🥱","🔍","❄️","🍥","🀄️","🚌","🦄","🥇","🥞","🥤","🌂","🤏","👐","😹","㊙️","🏆","🦌","🍪","💉","💋","🌍","⚾️","♣️","👬","🚀","🍝","🦦","💣","😽","🍆","♠️","👹","🦖","👎","🦐","🥑","🏵","🏡","👈","☎️","😛","⚕","🐉","💊","👵","🌤","🧁","❇️","🍶","👪","🎣","🥯","🌲","🌳","🏥","🏝","🎥","🦊","👽","🐘","🌛","🍡","🚙","☂️","💘","🗓","🧙","🍲","🌜","🐬","🐎","😈","🎾","🔰","🍧","📹","🐠","🏊","🗻","🐹","🎹","🧒","👁","🍼","◻️","📒","🦜","🎑","😟","☹️","🏕","🍘","🌽","🍗","🍤","🍦","🦑","🥖","😗","🥮","🚴","🤚","📞","🇰","👂","💇","👣","💅","🐇","🇬","🌆","🛌","🥵","🦷","🐡","🥟","😧","🔳","🎷","🧹","🥦","🏽","🏀","🏅","🥜","🌪","⚓️","🆖","🇪","🥂","🎧","📘","🔖","🦠","🎓","🌶","📲","🚩","♾","☯️","🥩","💈","🍉","🐄","🦧","🦒","↘️","🏘","🥊","↗️","🎙","👸","🤧","🌵","💴","🍢","🦵","🙀","🐜","☃️","😐","🦥","🎡","🥢","🚕","🐭","👮","🇭","🥛","🏨","🙍","🥓","📗","🤝","🤢","🚻","🔪","🌐","🔽","🃏","🍍","👓","🥈","🤑","🔎","⌚️","💀","🎬","🗒","🎞","😦","👭","🥒","🛀","🦆","⬛️","🖼","🐮","🦪","🧅","🇲","🔹","💠","📦","🤘","🍾","🗿","🚿","🦔","👕","🦢","▫️","🚏","😒","🤰","🍸","⚙️","⏰","🐒","🛁","🐞","🔮","✒️","🛣","🕰","🕷","🔵","💬","🛵","🚢","📔","⬅️","🇧","🤜","🏍","🆗","👾","🥬","🎩","😕","🏖","🧑","🔶","🏁","🔯","♓️","👖","🦲","🛏","⛅️","🇾","🔔","🕯","⌛️","🔄","🐲","💄","👫","➗","🧲","🆚","🎄","⏱","🐨","👃","🥪","🎺","🧖","🍯","🏳","🚬","🎰","✡️","🎌","⏩","🤛","🦁","🌧","🌩","⛰","🐛","🚪","🐋","🦩","♎️","🟦","🏐","🏰","💿","🇩","🔑","🌑","🏔","🗣","📍","🖊","🌇","👿","🗼","👴","🕴","👰","🧈","⛴","🙎","🇱","🍭","🚣","🧳","☄️","♑️","🟡","🥧","⛳️","🦞","👯","🦈","🔗","🚘","📆","🤎","🚒","🚨","🏪","🦮","🛫","🚺","🧊","🌎","🦛","👛","⛺️","🙁","🚂","🐽","⬜️","💵","➖","🏢","♋️","👺","🔨","🔴","🟢","🛍","🐖","🎪","🐐","🐑","😾","👠","🧂","🌋","🧶","👅","🔅","🏭","🌌","🐳","🎠","🤿","🚑","🧟","🏾","⏳","🌔","🥭","🪐","💒","🧱","🌖","🏞","🙊","↪️","🚚","📙","🟩","🌉","🌅","📊","🚓","🧽","😬","🐏","🔺","🗾","🎗","📈","🎲","🦳","🐩","🤖","🐵","⛵️","🅱️","🎒","🦎","⛄️","🖕","🩹","👄","👚","🏂","🐍","🚅","👳","🧉","🈵","♒️","🔌","🖖","📃","🚹","🏩","🗺","🕸","🎇","🎳","🎢","📎","😼","💑","🐁","🖌","🛐","📯","🌒","🛹","👜","👝","🛳","♈️","♊️","♍️","🦉","⚖️","🦰","🎫","⛪️","🎆","🤼","♿️","🗝","🌭","🇼","🧄","🚞","🦕","🟪","🧩","🛒","📡","🟥","🟨","🏌","🥃","🏓","🐫","🔋","🔆","🥉","🖥","🕵","🤠","🧛","🐅","➿","🩺","🚆","🌬","🔊","🌚","⛑","🧼","⛈","👱","🛡","🔼","📓","💆","➰","↙️","🔘","🐗","🅰️","🚋","🖍","🧔","🔫","🛑","🦱","🎏","📳","🌡","🚛","🥿","🎻","🏮","📩","🥠","⏫","♟","🙉","🦴","📄","🧺","🏎","🧥","🛥","♉️","♌️","🚦","🧭","⏲","⛲️","🧞","🚉","🐀","📀","🛰","🎿","🐊","🎟","⚰️","🤹","🐃","🈂","🎼","🧍","🥡","🔙","📁","🥾","🗑","🟧","🎋","🚇","🦽","🩸","🛎","🏑","📽","👙","🕐","🥄","⛏","🗯","🦅","🪓","📮","🏹","🦂","🏛","🌥","🏧","🦡","🕶","🆎","🖇","🥁","🌯","🧗","🏈","🏦","🔷","🈹","🚧","👞","🦹","🆙","🎴","💶","💷","🧆","🦾","♐️","📑","🤡","🧏","🥋","🌦","🚔","🛋","🧜","🤵","🦸","🎽","🛩","⚜️","🧫","🔒","🏙","🦗","🕒","⛱","🌓","🌗","🌘","📥","🔭 〽️","🔞","🕳","🈚️","🚄","🐂","👘","🚭","🗽","☸️","🚽","🐺","🎖","🍿","🕙","⛽️","🇻","🥙","↩️","🛸","🤒","🧵","🚰","🤕","🚁","📢","🪂","🏴","🤐","🏯","👡","↕️","🚮","🛬","❎","↖️","🧪","🔈","📧","📰","🆓"]


try:
    # パラメータ取得
    form = cgi.FieldStorage()
    sendtext = str(form.getvalue('text', ''))

    # 文字列が空の場合は絵文字を送る
    if(len(sendtext)==0):
        for i in range(10):
            index=random.randint(0, len(emoji)-1)
            sendtext=sendtext+emoji[index]

    # # ブラウザ・OS情報を取得
    # try:
    #     r_HTTP_USER_AGENT = os.environ['HTTP_USER_AGENT']
    # except:
    #     r_HTTP_USER_AGENT="不明"

    # # IPアドレスを取得
    # try:
    #     r_REMOTE_ADDR = os.environ['REMOTE_ADDR']
    # except :
    #     r_REMOTE_ADDR="不明"
    
    # # IPアドレスが取得できた場合は詳細も調べる
    # addtext=""
    # if(r_REMOTE_ADDR!="不明"):
    #     geo_r= geolite2.reader()
    #     res = geo_r.get(r_REMOTE_ADDR)
    #     addtext="\n地域："+res["country"]["names"]["ja"]+" , "+res["city"]["names"]["ja"]
    #     addtext=addtext+"\nGoogleマップで開く："+"https://www.google.com/maps?q="+str(res["location"]["latitude"])+","+str(res["location"]["longitude"])

    # LINE Notifyで送信
    bot = LINENotifyBot(access_token=os.environ.get('LINE_ACCESS_TOKEN'))
    bot.send(
        message="\n"+sendtext,
        # message="\n"+sendtext+"\n\n送信端末情報\n"+r_HTTP_USER_AGENT+"\n\nIPアドレス\n"+r_REMOTE_ADDR+addtext,
        # スタンプを送信する場合
        # sticker_package_id=1,
        # sticker_id=13,
        )
    
    # ページ表示
    print('Content-type:text/plain')
    print('')  # 空白行は、ヘッダーを終了するようにサーバーに指示します
    print("ok")

except Exception as e:
    print('Content-type:text/plain')
    print('')  # 空白行は、ヘッダーを終了するようにサーバーに指示します
    print("error:",e)
