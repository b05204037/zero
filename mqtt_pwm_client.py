import paho.mqtt.client as mqtt
import json

broker_ip = '20.191.97.53'

f = open('./pwm_info.json', 'r')
mamual_state = json.load(f)
f.close()

def on_connect(client, userdata, flags, rc):
    print('Connect with the result code ' + str(rc))
    client.subscribe('farm3/led/node1')
    client.subscribe('farm3/uv/node1')
    client.subscribe('farm3/ai_signal_zero/node1')

def on_message(client, userdata, msg):
    topic = msg.topic
    content = msg.payload.decode('utf-8')
    if topic == 'farm3/ai_signal_zero/node1':
        f = open('./pwm_info.json', 'w')
        json.dump(eval(content), f)
        f.close()
    if topic == 'farm3/led/node1':
        f = open('./pwm_info.json', 'w')
        mamual_state['led'] = content
        json.dump(mamual_state, f)
        f.close()
    if topic == 'farm3/uv/node1':
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