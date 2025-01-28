export function Question( props ) {
    const choiceList = props.choices.map((choice) =>
        <li key={choice.id}>{choice.text}</li>
    );
    return (
        <div className="question">
            <h1>{props.question}</h1>
            {choiceList}
        </div>
    )
}