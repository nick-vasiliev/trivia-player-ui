import './App.css';
import { CustomSender } from './components/CustomSender.tsx';

const socket = new WebSocket("ws://192.168.0.13:8765")

socket.addEventListener("message", event => {
  console.log("Message from server ", event.data)
});

function send(text: string) {
  socket.send(text);
}

function App() {
  return (
    <div className="App">
      <h1>Universal driver for trivia <i>host</i>.</h1>
      <CustomSender send={send} />
    </div>
  );
}

export default App;
