import asyncio
from websockets.asyncio.server import serve
import json
import game

async def run() -> None: # TODO: This eventually has to be built concurrent for many simultaneous games.
    """Run Game loop."""
    while not running_game.in_progress:
        await asyncio.sleep(1) # await to allow other tasks to go

async def handle_conn(websocket): # TODO: authentication - certificates? to authenticate different connections. For now, assume trust
    async for message in websocket: # websocket has an id
        try:
            message_dict = json.loads(message)
            message_respond = running_game.handle_message(message_dict, websocket.id)
        except ValueError:
            message_respond = {"response":"Error decoding json"}
        finally:
            await websocket.send(json.dumps(message_respond))
async def main():
    game_task = asyncio.create_task(run())
    async with serve(handle_conn, "0.0.0.0", 8765) as server:
        await server.serve_forever()

if __name__ == "__main__":
    running_game = game.Game("NICK",123)
    asyncio.run(main())