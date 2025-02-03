"""This module exists to provide questions until I connect to dynamodb.
"""
import json

class QuestionDatabase:
    """Object to provide quesstions as though it was a noSQL database.

    Attributes:
        questions (dict[]): List of json (as dict) string questions.
    """
    def __init__(self):
        """Initialise a QuestionDatabase, see game.py for Question"""
        self.questions = [
            {"question_id":1,"type":"multiple_choice","player_params":{"choices":[1,2,3,4,5,6]},"handler_params":{"answer":1}},
            {"question_id":2,"type":"multiple_choice","player_params":{"choices":["a","2","c"]},"handler_params":{"answer":"a"}},
            {"question_id":3,"type":"multiple_choice","player_params":{"choices":[11,22,33,44,55]},"handler_params":{"answer":22}},
            {"question_id":4,"type":"multiple_choice","player_params":{"choices":[10,20,30,40]},"handler_params":{"answer":30}}
        ]
    def get_question(self, id:int) -> str:
        if id >= len(self.questions):
            return None
        for question in self.questions:
            if question['question_id'] == id:
                return json.dumps(question)
        return None
