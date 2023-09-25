from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey

Base = declarative_base()


class Student(Base):
    __tablename__ = "student"
    student_id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    age = Column(Integer, nullable=False)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return (
            f"This is {self.student_id} student '{self.name}' Age: {self.age}"
        )


class Subject(Base):
    __tablename__ = "subject"

    subject_id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    length = Column(String(30), nullable=False)

    def __init__(self, name, length):
        self.name = name
        self.length = length

    def __repr__(self):
        return f"ID: {self.subject_id} subject: '{self.name}' lenght: '{self.length}'"


class StudentSubject(Base):
    __tablename__ = "student_subject"

    student_subject_id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("student.student_id"))
    subject_id = Column(Integer, ForeignKey("subject.subject_id"))

    def __init__(self, student_id, subject_id):
        self.student_id = student_id
        self.subject_id = subject_id

    def __repr__(self):
        return f"student_id: {self.student_id} subject_id: {self.subject_id} id: {self.student_subject_id}"


if __name__ == "__main__":
    DATABASE_URI = "postgresql://{user}:{password}@{host}:{port}/{database}"
    engine = create_engine(
        DATABASE_URI.format(
            host="localhost",
            database="postgres",
            user="serhii",
            password="",
            port=5432,
        ),
        echo=True,
    )

    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    s = Session()

    students_add = [
        Student("Bae", 22),
        Student("Eddy", 23),
        Student("Lily", 21),
        Student("Jenny", 22),
    ]
    s.bulk_save_objects(students_add)
    s.commit()

    subjects_add = [
        Subject("English", "32 weeks"),
        Subject("SQL", "4 weeks"),
        Subject("Spanish", "27 weeks"),
        Subject("Chinese", "142 weeks"),
        Subject("Math", "73 weeks"),
    ]
    s.bulk_save_objects(subjects_add)
    s.commit()

    students_subjects_add = [
        StudentSubject(1, 1),
        StudentSubject(2, 2),
        StudentSubject(3, 3),
        StudentSubject(4, 4),
        StudentSubject(2, 1),
    ]
    s.bulk_save_objects(students_subjects_add)
    s.commit()

    q = (
        s.query(Student.name)
        .select_from(StudentSubject)
        .join(Student, Student.student_id == StudentSubject.student_id)
        .join(Subject, Subject.subject_id == StudentSubject.subject_id)
        .where(Subject.name.like("English"))
    )
    for name in q:
        print(name)

    s.close()
