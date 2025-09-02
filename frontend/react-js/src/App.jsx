import nubisoftLogo from "./assets/nubisoft.svg";
import CityPanel from "./CityPanel";
import WeatherForecaster from "./WeatherForecaster";
function App() {
  return (
    <>
    <div className="flex justify-center flex-col gap-4 items-center">
      <div>
        <a href="https://nubisoft.io/" target="_blank">
          <img src={nubisoftLogo} className="" alt="Nubisoft logo" />
        </a>
      </div>
      <h1>NubiWeather</h1>
      <h2>Here are your results:</h2>
    </div>
    <div className="container-gliwice">
    
    <CityPanel city = "Gliwice"/>
    <CityPanel city = "Hamburg"/>
    </div>
      </>
  );
}

export default App;
