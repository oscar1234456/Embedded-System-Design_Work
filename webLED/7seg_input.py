#HW: 7 Segement
#Input the number you want to show
#If you enter the wrong word, warning message will be poped.
# *Raspberry 4*
# work video = "https://youtu.be/o5yNaYxZkj0" 

import RPi.GPIO as GPIO
from time import sleep
import sys
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

leda = 1
ledb = 2
ledc = 3
ledd = 4
lede = 5
ledf = 6
ledg = 7

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
def setNum(inNum):
    num = numMap[inNum]
    for i in num:
        GPIO.output(i,num[i])

setNum(0)
argList = list(sys.argv)
try:
    setNum(int(argList[1]))
except:
    print("Please enter the right argument")




    