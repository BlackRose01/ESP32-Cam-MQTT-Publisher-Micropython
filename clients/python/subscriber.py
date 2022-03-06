import paho.mqtt.client as mqtt
import time
import datetime

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe([
        ("plnts/cam1", 0),
    ])

def on_message(client, userdata, msg):
    f = open("./image" + str(time.mktime(datetime.datetime.today().timetuple())) + ".jpg", "wb")
    f.write(msg.payload)
    f.close()
    # print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.0.2", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()