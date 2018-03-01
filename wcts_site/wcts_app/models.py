from django.db import models

# Create your models here.
#MAJORS = ("Automotive Technology", "Building Technology", "Business Management", "Child Development", "Cinematography & Video Production", "Computer Programming", "Cosmetology", "Electrician (Residential & Commercial)", "Electronics Technology", "Graphic Arts & Printing Management", "General Engineering", "Health Science", "Hospitality Management & Culinary Arts", "Law Public Safety & Security")

class Applicant(models.Model):
    first_name = models.CharField(max_length = 100)
    middle_letter = models.CharField(max_length = 1, blank = True, null = True)
    last_name = models.CharField(max_length = 100)
    #function "birth_date" needs rework.
    birth_date = models.DateField()#forced value.
    mailing_address = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length = 10)
    zip_code = models.CharField(max_length = 10)
    student_home_phone = models.CharField(max_length = 100)
    township_municipality = models.CharField(max_length = 100)
    parent_name_1 = models.CharField(max_length = 100)
    parent_cell_1 = models.CharField(max_length = 100)
    parent_work_1 = models.CharField(max_length = 100, blank = True, null = True)
    parent_1_email = models.EmailField(max_length = 100)
    parent_name_2 = models.CharField(max_length = 100)
    parent_cell_2 = models.CharField(max_length = 100)
    parent_work_2 = models.CharField(max_length = 100, blank = True, null = True)
    parent_2_email = models.EmailField(max_length = 100)
    parent_2_adress = models.CharField(max_length = 100)
    school_presently_attending = models.CharField(max_length = 100)
    guidance_counselor = models.CharField(max_length = 100)
    counselor_phone = models.CharField(max_length = 100)
    choice_1 = models.CharField(max_length = 100)#, choices = MAJORS)
    choice_2 = models.CharField(max_length = 100)#, choices = MAJORS)
    choice_3 = models.CharField(max_length = 100)#, choices = MAJORS)

    def __str__(self):
        return self.first_name + " " + self.middle_letter + ". " + self.last_name