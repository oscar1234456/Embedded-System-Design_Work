#HW: 7 Segement + btn + pir
#You can use two btn,add and minus the number respectively.
#Addtionally, PIR will catch the body,and switch on the led. 
# *Raspberry 4*
# work video = "https://youtu.be/b_wXH08CGjE" 
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 21
btn = 26
btn2 = 19
leda = 1
ledb = 2
ledc = 3
ledd = 4
lede = 5
ledf = 6
ledg = 7
pir = 20

num0 = {leda:1, ledb:1, ledc:1, ledd:1, lede:1, ledf:1, ledg:0}
num1 = {leda:0, ledb:1, ledc:1, ledd:0, lede:0, ledf:0, ledg:0}
num2 = {leda:1, ledb:1, ledc:0, ledd:1, lede:1, ledf:0, ledg:1}
num3 = {leda:1, ledb:1, ledc:1, ledd:1, lede:0, ledf:0, ledg:1}
num4 = {leda:0, ledb:1, ledc:1, ledd:0, lede:0, ledf:1, ledg:1}
num5 = {leda:1, ledb:0, ledc:1, ledd:1, lede:0, ledf:1, ledg:1}
num6 = {leda:0, ledb:0, ledc:1, ledd:1, lede:1, ledf:1, ledg:1}
num7 = {leda:1, ledb:1, ledc:1, ledd:0, lede:0, ledf:1, ledg:0}
num8 = {leda:1, ledb:1, ledc:1, ledd:1, lede:1, ledf:1, ledg:1}
num9 = {leda:1, ledb:1, ledc:1, ledd:1, lede:0, ledf:1, ledg:1}

numMap = {0:num0,1:num1,2:num2,3:num3,4:num4,5:num5,6:num6,7:num7,8:num8,9:num9}

GPIO.setup(leda,GPIO.OUT)
GPIO.setup(ledb,GPIO.OUT)
GPIO.setup(ledc,GPIO.OUT)
GPIO.setup(ledd,GPIO.OUT)
GPIO.setup(lede,GPIO.OUT)
GPIO.setup(ledf,GPIO.OUT)
GPIO.setup(ledg,GPIO.OUT)
GPIO.setup(led,GPIO.OUT)
GPIO.setup(btn,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(btn2,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(pir,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

pre = 1
pre2 = 1
moved = 0

total = 0
def setNum(inNum):
    num = numMap[inNum]
    for i in num:
        GPIO.output(i,num[i])

setNum(0)
while True:
    state = GPIO.input(btn)
    state2 = GPIO.input(btn2)
    moved = GPIO.input(pir)
    print(state)
    if((not state) and pre):
        total+=1
        if total == 10:
            total = 0
        setNum(total)
    if((not state2) and pre2):
        total-=1
        if total == -1:
            total = 9
        setNum(total)
    if moved == 1:
        GPIO.output(led,True)
        print("You moved!")
    else:
        GPIO.output(led,False)
        

    pre = state
    pre2 = state2
    sleep(0.05)    