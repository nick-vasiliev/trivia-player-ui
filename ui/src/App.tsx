import { useEffect, useRef, useState } from 'react';
import './App.css';
import { ChoiceLayout } from './components/ChoiceLayout';
import { CodeEntry } from './components/CodeEntry.tsx';
import { useCookies, withCookies } from 'react-cookie';
import { BrowserRouter, Route, Routes } from "react-router-dom";

interface Message {
  action: string;
  parameters?: object; // REMINDER, THIS NEEDS TO CHANGE AND BE FLATTENED INTO SEVERAL PARAMS (task for tomorrow, goodnight!)
  code: string;
}

function App() {
  const [cookies, setCookie, removeCookie] = useCookies([]);
  const [stage, setStage] = useState<string>("code");

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

  function send(msg: Message): void {
    if (!ws.current) console.log("WS not open!"); // TODO: handle this with a UI notif!
    else ws.current.send(JSON.stringify(msg));
  };

  function sendCode(code: string): void {
    let msg: Message = {action:"check code", "code":code};
    send(msg);
  }

  return (
    <div className="App">
      <CodeEntry onSubmit={sendCode} />
    </div>
  );
}

export default App;
