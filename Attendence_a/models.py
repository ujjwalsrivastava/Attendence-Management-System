from django.db import models

class Signup_teacher(models.Model):
    userid=models.CharField(max_length=30)
    password=models.CharField(max_length=10)
    first_n=models.CharField(max_length=30)
    last_n=models.CharField(max_length=30)
    email_id=models.EmailField(null=True)
    class Meta:
        db_table='Signup_teacher'

class Add_student(models.Model):
    userid=models.CharField(max_length=50)
    password=models.CharField(max_length=10)
    first_n=models.CharField(max_length=20,null=True)
    last_n=models.CharField(max_length=20,null=True)
    email_id=models.EmailField(null=True)
    teacher_id=models.CharField(max_length=50,null=True)
    subject=models.CharField(max_length=50,null=True)
    class_c=models.CharField(max_length=50,null=True)
    class Meta:
        db_table='Add_student'

    def __str__(self):
        return self.userid

class Add_class(models.Model):
    teacher_id=models.CharField(max_length=50)
    class_c=models.CharField(max_length=30)
    class Meta:
        db_table='Add_class'

class Add_subject(models.Model):
    teacher_id=models.CharField(max_length=50)
    subject=models.CharField(max_length=30)
    class Meta:
        db_table='Add_subject'

class Teacher_subject_class(models.Model):
    teacher_id=models.CharField(max_length=20,null=True)
    subject=models.CharField(max_length=20,null=True)
    class_c=models.CharField(max_length=20,null=True)
    class Meta:
        db_table='teacher_subject_class'

class Attendence(models.Model):
    userid=models.CharField(max_length=40,null=True)
    teacher_id=models.CharField(null=True,max_length=10)
    date=models.DateField(null=True)
    present_absent=models.CharField(max_length=20,null=True)
    class Meta:
        db_table='Attendence'
