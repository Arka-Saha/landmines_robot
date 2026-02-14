import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from scipy.ndimage import gaussian_filter

# figure
fig, ax = plt.subplots(figsize=(12, 8))

start_point = (2, 2)
end_point = (18, 15)

heat_points = [
    (4, 3),
    (10, 5),
    (8, 11),
    # (10, 9),
    # (12, 11),
    (14, 13),
    (6, 4)
]

x_points = [point[0] for point in heat_points]
y_points = [point[1] for point in heat_points]

grid_size = 100
heatmap = np.zeros((grid_size, grid_size))

for x, y in zip(x_points, y_points):
    grid_x = int((x / 20) * grid_size)
    grid_y = int((y / 20) * grid_size)

    if 0 <= grid_x < grid_size and 0 <= grid_y < grid_size:
        heatmap[grid_y, grid_x] += 1

heatmap = gaussian_filter(heatmap, sigma=2)

colors = ['#000033', '#0000ff', '#00ffff', '#00ff00', '#ffff00', '#ff0000']
n_bins = 100
cmap = LinearSegmentedColormap.from_list('heat', colors, N=n_bins)

im = ax.imshow(heatmap, cmap=cmap, extent=[0, 20, 0, 20], origin='lower', alpha=0.7)

ax.plot(start_point[0], start_point[1], 'go', markersize=20,
        markeredgecolor='white', markeredgewidth=2, label='Start', zorder=5)
ax.plot(end_point[0], end_point[1], 'ro', markersize=20,
        markeredgecolor='white', markeredgewidth=2, label='End', zorder=5)

ax.text(start_point[0], start_point[1] - 0.8, 'START',
        ha='center', va='top', fontsize=12, fontweight='bold', color='white',
        bbox=dict(boxstyle='round', facecolor='green', alpha=0.7))
ax.text(end_point[0], end_point[1] + 0.8, 'END',
        ha='center', va='bottom', fontsize=12, fontweight='bold', color='white',
        bbox=dict(boxstyle='round', facecolor='red', alpha=0.7))

cbar = plt.colorbar(im, ax=ax)
cbar.set_label('Activity Intensity', rotation=270, labelpad=20, fontsize=12)
ax.set_xlabel('Distance (km)', fontsize=12)
ax.set_ylabel('Distance (km)', fontsize=12)
ax.set_title('Journey Heatmap: Activity Along the Route', fontsize=16, fontweight='bold', pad=20)
ax.grid(True, alpha=0.3, linestyle='--')
ax.legend(loc='upper left', fontsize=10)

ax.set_aspect('equal')

plt.tight_layout()
plt.savefig('heatmap.png', dpi=300, bbox_inches='tight')
plt.show()
