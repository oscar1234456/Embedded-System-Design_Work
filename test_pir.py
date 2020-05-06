import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 21
pir = 20

GPIO.setup(led,GPIO.OUT)
GPIO.setup(pir,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
moved = 0

try:
    while True:
        #sleep(0.1)
        moved = GPIO.input(pir)
        print(moved)
        if moved == 1:
            GPIO.output(led,True)
            print("You moved!")
        else:
            GPIO.output(led,False)
            sleep(0.5)
finally:
    print("Exit the program!")
    GPIO.cleanup()    

    
    