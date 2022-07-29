from time import sleep
import RPi.GPIO as GPIO
import sys
from Libraries.filelock import FileLock
import os

PATH_CURTAIN_LOCK = "~/kh-roller-curtain/curtain.lock"
PATH_CURTAIN_LOCK = os.path.expanduser(PATH_CURTAIN_LOCK)
PATH_CURTAIN_DIRECTION = "~/kh-roller-curtain/curtain.direction"
PATH_CURTAIN_DIRECTION = os.path.expanduser(PATH_CURTAIN_DIRECTION)

fl = FileLock("curtain", timeout=1, delay=.05, timerelease=100)
fl.acquire()

if os.path.isfile(PATH_CURTAIN_DIRECTION):
    with open(PATH_CURTAIN_DIRECTION, "r") as fh:
        curtain_state = fh.read().rstrip()
else:
    curtain_state = "DOWN"

PIN_RELAY  = 17
PIN_MS1  = 26
PIN_STEP = 13
PIN_DIR  = 6
PIN_MS2  = 19

DIR_DOWN = GPIO.LOW
DIR_UP = GPIO.HIGH

DELAY = 0.0002
MAX_COUNT = 31000

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
with open(PATH_CURTAIN_DIRECTION, "w+") as fh:
    if curtain_state == "UP":
        GPIO.output(PIN_DIR, DIR_DOWN)
        fh.write("DOWN")
        print('{"state": "down"}')
    elif curtain_state == "DOWN":
        GPIO.output(PIN_DIR, DIR_UP)
        fh.write("UP")
        print('{"state": "up"}')
    else:
        raise ValueError("Unexpected")

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


fl.release()