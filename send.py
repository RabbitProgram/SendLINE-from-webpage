#! /opt/alt/python37/bin/python3.7
# -*- coding: utf-8 -*-

import random
import requests
import cgi
import os
import sys
import io
import datetime
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
import urllib.parse
import json
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
            image=None,image_row=None, sticker_package_id=None, sticker_id=None,
            ):
        payload = {
            'message': message,
            'stickerPackageId': sticker_package_id,
            'stickerId': sticker_id,
            }
        files = {}
        if image != None:
            files = {'imageFile': open(image, 'rb')}
        if image_row != None:
            files = {'imageFile': image_row}
        r = requests.post(
            LINENotifyBot.API_URL,
            headers=self.__headers,
            data=payload,
            files=files,
            )


# 数値型のファイルサイズを調節した文字列型に置き換える
# size：ファイルサイズ（単位：バイト）、roundcount：小数第何位まで表示するか
def size_to_str(size,roundcount):
    unit=["Byte","KB","MB","GB","TB"]  # 単位
    changecount=0  #単位を変更した回数

    # 調節
    while(changecount<len(unit)-1):
        if(size/1024>1):
            size=size/1024
            changecount+=1
        else:
            break
    
    # 四捨五入
    if(roundcount==0):
        dec="1"
    else:
        dec=str(1/(10**roundcount))
    size=Decimal(str(size)).quantize(Decimal(dec), rounding=ROUND_HALF_UP)
    return str(size)+" "+unit[changecount]


# 絵文字一覧：https://note.com/kawatyanlife/n/ndf5e32d8dcd6
emoji=["✨","😊","☺️","💦","‼️","😅","❗️","😭","💕","❤️","😂","⭐️","👍","♂","♀","🙇","😌","😆","▶️","👋","💖","😁","✅","🤔","🤣","⁉️","🔥","🥺","🍀","🙏","❣️","🌟","😢","☀️","🌈","🏻","✌️","🎵","💪","♥️","⬇️","🥰","🌸","👇","😃","🤗","🙌","😱","😄","😉","💓","❓","👏","😍","👀","🎉","😳","😋","💡","🎶","🌱","💛","✳️","🌙","✖️","➡️","😓","😇","🙆","💧","☕️","🍎","😀","🙄","✍️","💢","😎","✔️","🧡","✋️","🌻","🌷","🐶","💫","⚡️","⚠️","💗","🙋","🌞","🌼","◼️","🍇","💁","🐾","®","💨","💭","📚","☝️","👌","✴️","✏️","😥","😣","🎯","😏","😪","😤","🍰","✂️","🤤","🥳","🌿","📝","🐰","😞","⏬","🍁","💙","😨","📖","✊️","💞","☔️","🎁","🏃","🙂","🏼","😝","😰","⤴️","🐈","❕","☁️","🐟","💰","🕊","👉","⚫️","💤","🧘","◾️","💐","😔","📷","🎊","😴","😵","©","🇺","㊗️","😫","🐥","👨","™","🎈","🍚","🌺","👊","🐕","👼","😡","🎂","📸","👩","🍓","⤵️","🥕","💌","😚","❌","😘","🍺","✈️","▪️","💚","👶","👆","🚶","💥","🐦","🍻","🙃","🌕","♨️","🍑","🍂","🐱","💮","🐚","🦀","☑️","🤦","🍃","⬆️","🍞","⭕️","🌊","💻","🙅","😲","🍋","🇦","🍜","🧐","🔸","🏇","🌹","🍙","◀️","📅","🌏","🍛","🎮","💜","💍","😩","♦️","🔬","📻","🎨","💎","🖐","🧸","😜","🍅","🌝","🍴","⚔️","🦙","😑","🌀","♻️","🧀","🐣","🌾","🍵","🎐","🚗","🍨","✉️","🌰","🤸","🥚","🔚","🍣","👗","🥀","🍒","🎃","🐴","🍊","😮","🐯","🤞","📣","🥣","🤍","🌠","😖","🎀","📕","🇵","💔","🎤","🥝","🚃","🉐","🍮","☘️","🐻","⚪️","🎸","⛩","🔁","🙈","🇸","🍏","👧","😸","🍽","😯","〰","😙","🍳","🍫","🍹","🍐","🌃","🇯","🔻","🍕","🥗","🍌","😷","😿","🕺","❔","🏫","💼","📺","🍩","🇹","💩","🍠","🐢","🍬","💯","⚽️","🦋","💝","👦","🍖","🧚","🌴","🤷","🍷","🐷","🍄","🤙","🌄","🇮","🤓","😺","🏋","🇳","📱","🥔","😠","🍈","🤳","🚲","👻","🇷","🦍","🍟","🏠","💟","🐤","🥴","😻","🐧","🍔","👑","🖤","🇫","😶","🖋","🐼","↔️","💃","💸","🇨","🥐","🏄","🐓","🐿","🐸","🐙","🧠","🐝","➕","☠️","☪️","🐔","🚤","🥶","🍱","🥱","🔍","❄️","🍥","🀄️","🚌","🦄","🥇","🥞","🥤","🌂","🤏","👐","😹","㊙️","🏆","🦌","🍪","💉","💋","🌍","⚾️","♣️","👬","🚀","🍝","🦦","💣","😽","🍆","♠️","👹","🦖","👎","🦐","🥑","🏵","🏡","👈","☎️","😛","⚕","🐉","💊","👵","🌤","🧁","❇️","🍶","👪","🎣","🥯","🌲","🌳","🏥","🏝","🎥","🦊","👽","🐘","🌛","🍡","🚙","☂️","💘","🗓","🧙","🍲","🌜","🐬","🐎","😈","🎾","🔰","🍧","📹","🐠","🏊","🗻","🐹","🎹","🧒","👁","🍼","◻️","📒","🦜","🎑","😟","☹️","🏕","🍘","🌽","🍗","🍤","🍦","🦑","🥖","😗","🥮","🚴","🤚","📞","🇰","👂","💇","👣","💅","🐇","🇬","🌆","🛌","🥵","🦷","🐡","🥟","😧","🔳","🎷","🧹","🥦","🏽","🏀","🏅","🥜","🌪","⚓️","🆖","🇪","🥂","🎧","📘","🔖","🦠","🎓","🌶","📲","🚩","♾","☯️","🥩","💈","🍉","🐄","🦧","🦒","↘️","🏘","🥊","↗️","🎙","👸","🤧","🌵","💴","🍢","🦵","🙀","🐜","☃️","😐","🦥","🎡","🥢","🚕","🐭","👮","🇭","🥛","🏨","🙍","🥓","📗","🤝","🤢","🚻","🔪","🌐","🔽","🃏","🍍","👓","🥈","🤑","🔎","⌚️","💀","🎬","🗒","🎞","😦","👭","🥒","🛀","🦆","⬛️","🖼","🐮","🦪","🧅","🇲","🔹","💠","📦","🤘","🍾","🗿","🚿","🦔","👕","🦢","▫️","🚏","😒","🤰","🍸","⚙️","⏰","🐒","🛁","🐞","🔮","✒️","🛣","🕰","🕷","🔵","💬","🛵","🚢","📔","⬅️","🇧","🤜","🏍","🆗","👾","🥬","🎩","😕","🏖","🧑","🔶","🏁","🔯","♓️","👖","🦲","🛏","⛅️","🇾","🔔","🕯","⌛️","🔄","🐲","💄","👫","➗","🧲","🆚","🎄","⏱","🐨","👃","🥪","🎺","🧖","🍯","🏳","🚬","🎰","✡️","🎌","⏩","🤛","🦁","🌧","🌩","⛰","🐛","🚪","🐋","🦩","♎️","🟦","🏐","🏰","💿","🇩","🔑","🌑","🏔","🗣","📍","🖊","🌇","👿","🗼","👴","🕴","👰","🧈","⛴","🙎","🇱","🍭","🚣","🧳","☄️","♑️","🟡","🥧","⛳️","🦞","👯","🦈","🔗","🚘","📆","🤎","🚒","🚨","🏪","🦮","🛫","🚺","🧊","🌎","🦛","👛","⛺️","🙁","🚂","🐽","⬜️","💵","➖","🏢","♋️","👺","🔨","🔴","🟢","🛍","🐖","🎪","🐐","🐑","😾","👠","🧂","🌋","🧶","👅","🔅","🏭","🌌","🐳","🎠","🤿","🚑","🧟","🏾","⏳","🌔","🥭","🪐","💒","🧱","🌖","🏞","🙊","↪️","🚚","📙","🟩","🌉","🌅","📊","🚓","🧽","😬","🐏","🔺","🗾","🎗","📈","🎲","🦳","🐩","🤖","🐵","⛵️","🅱️","🎒","🦎","⛄️","🖕","🩹","👄","👚","🏂","🐍","🚅","👳","🧉","🈵","♒️","🔌","🖖","📃","🚹","🏩","🗺","🕸","🎇","🎳","🎢","📎","😼","💑","🐁","🖌","🛐","📯","🌒","🛹","👜","👝","🛳","♈️","♊️","♍️","🦉","⚖️","🦰","🎫","⛪️","🎆","🤼","♿️","🗝","🌭","🇼","🧄","🚞","🦕","🟪","🧩","🛒","📡","🟥","🟨","🏌","🥃","🏓","🐫","🔋","🔆","🥉","🖥","🕵","🤠","🧛","🐅","➿","🩺","🚆","🌬","🔊","🌚","⛑","🧼","⛈","👱","🛡","🔼","📓","💆","➰","↙️","🔘","🐗","🅰️","🚋","🖍","🧔","🔫","🛑","🦱","🎏","📳","🌡","🚛","🥿","🎻","🏮","📩","🥠","⏫","♟","🙉","🦴","📄","🧺","🏎","🧥","🛥","♉️","♌️","🚦","🧭","⏲","⛲️","🧞","🚉","🐀","📀","🛰","🎿","🐊","🎟","⚰️","🤹","🐃","🈂","🎼","🧍","🥡","🔙","📁","🥾","🗑","🟧","🎋","🚇","🦽","🩸","🛎","🏑","📽","👙","🕐","🥄","⛏","🗯","🦅","🪓","📮","🏹","🦂","🏛","🌥","🏧","🦡","🕶","🆎","🖇","🥁","🌯","🧗","🏈","🏦","🔷","🈹","🚧","👞","🦹","🆙","🎴","💶","💷","🧆","🦾","♐️","📑","🤡","🧏","🥋","🌦","🚔","🛋","🧜","🤵","🦸","🎽","🛩","⚜️","🧫","🔒","🏙","🦗","🕒","⛱","🌓","🌗","🌘","📥","🔭 〽️","🔞","🕳","🈚️","🚄","🐂","👘","🚭","🗽","☸️","🚽","🐺","🎖","🍿","🕙","⛽️","🇻","🥙","↩️","🛸","🤒","🧵","🚰","🤕","🚁","📢","🪂","🏴","🤐","🏯","👡","↕️","🚮","🛬","❎","↖️","🧪","🔈","📧","📰","🆓"]


try:
    # パラメータ取得
    form = cgi.FieldStorage()

    try:
        fileitem = form['file_data']
        size=size_to_str(int(form['file_size'].value),2)
        
        if(fileitem.type=="image/jpeg" or fileitem.type=="image/png"):
            # jpeg・png画像の場合→そのまま送信
            bot = LINENotifyBot(access_token=os.environ.get('LINE_ACCESS_TOKEN'))
            bot.send(
                message="画像が送信されました",
                image_row=fileitem.file.read(),
            )
        else:
            # その他のファイル→サーバーにファイルを保存してURLを送る
            # ディレクトリが存在しない場合は新規作成
            if not os.path.exists("upload"):
                os.makedirs("upload")  # ディレクトリ作成（サブフォルダーを指定する場合はパスを「tmp/sub」のように指定する）

            # 現在の日時を取得
            dt_now = datetime.datetime.now()

            # ディレクトリ・ファイル名部分,拡張子部分（.～）
            fn_split = os.path.splitext(str(fileitem.filename))

            savename=fn_split[0]+"_"+dt_now.strftime('%Y%m%d%H%M%S')+fn_split[1]
            savename_long =  os.path.join("upload", savename) # uploadディレクトリ内に保存

            # ファイル内容を書き込み
            if fileitem.file:
                file_write = open(savename_long, 'wb')
                while True:
                    chunk = fileitem.file.read(1000000)
                    if not chunk:
                        break
                    file_write.write(chunk)
                file_write.close()

            # 権限変更（URLによる直接アクセスを禁止）       
            os.chmod(savename_long,0o600)

            # url = "https://rabbitprogram.com/python3.8.6/line/groupsend/"+urllib.parse.quote(savename_long)
            downloadurl="https://rabbitprogram.com/python3.8.6/line/groupsend/download.py" \
                +"?type="+urllib.parse.quote(fileitem.type) \
                +"&uri="+urllib.parse.quote(savename) \
                +"&name="+urllib.parse.quote(fileitem.filename)
            
            # URL短縮
            response = requests.get("https://is.gd/create.php?format=simple&format=json&url="+urllib.parse.quote(downloadurl))
            jsondata=json.loads(response.text)
            downloadurl=jsondata["shorturl"]

            # ダウンロード期限を算出
            today=datetime.datetime.now()
            enddate = today + datetime.timedelta(weeks=1)  # 1週間後

            # LINE Notifyで送信
            bot = LINENotifyBot(access_token=os.environ.get('LINE_ACCESS_TOKEN'))
            bot.send(
                message="【 ファイルが送信されました 】\n・ファイル名："+fileitem.filename \
                    +"\n・サイズ："+size \
                    +"\n・ダウンロードURL："+downloadurl \
                    +"\n・ダウンロード期限："+enddate.strftime("%Y/%m/%d")+"まで",
            )
    except Exception as e:
        # 文字列が空の場合は絵文字を送る
        sendtext = str(form.getvalue('text', ''))
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
