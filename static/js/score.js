window.onload = function Init() {
    startVideo();
}

let picture;

let base64;

function startVideo() {
    navigator.mediaDevices.getUserMedia({video: true, audio: false})
        .then(function (stream) {
            document.getElementById('local_video').srcObject = stream;
        }).catch(function (error) { // 失敗時の処理はこちら.
        console.error('mediaDevice.getUserMedia() error:', error);
    });
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    else {alert('jj')}
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');


function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}


function camera() {
    const shut = document.getElementById("shutter")
    const send = document.getElementById("send")

    shut.addEventListener('click', take_picture);
    send.addEventListener('click', tenso);

    function take_picture() {
        var canvas = document.getElementById('canvas');
        var video = document.getElementById('local_video')
        var ctx = canvas.getContext('2d');
        var w = video.offsetWidth * 0.5;	// videoの横幅取得.
        var h = video.offsetHeight * 0.5;	// videoの縦幅取得.
        canvas.setAttribute("width", w);	// canvasに書き出すための横幅セット.
        canvas.setAttribute("height", h);	// canvasに書き出すための縦幅セット.
        ctx.drawImage(video, 0, 0, w, h);	// videoの画像をcanvasに書き出し.

        base64 = canvas.toDataURL('image/jpg');	// canvas上の画像をbase64に変換.

    }

    $.ajaxSetup({

        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    function tenso() {
        alert('aa');
        let fd = new FormData();
        fd.append('image', base64);

        $.ajax({
            'url': 'http://127.0.0.1:8000/score/imgupload', // 撮った画像をbase64としてデータ化しfdという変数に代入後フォームデータとしてajax通信を用いてこのurlに転送する
            'type': 'POST',
            'processData': false,
            'contentType': false,
            'data': fd,
            error: function (xhr, status, error) {
                alert(xhr.responseText);
            }
        }).done(response => {
            $("#output img").attr('src', response);
        });

    }

}　//https://elsammit-beginnerblg.hatenablog.com/entry/2020/06/16/214024　参照


window.addEventListener('load', camera)