#!/usr/bin/env python3

def return_evens(sequence):
    return [num for num in sequence if num % 2 == 0]


result_evens = return_evens([0, 1, 3, 5, 7, 8, 9])
print(result_evens)  # Output: [0, 8]


def make_exclamation(sentences):
    return [sentence + '!' for sentence in sentences]


result_exclamation = make_exclamation(["Hello", "I'm doing great", "Python is fun"])
print(result_exclamation)