import click
from models import session, Department, Doctor, Patient, Appointment
from datetime import datetime

# Validation
def validate_date(date):
    try:
        return datetime.strptime(date, "%Y-%m-%d %H:%M")
    except ValueError:
        return None

# Add Department
def add_department(name):
    try:
        department = Department(department_name=name)
        session.add(department)
        session.commit()
        click.echo(f"'{name}' department added successfully.")
    except Exception as e:
        session.rollback()
        click.echo(f"Error adding department: {e}")
    finally:
        session.close()

# Adding Doctors
def add_doctor(name, department_id):
    try:
        department = session.query(Department).filter_by(department_id=department_id).one()
        doctor = Doctor(doctor_name=name, department_id=department_id)
        session.add(doctor)
        session.commit()
        click.echo(f"'{name}' added successfully in '{department.department_name}' department")
    except Exception as e:
        session.rollback()
        click.echo(f'Error adding Doctor: {e}')
    finally:
        session.close()

# Adding Patients
def add_patient(name, phone_number):
    try:
        patient = Patient(patient_name=name, phone_number=phone_number)
        session.add(patient)
        session.commit()
        click.echo(f"Patient {name} added successfully")
    except Exception as e:
        session.rollback()
        click.echo(f"Error adding patient: {e}")
    finally:
        session.close()

# Scheduling an Appointment
def schedule_appointment(doctor_id, patient_id, date_time):
    date_time = validate_date(date_time)
    if not date_time:
        click.echo("Invalid date format. Use 'YYYY-MM-DD HH:MM'.")
        return
    try:
        doctor = session.query(Doctor).filter_by(doctor_id=doctor_id).one()
        patient = session.query(Patient).filter_by(patient_id=patient_id).one()
        appointment = Appointment(doctor_id=doctor_id, patient_id=patient_id, appointment_date=date_time)
        session.add(appointment)
        session.commit()
        click.echo(f"Appointment for {patient.patient_name} scheduled on {date_time.strftime('%Y-%m-%d %H:%M')} with {doctor.doctor_name} added successfully")
    except Exception as e:
        session.rollback()
        click.echo(f"Error scheduling the appointment: {e}")
    finally:
        session.close()

# Viewing All Departments
def view_departments():
    departments = session.query(Department).all()
    if not departments:
        click.echo("No departments found")
    else:
        for department in departments:
            click.echo(f"{department.department_id}  Name: {department.department_name}")

# Viewing All Doctors
def view_doctors():
    doctors = session.query(Doctor).all()
    if not doctors:
        click.echo("No doctors found")
    else:
        for doctor in doctors:
            click.echo(f"{doctor.doctor_id}.  Name: {doctor.doctor_name}  Department: {doctor.department_id}")

# Viewing All Patients
def view_patients():
    patients = session.query(Patient).all()
    if not patients:
        click.echo("No patients found")
    else:
        for patient in patients:
            click.echo(f"{patient.patient_id}  Name: {patient.patient_name}  Phone Number: {patient.phone_number}")

# Viewing All Appointments
def view_appointments():
    appointments = session.query(Appointment).all()
    if not appointments:
        click.echo("No appointments found")
    else:
        for appointment in appointments:
            click.echo(f"{appointment.appointment_id},  Doctor ID: {appointment.doctor_id},  Patient ID: {appointment.patient_id},  Date: {appointment.appointment_date.strftime('%Y-%m-%d %H:%M')}")

# Delete Department
def delete_department(department_id):
    try:
        department = session.query(Department).filter_by(department_id=department_id).one()
        session.delete(department)
        session.commit()
        click.echo(f"{department.department_name} department deleted successfully")
    except Exception as e:
        session.rollback()
        click.echo(f"Error deleting the department: {e}")
    finally:
        session.close()

# Delete Doctor
def delete_doctor(doctor_id):
    try:
        doctor = session.query(Doctor).filter_by(doctor_id=doctor_id).one()
        session.delete(doctor)
        session.commit()
        click.echo(f"{doctor.doctor_name} deleted successfully")
    except Exception as e:
        session.rollback()
        click.echo(f"Error deleting the doctor: {e}")
    finally:
        session.close()

# Delete Patient
def delete_patient(patient_id):
    try:
        patient = session.query(Patient).filter_by(patient_id=patient_id).one()
        session.delete(patient)
        session.commit()
        click.echo(f"{patient.patient_name} deleted successfully")
    except Exception as e:
        session.rollback()
        click.echo(f"Error deleting the patient: {e}")
    finally:
        session.close()

# Delete Appointment
def delete_appointment(appointment_id):
    try:
        appointment = session.query(Appointment).filter_by(appointment_id=appointment_id).one()
        session.delete(appointment)
        session.commit()
        click.echo(f"Appointment {appointment.appointment_id} deleted successfully")
    except Exception as e:
        session.rollback()
        click.echo(f"Error deleting the appointment: {e}")
    finally:
        session.close()

# Update Appointment
def update_appointment(appointment_id):
    try:
        appointment = session.query(Appointment).filter_by(appointment_id=appointment_id).one()
        click.echo(f"Current Appointment Details:")
        click.echo(f"  Doctor ID: {appointment.doctor_id}")
        click.echo(f"  Patient ID: {appointment.patient_id}")
        click.echo(f"  Date/Time: {appointment.appointment_date.strftime('%Y-%m-%d %H:%M')}")

        # New details prompt
        new_doctor_id = click.prompt("Enter new doctor ID (or press Enter to keep current)", default=appointment.doctor_id, type=int)
        new_patient_id = click.prompt("Enter new patient ID (or press Enter to keep current)", default=appointment.patient_id, type=int)
        new_date_time = click.prompt("Enter new date and time (YYYY-MM-DD HH:MM) (or press Enter to keep current)", default=appointment.appointment_date.strftime("%Y-%m-%d %H:%M"))

        new_date_time = validate_date(new_date_time)
        if not new_date_time:
            click.echo("Error: Invalid date format. Use 'YYYY-MM-DD HH:MM'.")
            return

        appointment.doctor_id = new_doctor_id
        appointment.patient_id = new_patient_id
        appointment.appointment_date = new_date_time
        session.commit()
        click.echo(f"Appointment ID {appointment_id} updated successfully.")
    except Exception as e:
        session.rollback()
        click.echo(f"Error updating the appointment: {e}")
    finally:
        session.close()

# View Doctors in Department
def view_doctors_in_department(department_id):
    try:
        department = session.query(Department).filter_by(department_id=department_id).one()
        doctors = session.query(Doctor).filter_by(department_id=department_id).all()
        if not doctors:
            click.echo(f"No doctors found in {department.department_name} department")
        else:
            click.echo(f"Doctors in {department.department_name} department:")
            for doctor in doctors:
                click.echo(f"Doctor ID: {doctor.doctor_id}, Name: {doctor.doctor_name}")
    except Exception as e:
        click.echo(f"Error viewing doctors in this department: {e}")
    finally:
        session.close()

# View Appointments for Doctor
def view_appointments_for_doctor(doctor_id):
    try:
        doctor = session.query(Doctor).filter_by(doctor_id=doctor_id).one()
        appointments = session.query(Appointment).filter_by(doctor_id=doctor_id).all()
        if not appointments:
            click.echo(f"No appointments found for {doctor.doctor_name}")
        else:
            click.echo(f"Appointments for {doctor.doctor_name}:")
            for appointment in appointments:
                click.echo(f"Appointment ID: {appointment.appointment_id}, Patient ID: {appointment.patient_id}, Date: {appointment.appointment_date.strftime('%Y-%m-%d %H:%M')}")
    except Exception as e:
        click.echo(f"Error fetching appointments: {e}")
    finally:
        session.close()

# View Appointments for Patient
def view_appointments_for_patient(patient_id):
    try:
        patient = session.query(Patient).filter_by(patient_id=patient_id).one()
        appointments = session.query(Appointment).filter_by(patient_id=patient_id).all()
        if not appointments:
            click.echo(f"No appointments found for Patient {patient.patient_name}")
        else:
            click.echo(f"Appointments for {patient.patient_name}:")
            for appointment in appointments:
                click.echo(f"  Appointment ID: {appointment.appointment_id}, Doctor ID: {appointment.doctor_id}, Date: {appointment.appointment_date.strftime('%Y-%m-%d %H:%M')}")
    except Exception as e:
        click.echo(f"Error getting appointments: {e}")
    finally:
        session.close()

# List Doctors and Appointments for Department
def list_doctors_and_appointments(department_id):
    try:
        department = session.query(Department).filter_by(department_id=department_id).one()
        click.echo(f"Doctors and appointments in department '{department.department_name}':")

        doctors = session.query(Doctor).filter_by(department_id=department_id).all()
        if not doctors:
            click.echo("No doctors found in this department.")
            return

        for doctor in doctors:
            click.echo(f"\nDoctor ID: {doctor.doctor_id}, Name: {doctor.doctor_name}")
            appointments = session.query(Appointment).filter_by(doctor_id=doctor.doctor_id).all()
            if not appointments:
                click.echo("  No appointments found for this doctor.")
            else:
                for appointment in appointments:
                    patient = session.query(Patient).filter_by(patient_id=appointment.patient_id).one()
                    click.echo(f"  Appointment ID: {appointment.appointment_id}, Patient: {patient.patient_name}, Date: {appointment.appointment_date.strftime('%Y-%m-%d %H:%M')}")
    except Exception as e:
        click.echo(f"Error listing doctors and appointments for a certain department: {e}")
    finally:
        session.close()

# Search for Patient by Name
def search_patient_by_name(name):
    patients = session.query(Patient).filter(Patient.patient_name.ilike(f"%{name}%")).all()
    if not patients:
        click.echo(f"No patient found with name containing '{name}'")
    else:
        for patient in patients:
            click.echo(f"{patient.patient_id} Name: {patient.patient_name}")

# Search for Doctor by Name
def search_doctor_by_name(name):
    doctors = session.query(Doctor).filter(Doctor.doctor_name.ilike(f"%{name}%")).all()
    if not doctors:
        click.echo(f"No doctors found with name containing '{name}'.")
    else:
        click.echo(f"Doctors found with name containing '{name}':")
        for doctor in doctors:
            click.echo(f"ID: {doctor.doctor_id}, Name: {doctor.doctor_name}, Department ID: {doctor.department_id}")

# Menu System
def show_menu():
    click.echo("\nHospital Management System")
    click.echo("1. Add Department")
    click.echo("2. Add Doctor")
    click.echo("3. Add Patient")
    click.echo("4. Schedule Appointment")
    click.echo("5. View All Departments")
    click.echo("6. View All Doctors")
    click.echo("7. View All Patients")
    click.echo("8. View All Appointments")
    click.echo("9. Delete Department")
    click.echo("10. Delete Doctor")
    click.echo("11. Delete Patient")
    click.echo("12. Delete Appointment")
    click.echo("13. Update Appointment")
    click.echo("14. View Doctors in Department")
    click.echo("15. View Appointments for Doctor")
    click.echo("16. View Appointments for Patient")
    click.echo("17. List Doctors and Appointments for Department")
    click.echo("18. Search for a Patient by Name")
    click.echo("19. Search for a Doctor By Name")
    click.echo("20. EXIT")

def menu():
    while True:
        show_menu()
        choice = click.prompt("Enter your choice", type=int)

        if choice == 1:
            name = click.prompt("Enter department name")
            add_department(name)
        elif choice == 2:
            name = click.prompt("Enter doctor name")
            department_id = click.prompt("Enter the department ID", type=int)
            add_doctor(name, department_id)
        elif choice == 3:
            name = click.prompt("Enter patient name")
            phone_number = click.prompt("Enter patient's phone number")
            add_patient(name, phone_number)
        elif choice == 4:
            doctor_id = click.prompt("Enter doctor ID", type=int)
            patient_id = click.prompt("Enter patient ID", type=int)
            date_time = click.prompt("Enter the appointment date and time (YYYY-MM-DD HH:MM)")
            schedule_appointment(doctor_id, patient_id, date_time)
        elif choice == 5:
            view_departments()
        elif choice == 6:
            view_doctors()
        elif choice == 7:
            view_patients()
        elif choice == 8:
            view_appointments()
        elif choice == 9:
            department_id = click.prompt("Enter department ID to delete", type=int)
            delete_department(department_id)
        elif choice == 10:
            doctor_id = click.prompt("Enter doctor ID to delete", type=int)
            delete_doctor(doctor_id)
        elif choice == 11:
            patient_id = click.prompt("Enter patient ID to delete", type=int)
            delete_patient(patient_id)
        elif choice == 12:
            appointment_id = click.prompt("Enter appointment ID to delete", type=int)
            delete_appointment(appointment_id)
        elif choice == 13:
            appointment_id = click.prompt("Enter appointment ID to update", type=int)
            update_appointment(appointment_id)
        elif choice == 14:
            department_id = click.prompt("Enter department ID", type=int)
            view_doctors_in_department(department_id)
        elif choice == 15:
            doctor_id = click.prompt("Enter doctor ID", type=int)
            view_appointments_for_doctor(doctor_id)
        elif choice == 16:
            patient_id = click.prompt("Enter patient ID", type=int)
            view_appointments_for_patient(patient_id)
        elif choice == 17:
            department_id = click.prompt("Enter department ID", type=int)
            list_doctors_and_appointments(department_id)
        elif choice == 18:
            name = click.prompt("Enter patient name to search")
            search_patient_by_name(name)
        elif choice == 19:
            name = click.prompt("Enter doctor name to search")
            search_doctor_by_name(name)
        elif choice == 20:
            click.echo("Ending the session...")
            break
        else:
            click.echo("Invalid choice. Try again.")

# Click Group
@click.group()
def cli():
    """Hospital Management System CLI"""
    pass

# Menu Command
@cli.command()
def start_menu():
    menu()

if __name__ == "__main__":
    cli()