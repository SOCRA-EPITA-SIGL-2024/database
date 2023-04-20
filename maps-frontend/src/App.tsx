import React from "react";
import "./App.css";
import { Garden, initMaps } from "./maps";
import { getGardensAround } from "./places";

const RAYON = 15; // km

function App() {
  const etudiant: Garden = {
    title: "Étudiant",
    position: { lat: 45.764043, lng: 4.835659 },
    products: [],
    id: "etudiant",
  };

  const montavus: Garden = {
    title: "Montavus",
    position: { lat: 45.907546, lng: 6.611693 },
    products: [],
    id: "me",
  };

  React.useEffect(() => {
    const init = async () => {
      const myPlace = montavus;
      const places = await getGardensAround(myPlace, RAYON);
      await initMaps(myPlace, places);
    };
    init();
  }, []);

  return (
    <>
      <h1>SOCRA: Vue des potagers dans un rayon de {RAYON} km</h1>
      <div id="map"></div>
    </>
  );
}

export default App;
