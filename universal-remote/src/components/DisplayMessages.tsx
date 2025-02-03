export function DisplayMessages({responses}: string[]) {

  return (
      <div className="DisplayMessages">
      <h3>Response:</h3>
      {responses.map( (message) => 
        <li key={message.key}>{message.text}</li>
      )}
      </div>
  );
}