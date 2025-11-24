# **Student Admission Data Collector (Python Project)**

A simple and efficient **console-based student admission management system** written in Python.  
This program allows users to add new admissions, view all saved records, and search for a student by their Admission ID.  
All records are stored in a structured text file (`admissions.txt`) for easy retrieval.

---

## 📌 **Features**

- 🔢 **Auto-generated Admission ID**
- ➕ **Add new student admission**
- 📄 **Store records in a text file (`admissions.txt`)**
- 👀 **View all saved admissions**
- 🔍 **Search admission by ID**
- 🧱 **OOP-based design using classes**
- 💾 **Persistent storage**
- 🖥️ **Simple and clean text-based menu**

---

## 📁 **Project Structure**

```
.
├── main.py               # Main program (your provided code)
├── admissions.txt        # Auto-created data storage file
└── README.md             # GitHub project documentation
```

---

## 🧠 **How the Program Works**

### **StudentAdmission Class**
Handles:
- Initializing student data  
- Converting objects to file-friendly format  
- Parsing lines back into objects  
- Displaying formatted records  

### **Data Storage (`admissions.txt`)**
Each record is stored in a pipe-separated format:

```
AdmissionID|Name|Age|Gender|Course|Phone|Email|Address
```

Example:
```
1001|John Doe|18|M|B.Sc|9876543210|john@gmail.com|Delhi
```

### **Menu Options**
When the program runs, the following menu appears:

```
1. Add New Admission
2. View All Admissions
3. Search Admission by ID
4. Exit
```


### **Requirements**
- Python 3.x  
- Works on Windows, Linux, and macOS  


## 📈 **Future Enhancements**

- Input validation (email format, phone number, age, etc.)
- Update/Delete student records
- GUI version using Tkinter or PyQt
- SQLite/SQL database integration
- Export data to CSV or PDF
- Search by name, course, phone number
- Web-based version using Flask or Django

