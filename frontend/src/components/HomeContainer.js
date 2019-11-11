import React from 'react';
import logo from '../lunchtime1.png';
import StatsContainer from './stats/StatsContainer';

const style = {
  height: "200px",
}

const imageStyle = {
    height: "200px",
    display: "block",
    margin: "0 auto"
}

function HomeContainer() {


  return (
      <div>
          <div style={style} key={1}>
              <img src={logo} alt="logo" style={imageStyle}/>
          </div>
          <div style={{width: "1500px", marginBottom: "40px"}}>
            <hr />
          </div>
        <StatsContainer />
      </div>
  )
}

export default HomeContainer;
