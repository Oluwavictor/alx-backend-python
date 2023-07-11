#!/usr/bin/env python3
'''Module for measure_runtime
'''
import asyncio
import time
from importlib import import_module as use


async_comprehension = use('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Async function for measure_runtime
    '''
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end_time = time.time()
    return (end_time - start_time)
