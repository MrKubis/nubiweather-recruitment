import { useState, useEffect } from "react";
function WeatherForecaster(props){

    const [temp, setTemp] = useState(0)
   console.log(props.icon)
    return(
        <div className="container-weather-info">
            <p className="weather-info">{props.date}</p>
            <p className="weather-info">{props.text}</p>
            <p className="weather-info">{props.temp}°C</p>
            <img src={props.icon}/>
        </div>
    );
}

export default WeatherForecaster;