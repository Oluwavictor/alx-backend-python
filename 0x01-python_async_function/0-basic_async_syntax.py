#!/usr/bin/env python3
'''
    asynchronous coroutine that takes in an integer argument
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''generates random number of seconds.
    '''
    waiting_time = random.random() * max_delay
    await asyncio.sleep(waiting_time)
    return waiting_time
