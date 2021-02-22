function choose_way() {
    $(function () {
        // ダイアログの初期設定
        $("#mydialog2").dialog({
            autoOpen: false,  // 自動的に開かないように設定
            width: 500,       // 横幅のサイズを設定
            modal: true,      // モーダルダイアログにする
            buttons: [        // ボタン名 : 処理 を設定
                {
                    text: 'ボタン1',
                    click: function () {
                        alert("ボタン1をクリックしました");
                    }
                },
                {
                    text: 'ボタン2',
                    click: function () {
                        alert("ボタン2をクリックしました");
                    }
                },
            ]
        });

        $("#btn_action2").click(function () {
            // ダイアログの呼び出し処理
            $("#mydialog2").dialog("open");
        });
    })
}

window.addEventListener('load', choose_way)