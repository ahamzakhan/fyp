from django.db import models

class student_info(models.Model):

   roll_no = models.CharField(max_length = 7, primary_key=True)
   mail = models.CharField(max_length = 21)
   password = models.CharField(max_length = 30)
   city = models.CharField(max_length = 30)



   class Meta:
      db_table = "student_info"