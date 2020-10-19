import RPi.GPIO as GPIO
import time

PIN = 5
WAIT_DURATION = 1

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.OUT)

GPIO.output(PIN, GPIO.HIGH)
time.sleep(WAIT_DURATION)
GPIO.output(PIN, GPIO.LOW)
time.sleep(WAIT_DURATION)



