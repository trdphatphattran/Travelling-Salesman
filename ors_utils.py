import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("HERE_API_KEY")

def is_coord_input(text):
    parts = text.strip().split()
    return len(parts) == 3 and all(p.replace('.', '', 1).replace('-', '', 1).isdigit() for p in parts[1:])

def geocode_place(name):
    url = "https://geocode.search.hereapi.com/v1/geocode"
    params = {"q": name, "apiKey": API_KEY}
    res = requests.get(url, params=params).json()
    if res.get('items'):
        pos = res['items'][0]['position']
        return (pos['lat'], pos['lng'])
    else:
        raise ValueError(f"Không tìm thấy toạ độ cho: {name}")

def calculate_distance_here(origin, destination, mode="car"):
    url = "https://router.hereapi.com/v8/routes"
    params = {
        "transportMode": mode,
        "origin": f"{origin[0]},{origin[1]}",
        "destination": f"{destination[0]},{destination[1]}",
        "return": "summary",
        "apiKey": API_KEY
    }
    res = requests.get(url, params=params).json()
    try:
        summary = res["routes"][0]["sections"][0]["summary"]
        return summary["length"]
    except:
        raise ValueError("Không thể tính khoảng cách.")

def build_distance_matrix(addresses, mode="car"):
    coords = []
    names = []
    is_manual = all(is_coord_input(line) for line in addresses)

    for line in addresses:
        parts = line.strip().split()
        if is_coord_input(line):
            name, x, y = parts
            coords.append((float(y), float(x)))
            names.append(name)
        else:
            lat, lon = geocode_place(line)
            coords.append((lat, lon))
            names.append(line)

    n = len(coords)
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i != j:
                if is_manual:
                    dx = coords[i][1] - coords[j][1]
                    dy = coords[i][0] - coords[j][0]
                    matrix[i][j] = (dx**2 + dy**2)**0.5 * 1000
                else:
                    matrix[i][j] = calculate_distance_here(coords[i], coords[j], mode)

    return coords, matrix, names
