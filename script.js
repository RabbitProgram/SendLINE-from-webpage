var xhr = new XMLHttpRequest();
var nowmode = 1;  //送信モード（1：文章、2：ファイル）

//「文章を送る」リンクを押したときの処理
function OnMode1Click() {
    nowmode = 1;
    document.getElementById("mode1link").removeAttribute("href");
    document.getElementById("mode2link").setAttribute("href", "javascript:void(0);");
    document.getElementById("sendBox1").style.display = "block"; // ボックスを表示
    document.getElementById("sendBox2").style.display = "none"; // ボックスを非表示
}

//「ファイルを送る」リンクを押したときの処理
function OnMode2Click() {
    nowmode = 2;
    document.getElementById("mode1link").setAttribute("href", "javascript:void(0);");
    document.getElementById("mode2link").removeAttribute("href");
    document.getElementById("sendBox1").style.display = "none"; // ボックスを表示
    document.getElementById("sendBox2").style.display = "block"; // ボックスを非表示
}

// 最初はテキストの方を選択状態にする
OnMode1Click();

//「ファイルを選択」ボタンの処理
document.getElementById("selfile").addEventListener("change", function (evt) {
    var file = evt.target.files;　//選択ファイルを配列形式で取得
    // var num = file.length;       //選択されたファイル数を格納
    // var str = "";                 //ファイル情報を格納する変数

    if (file.length == 0) {
        //キャンセルされた場合
        document.getElementById("fileabout").innerText = "最大サイズは500MBです";
    } else {
        //ファイルのサイズチェック
        if (file[0].size / 1024 / 1024 > 500) {
            evt.target.value = "";
            alert("ファイルサイズが500MBを超えているため送信できません")
        } else {
            document.getElementById("fileabout").innerText = file[0].name;
        }
    }

    // for (var i = 0; i < num; i++) {
    //     str += "[" + parseInt(i + 1) + "番目のファイル]<br>";
    //     str += "ファイル名：" + file[i].name + "<br>";
    //     str += "ファイルサイズ：" + file[i].size + "byte<br>";
    //     str += "ファイルタイプ：" + file[i].type + "<br>";
    //     if (i < num - 1) str += "<br>";
    // }
}, false);

//アップロード関連のイベント処理
xhr.upload.addEventListener('loadstart', (evt) => {
    // アップロード開始
    console.log("アップロードを開始します！");
    document.getElementById("sendbutton").className = "btn btn-disabled";
});

xhr.upload.addEventListener('progress', (evt) => {
    // アップロード進行パーセント
    let percent = (evt.loaded / evt.total * 100).toFixed();  //少数以下四捨五入（少数第一位まで表示する場合：.toFixed(1);）
    // console.log("現在：" + String(percent) + " %");
    document.getElementById("sendbutton").innerText = String(percent) + " %";
});

xhr.upload.addEventListener('error', (evt) => {
    // アップロードエラー
    console.log('アップロード中にエラーが発生しました！');
    document.getElementById("sendbutton").innerText = "Error";
});

xhr.upload.addEventListener('load', (evt) => {
    // アップロード正常終了
    console.log("正常終了！");
});

xhr.upload.addEventListener('loadend', (evt) => {
    // アップロード終了 (エラー・正常終了両方)
    console.log("アップロード完了！");
    document.getElementById("sendbutton").className = "btn btn-border-shadow";
    done();  //完了処理
});

//送信完了後の処理
function done() {
    //時刻を取得してメッセージをセット
    const date1 = new Date();
    const time_text = ("00" + (date1.getHours())).slice(-2) + ":"
        + ("00" + (date1.getMinutes())).slice(-2) + ":"
        + ("00" + (date1.getSeconds())).slice(-2);
    document.getElementById("donetext").innerText = time_text + " DONE";
    showBox();  //メッセージ表示

    //入力内容をリセット
    form1.reset();
    document.getElementById("fileabout").innerText = "最大サイズは500MBです";
    document.getElementById("sendbutton").innerText = "Send";
}

// 送信ボタンを押したときの処理
function OnSendClick() {
    // form1.submit()

    var sendfile = document.getElementById("selfile").files[0];  //選択されたファイル

    //ファイルを送る場合は、空の場合は処理しない
    if (nowmode == 1 || (nowmode == 2 && sendfile != null)) {
        //POST送信
        xhr.open('POST', 'send.py', true);

        if (nowmode == 1) {
            xhr.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
            xhr.send("text=" + text.value);

            done();  //完了処理
        } else {
            // xhr.setRequestHeader('content-type', 'multipart/form-data;charset=UTF-8');
            const fd = new FormData();
            fd.append('file_data', sendfile);
            fd.append('file_size', sendfile.size);
            xhr.send(fd);

            // var reader = new FileReader;
            // reader.readAsDataURL(sendfile);
            // reader.onload = function () {
            //     var val = reader.result.replace(/data:.*\/.*;base64,/, '');
            //     console.log(val);
            //     xhr.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
            //     xhr.send("file=" + val);
            // }
        }
    } else {
        document.getElementById("donetext").innerText = "Please select a file";
        showBox();  //メッセージ表示
    }

    return false
}

// const $form = $('#form')
// $('.btn-send').on('click', evt => {
//     $form.submit()
//     $form[0].reset()
// })

// ボックスを表示してタイマーを開始
function showBox() {
    document.getElementById("temporaryBox").style.display = "block"; // ボックスを表示
    timerId = setTimeout(closeBox, 2000); // タイマーを開始
}

// ボックスを消してタイマーを終了
function closeBox() {
    document.getElementById("temporaryBox").style.display = "none"; // ボックスを消す
    clearTimeout(timerId); // タイマーを終了
}
