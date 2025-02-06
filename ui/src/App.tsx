import './App.css';
import { ChoiceLayout } from './components/ChoiceLayout';
import { useCookies } from 'react-cookie';

const socket = new WebSocket("ws://192.168.0.13:8765")
socket.addEventListener("open", event => {
  socket.send("Connection established")
});
// Listen for messages
socket.addEventListener("message", event => {
  console.log("Message from server ", event.data)
});

function sendChoice(id): void {
  socket.send(id.toString());
}

function App() {
  const [cookies, setCookie, removeCookie] = useCookies([]);
  const q_choices = [
    {id:0,text:"AAAAA"},
    {id:1,text:"CCCCC"},
    {id:2,text:"BBBBA"},
    {id:3,text:"DDDD"},
    {id:4,text:"JJKASA"}
  ]
  return (
    <div className="App">
      <ChoiceLayout choices={q_choices} question="What does the fox say?" buttonClick={sendChoice} />
    </div>
  );
}

export default App;
