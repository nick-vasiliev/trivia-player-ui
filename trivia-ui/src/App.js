import './App.css';
import { Question } from './components/Question.js';
import { Timer } from './components/Timer.js';

async function getQuestion() {
  const q = await fetch('http://localhost:9002/question');
  const response = q.json();
  console.log(response);
};

const socket = new WebSocket("ws://192.168.0.13:8765")
socket.addEventListener("open", event => {
  socket.send("Connection established")
});
// Listen for messages
socket.addEventListener("message", event => {
  console.log("Message from server ", event.data)
});

function sendChoice(id) {
  socket.send(id.toString());
}

function App() {
  const delivery = {
    "initialTime": 10, // initial time to answer the question
    "question": {
      "text":"What is love?", // question text, the question to be answered
      "choices": [
          {"id":0,"text":"Baby don't hurt me"},
          {"id":1,"text":"Don't hurt me"},
          {"id":2,"text":"No more"}
      ]
    }
  };

  return (
    <div className="App">
      <Timer initialTime={10} />
      <Question question={delivery.question}/>
    </div>
  );
}

export default App;
