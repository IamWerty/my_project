import django_setup
from scheduleapp.models import Student, Class, Teacher

students = Student.objects.all()

if __name__ == "__main__":
    for stud in students:
        print(f"{stud}")