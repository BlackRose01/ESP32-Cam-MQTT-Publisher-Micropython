import network
import upip
import config as cfg
import time

sta_if = network.WLAN(network.STA_IF)
    
if not sta_if.isconnected():
    sta_if.active(True)
    sta_if.connect(cfg.NETWORK['ssid'], cfg.NETWORK['password'])
    
    while not sta_if.isconnected():
        print("Cannot connect to WLAN")
        time.sleep(3)

for package in cfg.PACKAGES:
    upip.install(package)