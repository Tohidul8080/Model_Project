from django.db import models

# Create your models here.

class student(models.Model):
    #id=models.AutoField(primary_key=True)
    First_name=models.CharField(max_length=30)
    Last_name=models.CharField(max_length=30)
    student_id=models.IntegerField()
    student_cgpa=models.FloatField()

    def __str__(self):
        return self.First_name + " "+ self.Last_name


class shart(models.Model):
   # id=models.AutoField(Primary_key=True)
    shart_name=models.CharField(max_length=20)
   # shart_name=models.ForeignKey(student, on_delete=models.CASCADE)
   # shart_name=models.ForeignKey(student, on_delete=models.CASCADE)
    shart_color=models.CharField(max_length=20)
    shart_price=models.IntegerField()
    rating=(
        (1,"M_shart"),
        (2,"L_shart"),
        (3,"XL_shart"),
        (4, "XXL_shart"),
        (5,"XXXL_shart"),
    )

    all_sart=models.IntegerField(choices=rating)

    def __str__(self):
        return self.shart_name
