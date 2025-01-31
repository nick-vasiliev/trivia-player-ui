import asyncio
from websockets.asyncio.server import serve

class Player:
    def __init__(self, name):
        self.score = 0
        self.name = name

    def __str__(self):
        return f"{self.name}: {self.score}"

class Game:
    def __init__(self):
        self.in_progress = False
        self.code = "NICK"
        self.players = []

async def handle_conn(websocket):
    async for message in websocket:
        # TODO: authentication - certificates? to authenticate different connections. For now, assume trust
        if message.startswith("SCREEN"):
            print(f"SCREEN: {message[6:]}")
            return
        # Player
        print(message)

        await websocket.send(message)

async def main():
    async with serve(handle_conn, "0.0.0.0", 8765) as server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())