import React from "react";
import "./App.css";
import { initMaps } from "./maps";
import { getPlaces } from "./places";

function App() {
  React.useEffect(() => {
    const init = async () => {
      const places = await getPlaces();
      await initMaps(places);
    };
    init();
  }, []);
  return (
    <>
      <h1>Points on map</h1>
      <div id="map"></div>
    </>
  );
}

export default App;
