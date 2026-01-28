import sqlite3
import random
import pandas as pd


class EgyptianCarPlate:
    ARABIC_LETTERS = "بلاسىىبسيىؤةةؤىسوروور"
    GOVERNORATES = {
        "Cairo": "CAI",
        "Alexandria": "ALX",
        "Giza": "GIZ",
        "Mansoura": "MNS",
        "Assiut": "ASY",
        "Suez": "SUE"
}

    def __init__(self, governorate=None, numbers=None ,letters=None ):
        self.governorate = governorate or self.choose_governorate()
        self.numbers = numbers or self.generate_numbers()
        self.letters = letters or self.generate_letters()
        self.plate_number = f"{self.letters} - {self.numbers}"

    def choose_governorate(self):
        while True:
            print("Select the governorate from the following list :")
            for gov in self.GOVERNORATES.keys():
                print(f"- {gov}")
            choice = input("Enter the name of the governorate: ")
            if choice in self.GOVERNORATES:
                return choice
            else:
                print("⚠ Invalid governorate, please choose a valid governorate from the list.")

    def generate_numbers(self):
        return ''.join(random.choices("0123456789", k=4))

    def generate_letters(self):
        return ''.join(random.choices(self.ARABIC_LETTERS, k=3))

    def __str__(self):
        return f"{self.governorate} - {self.plate_number}"

if __name__ == "__main__":
    plate = EgyptianCarPlate()
    print(plate)
