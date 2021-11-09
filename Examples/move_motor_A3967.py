# https://learn.sparkfun.com/tutorials/easy-driver-hook-up-guide
#
# MS1	MS2	Microstep Resolution
# L 	L	Full Step (2 Phase)
# H 	L	Half Step
# L 	H	Quarter Step
# H 	H	Eigth Step (Default configuration)

from time import sleep
import RPi.GPIO as GPIO

PIN_SLP  = 5
PIN_MS1  = 6
PIN_STEP = 13
PIN_DIR  = 19
PIN_MS2  = 26

DIR_CW = GPIO.HIGH
DIR_CCW = GPIO.LOW

DELAY = 0.01

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_SLP , GPIO.OUT)
GPIO.setup(PIN_MS1 , GPIO.OUT)
GPIO.setup(PIN_STEP, GPIO.OUT)
GPIO.setup(PIN_DIR , GPIO.OUT)
GPIO.setup(PIN_MS2 , GPIO.OUT)


# Set Direction
GPIO.output(PIN_SLP, GPIO.HIGH)

# Set Microstep Type
GPIO.output(PIN_MS1, GPIO.LOW)
GPIO.output(PIN_MS2, GPIO.LOW)

# Set Direction
GPIO.output(PIN_DIR, DIR_CW)

try:
    while True:
        GPIO.output(PIN_STEP, GPIO.HIGH)
        sleep(DELAY)
        GPIO.output(PIN_STEP, GPIO.LOW)
        sleep(DELAY)
    
except KeyboardInterrupt:
    GPIO.cleanup()
    raise