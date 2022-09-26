class Patient:

    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.patient_id = ""
        self.patient_age = ""
        self.tests = []

    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def adult_or_minor(self):
        if self.patient_age >= 18:
            return "adult"
        else:
            return "minor"


def create_patient_entry(patient_first_name, patient_last_name, patient_id, patient_age):
        new_patient = Patient()
        new_patient.first_name = patient_first_name
        new_patient.last_name = patient_last_name
        new_patient.patient_id = patient_id
        new_patient.patient_age = patient_age
        return new_patient


def print_database(db):
    for key in db.values():
        print("Name: {}, id: {}, age: {}".format(key.full_name(),
              key.patient_id, key.patient_age))


def find_patient(db, patient_id):
    patient = db[patient_id]
    return patient


def add_test(db,patient_id,test_name,test_value):
    patient = find_patient(db,patient_id)
    patient.tests.append((test_name,test_value))


def main():
    db = {}
    db[11] = create_patient_entry("Ann", "Ables", 11, 30)
    db[22] = create_patient_entry("Bob", "Boyles", 22, 34)
    db[3] = create_patient_entry("Chris", "Chou", 3, 25)
    print_database(db)
    add_test(db, 3, "HDL", 100)
    print_database(db)
    print (db[3].tests)
    check = db[3]
    print("Patient {} is a {}".format(check.full_name(),
                                      check.adult_or_minor()))


if __name__ == "__main__":
    main ()