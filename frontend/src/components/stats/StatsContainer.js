import React, {useEffect, useState} from 'react';
import getCounterValues from '../../actions/counterActions';
import Count from '../count/Count';
import BarChart from '../BarChart';

function StatsContainer() {

    const [total, setTotal] = useState(0);
    const [record, setRecord] = useState({})
    
    useEffect(() => {
        const timer = startTimer()
        return () => {
            clearInterval(timer)
        }
    }, [startTimer])

    function startTimer() {
        return setTimeout(getValues, 5000)
    }

    function getValues() {
        getCounterValues().then(response => {
            setTotal(response.total);
            setRecord(response.record)
            startTimer();
        })
    }
    const space = {
        width: "150px"
    }
    const flex = {
    }
    return (
        <div style={flex}>
            <div>
                <Count total={total} />
            </div>
            <div style={space}></div>
            <div>
                <BarChart record={record}/>
            </div>
        </div>)
        
}

export default StatsContainer;