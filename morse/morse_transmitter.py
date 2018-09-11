#!/usr/bin/env python3
# Ensure argparse is correctly implemented --------- ***
import argparse
import RPi.GPIO as GPIO
from text_to_morse import morse_generator as mg
import time


parser = argparse.ArgumentParser()
parser.add_argument("pin", help="Specify pin number for GPIO transmission",
                    type=int)
args = parser.parse_args()


def transmit(pin, morse, time_unit=2.5):
    if morse == 1:
        print("Sorry, that message is not supported. Terminating...")
        sys.exit(1)
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(pin, GPIO.OUT)
    print("Transmitting...")
    for letter in morse:
        for sym in letter:
            GPIO.output(pin, GPIO.HIGH)
            if sym == '.':
                time.sleep(time_unit)
            elif sym == '_':
                time.sleep(time_unit * 3)
            elif sym == ' ':
                GPIO.output(pin, GPIO.LOW)
                time.sleep(time_unit * 7)
            GPIO.output(pin, GPIO.LOW)
            time.sleep(time_unit)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(time_unit * 3)
    print("Message transmitted. Thank you for using Raspberry Pi Morse",
          "Communication Services.")
    GPIO.cleanup(pin)
    
def establish_difficulty():
    difficulty = input("Are your morse skills beginner(1), intermediate(2) or advanced(3)? ")
    if difficulty == "1":
        time_unit = 0.25
    elif difficulty == "2":
        time_unit = 0.2
    elif difficulty == "3":
        time_unit = 0.15
    else:
        print("Sorry, that difficulty is not recognised. Defaulting to beginner.")
        time_unit = 0.25
    return time_unit



if __name__ == "__main__":
    print("Welcome to the Raspberry Pi Morse Communication Services.")
    difficulty = establish_difficulty()
    text = input("Please type your message here: ")
    morse_code = mg(text)
    transmit(args.pin, morse_code, difficulty)
