class ParkingLot:
    def __init__(self, total_spots):
        self.total_spots = total_spots
        self.parked_cars = {}

    def entry(self, vehicle_no):
        if len(self.parked_cars) < self.total_spots:
            self.parked_cars[vehicle_no] = 0
            print("Vehicle parked successfully")
        else:
            print("Parking Full")

    def exit(self, vehicle_no, hours):
        if vehicle_no in self.parked_cars:
            fee = hours * 20
            del self.parked_cars[vehicle_no]
            print("Parking Fee:", fee)
        else:
            print("Vehicle not found")

    def available_spots(self):
        print("Available Spots:", self.total_spots - len(self.parked_cars))


lot = ParkingLot(5)

lot.entry("WB01A1234")
lot.available_spots()
lot.exit("WB01A1234", 3)