# Animalchat デプロイ・起動手順書

Git URL : https://github.com/tky2302107/Pet_owner.git

現在、AWSサーバーはクローラによって検索エンジンに追加されることを防ぐため停止しています。
そのため、サイトの確認はローカルで構築して行う必要があります。

## 前提条件

Python3.11.xがインストール済み

## 手順

### ・手順1　解凍する

ZIPファイルを解凍する。

### ・手順2　ターミナルを開く

解凍したフォルダ内でターミナルを開く。

もしくは、

ターミナルを開き`cd 解凍したフォルダのパス`を入力する。

### ・手順3　仮想環境用モジュールのインストール

pipenvを使用し、仮想環境をインストールする。
`pip install pipenv`

### ・手順4　仮想環境の設定をインストール

ターミナルで`pipenv install`と入力し、仮想環境をインストールする。

### ・手順5

`pipenv run daphne -b 0.0.0.0 -p 8000 config.asgi:application`
と入力し、問題なく起動すれば  [localhost:8000](http://localhost:8000)  にて閲覧ができるようになります。エラーが発生した場合は以下の手順で操作してください。

## エラー対処

### ・ImportError: No module named xxx

モジュール不足のエラーが表示される場合は`pip install`を使用してモジュールをインストールする必要があります。`django`,`daphne`,`channel`,`django-cleanup`,`apscheduler`,`pillow`などが不足していると表示される場合があります。

### ・Error: That port is already in use

8000ポートが使用中の場合は手順5で示した、
`pipenv run daphne -b 0.0.0.0 -p 8000 config.asgi:application`
の`8000`を任意の文字列に変えることで指定したポートでの起動が可能です。

### ・pipenv not found

環境によっては

`pipenv run daphne -b 0.0.0.0 -p 8000 config.asgi:application`

の起動コマンドが使用できない場合があります。その場合は代わりに

`python3.11 -m pipenv run daphne -b 0.0.0.0 -p 8000 config.asgi:application`

または

`daphne -b 0.0.0.0 -p 8000 config.asgi:application`

と入力してください。

後者を選択した場合、必要なモジュールを追加でインストールする必要があります。

※`python manage.py runserver`で起動することも可能ですが、この場合、チャットの非同期通信機能はオフになります。

## アカウントとパスワードについて

### 一般ユーザー　　　全て小文字

usera@local.jp userapassword  　　|　 　 userb@local.jp userbpassword

userc@local.jp usercpassword

上記の3アカウントが利用可能です。

### 管理者ユーザー　　　全て小文字

superuser@local.jp superuserpassword

管理者アカウントは1つのみ存在します。

## 既知の問題

環境によってはadminページでcssが反映されない場合があります。
