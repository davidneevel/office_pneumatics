from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

pin = 14

GPIO.setup(pin,GPIO.OUT)
GPIO.setup(40,GPIO.OUT)

while True:
    print "%d on" % pin
    GPIO.output(pin, GPIO.HIGH)
    sleep(1)



    print "%s off" % pin
    GPIO.output(pin, GPIO.LOW)
    sleep(1)

