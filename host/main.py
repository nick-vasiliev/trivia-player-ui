import asyncio
from websockets.asyncio.server import serve


async def handle_conn(websocket):
    async for message in websocket:
        await websocket.send(message)
        print(message)


async def main():
    async with serve(handle_conn, "0.0.0.0", 8765) as server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())