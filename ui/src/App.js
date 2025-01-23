import './App.css';
import { ChoiceLayout } from './components/ChoiceLayout';

async function getQuestion() {
  const q = await fetch('http://localhost:9002/question');
  const response = q.json();
  console.log(response);
};


const socket = new WebSocket("ws://localhost:8765")
socket.addEventListener("open", event => {
  socket.send("Connection established")
});
// Listen for messages
socket.addEventListener("message", event => {
  console.log("Message from server ", event.data)
});

function App() {
  const q_choices = [
    {id:0,text:"AAAAA"},
    {id:1,text:"CCCCCA"},
    {id:2,text:"BBBBA"},
    {id:3,text:"DDDD"},
    {id:4,text:"JJKASA"}
  ]
  return (
    <div className="App">
      <ChoiceLayout key={q_choices.id} choices={q_choices} question="What does the fox say?" />
    </div>
  );
}

export default App;
