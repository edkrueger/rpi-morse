import RPi.GPIO as GPIO
import time

PIN = 5
DURATION = 1
MAX_BLINKS = 10

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.OUT)

blinks = 0
while blinks < MAX_BLINKS:
     GPIO.output(PIN, GPIO.HIGH)
     time.sleep(DURATION)
     GPIO.output(PIN, GPIO.LOW)
     time.sleep(DURATION)
     blinks += 1



