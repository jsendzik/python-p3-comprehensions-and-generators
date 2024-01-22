#!/usr/bin/env python3

def return_evens(num_list):
    evens = []
    for n in num_list:
        if n % 2 == 0:
            evens.append(n)
    return evens

def make_exclamation(sentence_list):
    sent = []
    if len(sentence_list) == 0:
        return sent
    else:
        for s in sentence_list:
            sent.append(s + "!")
        return sent