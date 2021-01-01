#import pigpio
#import RPi.GPIO as GPIO
import time
import json

pwm_info_filepath = './pwm_info.json'
PWM_LED_PIN = 13
PWM_FREQ = 2500
UV_PIN = 40

#GPIO.setmode(GPIO)
#GPIO.setup(UV_PIN, GPIO.OUT)
#pi = pigpio.pi()

def inverse(led_int):
    return 100 - led_int

#try:
while True:
    f = open(pwm_info_filepath)
    pwm_info = json.load(f)
    led_int = int(pwm_info['led'])
    uv_int = pwm_info['uv']
    print(led_int, uv_int)
    # continue here for the uv signal
    #if uv_int == "on" or uv_int == "true":
    #    GPIO.output(UV_PIN, GPIO.HIGH)
    #else :
    #    GPIO.output(UV_PIN, GPIO.LOW)
    
    # now use the inverse hardware
    led_inverse = inverse(led_int)
    #pi.hardware_PWM(PWM_LED_PIN, PWM_FREQ, led_inverse*10000)
    time.sleep(0.1)
    
#finally:
    #pi.set_mode(PWM_LED_PIN, pigpio.INPUT)
