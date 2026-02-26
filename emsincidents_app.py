
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
        
def get_gender(message):
    gender_map = {"f": "FEMININE", "m": "MASCULINE"}
    while True:
        gender = input(message).strip().lower()
        if gender in gender_map:
            return gender_map[gender]
        print("Gender must be M or F. Try again.")

def get_medical_history():
    history = []
    print("Enter medical conditions (type 'done' to finish):")
    
    while True:
        condition = input("> ").strip()
        if condition.lower() == "done":
            break
        if condition:
            history.append(condition)
    
    return history

class Response:
    def __init__(self, unit_dispatched, call_type):
        time_dispatched = datetime.now()
        formatted_time = time_dispatched.strftime("%H:%M:%S")
        self.unit_dispatched = unit_dispatched
        self.time_dispatched = formatted_time
        self.call_type = call_type  #"Medical", "Trauma"

# Sección Scene (ubicación y condiciones)
class Scene:
    def __init__(self, location, patient_condition, scene_notes):
        self.location = location
        self.patient_condition = patient_condition
        self.scene_notes = scene_notes

# Sección Personnel (equipo en escena)
class Personnel:
    def __init__(self, medic_name, role, certification):
        self.medic_name = medic_name
        self.role = role  # e.g., Paramedic, EMT
        self.certification = certification

# Sección Patient
class Patient:
    def __init__(self, name, lastname, age, gender, medical_history=None):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.gender = gender
        self.medical_history = medical_history or []

# Sección Medications (si se administraron)
class Medications:
    def __init__(self):
        self.administered = []  # lista de tuplas: (medication_name, dose, time)

    def add_medication(self, name, dose, time):
        self.administered.append((name, dose, time))

# Clase principal Incident
class Incident:
    counter = 1
    def __init__(self, agency_code, description, response, scene, personnel, patient, medications):
        self.date = datetime.now()
        self.num = f"{self.date.strftime('%Y-%m%d')}{Incident.counter:04d}-{agency_code}"
        Incident.counter += 1

        self.description = description

        self.response = response
        self.scene = scene
        self.personnel = personnel
        self.patient = patient
        self.medications = medications

    def __str__(self):
        date_str = self.date.strftime("%Y-%m-%d %H:%M:%S")
        meds_str = "\n".join([f"{m[0]}: {m[1]} at {m[2]}" for m in self.medications.administered]) or "None"

        return (
            f"Incident Number: {self.num}\n"
            f"Description: {self.description}\n"
            f"Date: {date_str}\n\n"
            f"--- Response ---\n"
            f"Unit: {self.response.unit_dispatched}\n"
            f"Time Dispatched: {self.response.time_dispatched}\n"
            f"Call Type: {self.response.call_type}\n\n"
            f"--- Scene ---\n"
            f"Location: {self.scene.location}\n"
            f"Patient Condition: {self.scene.patient_condition}\n"
            f"Notes: {self.scene.scene_notes}\n\n"
            f"--- Personnel ---\n"
            f"Name: {self.personnel.medic_name}\n"
            f"Role: {self.personnel.role}\n"
            f"Certification: {self.personnel.certification}\n\n"
            f"--- Patient ---\n"
            f"Name: {self.patient.name} {self.patient.lastname}\n"
            f"Age: {self.patient.age}\n"
            f"Gender: {self.patient.gender}\n"
            f"Medical History: {', '.join(self.patient.medical_history) if self.patient.medical_history else 'None'}\n\n"
            f"--- Medications ---\n"
            f"{meds_str}"
        )
 
    
def create_incident(agency_id):
    description = input("Description: ")
    print("\n" + "--RESPONSE--")
    unit = input("Assigned Unit: ")
    type_call = input("Call Type: ")
    print("\n" + "--SCENE--")
    scene_location = input("Scene Location: ")
    person_condition = input("Patient Condition: ")
    notes = input("Scene Notes: ")
    print("\n" + "--PERSONNEL--")
    paramedic_name = input("Medic Full Name: ")
    medic_role = input("Role: ")
    medic_certification = input("Certification: ")
    print("\n" + "--PATIENT--")
    patient_name = input("Patient Name: ")
    patient_lastname = input("Patient Lastname: ")
    patient_age = get_int_age("Patient Age: ")
    patient_gender = get_gender("Select gender: MASCULINE(m) | FEMININE(f)")
    medical_history = get_medical_history()
    medical_history = [item.strip() for item in medical_history if item.strip()]
    print("\n" + "--MEDICATIONS--")
    meds = Medications()
    medication_name = input("Medication Name: ")
    medication_dose = input("Medication Dose: ")
    administration_time = input("Administration Time: ")
    meds.add_medication(medication_name, medication_dose, administration_time)
    


    incident_response = Response(unit, type_call)
    incident_scene = Scene(scene_location, person_condition, notes)
    personnel_information = Personnel(paramedic_name, medic_role, medic_certification)
    patient_information = Patient(patient_name, patient_lastname, patient_age, patient_gender, medical_history)
    record = Incident(agency_id, description, incident_response, incident_scene, personnel_information, patient_information, meds)
    print("\n" + "-" * 35)
    print("\n" + "-" * 35)
    print(f"\nIncident added successfully \n{record}")
    print("\n" + "-" * 35)
    print("\n" + "-" * 35)
    return record

def menu():
    agency_code = get_agency_code("Enter your agency code: ")
    incidents_list = []
    while True:
        print("\n" + "-" * 35)
        print("| CareReport 0.01 alfa version |")
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