#!/usr/bin/python3

def multiple_returns(sentence):
    if len(sentence) == 0:
        return (0, None)
    else:
        length = len(sentence)
        return (length, sentence[0])
