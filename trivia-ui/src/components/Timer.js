import { useState, useRef, useEffect } from "react";

export function Timer( props ) {

    const firstRender = useRef(true);
    const [countdown, setCountdown] = useState(props.initialTime);

    useEffect( () => {
        if (firstRender.current || countdown<=0){
            firstRender.current=false;
            return;
        }
        setTimeout(()=>{
            setCountdown((countdown) => countdown - 1);
        },1000);
    }, [countdown]);

    return <div className="Timer">{countdown}</div>;
}