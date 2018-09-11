#!/usr/bin/env python3
import argparse
import RPi.GPIO as GPIO
import time


parser = argparse.ArgumentParser()
parser.add_argument("interval", help="specify the gap between lights",
                    nargs='?', const=1, type=int, default=3)
parser.add_argument("time_unit", help="specify the time interval for lights to change",
                    nargs='?', const=1, type=float, default=0.5)
args = parser.parse_args()


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


def alternate():
    while True:
        for group in range(args.interval):
            for pin in range(group, 25, args.interval):
                GPIO.setup(pin, GPIO.OUT)
                GPIO.output(pin, GPIO.HIGH)
            time.sleep(args.time_unit)
            for pin in range(group, 25, args.interval):
                GPIO.output(pin, GPIO.LOW)


if __name__ == "__main__":
    alternate()
