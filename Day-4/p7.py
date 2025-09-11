#Parking system
from abc import ABC, abstractmethod
import time
class Vehicle:
    def __init__(self, license_plate, owner_name):
        self.__license_plate = license_plate  
        self.__owner_name = owner_name        
    def get_license_plate(self):
        return self.__license_plate
    def set_license_plate(self, license_plate):
        self.__license_plate = license_plate
    def get_owner_name(self):
        return self.__owner_name
    def set_owner_name(self, owner_name):
        self.__owner_name = owner_name
    def display(self):
        print(f"Vehicle: {self.__license_plate}, Owner: {self.__owner_name}")
    def calculate_parking_fee(self, hours):
        raise NotImplementedError("Subclass must implement this method!")
class Bike(Vehicle):
    def __init__(self, license_plate, owner_name, helmet_required=True):
        super().__init__(license_plate, owner_name)
        self.helmet_required = helmet_required
    def display(self):
        print(f"Bike [Plate: {self.get_license_plate()}, Owner: {self.get_owner_name()}, Helmet Required: {self.helmet_required}]")
    def calculate_parking_fee(self, hours):
        return 20 * hours
class Car(Vehicle):
    def __init__(self, license_plate, owner_name, seats=4):
        super().__init__(license_plate, owner_name)
        self.seats = seats
    def display(self):
        print(f"Car [Plate: {self.get_license_plate()}, Owner: {self.get_owner_name()}, Seats: {self.seats}]")
    def calculate_parking_fee(self, hours):
        return 50 * hours
class SUV(Vehicle):
    def __init__(self, license_plate, owner_name, four_wheel_drive=True):
        super().__init__(license_plate, owner_name)
        self.four_wheel_drive = four_wheel_drive
    def display(self):
        print(f"SUV [Plate: {self.get_license_plate()}, Owner: {self.get_owner_name()}, 4WD: {self.four_wheel_drive}]")
    def calculate_parking_fee(self, hours):
        return 70 * hours
class Truck(Vehicle):
    def __init__(self, license_plate, owner_name, max_load_capacity=10000):
        super().__init__(license_plate, owner_name)
        self.max_load_capacity = max_load_capacity
    def display(self):
        print(f"Truck [Plate: {self.get_license_plate()}, Owner: {self.get_owner_name()}, Max Load: {self.max_load_capacity}kg]")
    def calculate_parking_fee(self, hours):
        return 100 * hours
class ParkingSpot:
    def __init__(self, spot_id, size):
        self.__spot_id = spot_id
        self.__size = size  
        self.__is_occupied = False
        self.__vehicle = None
        self.__start_time = None
    def get_spot_id(self):
        return self.__spot_id
    def is_occupied(self):
        return self.__is_occupied
    def assign_vehicle(self, vehicle):
        if self.__is_occupied:
            print(f"Spot {self.__spot_id} is already occupied!")
            return False
        if isinstance(vehicle, Bike) and self.__size in ["S", "M", "L", "XL"]:
            pass
        elif isinstance(vehicle, Car) and self.__size in ["M", "L", "XL"]:
            pass
        elif isinstance(vehicle, SUV) and self.__size in ["L", "XL"]:
            pass
        elif isinstance(vehicle, Truck) and self.__size == "XL":
            pass
        else:
            print(f"Vehicle {vehicle.get_license_plate()} does not fit in spot {self.__spot_id} ({self.__size})")
            return False
        self.__vehicle = vehicle
        self.__is_occupied = True
        self.__start_time = time.time()
        print(f"Vehicle {vehicle.get_license_plate()} parked at Spot {self.__spot_id}")
        return True
    def remove_vehicle(self):
        if not self.__is_occupied:
            print(f"Spot {self.__spot_id} is already empty!")
            return None, 0
        end_time = time.time()
        hours = max(1, int((end_time - self.__start_time) // 1)) 
        fee = self.__vehicle.calculate_parking_fee(hours)
        vehicle = self.__vehicle
        print(f"Vehicle {vehicle.get_license_plate()} unparked from Spot {self.__spot_id} after {hours} hour(s)")
        self.__vehicle = None
        self.__is_occupied = False
        self.__start_time = None
        return vehicle, fee
    def show_status(self):
        status = "Occupied" if self.__is_occupied else "Available"
        print(f"Spot {self.__spot_id} ({self.__size}) → {status}")
class ParkingLot:
    def __init__(self):
        self.spots = []
    def add_spot(self, spot):
        self.spots.append(spot)
    def show_spots(self):
        for spot in self.spots:
            spot.show_status()
    def park_vehicle(self, vehicle):
        for spot in self.spots:
            if not spot.is_occupied() and spot.assign_vehicle(vehicle):
                return True
        print("No suitable spot available!")
        return False
    def unpark_vehicle(self, vehicle):
        for spot in self.spots:
            if spot.is_occupied() and spot._ParkingSpot__vehicle == vehicle:
                v, fee = spot.remove_vehicle()
                return fee
        print("Vehicle not found in lot!")
        return 0
class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass
class CashPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} via Cash")
class CardPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} via Credit/Debit Card")
class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} via UPI")
if __name__ == "__main__":
    lot = ParkingLot()
    lot.add_spot(ParkingSpot(1, "S"))
    lot.add_spot(ParkingSpot(2, "M"))
    lot.add_spot(ParkingSpot(3, "L"))
    lot.add_spot(ParkingSpot(4, "XL"))
    v1 = Bike("TS09A1234", "Ashritha")
    v2 = Car("TS10B5678", "Akhila", 5)
    v3 = SUV("TS11C9999", "Ravi")
    v4 = Truck("TS12D4321", "Ramesh")
    vehicles = [v1, v2, v3, v4]
    for v in vehicles:
        v.display()
    print("\nParking Vehicles")
    lot.park_vehicle(v1)
    lot.park_vehicle(v2)
    lot.park_vehicle(v3)
    lot.park_vehicle(v4)
    lot.show_spots()
    print("\n Unparking Vehicle (Car)")
    fee = lot.unpark_vehicle(v2)
    if fee > 0:
        payment_method = UPIPayment()   
        payment_method.process_payment(fee)
