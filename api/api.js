const express = require('express');

const app = express();
const PORT = 9002;

app.get('/answers', (req, res)=>{
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