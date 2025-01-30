import { useRef } from "react";

export function CustomSender({send}: (text: string) => void) {

  const textRef = useRef(null);

  return (
      <div className="CustomSender">
      <p>Custom Send</p>
      <input ref={textRef} /><button onClick={() => send(textRef.current.value)}>Send</button>
      </div>
  );
}