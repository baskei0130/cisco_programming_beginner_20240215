from netmiko import ConnectHandler

# ネットワーク機器の接続情報
device = {
    'device_type': 'cisco_xe',  # IOS-XE 用のデバイスタイプ
    'ip': '{change-this}',      # ネットワーク機器の IP アドレス
    'username': '{change-this}',        # ログインユーザー名
    'password': '{change-this}',  # パスワード
    'secret': '{change-this}',    # enable モードのパスワード
}

# ネットワーク機器に接続
net_connect = ConnectHandler(**device)

# enable モードに切り替え
net_connect.enable()

# コンフィギュレーションモードに入る
net_connect.config_mode()

# インターフェースを shutdown
commands = [
    'interface GigabitEthernet1/0/1',
    'shutdown'
]
net_connect.send_config_set(commands)

# 実行結果を確認するためのコマンド
output = net_connect.send_command('show interfaces GigabitEthernet1/0/1 status')

# 結果を表示
print(output)

# 接続終了
net_connect.disconnect()

