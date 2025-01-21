const express = require('express');
var cors = require('cors')

const app = express();
const PORT = 9002;

app.get('/answers', (req, res)=>{
    res.status(200);
    res.send("welcome");
});

app.get('/question', cors(), (req, res)=>{
    res.status(200);
    res.send("welcome");
});

app.listen(PORT, (error) =>{
    if(!error)
        console.log("Server started port: "+ PORT)
    else 
        console.log("Startup error", error);
    }
);