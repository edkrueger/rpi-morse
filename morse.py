import RPi.GPIO as GPIO
import time

PIN = 5
DOT_DURATION = 1

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

def s():
     dot()
     pause() 
     dot()
     pause() 
     dot()
     pause() 

def o():     
     dash()
     pause() 
     dash()
     pause() 
     dash()
     pause() 

def sos():
     s()
     o()
     s()

sos()


