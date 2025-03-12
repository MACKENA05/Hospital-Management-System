import click
from models import session, Department, Doctor, Patient, Appointment
from datetime import datetime

# validation
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
        click.echo("Error adding department as {e}")
    finally:
        session.close

def add_doctor(name,department_id):
    try:
        department = session.query(Department).filter_by(department_id = department_id).one()
        doctor = Doctor(doctor_name = name, department_id=department_id)
        session.add(doctor)
        session.commit()
        click.echo(f"'{name}' added successfuly in '{department.department_name}' department")
    except Exception as e:
        session.roll()
        click.echo(f'Error adding Doctor: {e}')
    finally:
        session.close()

def add_patient(name, phone_number):
    try:
        patient = Patient(patient_name = name, phone_number=phone_number)
        session.add(patient)
        session.commit()
        click.echo(f"Patient {name} added successfully")
    except Exception as e:
        session.rollback()
        click.echo(f"Error adding patient: {e} ")
    finally:
        session.close()

# def schedule_appointment():
#     date_time = validate_date(date_time)
#     if not date_time:
#         click.echo("Invalid date format.Use 'YYYY-MM-DD HH:MM'.")
#         return
#     try:
#         doctor = session.query(Doctor).filter_by(doctor_id=doctor_id).one()
#         patient = session.query(Patient).filter_by(patient_id=patient_id).one()
#         appointment = Appointment(doctor_id=doctor_id,patient_id=patient_id, appointment_date=date_time)
#         session.add(appointment)
#         session.commit()
#         click.echo(f"Appointment for {patient.patient_name}  scheduled on {date} to {doctor.doctor_name} added successfully ")
#     except Exception as e:
#         session.rollback()
#         click.echo(f"Error scheduling the appointment: {e}")
#     finally:
#         session.close()



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
    click.echo("13. View Doctors in Department")
    click.echo("14. View Appointments for Doctor")
    click.echo("15. View Appointments for Patient")
    click.echo("16. List Doctors and Appointments for Department")
    click.echo("17. Search for a Patient by Name")
    click.echo("18. Search for a Doctor By Name")
    click.echo("19. Exit")

def menu():
    while True:
        show_menu()
        choice = click.prompt("Enter your choice", type = int)

        if choice == 1:
            name = click.prompt("Enter department name")
            add_department(name)
        elif choice == 2:
            name = click.prompt("Enter Doctors name")
            department_id = click.prompt("Enter the department ID")
            add_doctor(name, department_id)
        elif choice == 3:
            name = click.prompt("Enter patient name")
            phone_number = click.prompt("Enter patients phone number")
            add_patient(name,phone_number)
        
        elif choice == 19:
            click.echo("Ending the session .....")
            break

        else:
            click.echo("Invalid choice.Try again")

# Click Group
@click.group()
def cli():
    """Hospital Management System CLI"""
    pass

#menu command
@cli.command()
def start_menu():
    menu()

if __name__ == "__main__":
    cli()