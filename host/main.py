import asyncio
from websockets.asyncio.server import serve
import json
from game import Game

game = Game()
    
async def run_game():
    print("hello")
    await asyncio.sleep(10)
    print("hello again")

async def handle_conn(websocket): # TODO: authentication - certificates? to authenticate different connections. For now, assume trust
    async for message in websocket: # websocket has an id
        try:
            message_dict = json.loads(message)
            print(game.handle_message(message_dict, websocket.id))
        except ValueError:
            print("Error decoding json")
            continue
        await websocket.send(message)

async def main():
    game_task = asyncio.create_task(run_game())
    async with serve(handle_conn, "0.0.0.0", 8765) as server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())