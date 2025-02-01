import asyncio
from websockets.asyncio.server import serve
import json

class Player:
    """Player of a trivia game.

    Attributes:
        score (int): Their score in the game.
        name (str): What the player is called.
    """
    def __init__(self, name: str):
        """Initializes them a player with their name.
        
        Args:
            name (str): How the player is called.
        """
        self.score = 0
        self.name = name

    def __str__(self):
        """Represent Player as <name>: <score>"""
        return f"{self.name}: {self.score}"
    
    def __eq__(self, other):
        """Players with the same name are 'equal'.
        
        Args:
            other (Any): Compare self to other
        
        Returns:
            bool: True if they share name
        """
        if isinstance(other, Player):
            return self.getName == other.getName()
        return False
    
    def getName(self):
        """Get player's name
        
        Returns (str): self.name
        """
        return self.name

class Game:
    """A Game of trivia.

    Attributes:
        in_progress (bool): Is the game currently running?
        code (str): Identifier for the room.
        players (Player[]): Player(s) in the game.
    """
    def __init__(self):
        """Initialize a Game"""
        self.in_progress = False
        self.code = "NICK"
        self.players = []
    
    def has_player(self, player: Player):
        """Check if Game has this player

        Args:
            player (Player): Player to check.
        
        Returns:
            bool: Does this Player exist in the Game?
        """
        for existing_player in self.players:
            if existing_player == player:
                return True
        return False

    def join(self, player: Player) -> bool:
        """Adds a player to the game.

        Args:
            player (Player): Player to add.
        
        Returns:
            bool: If player was added successfully.
        """
        if self.has_player(player):
            return False
        self.players.append(player)
        return True
    
game = Game()

def handle_player(message: dict):
    """Handle a message from a Player
    
    Args:
        message (dict): message from the player.

    Returns:
        str: Response to send the player.
    """
    action = message['action']
    if action == 'join':
        print(game.join(message['parameters']['name']))
        print( game.players )

async def handle_conn(websocket): # TODO: authentication - certificates? to authenticate different connections. For now, assume trust
    async for message in websocket:
        try:
            message_dict = json.loads(message)
            handle_player(message_dict)
        except ValueError:
            print("Error decoding json")
            continue
        await websocket.send(message)

async def main():
    async with serve(handle_conn, "0.0.0.0", 8765) as server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())