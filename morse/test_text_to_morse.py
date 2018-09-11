#!/usr/bin/env python3

import pytest
from text_to_morse import morse_generator

def test_morse_generator():
    assert morse_generator('sos') == ['...', '___', '...']
