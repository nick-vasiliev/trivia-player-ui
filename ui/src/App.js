import './App.css';

async function getQuestion() {
  const q = await fetch('http://localhost:9002/question');
  const response = q.json();
  console.log(response);
};

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Trivia</h1>
        <button type="button" onClick={getQuestion}>Click Me!</button>
      </header>
    </div>
  );
}

export default App;
