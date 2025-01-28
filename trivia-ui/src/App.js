import './App.css';

async function getQuestion() {
  const q = await fetch('http://localhost:9002/question');
  const response = q.json();
  console.log(response);
};

const socket = new WebSocket("ws://192.168.0.13:8765")
socket.addEventListener("open", event => {
  socket.send("Connection established")
});
// Listen for messages
socket.addEventListener("message", event => {
  console.log("Message from server ", event.data)
});

function sendChoice(id) {
  socket.send(id.toString());
}

function App() {
  return (
    <div className="App">
      <p>Hi</p>
    </div>
  );
}

export default App;
