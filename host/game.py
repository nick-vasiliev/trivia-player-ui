"""Classes and functions for running a game.
Game allows a game of trivia to be played with Player(s) and Question(s).
Typical usage:
game = Game() # returns a game code ABCD
game.check_code("ABCD") # from player A
game.join("A")
"""

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
    
class Question:
    """Given to a player to provide an answer.
    Attributes:
        handler (callable): function to call to handle the result of the question.
        params (dict): python dict representation of params sent to player.
    """
    def __init__(self, handler: callable, params: dict):
        self.handler = handler 
        self.params = params

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
    
    def check_code(self, check_code:str) -> bool:
        """Check if the room code is valid for this Game.
        Args:
            check_code (str): Game code to check.

        Returns:
            bool: Do the codes match?
        """
        return check_code == self.code

    def handle_message(self, message: dict) -> str:
        """Handle and process a message from a client.

        Args:
            message (dict): decoded json of message.
        
        Returns:
            string: Response to send client.
        """
        if not self.check_code(message['code']):
            return {"response":"Invalid Code"}
        action = message['action']
        if action == "check code":
            print("good code")
            return {"response":"Valid Code"}
        if action == 'join':
            print(self.join(message['parameters']['name']))
            print( self.players )
            return
        print("unidentified")