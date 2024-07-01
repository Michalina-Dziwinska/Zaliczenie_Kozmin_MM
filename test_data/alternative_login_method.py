from faker import Faker
import random
import csv

def get_csv_data(filename):
    rows = []
    data_file = open(filename, "r")
    reader = csv.reader(data_file)
    # Pomiń pierwszy wiersz
    next(reader, None)
    for row in reader:
        rows.append(row)
    return rows

class AlternativeLoginMethodData:
    def __init__(self):
        fake = Faker("pl_PL")
        self.alternative_reservation_number = fake.random_int(3, 6)
        self.alternative_email = fake.email()
        self.alternative_iata_code = fake.random_letters(3)



