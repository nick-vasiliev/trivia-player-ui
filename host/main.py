import asyncio
from websockets.asyncio import server
import json
import game

async def run(game_server) -> None: # TODO: This eventually has to be built concurrent for many simultaneous games, running_game would become a parameter.
    """Run Game loop."""
    while not running_game.in_progress:
        await asyncio.sleep(1) # await to allow other tasks to go
    print("Starting")
    await server.broadcast(game_server.connections, message='{"action":"game status","game_status":"Begin"}', raise_exceptions=True) # TODO: unset raise
    print("Done")

async def handle_conn(websocket): # TODO: authentication - certificates? to authenticate different connections. For now, assume trust
    async for message in websocket: # websocket has an id
        try:
            message_dict = json.loads(message)
            message_respond = running_game.handle_message(message_dict, websocket.id)
        except:
            message_respond = {"response":"Error decoding json"} # logging
        finally:
            await websocket.send(json.dumps(message_respond))
            print(message_respond)
async def main():
    async with server.serve(handle_conn, "0.0.0.0", 8765) as game_server:
        game_task = asyncio.create_task(run(game_server))
        await game_server.serve_forever()

if __name__ == "__main__":
    running_game = game.Game("NICK",123)
    asyncio.run(main())