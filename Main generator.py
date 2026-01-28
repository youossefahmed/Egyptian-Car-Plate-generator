import random
import sqlite3


class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def __str__(self):
        return f"{self.color} {self.brand} {self.model}"


class EgyptianCarPlate:
    ARABIC_LETTERS = "أبجدهوزحطيكلمنسعفصقرشتثخذضظغ"

    GOVERNORATES = {
        "cairo": "ق",
        "alexandria": "س",
        "giza": "ج",
        "mansoura": "م",
        "assiut": "ص",
        "suez": "ز",
        "fayoum": "ف",
        "beni suef": "ب",
        "minya": "ن",
        "luxor": "ل",
        "aswan": "و",
        "sharqia": "ش",
        "dakahlia": "د",
        "kafr el-sheikh": "ك",
        "beheira": "ه",
        "gharbia": "غ",
        "qena": "ق",
        "matrouh": "ط",
        "red sea": "ح",
        "new valley": "ي"
    }

    def __init__(self):
        self.governorate = self.choose_governorate()
        self.gov_letter = self.GOVERNORATES[self.governorate]
        self.numbers = self.generate_numbers()
        self.letters = self.generate_letters()
        self.plate_number = f"{self.letters} - {self.numbers}"

    def choose_governorate(self):
        print("Available Governorates:")
        for gov in self.GOVERNORATES:
            print(f"- {gov.title()}")

        while True:
            choice = input("\nEnter governorate name from the list above: ").strip().lower()
            if choice in self.GOVERNORATES:
                return choice
            else:
                print("⚠ Invalid governorate. Please try again from the list.\n")

    def generate_numbers(self):
        return ''.join(random.choices("0123456789", k=4))

    def generate_letters(self):
        other_letters = [ch for ch in self.ARABIC_LETTERS if ch != self.gov_letter]
        random_letters = random.sample(other_letters, 2)
        letters_list = random_letters + [self.gov_letter]
        random.shuffle(letters_list)
        return ''.join(letters_list)

    def __str__(self):
        return f"{self.plate_number}"


class Vehicle:
    def __init__(self, car: Car, plate: EgyptianCarPlate, owner_name, id_number, age):
        self.car = car
        self.plate = plate
        self.owner_name = owner_name
        self.id_number = id_number
        self.age = age

    def display_info(self):
        print("\n=== Vehicle Information ===")
        print(f"Owner : {self.owner_name} (ID: {self.id_number}, Age: {self.age})")
        print(f"Car   : {self.car}")
        print(f"Plate : {self.plate} (Governorate: {self.plate.governorate.title()})")

    def save_to_db(self, conn):
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO vehicles (brand, model, color, governorate, plate_letters, plate_numbers, owner_name, id_number, age)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            self.car.brand,
            self.car.model,
            self.car.color,
            self.plate.governorate.title(),
            self.plate.letters,
            self.plate.numbers,
            self.owner_name,
            self.id_number,
            self.age
        ))
        conn.commit()


def setup_database():
    conn = sqlite3.connect("cars.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vehicles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            brand TEXT,
            model TEXT,
            color TEXT,
            governorate TEXT,
            plate_letters TEXT,
            plate_numbers TEXT,
            owner_name TEXT,
            id_number TEXT,
            age INTEGER
        )
    """)
    conn.commit()
    return conn


def main():
    conn = setup_database()

    print("\n--- Car Plate Registration ---\n")

    owner_name = input("Enter owner name: ")
    id_number = input("Enter owner ID number: ")
    while True:
        try:
            age = int(input("Enter owner age: "))
            break
        except ValueError:
            print("⚠ Please enter a valid number for age.")

    brand = input("Enter car brand: ")
    model = input("Enter car model: ")
    color = input("Enter car color: ")

    car = Car(brand, model, color)
    plate = EgyptianCarPlate()
    vehicle = Vehicle(car, plate, owner_name, id_number, age)

    vehicle.display_info()
    vehicle.save_to_db(conn)

    conn.close()


if __name__ == "__main__":
    main()
