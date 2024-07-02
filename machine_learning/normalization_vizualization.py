import matplotlib.pyplot as plt

# Original data
original_data = [
    [1400, 100, 450],
    [1500, 120, 460],
    [1600, 130, 470],
    [1700, 140, 480],
    [1800, 150, 490],
    [1900, 160, 500],
    [2000, 170, 510],
    [2100, 180, 520],
    [2200, 190, 530],
    [2300, 200, 540]
]

# Min-Max Scaled data
min_max_scaled_data = [
    [0.0, 0.0, 0.0],
    [0.1111111111111111, 0.2222222222222222, 0.1111111111111111],
    [0.2222222222222222, 0.3333333333333333, 0.2222222222222222],
    [0.3333333333333333, 0.4444444444444444, 0.3333333333333333],
    [0.4444444444444444, 0.5555555555555556, 0.4444444444444444],
    [0.5555555555555556, 0.6666666666666666, 0.5555555555555556],
    [0.6666666666666666, 0.7777777777777778, 0.6666666666666666],
    [0.7777777777777778, 0.8888888888888888, 0.7777777777777778],
    [0.8888888888888888, 0.9999999999999999, 0.8888888888888888],
    [1.0, 1.0, 1.0]
]

# Z-score Scaled data
z_score_scaled_data = [
    [-1.5666989036012806, -1.5666989036012806, -1.5666989036012806],
    [-1.2185435916898848, -1.2185435916898848, -1.2185435916898848],
    [-0.8703882797784892, -0.8703882797784892, -0.8703882797784892],
    [-0.5222329678670935, -0.5222329678670935, -0.5222329678670935],
    [-0.17407765595569785, -0.17407765595569785, -0.17407765595569785],
    [0.17407765595569785, 0.17407765595569785, 0.17407765595569785],
    [0.5222329678670935, 0.5222329678670935, 0.5222329678670935],
    [0.8703882797784892, 0.8703882797784892, 0.8703882797784892],
    [1.2185435916898848, 1.2185435916898848, 1.2185435916898848],
    [1.5666989036012806, 1.5666989036012806, 1.5666989036012806]
]

# Robust Scaled data
robust_scaled_data = [
    [-1.25, -1.25, -1.25],
    [-0.75, -0.75, -0.75],
    [-0.25, -0.25, -0.25],
    [0.25, 0.25, 0.25],
    [0.75, 0.75, 0.75],
    [1.25, 1.25, 1.25],
    [1.75, 1.75, 1.75],
    [2.25, 2.25, 2.25],
    [2.75, 2.75, 2.75],
    [3.25, 3.25, 3.25]
]

# Create plots
plt.figure(figsize=(12, 8))

# Original Data
plt.subplot(2, 2, 1)
plt.plot([row[0] for row in original_data], 'o-', label='Weight')
plt.plot([row[1] for row in original_data], 'o-', label='Horsepower')
plt.plot([row[2] for row in original_data], 'o-', label='Torque')
plt.title('Original Data')
plt.legend()

# Min-Max Scaled Data
plt.subplot(2, 2, 2)
plt.plot([row[0] for row in min_max_scaled_data], 'o-', label='Weight')
plt.plot([row[1] for row in min_max_scaled_data], 'o-', label='Horsepower')
plt.plot([row[2] for row in min_max_scaled_data], 'o-', label='Torque')
plt.title('Min-Max Scaled Data')
plt.legend()

# Z-score Scaled Data
plt.subplot(2, 2, 3)
plt.plot([row[0] for row in z_score_scaled_data], 'o-', label='Weight')
plt.plot([row[1] for row in z_score_scaled_data], 'o-', label='Horsepower')
plt.plot([row[2] for row in z_score_scaled_data], 'o-', label='Torque')
plt.title('Z-score Scaled Data')
plt.legend()

# Robust Scaled Data
plt.subplot(2, 2, 4)
plt.plot([row[0] for row in robust_scaled_data], 'o-', label='Weight')
plt.plot([row[1] for row in robust_scaled_data], 'o-', label='Horsepower')
plt.plot([row[2] for row in robust_scaled_data], 'o-', label='Torque')
plt.title('Robust Scaled Data')
plt.legend()

plt.tight_layout()
plt.show()
