class Elevator:
    def __init__(self, num_floors):
        self.current_floor = 0
        self.num_floors = num_floors
        self.state = "idle"
        self.request_list = []

    def request_floor(self, floor):
        if 0 <= floor < self.num_floors:
            if floor not in self.request_list: # Don't need duplicates
                self.request_list.append(floor)
                print(f"Floor {floor} has been requested")

                # Ensure the floors are handled in ascending order
                self.request_list.sort()
            else:
                print(f"Floor {floor} has already been requested")
        else:
            # Ensure the requested floor is in range
            print(f"Choose a floor between 0 and {self.num_floors - 1}")

    def move(self):
        if self.request_list:
            next_floor = self.request_list[0]

            if self.current_floor < next_floor:
                self.state = "going up"
                self.print_move()
                self.current_floor += 1

            elif self.current_floor > next_floor:
                self.state = "going down"
                self.print_move()
                self.current_floor -= 1

            else:
                self.request_list.pop(0) # Remove requested floor once it is reached
                self.state = "idle"
                print(f"Elevator has arrived at floor {self.current_floor}")
        else:
            self.state = "idle"
            print("No requests. Elevator is idle")

    def print_move(self):
        print(f"On floor {self.current_floor} {self.state}")
