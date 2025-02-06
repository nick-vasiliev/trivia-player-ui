import { useEffect, useRef } from 'react';
import './App.css';
import { ChoiceLayout } from './components/ChoiceLayout';
import { useCookies } from 'react-cookie';

function App() {
  const [cookies, setCookie, removeCookie] = useCookies([]);

  const ws = useRef<WebSocket | null>(null); // null when uninitiliazed
  useEffect(() => {
    const socket = new WebSocket("ws://192.168.0.15:8765");
    const message_handler = (event) => { // TODO: https://developer.mozilla.org/en-US/docs/Web/API/WebSocket CODE FOR OTHER EVENTS
      let parse_message = JSON.parse(event.data);
      console.log(parse_message);
    }
    socket.addEventListener("message", message_handler );
    socket.addEventListener("open", event => {
      console.log("open"); // TODO
    });
    ws.current = socket;

    return () => socket.close();
  },[]);

  function sendChoice(id: int): void {
    if (!ws.current) console.log("WS not open!"); // TODO: handle this with a UI notif!
    else ws.current.send(id.toString());
  };

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
