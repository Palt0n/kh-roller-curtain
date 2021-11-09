from time import sleep
import RPi.GPIO as GPIO
import sys
from Libraries.filelock import FileLock
import os

PATH_CURTAIN_LOCK = "curtain"
PATH_CURTAIN_DIRECTION = "curtain"

fl = FileLock("curtain", timeout=1, delay=.05, timerelease=100)
fl.acquire()

path_dir = os.path.join(os.getcwd(), "{}.direction".format(PATH_CURTAIN_DIRECTION))
if os.path.isfile(path_dir):
    with open(path_dir, "r") as fh:
        curtain_state = fh.read().rstrip()
else:
    curtain_state = "DOWN"

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
if curtain_state == "UP":
    GPIO.output(PIN_DIR, DIR_DOWN)
elif curtain_state == "DOWN":
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

with open(path_dir, "w+") as fh:
    if curtain_state == "UP":
        fh.write("DOWN")
    elif curtain_state == "DOWN":
        fh.write("UP")
    else:
        raise ValueError("Unexpected")

fl.release()