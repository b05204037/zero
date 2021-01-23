import pigpio
import RPi.GPIO as GPIO
import time
import json

pwm_info_filepath = './pwm_info.json'
PWM_LED_PIN = 13
PWM_FREQ = 2500
UV_PIN = 21
IR_PIN = 20
#  pin20(ir) pin21(uv)
#            gnd
GPIO.setmode(GPIO.BCM)
GPIO.setup(UV_PIN, GPIO.OUT)
GPIO.setup(IR_PIN, GPIO.OUT)
pi = pigpio.pi()


def inverse(led_int):
    return 100 - led_int


def uv_output(uv_state):
    if uv_state == "1" or uv_state == "true":
        GPIO.output(UV_PIN, GPIO.HIGH)
        return 'uv is on'
    else:
        GPIO.output(UV_PIN, GPIO.LOW)
        return 'uv is down'


def ir_output(ir_state):
    if ir_state == "1" or ir_state == "true":
        GPIO.output(IR_PIN, GPIO.HIGH)
        return 'ir is up'
    else:
        GPIO.output(IR_PIN, GPIO.LOW)
        return 'ir is down'


try:
    while True:
        f = open(pwm_info_filepath)
        pwm_info = json.load(f)
        led_int = int(pwm_info['led'])
        uv_int = pwm_info['uv']
        ir_int = pwm_info['ir']

        # continue here for the uv signal
        uv_status = uv_output(uv_int)
        print(uv_status)
        ir_status = ir_output(ir_int)
        print(ir_status)

        # now use the inverse hardware
        # led_inverse = inverse(led_int)
        pi.hardware_PWM(PWM_LED_PIN, PWM_FREQ, led_int*10000)
        time.sleep(0.1)
except:
    print('except')
# finally:
    # pi.set_mode(PWM_LED_PIN, pigpio.INPUT)
