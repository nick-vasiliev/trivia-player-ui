import { CodeEntry } from '../components/CodeEntry.tsx';

export function EnterRoom({sendCode}: {(msg: string)}) {
    return (
        <div className="EnterRoom">
            <h1>EnterRoom</h1>
            <CodeEntry onSubmit={sendCode} />
        </div>
    )
};