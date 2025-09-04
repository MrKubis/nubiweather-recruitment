import WeatherForecaster from "./WeatherForecaster.jsx";
import { useState, useEffect } from "react";

function CityPanel(props){

    const [forecastdays, setForecastdays] = useState(null)
    const date = new Date()
    const dateString = date.getFullYear() + "-" + (date.getMonth() + 2) + "-" + date.getDay()
        
    const apiKey = '6590bd6f6df5422e90a154646250209'
    const URL = 'http://127.0.0.1:8000/api/forecast-weather/?city='+props.city+'&days=4'
    useEffect(() => {
        fetch(URL)
        .then(res => {
            return res.json();
        })
        .then(data => {
            console.log(data)
            setForecastdays(data);
        })            
        
    },[]);

    console.log(URL)

    return(
        <div className="city-container">
            <p className="text-city-name">{props.city}</p>
            <div className="container-weather-panels">
                {forecastdays && forecastdays.map((forecastday) =>
                {
                    console.log(forecastday);
                    return <WeatherForecaster key = {forecastday.id} date = {forecastday.date} temp = {forecastday.temp_c} text = {forecastday.description} icon = {forecastday.icon}/>;
                }
                )}
            </div>
        </div>            

    );
}
export default CityPanel;