import React from 'react';

function Count(props) {

    const style = {
        border: "1px solid white",
        width: "150px",
        height: "150px",
        margin: "0 auto 50px",
        textAlign: "center"
    }

    const h3Style = {
        marginBottom: "0"
    }

    const colorStyle = {
        color: props.total >= 200 ? "red" : props.total >= 100 ? "yellow" : "green",
        margin: "0"
    }
    
    return (
        <div style={style}>
            <h3 style={h3Style}>Total: </h3>
            <h4 style={colorStyle}>{props.total}</h4>
        </div>
    )
}

export default Count;