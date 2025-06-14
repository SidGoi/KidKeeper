from django.db import models


# Kids Database Model -
class Kid(models.Model):
    kid_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    surename = models.CharField(max_length=100)
    standard = models.CharField(max_length=20)
    birthdate = models.DateField()
    mobile_number = models.CharField(max_length=15)

    def __str__(self):
        return self.kid_name


# Attedence Data -
class Attendance(models.Model):
    kid = models.ForeignKey(Kid, on_delete=models.CASCADE)
    date = models.DateField()
    is_present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.kid.kid_name} - {self.date} - {'Present' if self.is_present else 'Absent'}"
