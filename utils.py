import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def plot_animation(path, coords, filename='static/plot.gif', city_names=None):
    fig, ax = plt.subplots(figsize=(8, 6))
    x = [coords[i][1] for i in path]
    y = [coords[i][0] for i in path]

    ax.set_xlim(min(x) - 0.5, max(x) + 0.5)
    ax.set_ylim(min(y) - 0.5, max(y) + 0.5)
    ax.set_title("Hành trình TSP")

    if city_names:
        for i, idx in enumerate(path):
            ax.text(x[i], y[i], city_names[idx], fontsize=10, color='blue', ha='right')

    ln, = ax.plot([], [], 'ro-', linewidth=2)

    def init():
        ln.set_data([], [])
        return ln,

    def update(i):
        ln.set_data(x[:i+1], y[:i+1])
        return ln,

    ani = FuncAnimation(fig, update, frames=len(path), init_func=init, interval=800, repeat=False)
    ani.save(filename, writer='pillow')
    plt.close()
