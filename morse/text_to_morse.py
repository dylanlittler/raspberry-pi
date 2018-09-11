#!/usr/bin/env python3
from morse import characters as ch


def morse_generator(text):
    morse_chars = []
    for char in list(text.lower()):
        if char not in ch.keys():
            return 1
        morse_chars.append(ch[char])
    return morse_chars


if __name__ == "__main__":
    text = input("Please type your message: ")
    morse_code = morse_generator(text)
    if morse_code == 1:
        print("Sorry, I don't know that letter. Terminating...")
    else:
        print(morse_code)
