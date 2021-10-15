import RPi.GPIO as GPIO
import time
import sys

outA1 = 22
outA2 = 27
outB1 = 23
outB2 = 24

i = 0
positive = 0
negative = 0
y = 0



GPIO.setmode(GPIO.BCM)
GPIO.setup(outA1, GPIO.OUT)
GPIO.setup(outB1, GPIO.OUT)
GPIO.setup(outA2, GPIO.OUT)
GPIO.setup(outB2, GPIO.OUT)
GPIO.output(outA1, GPIO.LOW)
GPIO.output(outB1, GPIO.LOW)
GPIO.output(outA2, GPIO.LOW)
GPIO.output(outB2, GPIO.LOW)

print "First calibrate by giving some +ve and -ve values....."

try:
    i = 0
    while(1):
        if i == 0:
            GPIO.output(outA1, GPIO.HIGH)
            GPIO.output(outB1, GPIO.LOW)
            GPIO.output(outA2, GPIO.LOW)
            GPIO.output(outB2, GPIO.LOW)
            time.sleep(0.001)
            # time.sleep(2)
        elif i == 1:
            GPIO.output(outA1, GPIO.HIGH)
            GPIO.output(outB1, GPIO.HIGH)
            GPIO.output(outA2, GPIO.LOW)
            GPIO.output(outB2, GPIO.LOW)
            time.sleep(0.001)
            # time.sleep(2)
        elif i == 2:  
            GPIO.output(outA1, GPIO.LOW)
            GPIO.output(outB1, GPIO.HIGH)
            GPIO.output(outA2, GPIO.LOW)
            GPIO.output(outB2, GPIO.LOW)
            time.sleep(0.001)
            # time.sleep(2)
        elif i == 3:    
            GPIO.output(outA1, GPIO.LOW)
            GPIO.output(outB1, GPIO.HIGH)
            GPIO.output(outA2, GPIO.HIGH)
            GPIO.output(outB2, GPIO.LOW)
            time.sleep(0.001)
            # time.sleep(2)
        elif i == 4:  
            GPIO.output(outA1, GPIO.LOW)
            GPIO.output(outB1, GPIO.LOW)
            GPIO.output(outA2, GPIO.HIGH)
            GPIO.output(outB2, GPIO.LOW)
            time.sleep(0.001)
            # time.sleep(2)
        elif i == 5:
            GPIO.output(outA1, GPIO.LOW)
            GPIO.output(outB1, GPIO.LOW)
            GPIO.output(outA2, GPIO.HIGH)
            GPIO.output(outB2, GPIO.HIGH)
            time.sleep(0.001)
            # time.sleep(2)
        elif i == 6:    
            GPIO.output(outA1, GPIO.LOW)
            GPIO.output(outB1, GPIO.LOW)
            GPIO.output(outA2, GPIO.LOW)
            GPIO.output(outB2, GPIO.HIGH)
            time.sleep(0.001)
            # time.sleep(2)
        elif i == 7:    
            GPIO.output(outA1, GPIO.HIGH)
            GPIO.output(outB1, GPIO.LOW)
            GPIO.output(outA2, GPIO.LOW)
            GPIO.output(outB2, GPIO.HIGH)
            time.sleep(0.001)
            # time.sleep(2)
        if i == 7:
            i = 0
            continue
        else:
            i += 1
      
              
except KeyboardInterrupt:
    GPIO.cleanup()