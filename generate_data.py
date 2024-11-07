# This script generates a csv file filled with randomized patient data that is aligned with FlatIron's schema.
# The data is generated using the Faker library, which generates fake data for a variety of fields.
# The script takes in a single argument, the number of patients to generate.
# The script will output a csv file with the specified number of patients.

import csv
import sys
from faker import Faker
import random

# Cancer Types
diagnosis_types = ['Breast Cancer', 'Lung Cancer', 'Prostate Cancer', 'Colorectal Cancer', 'Bladder Cancer', 'Melanoma', 'Kidney Cancer', 'Leukemia', 'Non-Hodgkin Lymphoma', 'Thyroid Cancer']

# Function to generate a random date of birth
def generate_dob():
    year = random.randint(1900, 2019)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return f"{year}-{month}-{day}"

# Function to generate
def generate_data(num_patients):
    fake = Faker()
    with open('data.csv', mode='w') as data_file:
        data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        data_writer.writerow(['patient_id', 'first_name', 'last_name', 'age', 'diagnosis', 'severity', 'birth_date', 'created_at', 'updated_at'])
        for i in range(num_patients):
            patient_id = i
            first_name = fake.first_name()
            last_name = fake.last_name()
            age = random.randint(1, 100)
            diagnosis = random.choice(diagnosis_types)
            severity = random.randint(1, 10)
            birth_date = generate_dob()
            created_at = fake.date_time_this_year()
            updated_at = fake.date_time_this_year()
            data_writer.writerow([patient_id, first_name, last_name, age, diagnosis, severity, birth_date, created_at, updated_at])
    print(f"Generated {num_patients} patients")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_data.py <num_patients>")
        sys.exit(1)
    num_patients = int(sys.argv[1])
    generate_data(num_patients)
    