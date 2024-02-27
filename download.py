#! /opt/alt/python37/bin/python3.7
# -*- coding: utf-8 -*-

import cgi
import sys
import urllib.parse
import urllib

try:
    # パラメータ取得
    form = cgi.FieldStorage()
    filetype=str(form.getvalue('type', ''))
    fileuri=str(form.getvalue('uri', ''))
    filename = str(form.getvalue('name', ''))

    if(len(filetype)==0 or len(fileuri)==0 or len(filename)==0):
        # パラメーターが含まれていない場合
        raise ValueError("parameter error")
    
    filetype=urllib.parse.unquote(filetype)
    fileuri=urllib.parse.unquote(fileuri)
    filename=urllib.parse.unquote(filename)

    print(f"Content-Type: {filetype};\r\nContent-Disposition: attachment; filename={filename}")
    print('')  # 空白行は、ヘッダーを終了するようにサーバーに指示します
    sys.stdout.flush() # printとwriteの間に呼ぶ
    with open("upload/"+fileuri, 'rb') as f:
        sys.stdout.buffer.write(f.read())
    
except Exception as e:
    print('Content-type:text/plain')
    print('')  # 空白行は、ヘッダーを終了するようにサーバーに指示します
    print("error:",e)
