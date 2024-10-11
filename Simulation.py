import random
from Elevator import Elevator

# Make elevator system
elevator = Elevator(num_floors = 7)

# Random number of requests
num_requests = random.randint(1, 5)

# Random number of moves
num_moves = random.randint(5,10)

print(f"\nRequesting {num_requests} random floors")
for _ in range(num_requests):
    floor = random.randint(0, elevator.num_floors - 1)
    elevator.request_floor(floor)

print(f"\nSimulating {num_moves} random moves:")
for _ in range(num_moves):
    elevator.move()