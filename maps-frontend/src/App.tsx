import React from "react";
import "./App.css";
import { Garden, initMaps } from "./maps";
import { getGardensAround } from "./places";

function App() {
  const lyon: Garden = {
    title: "Lyon",
    position: { lat: 45.764043, lng: 4.835659 },
    products: [],
    id: "me",
  };
  const montavus: Garden = {
    title: "Montavus",
    position: { lat: 45.907546, lng: 6.611693 },
    products: [],
    id: "me",
  };
  const bagnolet: Garden = {
    title: "Clotte",
    position: { lat: 48.873760785852795, lng: 2.419567567838784 },
    products: [],
    id: "me",
  };
  React.useEffect(() => {
    const init = async () => {
      const myPlace = bagnolet;
      const places = await getGardensAround(myPlace, 100);
      await initMaps(myPlace, places);
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
