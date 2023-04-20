import csv
from random import randrange, sample, random
from math import sqrt, pi, cos, sin, radians
import json
from multiprocessing import Pool

PARIS_REFERENCE_POSITION = {"lat": 48.856614, "lng": 2.352222}  # Paris
LYON_REFERENCE_POSITION = {"lat": 45.764043, "lng": 4.835659}  # Lyon
RANDOM_POSITION_RADIUS = 150e3  # 150km


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
            garden_position = create_user_garden_position(garden_id, ref_position)
            return dict(
                {
                    "title": f"Potager {garden_id}",
                    "id": garden_position["id"],
                    "position": {
                        "lat": garden_position["lat"],
                        "lng": garden_position["lng"],
                    },
                }
            )

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


def create_user_garden_position(user_id, ref_position):
    (lat, lng) = random_location(ref_position)
    return {
        "id": f"u{user_id}",
        "lat": lat,
        "lng": lng,
    }


if __name__ == "__main__":
    create_random_garden_positions(
        "data/gardens.json",
    )
