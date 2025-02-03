import { useRef } from "react";

export function CustomSender({send}: (text: string) => void) {

  const textRef = useRef("");

  return (
      <div className="CustomSender">
      <h3>Custom Send:</h3>
      <textarea ref={textRef} rows={20} cols={50} />
      <br></br><button onClick={() => send(textRef.current.value)}>Send</button>
      </div>
  );
}