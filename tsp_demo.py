from tsp_solver import tsp_solver  
distances = [
    #   HCM    NhaTrang DaNang  HaNoi
    [    0,     435,     961,   1726],  # HCM
    [  435,       0,     530,   1291],  # Nha Trang
    [  961,     530,       0,    764],  # Đà Nẵng
    [ 1726,    1291,     764,      0]   # Hà Nội
]

city_names = ["Hồ Chí Minh", "Nha Trang", "Đà Nẵng", "Hà Nội"]
cities = [0, 1, 2, 3]
start = 0
path, cost = tsp_solver(cities, distances, start)
path_with_names = [city_names[i] for i in path + [path[0]]]  
print(" → ".join(path_with_names))
print(f"Tổng chi phí: {cost} km")
