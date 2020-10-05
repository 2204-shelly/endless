import asyncio
import sys

def start(handler):
    if len(sys.argv) == 1:
        print(f'Usage: {sys.argv[0]} PORT', file=sys.stderr)
        sys.exit(1)
    port = int(sys.argv[1])

    loop = asyncio.get_event_loop()
    coro = asyncio.start_server(handler, '0.0.0.0', port, loop=loop)
    server = loop.run_until_complete(coro)

    # Serve requests until Ctrl+C is pressed
    print('Serving on {}'.format(server.sockets[0].getsockname()))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    # Close the server
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()

