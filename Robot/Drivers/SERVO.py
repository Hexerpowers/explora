# noinspection PyUnresolvedReferences
import RPi.GPIO as GPIO
from threading import Thread
import time


class SERVO:
    def __init__(self, pin):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        self.speed = 127
        self.pin = int(pin)
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin, 50)
        self.position = 7.5
        self.pwm.start(self.position)
        self.thread = Thread(target=self.update, daemon=True, args=()).start()

    def __exit__(self, exc_type, exc_val, exc_tb):
        GPIO.cleanup()

    def move(self, speed):
        self.speed = speed

    def update(self):
        time.sleep(1)
        while True:
            if self.speed > 127:
                self.position = self.position + 0.25
                if self.position > 11.5:
                    self.position = 11.5
                self.pwm.ChangeDutyCycle(self.position)
            elif self.speed < 127:
                self.position = self.position - 0.25
                if self.position < 4:
                    self.position = 4
                self.pwm.ChangeDutyCycle(self.position)
            else:
                self.pwm.ChangeDutyCycle(0)
            time.sleep(0.2)
