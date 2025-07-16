from tsp_solver import tsp_solver
def main():
    n = int(input("Nhập số lượng thành phố: "))
    city_names = []
    for i in range(n):
        name = input(f"Tên thành phố thứ {i+1}: ")
        city_names.append(name)
    distances = [[0 for _ in range(n)] for _ in range(n)]
    print("\nNhập khoảng cách giữa các cặp thành phố:")
    for i in range(n):
        for j in range(i + 1, n):
            d = int(input(f"Khoảng cách giữa {city_names[i]} và {city_names[j]} (km): "))
            distances[i][j] = d
            distances[j][i] = d  
    print("\nCác thành phố:")
    for idx, name in enumerate(city_names):
        print(f"{idx+1}. {name}")
    start = int(input("Chọn thành phố xuất phát (số thứ tự): ")) - 1
    cities = list(range(n))
    path, cost = tsp_solver(cities, distances, start)
    path_with_names = [city_names[i] for i in path + [path[0]]]
    print("\nHành trình tối ưu:")
    print(" → ".join(path_with_names))
    print(f"Tổng quãng đường: {cost} km")
if __name__ == "__main__":
    main()
