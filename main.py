import click
from models import session, Department, Doctor, Patient, Appointment
from sqlalchemy.exc import IntegrityError, NoResultFound
from datetime import datetime

# validation
def validate_date(date):
    try:
        return datetime.strptime(date, "%Y-%m-%d %H:%M")
    except ValueError:
        return None
    
# Click Group
@click.group()
def cli():
    """Hospital Management System CLI"""
    pass

# Add Department
def add_department(name):
    try:
        department = Department(department_name=name)
        session.add(department)
        session.commit()
        click.echo(f"'{name}' department added successfully.")
    except IntegrityError:
        session.rollback()
        click.echo("Error: Department name must be unique.")
    finally:
        session.close


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
    while true:
        show_menu()
        choice = click.prompt("Enter your choice", type = int)

    if choice == 1:
        name = click.prompt("Enter department name")
        add_department(name)

    else:
        click.echo("Invalid choice.Try again")

#menu command
@cli.command()
def start_menu():
    menu()

if __name__ == "__main__":
    cli()