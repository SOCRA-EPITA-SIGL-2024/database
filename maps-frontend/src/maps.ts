import { Loader } from "@googlemaps/js-api-loader";

export const mapLoader = new Loader({
  apiKey: "AIzaSyAw4mJqGI6HexEslBR6ATBvqu1pk_-bOv4",
  version: "weekly",
  language: "fr",
});

let map: google.maps.Map;

export interface Place {
  position: { lat: number; lng: number };
  title: string;
  id: string;
}

export const initMaps = async (places: Place[]) => {
  await mapLoader.load();
  await mapLoader.load();
  const lyon = {
    title: "Lyon",
    position: { lat: 45.764043, lng: 4.835659 },
  };
  const { Map } = (await google.maps.importLibrary(
    "maps"
  )) as google.maps.MapsLibrary;
  const { Marker } = (await google.maps.importLibrary(
    "marker"
  )) as google.maps.MarkerLibrary;

  map = new Map(document.getElementById("map") as HTMLElement, {
    center: lyon.position,
    zoom: 6,
  });

  places.forEach(({ title, position }) => {
    const marker = new Marker({
      map,
      position,
      title,
    });
  });
};
