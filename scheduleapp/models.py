from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=128)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Class(models.Model):
    name = models.CharField(max_length=32)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=128)
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Schedule(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    class_group = models.ForeignKey(Class, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    data = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.IntegerField(max_length=2)

    def __str__(self) -> str:
        return f"{self.student}' in {self.subject} grade is {self.grade}"