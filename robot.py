#!/usr/bin/python3
import pygame
import sys
import RPi.GPIO as GPIO
import os

pygame.init()
screen = pygame.display.set_mode((200, 200))


class Robot:
    def __init__(self):
        self.PIN_STATUS = 0
        self.PINS = [16, 18]
        self.K_UP = pygame.K_UP
        self.foward = 0
        self.right = 0
        self.left = 0
        self.DEBUG = 0

    def gpio_setup(self):
        # Setup the wiring
        GPIO.setmode(GPIO.BOARD)
        # Setup Ports
        for pin in self.PINS:
            GPIO.setup(pin, GPIO.OUT)

    def main(self):
        self.gpio_setup()
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        os.system("sudo shutdown -h now")
                        sys.exit()
                    if event.key == pygame.K_UP:
                        if self.DEBUG: print("pressing up")
                        self.foward = 1
                    if event.key == pygame.K_RIGHT:
                        if self.DEBUG: print("pressing right")
                        self.right = 1
                    if event.key == pygame.K_LEFT:
                        if self.DEBUG: print("pressing left")
                        self.left = 1
                if event.type == pygame.KEYUP:
                    if self.DEBUG: print("released")
                    self.foward = 0
                    self.right = 0
                    self.left = 0
            if self.foward:
                if self.DEBUG: print("pressing FOWARD")
                if self.PIN_STATUS == 0:
                    GPIO.output(self.PINS[0], 1)
                    GPIO.output(self.PINS[1], 1)
                    if self.DEBUG:
                        print("SO UMA VEZ")
                        print("FOWARD")
                if self.PIN_STATUS: pass
                self.PIN_STATUS = 1
            elif self.right:
                if self.DEBUG: print("pressing RIGHT")
                if self.PIN_STATUS == 0:
                    GPIO.output(self.PINS[0], 0)
                    GPIO.output(self.PINS[1], 1)
                    if self.DEBUG:
                        print("SO UMA VEZ")
                        print("RIGTH")
                if self.PIN_STATUS: pass
                self.PIN_STATUS = 1
            elif self.left:
                if self.DEBUG: print("pressing LEFT")
                if self.PIN_STATUS == 0:
                    GPIO.output(self.PINS[0], 1)
                    GPIO.output(self.PINS[1], 0)
                    if self.DEBUG:
                        print("SO UMA VEZ")
                        print("LEFT")
                if self.PIN_STATUS: pass
                self.PIN_STATUS = 1
            else:
                if self.DEBUG: print("released")
                if self.PIN_STATUS:
                    GPIO.output(self.PINS[0], 0)
                    GPIO.output(self.PINS[1], 0)
                    self.PIN_STATUS = 0

if __name__ == '__main__':
    try:
        robot = Robot()
        robot.main()
    finally:
        GPIO.cleanup()
        print("Closed Everything. END")
