import paho.mqtt.client as mqtt
import json

broker_ip = '172.20.10.2'
farm_num = 'farm4'

f = open('./pwm_info.json', 'r')

state = json.load(f)
f.close()


def on_connect(client, userdata, flags, rc):
    print('Connect with the result code ' + str(rc))
    client.subscribe(farm_num + '/zero/led')
    client.subscribe(farm_num + '/zero/uv')
    client.subscribe(farm_num + '/zero/ir')


def on_message(client, userdata, msg):
    topic = msg.topic
    content = msg.payload.decode('utf-8')
    if topic == farm_num + '/zero/ir':
        f = open('./pwm_info.json', 'w')
        state['ir'] = content
        json.dump(state, f)
        f.close()
    if topic == farm_num + '/zero/led':
        f = open('./pwm_info.json', 'w')
        state['led'] = content
        json.dump(state, f)
        f.close()
    if topic == farm_num + '/zero/uv':
        f = open('./pwm_info.json', 'w')
        state['uv'] = content
        json.dump(state, f)
        f.close()

    print('topic : ' + topic + ' msg : ' + content)


client = mqtt.Client('zero_01')
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_ip, 1883, 60)
client.loop_forever()
