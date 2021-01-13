# バックエンド側の色々

# フォルダ構成
- main : ファッションの点数化を行う
- segmentation : 画像のセグメンテーション（
- face_blur : 顔を検出してその矩形をぼかす

# TL;DR

## main
- downloader.pyでダウンロードする、pictureフォルダに画像データが格納されるはず
- gitに画像データは上げないでね
- 学習はがんばるぞい！

## face_blue
- cascadeで顔認識して、顔のRectを作成(face_detect())した後、blur_imgで特定のRectangleにブラーをかける
- これを組み込むにあたって、ユーザーがブラーをかける位置を調整する機能が必須

## segmentation
- がんばrrr.....
