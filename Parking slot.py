import random
import string

class ParkingLot:
    def __init__(self, square_footage, spot_width=8, spot_length=12):
        self.square_footage = square_footage
        self.spot_width = spot_width
        self.spot_length = spot_length
        self.parking_lot_size = self.calculate_parking_lot_size()
        self.parking_lot = [None] * self.parking_lot_size
        self.parked_cars = {}

    def calculate_parking_lot_size(self):
        return int(self.square_footage / (self.spot_width * self.spot_length))

    def park_car(self, car, spot):
        if self.parking_lot[spot] is None:
            self.parking_lot[spot] = car
            self.parked_cars[car.license_plate] = spot
            return True
        else:
            return False


class Car:
    def __init__(self, license_plate):
        self.license_plate = license_plate

    def __str__(self):
        return f"Car with license plate {self.license_plate}"

    def park(self, parking_lot):
        spot = random.randint(0, len(parking_lot.parking_lot) - 1)
        while not parking_lot.park_car(self, spot):
            spot = random.randint(0, len(parking_lot.parking_lot) - 1)


def main():
    # Set the parking lot size (square footage)
    parking_lot_size = 2000

    # Create a parking lot
    parking_lot = ParkingLot(parking_lot_size)

    # Create an array of cars with random license plates
    cars = [Car(''.join(random.choices(string.ascii_uppercase + string.digits, k=7))) for _ in range(30)]

    # Park cars in the parking lot until it's full or there are no more cars
    for car in cars:
        try:
            car.park(parking_lot)
            print(f"{car} parked successfully in spot {parking_lot.parked_cars[car.license_plate]}")
        except IndexError:
            print("Parking lot is full. Exiting program.")
            break


if __name__ == "__main__":
    main()
