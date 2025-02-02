"""Classes and functions for running a game.
Game allows a game of trivia to be played with Player(s) and Question(s).
Typical usage:
game = Game() # returns a game code ABCD
game.check_code("ABCD") # from player A
game.join("A")
"""
from uuid import UUID

class Player:
    """Player of a trivia game.

    Attributes:
        score (int): Their score in the game.
        name (str): What the player is called.
        ws_id (UUID): Websocket the player is sent from. # TODO: when a ws is closed, handle this and allow for them to reconnect
    """
    def __init__(self, name: str, ws_id: UUID):
        """Initializes them a player with their name.
        
        Args:
            name (str): How the player is called.
        """
        self.score = 0
        self.name = name
        self.ws_id = ws_id

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
        screen_id (UUID): ws_id of the screen displaying questions.
    """
    def __init__(self, code: str, screen_id: UUID):
        """Initialize a Game.
        
        Args:
            code (str): code for the game.
            screen_id (UUID): ws_id of the screen.
        """
        self.code = code 
        self.screen_id = screen_id

        self.in_progress = False
        self.players = []
        self.question = None
    
    def find_player(self, name: str) -> Player:
        """Get player with this name if they exist.

        Args:
            name (str): Player name to check.
        
        Returns:
            Player: Player with name, or None if not found.
        """
        for existing_player in self.players:
            if existing_player.name == name:
                return existing_player
        return None # not found
    
    def auth_player(self, name: str, ws_id: UUID):
        """Confirm a player exists and name matches their ws_id.

        Args:
            name (str): Name to check.
            ws_id (UUID): UUID to confirm player against.
        """
        existing_player = self.find_player(name)
        if existing_player is None:
            return False
        if ws_id == existing_player.ws_id:
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

    def join(self, name: str, ws_id: UUID) -> bool:
        """Adds a player to the game.

        Args:
            name (str): name of Player to add.
        
        Returns:
            bool: If player was added successfully.
        """
        if self.find_player(name) is not None:
            return False
        player = Player(name, ws_id)
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
    
    def handle_screen(self, message: dict) ->str:
        """Pass message parameters to the correct function, and handle return from screen ws_id.

        Args:
            message (dict): decoded json of message.
        
        Returns:
            string: Response to send client.
        """
        pass # TODO

    def handle_message(self, message: dict, ws_id: UUID) -> str:
        """Pass message parameters to the correct function, and handle return.

        Args:
            message (dict): decoded json of message.
            ws_id (UUID): unique id of websocket sending it.
        
        Returns:
            string: Response to send client.
        """
        print(ws_id)
        if ws_id == self.screen_id:
            self.handle_screen(message)

        # Validate code
        if not self.check_code(message['code']):
            return {"response":"Invalid Code"}
        
        action = message['action']

        action = message['action']
        if action == "start":
            pass #TODO
        
        # Does not require authentication
        if action == "check code":
            return {"response":"Success"}
        if action == 'join':
            if (self.join(message['name'], ws_id)):
                return {"response":"Success"}
            return {"response":"Invalid Name"}
        
        # Requires game start
        if not self.in_progress:
            return {"response": "Invalid Action"}
        
        # Requires authentication
        if not self.auth_player(message['name'],ws_id):
            return {"response":"Unauthorized"}
        if action == "answer":
            if not self.answer(message):
                return {"response":"Invalid Question Id"}
            return {"response":"Success"}
        
        # Not found
        return {"response":"Invalid Action"}