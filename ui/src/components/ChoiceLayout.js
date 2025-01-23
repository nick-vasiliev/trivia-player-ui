export function ChoiceLayout( props ) {
    const choice_n = props.choices.length;
    const choiceArray = [];
    for ( let i=0; i < choice_n-1; i=i+2 ) {
        choiceArray.push(
            <tr key={i}>
                <td><button className="answerButton" onClick={() => props.buttonClick(props.choices[i].id)}>{props.choices[i].text}</button></td>
                <td><button className="answerButton" onClick={() => props.buttonClick(props.choices[i+1].id)}>{props.choices[i+1].text}</button></td>
            </tr>
        );
    }
    if (choice_n%2===1){choiceArray.push(
        <tr key={choice_n}>
                <td><button className="answerButton" onClick={() => props.buttonClick(props.choices[choice_n-1].id)}>{props.choices[choice_n-1].text}</button></td>
        </tr>
    )}
    return (
        <table><tbody>
            {choiceArray}
        </tbody></table>
    )
}