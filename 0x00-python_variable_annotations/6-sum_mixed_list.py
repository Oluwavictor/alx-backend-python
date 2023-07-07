#!/usr/bin/env python3
'''
    Task 6: Write a type-annotated function sum_mixed_list
'''
from typing import List, Union


def sum_mixed_list(mixed_list: List[Union[int, float]]) -> float:
    '''
        Computes the sum of a list of integers and floating-point numbers.
    '''
    return float(sum(mixed_list))
