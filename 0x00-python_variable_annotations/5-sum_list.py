#!/usr/bin/env python3
'''
    Task 5: Write a type-annotated function sum_list
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''
        Computes the sum of a list of floating-point numbers.
    '''
    total = 0.0
    for number in input_list:
        total += number
    return total
