
from datetime import datetime

def get_int(message):
    while True:
        try:
            return int(input(message))
        except ValueError as error:
            print(f"Incorrect value. \n{error}. Try again")

def get_int_age(message):
    while True:
        try:
            age = int(input(message))
            if 1<= age <= 100:
                return age
            print("Age is out of range(1-100)")
        except ValueError:
            print("Wrong value. Age must be an integer.")

def get_agency_code(message):
    while True:
        agency_id = input(message).strip()
        if not agency_id:
            print("Warning: Agency code can't be a blank space.")
        else:
            return agency_id


class Response():
    def __init__(self, )

    
class Patient():
    def __init__(self, patient_name, patient_lastname, patient_age):
        self.p_name = patient_name
        self.p_last = patient_lastname
        self.p_age = patient_age

    def __str__(self):
        return (
            f"Patient Name: {self.p_name}\n"
            f"Patient Last Name: {self.p_last}\n"
            f"Age: {self.p_age}"        
        )
    
class Incident():
    counter = 1
    def __init__(self, agency_code, description, patient):
        self.date = datetime.now()
        self.num = f"{self.date.strftime('%Y-%m%d')}{Incident.counter:04d}-{agency_code}"
        Incident.counter += 1
        self.descrip = description
        self.patient = patient
    
    def __str__(self):
        formatted_date = self.date.strftime("%Y-%m-%d %H:%M:%S")
        return (f"Incident Number: {self.num}\n"
                f"Incident Description: {self.descrip}\n"
                f"Incident Date: {formatted_date}\n"
                f"{self.patient}"
            )    
    
def create_incident(agency_id):
    print("New incident. Enter incident data.")
    description = input("Description: ")
    patient_name = input("Patient Name: ")
    patient_lastname = input("Patient Lastname: ")
    patient_age = get_int_age("Patient Age: ")

    patient_information = Patient(patient_name, patient_lastname, patient_age)
    record = Incident(agency_id, description, patient_information)
    print(f"\nIncident added successfully \n{record}")
    return record

def menu():
    agency_code = get_agency_code("Enter your agency code: ")
    incidents_list = []
    while True:
        print("\n" + "-" * 35)
        print("| CareReport 0.1 alfa version |")
        print("-" * 35)
        print("1. Add PCR | 2. Print Incident Information")
        print("0. Exit")

        choice = get_int("Select an option:\n")

        if choice == 1:
            incident = create_incident(agency_code)
            incidents_list.append(incident)
        elif choice == 2:
            if not incidents_list:
                print("No incidents found!")
            else:
                print("Existing Incidents:")

                for i, incident in enumerate(incidents_list, start=1):
                    print(f"{i}. Incident {incident.num}")

                choice_b = get_int("Select incident: ")

                if 1 <= choice_b <= len(incidents_list):
                    selected_incident = incidents_list[choice_b - 1]
                    print("\n", selected_incident)
                else:
                    print("Selection not found")
        elif choice == 0:
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.")

menu()
