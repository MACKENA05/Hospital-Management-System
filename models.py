from sqlalchemy import Column, Integer,String,ForeignKey,create_engine,DateTime
from sqlalchemy.orm import sessionmaker,declarative_base,relationship

db_url = "sqlite:///hospital.db"

engine = create_engine(db_url)

Base = declarative_base()

class Department(Base):
    __tablename__ = 'departments'

    department_id = Column(Integer, primary_key=True)
    department_name = Column(String, nullable=False)
    
    doctors = relationship('Doctor', back_populates='department')


class Doctor(Base):
    __tablename__ = 'doctors'

    doctor_id = Column(Integer, primary_key=True)
    doctor_name = Column(String, nullable=False)
    department_id = Column(Integer, ForeignKey('departments.department_id'))

    department = relationship('Department', back_populates='doctors')
    appointments = relationship('Appointment', back_populates = 'doctor')

class Patient(Base):
    __tablename__ = 'patients'

    patient_id = Column(Integer, primary_key=True)
    patient_name = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)

    appointments = relationship('Appointment', back_populates='patient')

class Appointment(Base):
    __tablename__ = 'appointments'

    appointment_id = Column(Integer, primary_key=True)
    doctor_id = Column(Integer, ForeignKey('doctors.doctor_id'))
    patient_id = Column(Integer, ForeignKey('patients.patient_id'))
    appointment_date = Column(DateTime, nullable=False)

    doctor = relationship('Doctor', back_populates='appointments')
    patient = relationship('Patient', back_populates='appointments')
    
Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()