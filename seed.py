from models import session,Department,Doctor,Patient,Appointment
from datetime import datetime

def hosp_data():

    #departments 
    department1 = Department(department_name ="Cardiology")
    department2 = Department(department_name = "Neurology")
    session.add_all([department1, department2])
    session.commit()

    #doctors
    doctor1 = Doctor(doctor_name = "Dr.Monicah", department_id = department1.department_id)
    doctor2 = Doctor(doctor_name= "Dr.Jeff", department_id = department2.department_id)
    session.add_all([doctor1, doctor2])
    session.commit()

    #patients
    patient1 = Patient(patient_name = "Alex Martin", phone_number = "123 456 566")
    patient2 = Patient(patient_name = "Jane Alice", phone_number = "078 345 678")
    session.add_all([patient1, patient2])
    session.commit()

    #appointments
    appointment1 = Appointment(
        doctor_id = doctor1.doctor_id,
        patient_id = patient1.patient_id,
        appointment_date = datetime(2023,10,16,10,0)
    )
    
    appointment2 = Appointment(
        doctor_id = doctor2.doctor_id,
        patient_id = patient2.patient_id,
        appointment_date = datetime(2023,10,16,11,0)
    )
    session.add_all([appointment1, appointment2])
    session.commit()

    print("seeded successfully")

if __name__ == "__main__":
    hosp_data()