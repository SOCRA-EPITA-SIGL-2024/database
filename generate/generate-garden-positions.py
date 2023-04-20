import json
from math import cos, pi, radians, sin, sqrt
from random import random, randrange, choices

PARIS_REFERENCE_POSITION = {"lat": 48.856614, "lng": 2.352222}  # Paris
LYON_REFERENCE_POSITION = {"lat": 45.764043, "lng": 4.835659}  # Lyon
RANDOM_POSITION_RADIUS = 150e3  # 150km


vegetables = [
    {"categoryId": "vegetable", "name": "carotte"},
    {"categoryId": "vegetable", "name": "Abricot"},
    {"categoryId": "vegetable", "name": "Ail"},
    {"categoryId": "vegetable", "name": "Artichaut"},
    {"categoryId": "vegetable", "name": "Asperge"},
    {"categoryId": "vegetable", "name": "Aubergine"},
    {"categoryId": "vegetable", "name": "Betterave"},
    {"categoryId": "vegetable", "name": "Blette"},
    {"categoryId": "vegetable", "name": "Brocoli"},
    {"categoryId": "vegetable", "name": "Carotte"},
    {"categoryId": "vegetable", "name": "Carottes"},
    {"categoryId": "vegetable", "name": "Cassis"},
    {"categoryId": "vegetable", "name": "Céleri"},
    {"categoryId": "vegetable", "name": "Cerise"},
    {"categoryId": "vegetable", "name": "Champignon de Paris"},
    {"categoryId": "vegetable", "name": "Champignons de Paris"},
    {"categoryId": "vegetable", "name": "Châtaigne"},
    {"categoryId": "vegetable", "name": "Chou"},
    {"categoryId": "vegetable", "name": "Chou de Bruxelles"},
    {"categoryId": "vegetable", "name": "Chou-fleur"},
    {"categoryId": "vegetable", "name": "Choux"},
    {"categoryId": "vegetable", "name": "Choux de Bruxelles"},
    {"categoryId": "vegetable", "name": "Citron"},
    {"categoryId": "vegetable", "name": "Clémentine"},
    {"categoryId": "vegetable", "name": "Coing"},
    {"categoryId": "vegetable", "name": "Concombre"},
    {"categoryId": "vegetable", "name": "Courge"},
    {"categoryId": "vegetable", "name": "Courgette"},
    {"categoryId": "vegetable", "name": "Cresson"},
    {"categoryId": "vegetable", "name": "Échalote"},
    {"categoryId": "vegetable", "name": "Échalotte"},
    {"categoryId": "vegetable", "name": "Endive"},
    {"categoryId": "vegetable", "name": "Épinard"},
    {"categoryId": "vegetable", "name": "Fenouil"},
    {"categoryId": "vegetable", "name": "Figue"},
    {"categoryId": "vegetable", "name": "Fraise"},
    {"categoryId": "vegetable", "name": "Framboise"},
    {"categoryId": "vegetable", "name": "Groseille"},
    {"categoryId": "vegetable", "name": "Haricot vert"},
    {"categoryId": "vegetable", "name": "Kaki"},
    {"categoryId": "vegetable", "name": "Kiwi"},
    {"categoryId": "vegetable", "name": "Mâche"},
    {"categoryId": "vegetable", "name": "Maïs"},
    {"categoryId": "vegetable", "name": "Mandarine"},
    {"categoryId": "vegetable", "name": "Melon"},
    {"categoryId": "vegetable", "name": "Mirabelle"},
    {"categoryId": "vegetable", "name": "Mûre"},
    {"categoryId": "vegetable", "name": "Myrtille"},
    {"categoryId": "vegetable", "name": "Navet"},
    {"categoryId": "vegetable", "name": "Nectarine"},
    {"categoryId": "vegetable", "name": "Noisette"},
    {"categoryId": "vegetable", "name": "Noix"},
    {"categoryId": "vegetable", "name": "Oignon"},
    {"categoryId": "vegetable", "name": "Orange"},
    {"categoryId": "vegetable", "name": "Pamplemousse"},
    {"categoryId": "vegetable", "name": "Panais"},
    {"categoryId": "vegetable", "name": "Pastèque"},
    {"categoryId": "vegetable", "name": "Pêche"},
    {"categoryId": "vegetable", "name": "Petit pois"},
    {"categoryId": "vegetable", "name": "Poire"},
    {"categoryId": "vegetable", "name": "Poireau"},
    {"categoryId": "vegetable", "name": "Poivron"},
    {"categoryId": "vegetable", "name": "Pomme"},
    {"categoryId": "vegetable", "name": "Potiron"},
    {"categoryId": "vegetable", "name": "Prune"},
    {"categoryId": "vegetable", "name": "Radis"},
    {"categoryId": "vegetable", "name": "Raisin"},
    {"categoryId": "vegetable", "name": "Rhubarbe"},
    {"categoryId": "vegetable", "name": "Salade"},
    {"categoryId": "vegetable", "name": "Salsifis"},
    {"categoryId": "vegetable", "name": "Tomate"},
    {"categoryId": "vegetable", "name": "Topinambour"},
]


def create_random_garden_positions(json_path):
    with open(json_path, "w") as garden_position_json_file:
        positions = []
        gardens_around_paris = [
            (idx, PARIS_REFERENCE_POSITION) for idx in list(range(1, 1001))
        ]
        gardens_around_lyon = [
            (idx, LYON_REFERENCE_POSITION) for idx in list(range(1001, 2001))
        ]

        def generate(garden_id, ref_position):
            garden_props = create_garden(garden_id, ref_position)
            garden = dict(
                {
                    "title": f"Potager {garden_id}",
                }
            )
            garden.update(garden_props)
            return garden

        for cpt, ref_position in gardens_around_paris:
            positions.append(generate(cpt, ref_position))
        for cpt, ref_position in gardens_around_lyon:
            positions.append(generate(cpt, ref_position))

        garden_position_json_file.write(json.dumps(positions))


def random_location(ref_position):
    """
    pick a random geo position (lat, lon) within a RANDOM_POSITION_RADIUS
    from the REFERENCE_POSITION.

    Returns a tuple (lat, lon)

    See. https://gis.stackexchange.com/questions/25877/generating-random-locations-nearby
    """
    radius_in_degrees = RANDOM_POSITION_RADIUS / 111000
    x0 = ref_position["lng"]
    y0 = ref_position["lat"]

    u = random()
    v = random()

    w = radius_in_degrees * sqrt(u)
    t = 2 * pi * v
    x = w * cos(t)
    y = w * sin(t)

    new_x = x / cos(radians(y0))

    lng = round(new_x + x0, 6)
    lat = round(y + y0, 6)

    return (lat, lng)


def create_garden(user_id, ref_position):
    (lat, lng) = random_location(ref_position)
    total_vegetables_types = len(vegetables)
    number_of_vegetable_grown_in_garden = randrange(
        round(total_vegetables_types / 4), total_vegetables_types
    )
    vegatables_grown = list(choices(vegetables, k=number_of_vegetable_grown_in_garden))
    return {
        "id": f"u{user_id}",
        "position": {"lat": lat, "lng": lng},
        "products": vegatables_grown,
    }


if __name__ == "__main__":
    create_random_garden_positions(
        "data/gardens.json",
    )
