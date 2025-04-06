import numpy as np
points = np.random.randint(10, 41, (5, 10))
player_names = [f"Player {i+1}" for i in range(5)]
avg_points = np.mean(points, axis=1)
print("Average points per game:")
print([round(avg, 1) for avg in avg_points])
print()
total_points = np.sum(points, axis=1)
best_player = np.argmax(total_points)
worst_player = np.argmin(total_points)
print(f"Best-performing player: {player_names[best_player]} (Total: {total_points[best_player]} points)")
print(f"Worst-performing player: {player_names[worst_player]} (Total: {total_points[worst_player]} points)")
print()
print("Games with scores above 30:")
for i in range(points.shape[0]):
    games = np.where(points[i] > 30)[0] + 1
    if games.size > 0:
        print(f"{player_names[i]}: Games {list(games)}")
print()
sorted_indices = np.argsort(total_points)[::-1]
print("Sorted Players by Total Points:")
for i, idx in enumerate(sorted_indices):
    print(f"{i + 1}. {player_names[idx]} - {total_points[idx]} points")
