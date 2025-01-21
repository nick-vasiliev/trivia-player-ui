const express = require('express');
var cors = require('cors')

const app = express();
const PORT = 9002;

var question = {
    id:1,
    text:"What is a cat called?",
    choices:["Cat","Dog","Steven","Schweppe"]
}

app.get('/answers', (req, res)=>{
    res.status(200);
    res.send({"alan":"answer"});
});

app.get('/question', cors(), (req, res)=>{
    res.status(200);
    res.send(question);
});

app.listen(PORT, (error) =>{
    if(!error)
        console.log("Server started port: "+ PORT)
    else 
        console.log("Startup error", error);
    }
);