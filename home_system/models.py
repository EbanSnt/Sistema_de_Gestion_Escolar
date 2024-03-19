from django.db import models

# Create your models here.
class SchoolInformation(models.Model):
    school_logo = models.ImageField(upload_to="school_logo_image/",default='images/school_logo_default.png')
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    district = models.CharField(max_length=60)
    locality = models.CharField(max_length=50)
    telephone_number = models.CharField(max_length=40)
    telephone_number2 = models.CharField(max_length=40)
    telephone_number3 = models.CharField(max_length=40)
    telephone_number4 = models.CharField(max_length=40)
    email = models.EmailField()
    alternative_email = models.EmailField()
    school_type = models.CharField(max_length=20)
    facebook = models.URLField()
    instagram = models.URLField()
    twitter_x = models.URLField()
    linkedin = models.URLField()
    youtube = models.URLField()
    telegram = models.URLField()
    whatsapp = models.URLField()
    web_site = models.URLField()


class SchoolUsers(models.Model):
    dni = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=254) 
    email = models.EmailField()
    active = models.BooleanField(default=False)
    position = models.CharField(max_length=30)

class SchoolStaff(models.Model):
    profile_photo = models.ImageField(upload_to="school_staff_members/",default='images/user.png')
    name = models.CharField(max_length=80)
    lastname = models.CharField(max_length=80)
    birthdate = models.DateField()
    dni = models.BigIntegerField(primary_key=True)
    email = models.EmailField()
    telephone_number = models.CharField(max_length=40)
    telephone_number2 = models.CharField(max_length=40)
    address = models.CharField(max_length=100)
    district = models.CharField(max_length=60)
    locality = models.CharField(max_length=50)
    position = models.CharField(max_length=30)
    active = models.BooleanField(default=False)
    cv =  models.FileField(upload_to='school_staff_cv/')
    dni =  models.FileField(upload_to='school_staff_dni/')
    degree =  models.FileField(upload_to='school_staff_degree/')
    degree2 =  models.FileField(upload_to='school_staff_degree2/')
    extra_file =  models.FileField(upload_to='school_staff_extra_file/')
    extra_file_details = models.CharField(max_length=100)
    extra_file2 =  models.FileField(upload_to='school_staff_extra_file2/')
    extra_file2_details = models.CharField(max_length=100)
    extra_file3 =  models.FileField(upload_to='school_staff_extra_file3/')
    extra_file3_details = models.CharField(max_length=100)
    extra_file4 =  models.FileField(upload_to='school_staff_extra_file4/')
    extra_file4_details = models.CharField(max_length=100)


class Students(models.Model):
    profile_photo = models.ImageField(upload_to="students_profile_photos",default='images/user.png')
    name = models.CharField(max_length=80)
    lastname = models.CharField(max_length=80)
    birthdate = models.DateField()
    dni = models.BigIntegerField(primary_key=True)
    active = models.BooleanField(default=True)


class SchoolYear(models.Model):
    year = models.IntegerField()
    division = models.CharField(max_length=10)
    shift = models.CharField(max_length=20)
    preceptor = models.ForeignKey(SchoolStaff,on_delete=models.SET_NULL,null=True)


class Subjects(models.Model):
    name = models.CharField(max_length=30)
    school_year = models.ForeignKey(SchoolYear,on_delete=models.SET_NULL,null=True)
    teacher = models.ForeignKey(SchoolStaff,on_delete=models.SET_NULL,null=True)


class Grades(models.Model):
    student = models.ForeignKey(Students,on_delete=models.SET_NULL,null=True)
    subject = models.ForeignKey(Subjects,on_delete=models.SET_NULL,null=True)
    grade = models.IntegerField()
    grade_type = models.CharField(max_length=30)
    period = models.CharField(max_length=30)
    date = models.DateField()


class Attendances(models.Model):
    date = models.DateField()
    student = models.ForeignKey(Students,on_delete=models.SET_NULL,null=True)
    attendance_type = models.CharField(max_length=30)
    non_attendance_details = models.CharField(max_length=30)


class StudentsPayments(models.Model):
    date = models.DateField()
    payment_concept = models.CharField(max_length=30)
    amount = models.IntegerField()
    student = models.ForeignKey(Students,on_delete=models.SET_NULL,null=True)


class StudentFile(models.Model):
    creation_date = models.DateField()
    school_year = models.ForeignKey(SchoolYear,on_delete=models.SET_NULL,null=True)
    student = models.ForeignKey(Students,on_delete=models.SET_NULL,null=True)
    email = models.EmailField()
    telephone_number = models.CharField(max_length=40)
    telephone_number2 = models.CharField(max_length=40)
    address = models.CharField(max_length=100)
    district = models.CharField(max_length=60)
    locality = models.CharField(max_length=50)
    position = models.CharField(max_length=30)
    grades = models.TextField()
    attendances = models.TextField()
    disciplinary_measures = models.TextField()
    school_insurance = models.BooleanField(default=False)
    student_condition = models.CharField(max_length=30)
    payments_history = models.TextField()
    students_file1 =  models.FileField(upload_to='students_files/')
    students_file1_details = models.CharField(max_length=100)
    students_file2 =  models.FileField(upload_to='students_files/')
    students_file2_details = models.CharField(max_length=100)
    students_file3 =  models.FileField(upload_to='students_files/')
    students_file3_details = models.CharField(max_length=100)
    students_file4 =  models.FileField(upload_to='students_files/')
    students_file4_details = models.CharField(max_length=100)
    students_file5 =  models.FileField(upload_to='students_files/')
    students_file5_details = models.CharField(max_length=100)
    students_file6 =  models.FileField(upload_to='students_files/')
    students_file6_details = models.CharField(max_length=100)
    students_file7 =  models.FileField(upload_to='students_files/')
    students_file7_details = models.CharField(max_length=100)
    students_file8 =  models.FileField(upload_to='students_files/')
    students_file8_details = models.CharField(max_length=100)
    students_file9 =  models.FileField(upload_to='students_files/')
    students_file9_details = models.CharField(max_length=100)
    students_file10 =  models.FileField(upload_to='students_files/')
    students_file10_details = models.CharField(max_length=100)
    students_file11 =  models.FileField(upload_to='students_files/')
    students_file11_details = models.CharField(max_length=100)
    students_file12 =  models.FileField(upload_to='students_files/')
    students_file12_details = models.CharField(max_length=100)
    students_file13 =  models.FileField(upload_to='students_files/')
    students_file13_details = models.CharField(max_length=100)
    students_file14 =  models.FileField(upload_to='students_files/')
    students_file14_details = models.CharField(max_length=100)
    students_file15 =  models.FileField(upload_to='students_files/')
    students_file15_details = models.CharField(max_length=100)
    

class ActionsHistory(models.Model):
    date = models.DateTimeField()
    user = models.ForeignKey(SchoolUsers,on_delete=models.SET_NULL,null=True)
    details = models.TextField()
    action_type = models.CharField(max_length=40)