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

    def __repr__(self):
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
            return self.get_name() == other.get_name()
        return False
    
    def get_name(self):
        """Get player's name
        
        Returns (str): self.name
        """
        return self.name
    
class Question:
    """Given to a player to provide an answer.

    Attributes:
        id (int): unique identifier for the question, to ensure it does not recieve and answer for a different question.
        handler (callable): function to call to handle the result of the question.
        params (dict): python dict representation of params sent to player.
        answers (dict[]): a list of answers from Player(s) to be marked by handler.
    """
    def __init__(self, id: int, handler: callable, params: dict):
        """Initializes a Question.
        
        Args:
            id (int): Identifier for the Question, should be unique.
            handler (callable): function to mark answers.
            params: params to give the Player(s).
        """
        self.id = id
        self.handler = handler 
        self.params = params
        self.answers = {}

    def get_id(self):
        """Return id.
        
        Returns:
            (int): self.id
        """
        return self.id
    
    def add_answer(self, answer: dict, player: str) -> None:
        """Add an answer to be marked. 
        If player has already submitted this answer, replace their old one.
        
        Args:
            answer (dict): answer dict for this question.
            player (str): name of the player who submitted answer
        """
        self.answers[player]=answer
        return

class Game:
    """A Game of trivia.

    Attributes:
        in_progress (bool): Is the game currently running?
        code (str): Identifier for the room.
        players (Player[]): Player(s) in the game.
        question (Question): Current question being played.
    """
    def __init__(self):
        """Initialize a Game"""
        self.in_progress = False
        self.code = "NICK"
        self.players = []
        self.question = None
    
    def has_player(self, player: Player):
        """Check if Game has this player

        Args:
            player (Player): Player to check.
        
        Returns:
            bool: Does this Player exist in the Game?
        """
        print("aaaa:",player, self.players)
        for existing_player in self.players:
            if existing_player == player:
                return True
        return False
    
    def check_code(self, check_code:str) -> bool:
        """Check if the room code is valid for this Game.
        Args:
            check_code (str): Game code to check.

        Returns:
            bool: Do the codes match?
        """
        return check_code == self.code

    def join(self, name: str) -> bool:
        """Adds a player to the game.

        Args:
            name (str): name of Player to add.
        
        Returns:
            bool: If player was added successfully.
        """
        player = Player(name)
        if self.has_player(player):
            return False
        self.players.append(player)
        return True
    
    def answer(self, message: dict) -> bool:
        """Take answer from a Player and store it in current Question's answers.

        Args:
            message (dict): decoded json of Player answer message.
        
        Returns:
            bool: Was adding the answer a success?
        """
        if self.question.get_id != message['parameters']["question_id"]:
            return False
        self.question.add_answer( message['parameters'],message['name'])
        print( self.question.answers ) # TODO: rm debug print
        return True

    def handle_message(self, message: dict) -> str:
        """Pass message parameters to the correct function, and handle return.

        Args:
            message (dict): decoded json of message.
        
        Returns:
            string: Response to send client.
        """
        # Validate code
        if not self.check_code(message['code']):
            return {"response":"Invalid Code"}
        
        action = message['action']
        if action == "check code":
            return {"response":"Success"}
        if action == 'join':
            if (self.join(message['name'])):
                return {"response":"Success"}
            return {"response":"Invalid Name"}
        if action == "answer":
            if not self.answer(message):
                return {"response":"Invalid Question Id"}
            return {"response":"Success"}
        return {"response":"Invalid Action"}