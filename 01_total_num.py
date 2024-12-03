import numpy as np

ticket_prices_roller_coaster = np.array([44, 38, 21])
ticket_prices_4d_cinema = np.array([32, 28, 15])
ticket_prices_cable_car = np.array([24, 20, 10])

total_roller_coaster = 1412
total_4d_cinema = 1024
total_cable_car = 728


A = np.array([[44, 38, 21],
              [32, 28, 15],
              [24, 20, 10]])
B = np.array([1412, 1024, 728])

x, y, z = np.linalg.solve(A, B)

print(f'Number of males: {x}')
print(f'Number of females: {y}')
print(f'Number of kids: {z}')
