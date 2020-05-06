import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 21
btn = 26

GPIO.setup(led,GPIO.OUT)
GPIO.setup(btn,GPIO.IN,pull_up_down=GPIO.PUD_UP)
pre = 1

while True:
    state = GPIO.input(btn)
    print(state)
    if((not state) and pre):
        GPIO.output(led, True)
        sleep(3)
        GPIO.output(led,False)
    pre = state
    sleep(0.05)    