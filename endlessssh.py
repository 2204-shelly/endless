import server

import asyncio
import random

async def handler(_reader, writer):
    try:
        while True:
            await asyncio.sleep(10)
            writer.write(b'%x\r\n' % random.randint(0, 2**32))
            await writer.drain()
    except ConnectionResetError:
        pass

server.start(handler)
