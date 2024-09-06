import django
django.setup()

from scheduleapp.models import Subject, Teacher, Class, Student, Schedule, Grade

def add_subject():
    name = input("Введіть назву предмета: ")
    if Subject.objects.filter(name=name).exists():
        print("Предмет вже існує!")
    else:
        subject = Subject(name=name)
        subject.save()
        print(f"Предмет {name} успішно додано.")

def add_teacher():
    first_name = input("Введіть ім'я вчителя: ")
    last_name = input("Введіть прізвище вчителя: ")
    subject_name = input("Введіть назву предмета: ")

    try:
        subject = Subject.objects.get(name=subject_name)
    except Subject.DoesNotExist:
        print(f"Предмет {subject_name} не знайдено.")
        return

    teacher = Teacher(first_name=first_name, last_name=last_name, subject=subject)
    teacher.save()
    print(f"Вчителя {first_name} {last_name} успішно додано.")

def add_class():
    name = input("Введіть назву класу: ")
    year = input("Введіть рік навчання: ")

    if Class.objects.filter(name=name).exists():
        print(f"Клас {name} вже існує!")
    else:
        new_class = Class(name=name, year=year)
        new_class.save()
        print(f"Клас {name} ({year}) успішно додано.")

def add_student():
    first_name = input("Введіть ім'я учня: ")
    last_name = input("Введіть прізвище учня: ")
    class_name = input("Введіть назву класу: ")

    try:
        student_class = Class.objects.get(name=class_name)
    except Class.DoesNotExist:
        print(f"Клас {class_name} не знайдено.")
        return

    student = Student(first_name=first_name, last_name=last_name, student_class=student_class)
    student.save()
    print(f"Учня {first_name} {last_name} успішно додано.")

def add_schedule():
    day_of_week = input("Введіть день тижня: ")
    start_time = input("Введіть час початку (формат ЧЧ:ХХ): ")
    subject_name = input("Введіть назву предмета: ")
    class_name = input("Введіть назву класу: ")
    teacher_name = input("Введіть прізвище вчителя: ")

    try:
        subject = Subject.objects.get(name=subject_name)
        class_group = Class.objects.get(name=class_name)
        teacher = Teacher.objects.get(last_name=teacher_name)
    except (Subject.DoesNotExist, Class.DoesNotExist, Teacher.DoesNotExist) as e:
        print(f"Помилка: {e}")
        return

    schedule = Schedule(day_of_week=day_of_week, start_time=start_time, subject=subject, class_group=class_group, teacher=teacher)
    schedule.save()
    print("Заняття додано до розкладу.")

def add_grade():
    student_name = input("Введіть ім'я учня: ")
    subject_name = input("Введіть назву предмета: ")
    grade_value = input("Введіть оцінку: ")
    date_value = input("Введіть дату (формат РРРР-ММ-ДД): ")

    try:
        student = Student.objects.get(first_name=student_name)
        subject = Subject.objects.get(name=subject_name)
    except (Student.DoesNotExist, Subject.DoesNotExist) as e:
        print(f"Помилка: {e}")
        return

    grade = Grade(student=student, subject=subject, grade=grade_value, date=date_value)
    grade.save()
    print("Оцінку додано.")
if __name__ == "__main__":
    while True:
        print("\nОберіть операцію:")
        print("1. Додати предмет")
        print("2. Додати вчителя")
        print("3. Додати клас")
        print("4. Додати учня")
        print("5. Додати заняття в розклад")
        print("6. Додати оцінку")
        print("7. Вийти")

        choice = input("Ваш вибір: ")

        if choice == '1':
            add_subject()
        elif choice == '2':
            add_teacher()
        elif choice == '3':
            add_class()
        elif choice == '4':
            add_student()
        elif choice == '5':
            add_schedule()
        elif choice == '6':
            add_grade()
        elif choice == '7':
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")
