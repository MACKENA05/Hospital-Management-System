# Hospital Management System

This is a simple Hospital Management System built using Python, SQLAlchemy, and Click. The system allows you to manage departments, doctors, patients, and appointments in a hospital setting.

## Table of Contents
1. [Features](#features)
2. [Installation](#installation)
   - [Step 1: Set Up a Virtual Environment](#step-1-set-up-a-virtual-environment)
   - [Step 2: Install Required Dependencies](#step-2-install-required-dependencies)
   - [Step 3: Set Up the Database](#step-3-set-up-the-database)
   - [Step 4: Run the Application](#step-4-run-the-application)
3. [Usage](#usage)
   - [Start the Menu](#start-the-menu)
   - [Follow the On-Screen Prompts](#follow-the-on-screen-prompts)
4. [Database Schema](#database-schema)
   - [Departments](#departments)
   - [Doctors](#doctors)
   - [Patients](#patients)
   - [Appointments](#appointments)
5. [Example Data](#example-data)
   - [How to Run the Seed Script](#how-to-run-the-seed-script)
   - [Example Data Included](#example-data-included)
6. [Contributing](#contributing)
7. [License](#license)
8. [Acknowledgments](#acknowledgments)

## Features

- **Add Department**: Add a new department to the hospital.
- **Add Doctor**: Add a new doctor to a specific department.
- **Add Patient**: Add a new patient to the system.
- **Schedule Appointment**: Schedule an appointment between a doctor and a patient.
- **View Departments**: View all departments in the hospital.
- **View Doctors**: View all doctors in the hospital.
- **View Patients**: View all patients in the system.
- **View Appointments**: View all scheduled appointments.
- **Delete Department**: Delete a department from the system.
- **Delete Doctor**: Delete a doctor from the system.
- **Delete Patient**: Delete a patient from the system.
- **Delete Appointment**: Delete an appointment from the system.
- **Update Appointment**: Update an existing appointment.
- **View Doctors in Department**: View all doctors in a specific department.
- **View Appointments for Doctor**: View all appointments for a specific doctor.
- **View Appointments for Patient**: View all appointments for a specific patient.
- **List Doctors and Appointments for Department**: List all doctors and their appointments in a specific department.
- **Search for Patient by Name**: Search for a patient by their name.
- **Search for Doctor by Name**: Search for a doctor by their name.

---

## Installation

### Step 1: Set Up a Virtual Environment
It is recommended to use a virtual environment to manage dependencies for this project.

1. **Create a virtual environment**:
```bash
   python -m venv env
```
2. **Activate the virtual environment**:
```bash
source venv/bin/activate
```
3. **Deactivate the virtual environment (when done)**:
```bash
deactivate
```

### Step 2: Install Required Dependencies
Install the required Python packages using pip.

1. **Install SQLAlchemy**:
SQLAlchemy is used for ORM (Object-Relational Mapping) to interact with the database.
```bash
pip install sqlalchemy
```
2. **Install Alembic**:
Alembic is used for database migrations.
```bash
pip install alembic
```
3. **Install Click**:
Click is used to create the command-line interface (CLI) for the application.
```bash
pip install click
```
4. **Install other dependencies**:
If you have a requirements.txt file, you can install all dependencies at once:
```bash
pip install -r requirements.txt
```

### Step 3: Set Up the Database
The system uses SQLite as the database. The database file hospital.db will be created automatically when you run the application for the first time.

### Step 4: Run the Application
To start the application, run:
```bash
python main.py
```

## Usage
1. **Start the Menu**

To start the application, run:
```bash
python main.py start-menu
```

2. **Follow the On-Screen Prompts**
The system will display a menu with options to manage departments, doctors, patients, and appointments. Follow the prompts to perform actions like adding, viewing, updating, or deleting records.

## Database Schema
The database consists of the following tables:

1.**Departments**
- `department_id` (Primary Key)

- `department_name`

2. **Doctors**
- `doctor_id` (Primary Key)

- `doctor_name`

- `department_id` (Foreign Key referencing departments)

3. **Patients**
- `patient_id` (Primary Key)

- `patient_name`

- `phone_number`

4. **Appointments**
- `appointment_id` (Primary Key)

- `doctor_id` (Foreign Key referencing doctors)

- `patient_id` (Foreign Key referencing patients)

- `appointment_date`

## Example Data (SEEDING)
The system comes with a `seed.py` script that populates the database with example data. This is useful for testing and demonstration purposes.

### How to Run the Seed Script
1. Ensure the database is set up and the application is installed.

2. Run the seed script using the following command:

```bash
python seed.py
```

#### Example Data Included
The seed script adds the following data to the database:

1. **Departments**
- Cardiology

- Neurology

2. **Doctors**
- Dr. Monicah (Cardiology)

- Dr. Jeff (Neurology)

3. Patients
- Alex Martin

- Jane Alice

4. Appointments
Sample appointments for the above doctors and patients.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue if you find any bugs or have suggestions for improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments
1. SQLAlchemy for ORM support.

2. Alembic for database migrations.

3. Click for creating command-line interfaces.