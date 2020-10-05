import server

import asyncio
import random

async def handler(_reader, writer):
    try:
        while True:
            writer.write(b'%x\r\n' % random.randint(0, 2**32))
            await writer.drain()
            await asyncio.sleep(5)
    except ConnectionResetError:
        pass

server.start(handler)
