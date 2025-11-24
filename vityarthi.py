import os

DATA_FILE = "admissions.txt"


class StudentAdmission:
    def __init__(self, adm_id, name, age, gender, course, phone, email, address):
        self.adm_id = adm_id
        self.name = name
        self.age = age
        self.gender = gender
        self.course = course
        self.phone = phone
        self.email = email
        self.address = address

    def to_line(self):
        # Convert object to one line for file storage
        return f"{self.adm_id}|{self.name}|{self.age}|{self.gender}|{self.course}|{self.phone}|{self.email}|{self.address}\n"

    @staticmethod
    def from_line(line):
        parts = line.strip().split("|")
        if len(parts) != 8:
            return None
        return StudentAdmission(*parts)

    def display(self):
        print("-" * 40)
        print(f"Admission ID : {self.adm_id}")
        print(f"Name         : {self.name}")
        print(f"Age          : {self.age}")
        print(f"Gender       : {self.gender}")
        print(f"Course       : {self.course}")
        print(f"Phone        : {self.phone}")
        print(f"Email        : {self.email}")
        print(f"Address      : {self.address}")
        print("-" * 40)


def ensure_file():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            pass  # create empty file


def generate_new_id():
    ensure_file()
    last_id = 1000
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        for line in f:
            obj = StudentAdmission.from_line(line)
            if obj:
                try:
                    num = int(obj.adm_id)
                    if num > last_id:
                        last_id = num
                except ValueError:
                    continue
    return str(last_id + 1)


def add_admission():
    print("\n=== Add New Student Admission ===")
    adm_id = generate_new_id()
    print(f"Generated Admission ID: {adm_id}")

    name = input("Student Name          : ").strip()
    age = input("Age                   : ").strip()
    gender = input("Gender (M/F/Other)    : ").strip()
    course = input("Course Applied For    : ").strip()
    phone = input("Phone Number          : ").strip()
    email = input("Email                 : ").strip()
    address = input("Address               : ").strip()

    student = StudentAdmission(adm_id, name, age, gender, course, phone, email, address)

    with open(DATA_FILE, "a", encoding="utf-8") as f:
        f.write(student.to_line())

    print("\nRecord saved successfully!")
    input("Press Enter to continue...")


def load_all_admissions():
    ensure_file()
    records = []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        for line in f:
            obj = StudentAdmission.from_line(line)
            if obj:
                records.append(obj)
    return records


def view_all_admissions():
    print("\n=== All Student Admissions ===")
    records = load_all_admissions()
    if not records:
        print("No records found.")
    else:
        for s in records:
            s.display()
    input("Press Enter to continue...")


def search_by_id():
    print("\n=== Search Admission by ID ===")
    search_id = input("Enter Admission ID: ").strip()
    found = False
    for s in load_all_admissions():
        if s.adm_id == search_id:
            print("\nRecord found:")
            s.display()
            found = True
            break
    if not found:
        print("No record found with that Admission ID.")
    input("Press Enter to continue...")


def main_menu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("====================================")
        print("   STUDENT ADMISSION DATA COLLECTOR ")
        print("====================================")
        print("1. Add New Admission")
        print("2. View All Admissions")
        print("3. Search Admission by ID")
        print("4. Exit")
        print("====================================")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_admission()
        elif choice == "2":
            view_all_admissions()
        elif choice == "3":
            search_by_id()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")


if __name__ == "__main__":
    main_menu()
