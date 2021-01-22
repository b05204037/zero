import paho.mqtt.client as mqtt
import json

broker_ip = '172.20.10.2'

f = open('./pwm_info.json', 'r')
mamual_state = json.load(f)
f.close()

def on_connect(client, userdata, flags, rc):
    print('Connect with the result code ' + str(rc))
    client.subscribe('farm4/zero/led')
    client.subscribe('farm4/zero/uv')
    client.subscribe('farm3/ai_signal_zero/node1')

def on_message(client, userdata, msg):
    topic = msg.topic
    content = msg.payload.decode('utf-8')
    if topic == 'farm3/ai_signal_zero/node1':
        f = open('./pwm_info.json', 'w')
        json.dump(eval(content), f)
        f.close()
    if topic == 'farm4/zero/led':
        f = open('./pwm_info.json', 'w')
        mamual_state['led'] = content
        json.dump(mamual_state, f)
        f.close()
    if topic == 'farm4/zero/uv':
        f = open('./pwm_info.json', 'w')
        mamual_state['uv'] = content
        json.dump(mamual_state, f)
        f.close()
    
    print('topic : ' + topic + ' msg : ' + content)

client = mqtt.Client('zero_01')
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_ip, 1883, 60)
client.loop_forever()