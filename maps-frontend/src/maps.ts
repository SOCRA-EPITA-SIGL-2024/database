import { Loader } from "@googlemaps/js-api-loader";

export const mapLoader = new Loader({
  apiKey: "AIzaSyAw4mJqGI6HexEslBR6ATBvqu1pk_-bOv4",
  version: "weekly",
  language: "fr",
});

let map: google.maps.Map;
export interface Garden {
  title: string;
  id: string;
  position: Position;
  products: Product[];
}

interface Product {
  categoryId: string;
  name: string;
}

interface Position {
  lat: number;
  lng: number;
}

export const initMaps = async (myPlace: Garden, gardens: Garden[]) => {
  await mapLoader.load();
  await mapLoader.load();

  const { Map } = (await google.maps.importLibrary(
    "maps"
  )) as google.maps.MapsLibrary;
  const { Marker } = (await google.maps.importLibrary(
    "marker"
  )) as google.maps.MarkerLibrary;

  map = new Map(document.getElementById("map") as HTMLElement, {
    center: myPlace.position,
    zoom: 6,
  });

  new Marker({
    map,
    position: myPlace.position,
    title: myPlace.title,
    icon: {
      url: "http://maps.google.com/mapfiles/ms/icons/blue-dot.png",
    },
  });

  gardens.forEach(({ title, position }) => {
    new Marker({
      map,
      position,
      title,
    });
  });
};
