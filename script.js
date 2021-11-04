xhr = new XMLHttpRequest();

// 送信ボタンを押したときの処理
function OnSendClick() {
    // form1.submit()

    //POST送信
    xhr.open('POST', 'send.py', true);
    xhr.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
    var request = "text=" + text.value;
    xhr.send(request);

    //時刻を取得してメッセージをセット
    const date1 = new Date();
    const time_text = ("00" + (date1.getHours())).slice(-2) + ":"
        + ("00" + (date1.getMinutes())).slice(-2) + ":"
        + ("00" + (date1.getSeconds())).slice(-2);
    document.getElementById("donetext").innerText = time_text + " DONE"

    //完了メッセージを表示
    showBox()

    //入力内容をリセット
    form1.reset()

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
