# https://learn.sparkfun.com/tutorials/easy-driver-hook-up-guide
#
# MS1	MS2	Microstep Resolution
# L 	L	Full Step (2 Phase)
# H 	L	Half Step
# L 	H	Quarter Step
# H 	H	Eigth Step (Default configuration)

from time import sleep
import RPi.GPIO as GPIO

PIN_RELAY  = 17
PIN_MS1  = 26
PIN_STEP = 13
PIN_DIR  = 6
PIN_MS2  = 19

DIR_DOWN = GPIO.HIGH
DIR_UP = GPIO.LOW

DELAY = 0.00005
MAX_COUNT = 80000

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_RELAY , GPIO.OUT)
GPIO.setup(PIN_MS1 , GPIO.OUT)
GPIO.setup(PIN_STEP, GPIO.OUT)
GPIO.setup(PIN_DIR , GPIO.OUT)
GPIO.setup(PIN_MS2 , GPIO.OUT)

# Set Relay
GPIO.output(PIN_RELAY, GPIO.LOW)

# Set Microstep Type
GPIO.output(PIN_MS1, GPIO.LOW)
GPIO.output(PIN_MS2, GPIO.LOW)

# Set Direction
# GPIO.output(PIN_DIR, DIR_DOWN)
GPIO.output(PIN_DIR, DIR_UP)


count = 0
try:
    while count < MAX_COUNT:
        count += 1
        GPIO.output(PIN_STEP, GPIO.HIGH)
        sleep(DELAY)
        GPIO.output(PIN_STEP, GPIO.LOW)
        sleep(DELAY)
except KeyboardInterrupt:
    GPIO.output(PIN_RELAY, GPIO.HIGH)
    GPIO.cleanup()
    raise

GPIO.output(PIN_RELAY, GPIO.HIGH)
GPIO.cleanup()