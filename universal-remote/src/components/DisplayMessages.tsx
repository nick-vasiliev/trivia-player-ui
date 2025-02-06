type Response = { // todo, put this in some types folder
  text:string;
  key:number;
};

export function DisplayMessages({responses}: {responses: Response[]}) {
  return (
      <div className="DisplayMessages">
      <h3>Response:</h3>
      {responses.map( (message) => 
        <li key={message.key}>{message.text}</li>
      )}
      </div>
  );
}