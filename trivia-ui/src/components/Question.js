export function Question( props ) {
    const choiceList = props.question.choices.map((choice) =>
        <li key={choice.id}>{choice.text}</li>
    );
    return (
        <div className="question">
            <h1>{props.question.text}</h1>
            {choiceList}
        </div>
    )
}