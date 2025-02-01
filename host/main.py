import asyncio
from websockets.asyncio.server import serve
import json
from game import Game
    
game = Game()

async def handle_conn(websocket): # TODO: authentication - certificates? to authenticate different connections. For now, assume trust
    async for message in websocket:
        try:
            message_dict = json.loads(message)
            game.handle_message(message_dict)
        except ValueError:
            print("Error decoding json")
            continue
        await websocket.send(message)

async def main():
    async with serve(handle_conn, "0.0.0.0", 8765) as server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())