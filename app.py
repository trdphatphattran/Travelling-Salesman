from flask import Flask, render_template, request, jsonify
from ors_utils import build_distance_matrix, is_coord_input
from tsp_solver import tsp_solver
from utils import plot_animation

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/solve", methods=["POST"])
def solve_api():
    data = request.get_json()
    addrs = list(data["coords"].keys())
    start_city = data.get("start_city", addrs[0])
    mode = data.get("mode", "car")

    coords, distances, city_names = build_distance_matrix(addrs, mode)
    manual_flags = [is_coord_input(line) for line in addrs]

    coord_dict = {
        city_names[i]: coords[i]
        for i in range(len(coords))
        if not manual_flags[i]
    }

    if start_city not in city_names:
        start_city = city_names[0]

    path, cost = tsp_solver(list(range(len(coords))), distances, start=city_names.index(start_city))
    ordered_coords = [coords[i] for i in path + [path[0]]]

    plot_animation(path + [path[0]], coords, filename='static/plot.gif', city_names=city_names)

    return jsonify({
        "raw_path": path + [path[0]],
        "path": [city_names[i] for i in path + [path[0]]],
        "cost": round(cost / 1000, 2),
        "img": "/static/plot.gif",
        "coords": coord_dict
    })

'''if __name__ == "__main__":
    app.run(debug=True)'''

import os
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)

