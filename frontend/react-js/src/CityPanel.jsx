import WeatherForecaster from "./WeatherForecaster.jsx";
import { useState, useEffect } from "react";

function CityPanel(props){

    const [forecastdays, setForecastdays] = useState(null)
    const date = new Date()
    const dateString = date.getFullYear() + "-" + (date.getMonth() + 2) + "-" + date.getDay()
        
    const apiKey = '6590bd6f6df5422e90a154646250209'
    const URL = 'http://api.weatherapi.com/v1/forecast.json?key='+ apiKey + '&q=' + props.city + '&days=4&aqi=no&alerts=no'

    useEffect(() => {
        fetch(URL)
        .then(res => {
            return res.json();
        })
        .then(data => {
            setForecastdays(data.forecast.forecastday);
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
                    return <WeatherForecaster key = {forecastday.date} date = {forecastday.date} temp = {forecastday.day.avgtemp_c} text = {forecastday.day.condition.text} icon = {forecastday.day.condition.icon}/>;
                }
                )}
            </div>
        </div>            

    );
}
export default CityPanel;