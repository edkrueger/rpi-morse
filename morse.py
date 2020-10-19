import RPi.GPIO as GPIO

import time

from morse_lookup import char_to_morse

PHRASE = "SOS"

PIN = 5
DOT_DURATION = 100 / 1000

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.OUT)

def light_on(duration):
     GPIO.output(PIN, GPIO.HIGH)
     time.sleep(duration)
     GPIO.output(PIN, GPIO.LOW)

def dot():
     light_on(DOT_DURATION)

def dash():
     light_on(3 * DOT_DURATION)

def pause():
     time.sleep(DOT_DURATION)

def signal_char(char):
     for bit in char_to_morse(char):
          if bit == ".":
               dot()
               pause()
          if bit == "-":
               dash()
               pause()

     # pause for 3 after each character
     for _ in range(3):
          pause()

def signal_string(s):
     for char in s:
          signal_char(char)

signal_string(PHRASE)
