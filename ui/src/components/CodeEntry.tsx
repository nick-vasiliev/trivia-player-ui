import { useRef } from 'react';
export function CodeEntry({onSubmit}: {(code: string)}) {

    const code = useRef<HTMLInputElement>(null);


    return (
        <div className="codeEntry">
        <input className="codeEntryInput" type="text" ref={code} />
        <button className="codeEntryButton" onClick={() => onSubmit(code.current?.value)}>Go!</button>
        </div>
    );
}