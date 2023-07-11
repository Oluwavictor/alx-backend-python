#!/usr/bin/env python3
"""Task 1's module.
"""
from typing import List
from importlib import import_module as use


async_generator = use('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """returns a list of 10 numbers from a 10-number generator.
    """
    return [numb async for numb in async_generator()]
