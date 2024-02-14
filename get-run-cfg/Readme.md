# get-run-cfg

get-run-cfg は Cisco Modeling Labs (CML) 上の
仮想機器 Catalyst9000v の running-config を取得するスクリプトです。

## フォルダ構成
- Readme.md
  - フォルダの概要や実施方法を示したものです
- get-run-cfg-netmiko-iosxe.py
  - CML上のIOS-XEで動作する機器のrunning-configをnetmikoライブラリを使い取得するスクリプトです
  - ChatGPT作です
- get-run-cfg-telnet-iosxe.py
  - CML上のIOS-XEで動作する機器のrunning-configをtelnetlibライブラリを使い取得するスクリプトです
  - ChatGPT作です

## 実行順序
1. CMLでLabを準備
   1. Programmability(IOS-XE).yaml をインポートし、初期設定 (IP address/default gw/username/password/enable password/line 0 4; login local) を入力
   2. Catalyst9000vを使う場合は、Login password は ```username {username} secret {password}``` で入力してください。
2. ChatGPT にPythonスクリプト作成を依頼
   1. 本作者の環境でChatGPTに作成してもらったPythonファイルは ```get-run-cfg-netmiko-iosxe.py``` で保存
3. ChatGPTに作成してもらったPythonファイルを実行するために必要なパッケージをインストール
   1. 本作者の場合：Python3, pip3, netmiko をインストール
   2. これらのインストール方法はせっかくなのでChatGPTに聞いたりネットで調べてみましょう
   3. Pythonを使う場合は仮想環境を使うとパッケージの管理が容易になります
4. ChatGPTに作成してもらったPythonファイルを実行 (```python3 get-run-cfg-netmiko-iosxe.py```)
   1. {change-this} と書かれた部分を変更してください

## ChatGPT プロンプト
```
あなたはCisco Modeling Labs(CML)、ネットワーク機器、プログラミングのスペシャリストです。ネットワーク機器A (IOS-XE {change-this}, IP: {change-this}, username: {change-this}, password: {change-this}, enable password: {change-this}) の running-config を取得するスクリプトをPythonで作成してください。
```

:::note warn
{change-this}の部分を環境に合わせて変更してください。
:::