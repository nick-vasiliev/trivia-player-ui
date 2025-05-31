Not given up on this, just taking a break while working on other things. WIP!
# Trivia
This repo contains 3 applications/modules that are part of a trivia game.

## trivia-ui
A UI Module that will display questions, scores and answers.

Recieves objects:
```
{
  "initialTime": 10, // initial time to answer the question
  "question": {
    "text":"What is love?" // question text, the question to be answered
    "choices": [
        "Baby don't hurt me",
        "Don't hurt me",
        "No more"
    ]
  }
}
```

## ui
A UI module that has an interface for players to answer questions shown on *trivia-ui*.

## host
The controller for *trivia-ui* and *ui* that performs the logic to host the game.

## Other notes
This is a project I'm doing in my freetime to learn React and AWS (intent is to host this with ECS).

## universal-remote
A driver application that allows sending data to *host*, used for debugging and testing.

## What is used
### Typescript
https://react.dev/learn/typescript, 

https://www.w3schools.com/typescript/typescript_getstarted.php

### React

### Python
Styleguide: https://google.github.io/styleguide/pyguide.html,

json library: https://docs.python.org/3/library/json.html

websockets library: https://websockets.readthedocs.io/en/stable/reference/asyncio/server.html
