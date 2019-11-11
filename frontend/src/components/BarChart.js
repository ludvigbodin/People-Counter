import React from 'react';
import {XYPlot, XAxis, YAxis, VerticalBarSeries} from 'react-vis';
import '../../node_modules/react-vis/dist/style.css';
import logo from '../tele2logo.png'

function BarChart(props) {

    const record = props.record;

    let times = {}
    let data1 = {}

    Object.keys(record).forEach(day => {
        Object.keys(record[day]).forEach(time => {
            const values = record[day][time];

            const valueIn = values["in"] ? values["in"] : 0
            const valueOut = values["out"] ? values["out"] : 0
            
            const total = !!data1[time] ? data1[time] + (valueIn - valueOut) : (valueIn - valueOut)
            times[time] = !!times[time] ? times[time] + 1 : 1
            data1[time] = total
        })
    })

    const data = Object.keys(data1).map((time, index) => {
        return {
            x: time,
            y: (data1[time] / times[time])
        }
    })


    data.sort((a,b) => (parseInt(a.x.split("-")[0]) > parseInt(b.x.split("-")[0])) ? 1 : ((parseInt(b.x.split("-")[0]) > parseInt(a.x.split("-")[0])) ? -1 : 0)); 

    return ( 
        <div style={{textAlign: "center"}}>
            <h5 style={{margin: "0"}}>Average (Last week)</h5>
            <div style={{width: "400px", margin: "0 auto"}}>
                <XYPlot margin={{bottom: 70}} xType="ordinal" width={400} height={300}>
                    <XAxis/>
                    <YAxis/>
                    <VerticalBarSeries
                        data={data}
                    />
                </XYPlot>
            </div>
            <div>
                <p style={{display: "inline-block", marginRight: "30px"}}> Powered by Tele2 AB © </p>
            </div>
        </div>)

}

export default BarChart;