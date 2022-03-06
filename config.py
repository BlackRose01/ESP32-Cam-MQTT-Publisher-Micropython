NETWORK = {
    "ssid": "",
    "password": ""
}

MQTT = {
    "client_id": "cam1",
    "server": "192.168.0.2",
    "port": 1883,
    "topic": "plnts/cam1",
    "send_interval": 5000
}

PACKAGES = [
    "micropython-umqtt.simple2",
    "micropython-umqtt.robust2"
]
