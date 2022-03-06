import camera
import time
import sys
import config as cfg
from umqtt.simple2 import MQTTClient, MQTTException

try:
    camera.deinit()
    camera.init(0, format=camera.JPEG)
    ## Other settings:
    # flip up side down
    camera.flip(0)
    # left / right
    camera.mirror(1)

    # framesize
    camera.framesize(camera.FRAME_UXGA)
    # The options are the following:
    # FRAME_96X96 FRAME_QQVGA FRAME_QCIF FRAME_HQVGA FRAME_240X240
    # FRAME_QVGA FRAME_CIF FRAME_HVGA FRAME_VGA FRAME_SVGA
    # FRAME_XGA FRAME_HD FRAME_SXGA FRAME_UXGA FRAME_FHD
    # FRAME_P_HD FRAME_P_3MP FRAME_QXGA FRAME_QHD FRAME_WQXGA
    # FRAME_P_FHD FRAME_QSXGA
    # Check this link for more information: https://bit.ly/2YOzizz

    # special effects
    camera.speffect(camera.EFFECT_NONE)
    # The options are the following:
    # EFFECT_NONE (default) EFFECT_NEG EFFECT_BW EFFECT_RED EFFECT_GREEN EFFECT_BLUE EFFECT_RETRO

    # white balance
    camera.whitebalance(camera.WB_HOME)
    # The options are the following:
    # WB_NONE (default) WB_SUNNY WB_CLOUDY WB_OFFICE WB_HOME

    # saturation
    camera.saturation(0)
    # -2,2 (default 0). -2 grayscale 

    # brightness
    camera.brightness(0)
    # -2,2 (default 0). 2 brightness

    # contrast
    camera.contrast(0)
    #-2,2 (default 0). 2 highcontrast

    # quality
    camera.quality(10)
    # 10-63 lower number means higher quality
except OSError as e:
    camera.deinit()
    print("Camera error - Line No. ", str(e))
    sys.exit(0)

try:
    mqtt = MQTTClient(client_id=cfg.MQTT['client_id'], server=cfg.MQTT['server'], port=cfg.MQTT['port'])
    mqtt.connect()

    while True:
        buf = camera.capture()
        mqtt.publish(cfg.MQTT['topic'], bytearray(buf))
        time.sleep(cfg.MQTT['send_interval'])
except MQTTException as e:
    camera.deinit()
    print("Mqtt Error - ", str(e))
