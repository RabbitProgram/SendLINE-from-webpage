# SendLINE-from-webpage
#### Webページから特定のグループor自分にLINEメッセージを送る

送信したい内容をテキストボックスに入力して[Send]をクリックすると、予め指定したトークルームにメッセージを送信します。<br>
何も入力せずにボタンを押した場合、絵文字をランダムで10個選んで送ります。（[send.py](send.py) を参照）<br>
送信が完了したら、送信時刻を2秒間表示します。<br>
<br>

## 使用方法
まずLINE Notifyのページでアクセストークンを生成してください。（ここで送信先を指定します）<br>
https://notify-bot.line.me/ja/<br>
↓<br>
コピーしたトークンを「LINE_ACCESS_TOKEN」の名前で環境変数に登録してください。<br>
（環境変数を使用しない場合は、[send.py](send.py) の「access_token=」より後の部分を適宜変更してください）<br>
↓<br>
index.html を開いて動作を確認します

## 実際の様子
![image1](https://user-images.githubusercontent.com/74450836/140334090-7819efd3-8e3f-4228-964b-e4617cf22766.png)
<br>
<img width="400" src="https://user-images.githubusercontent.com/74450836/140334096-8d862a17-bf0d-4bc3-925f-646d82091e87.png">
<br>
