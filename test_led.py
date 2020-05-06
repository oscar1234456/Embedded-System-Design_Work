import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 21


GPIO.setup(led,GPIO.OUT)

GPIO.output(led,1)
    
    