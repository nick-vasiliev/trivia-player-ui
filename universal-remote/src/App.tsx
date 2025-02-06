import { useEffect, useState, useRef } from 'react';
import './App.css';
import { CustomSender } from './components/CustomSender.tsx';
import { DisplayMessages } from './components/DisplayMessages.tsx';

function App() {
  const [ws_responses, set_ws_responses] = useState([]);
  const [ws_responses_key, set_ws_responses_key] = useState(0)

  const ws = useRef<WebSocket | null>(null);
  useEffect(() => {
    const socket = new WebSocket("ws://192.168.0.15:8765");
    socket.addEventListener("message", event => { // TODO: https://developer.mozilla.org/en-US/docs/Web/API/WebSocket CODE FOR OTHER EVENTS
      console.log(event.data)
      let parse_message = JSON.parse(event.data);
      set_ws_responses([{"text":parse_message.response,"key":ws_responses_key},...ws_responses.slice(0,21)]);
      set_ws_responses_key( i => i+1 )
    });
    socket.addEventListener("open", event => {
      console.log("open");
    });
    ws.current = socket;

    return () => socket.close()
  }, []);

  function send(msg: string) : void {
    if (!ws.current) console.log("WS not open");
    else ws.current.send(msg);
  }

  return (
    <div className="App">
      <h1>Universal driver for trivia <i>host</i>.</h1>
      <CustomSender send={send} />
      <DisplayMessages responses={ws_responses} />
    </div>
  );
}

export default App;
