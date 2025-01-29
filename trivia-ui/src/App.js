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
  const choices = [
      {"id": 0,"text":"aaaaa"},
      {"id": 1,"text":"BBbaa"}
    ]
  ;
  return (
    <div className="App">
      <Question question="What is the meaning?" choices={choices}/>
      <Timer initialTime={10} />
    </div>
  );
}

export default App;
