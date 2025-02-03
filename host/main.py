import asyncio
from websockets.asyncio.server import serve
import json
from game import Game

game = Game("NICK",123)
    
async def run_game():
    while not game.in_progress:
        await asyncio.sleep(1)
    print("Game is started!")

async def handle_conn(websocket): # TODO: authentication - certificates? to authenticate different connections. For now, assume trust
    async for message in websocket: # websocket has an id
        try:
            message_dict = json.loads(message)
            message_respond = game.handle_message(message_dict, websocket.id)
        except ValueError:
            message_respond = {"response":"Error decoding json"}
        finally:
            await websocket.send(json.dumps(message_respond))
async def main():
    game_task = asyncio.create_task(run_game())
    async with serve(handle_conn, "0.0.0.0", 8765) as server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())