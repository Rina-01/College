from django.db import models



class Students(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    second_name = models.CharField(max_length=128, blank=True)
    date_of_birth = models.DateField()

class Groups(models.Model):
    name = models.CharField(max_length=16)

class Disciplines(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1000)

class Titors(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    second_name = models.CharField(max_length=128, blank=True)
    date_of_birth = models.DateField()

class Group_semesters(models.Model):
    semester_num = models.PositiveSmallIntegerField()

# class Group_members(models.Model):

class Curriculum(models.Model):
    duration = models.PositiveSmallIntegerField()

class Final_grades(models.Model):
    # semester_num = models.PositiveSmallIntegerField()
    is_final = models.BooleanField()
    scale_5 = models.PositiveSmallIntegerField()
    scale_100 = models.PositiveSmallIntegerField()
    scale_letter = models.CharField(max_length=1)
    scale_word = models.CharField(max_length=128)


class Curriculum_lesson(models.Model):
    lesson_type = models.PositiveSmallIntegerField()


