'''
initial models.py for wcts_app
originally created by Thomas Sperduto
on Feb 23rd 2018
'''

from django.db import models
from django.core.validators import RegexValidator

'''
regex written by Andrew Flyte. Gives user the option of entering
numbers in any of the following formats:
1-908-123-4567
908-123-4567
19081234567
9081234567
'''
phone_regex = RegexValidator(
	regex=r'^\d{0,1}[\-]?\d{3}[\-]?\d{3}[\-]?\d{4}$',
	message="Phone number should be between 10 and 11 digits")

#career major options compiled by Thomas Sperduto
MAJORS = (
	("AT","Automotive Technology"),
	("BT","Building Technology"),
	("BM","Business Management"),
	("CD","Child Development"),
	("CVP","Cinematography Video Production"),
	("CP","Computer Programming"),
	("C","Cosmetology"),
	("ERC","Electrician Residential Commercial"),
	("ET","Electronics Technology"),
	("GAPM","Graphic Arts Printing Management"),
	("GE","General Engineering"),
	("HS","Health Science"),
	("HMCA","Hospitality Management Culinary Arts"),
	("LPSS","Law Public Safety Security"),
	)

#middle school options compiled by Ally McDonald and Thomas Sperduto on 3/2/18
SCHOOLS = (
	("ATS","Allamuchy Township School"),
	("AS","Alpha School"),
	("OSES","Oxford Street Elementary School"),
	("NWRHS","North Warren Regional High School"),
	("WHRMS","Warren Hills Regional Middle School"),
	("SS","Stewarstville School"),
	("HMS","Hackettstown Middle School"),
	("HTES","Harmony Township Elementary School"),
	("HTS","Hope Township School"),
	("GMRMS","Great Meadows Regional Middle School"),
	("LTMS","Lopatcong Township Middle School"),
	("PMS","Phillipsburg Middle School"),
	("PALS","Phillipsburg Alternative Learning School"),
	("WTCS","White Township Consolidated School"),
	("RVCS","Ridge and Valley Charter School"),
	("WCSSSD","Warren County Special Services School District"),
	("O","Other")
	)

#warren county townships compiled by Ally McDonald and Thomas Sperduto on 3/15/18
TOWNSHIPS = (
	 ("AT","Allamuchy Township"),
	 ("AB","Alpha Borough"),
	 ("TOB","Town of Belvidere"),
	 ("BT","Blairstown Township"),
	 ("FT_1","Franklin Township"),
	 ("FT_2","Frelinghuysen Township"),
	 ("GT","Greenwich Township"),
	 ("H","Hackettstown"),
	 ("HT_1","Hardwick Township"),
	 ("HT_2","Harmony Township"),
	 ("HT_3","Hope Township"),
	 ("IT","Independence Township"),
	 ("KT","Knowlton Township"),
	 ("LT_1","Liberty Township"),
	 ("LT_2","Lopatcong Township"),
	 ("MT","Mansfield Township"),
	 ("OT","Oxford Township"),
	 ("TOP","Town of Phillipsburg"),
	 ("PT","Pohatcong Township"),
	 ("WB","Washington Borough"),
	 ("WT_1","Washington Township"),
	 ("WT_2","White Township"),
	 ("O","Other"),
 )
 
#warren county cities compiled by Ally McDonald
CITIES = (
	("AL","Allamuchy"),
	("AT","Allamuchy Township"),
	("ALP","Alpha"),
	("BE","Belvidere"),
	("BL","Blairstown"),
	("BR","Broadway"),
	("BU","Buttzville"),
	("CH","Changewater"),
	("CO","Columbia"),
	("DE","Delaware"),
	("DEP","Delaware Park"),
	("GM","Great Meadows"),
	("HAC","Hackettstown"),
	("HAR","Hardwick"),
	("HT","Harmony Township"),
	("HO","Hope"),
	("JO","Johnsonburg"),
	("LO","Lopatcong"),
	("OX","Oxford"),
	("PH","Phillipsburg"),
	("PM","Port Murray"),
	("ST","Stewartsville"),
	("VI","Vienna"),
	("WA","Washington"),
	("O","Others")
	)

#compiled by Ally McDonald
ZIPS = (
	("07820","07820 Allamuchy"),
	("07840","07840 Allamuchy Township"),
	("08865","08865 Alpha"),
	("07823","07823 Belvidere"),
	("07825","07825 Blairstown"),
	("08808","08808 Broadway"),
	("07829","07829 Buttzville"),
	("07831","07831 Changewater"),
	("07832","07832 Columbia"),
	("07833","07833 Delaware"),
	("08865","08865 Delaware Park"),
	("07838","07838 Great Meadows"),
	("07840","07840 Hackettstown"),
	("07825","07825 Hardwick"),
	("08865","08865 Harmony Township"),
	("07844","07844 Hope"),
	("07846","07846 Johnsonburg"),
	("08865","08865 Lopatcong"),
	("07863","07863 Oxford"),
	("08865","08865 Phillipsburg"),
	("07865","07865 Port Murray"),
	("08886","08886 Stewartsville"),
	("07880","07880 Vienna"),
	("07882","07882 Washington"),
	("O","Others")
	)

#compiled by Omar Mohammed
STATES = (
    ('AK', 'Alaska'),
    ('AL', 'Alabama'),
    ('AR', 'Arkansas'),
    ('AS', 'American Samo'),
    ('AZ', 'Arizona'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DC', 'District of Columbia'),
    ('DE', 'Delaware'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('GU', 'Guam'),
    ('HI', 'Hawaii'),
    ('IA', 'Iowa'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('MA', 'Massachusetts'),
    ('MD', 'Maryland'),
    ('ME', 'Maine'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MO', 'Missouri'),
    ('MP', 'Northern Mariana Islands'),
    ('MS', 'Mississippi'),
    ('MT', 'Montana'),
    ('NA', 'National'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('NE', 'Nebraska'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NV', 'Nevada'),
    ('NY', 'New York'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('PR', 'Puerto Rico'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VA', 'Virginia'),
    ('VI', 'Virgin Islands'),
    ('VT', 'Vermont'),
    ('WA', 'Washington'),
    ('WI', 'Wisconsin'),
    ('WV', 'West Virginia'),
    ('WY', 'Wyoming')
)

class Applicant(models.Model):
    first_name = models.CharField(max_length = 100)
    middle_letter = models.CharField(max_length = 1, blank = True)#OM removed null=True to fix ValueError
    last_name = models.CharField(max_length = 100)
    #function "birth_date" needs rework.
    birth_date = models.DateField()#forced value.
    mailing_address = models.CharField(max_length = 100)
    apartment_number = models.CharField(max_length = 100, blank = True)
    city = models.CharField(max_length = 100, choices = CITIES)
    state = models.CharField(max_length = 30, default='NJ', choices = STATES)#OM added default 3/5
    zip_code = models.CharField(max_length = 10, choices = ZIPS)
    student_home_phone = models.CharField(validators=[phone_regex,], max_length = 100)
    township_municipality = models.CharField(max_length = 100, choices = TOWNSHIPS)
    parent_name_1 = models.CharField(max_length = 100)
    parent_cell_1 = models.CharField(validators=[phone_regex,],max_length = 100)
    parent_work_1 = models.CharField(validators=[phone_regex,],max_length = 100, blank = True)#OM removed null=True to fix ValueError
    parent_1_email = models.EmailField(max_length = 100)
    parent_name_2 = models.CharField(max_length = 100, blank = True)#JG
    parent_cell_2 = models.CharField(validators=[phone_regex,], max_length = 100, blank = True)
    parent_work_2 = models.CharField(validators=[phone_regex,], max_length = 100, blank = True)#OM removed null=True to fix ValueError
    parent_2_email = models.EmailField(max_length = 100, blank = True)
    parent_2_address = models.CharField(max_length = 100, blank = True)#OM removed null=True to fix ValueError
    parent_2_apartment_number = models.CharField(max_length = 100, blank = True)
    parent_2_city = models.CharField(max_length = 100, blank = True, choices = CITIES)
    parent_2_state = models.CharField(max_length = 100, blank = True, choices = STATES)
    parent_2_zip = models.CharField(max_length = 100, blank = True, choices = ZIPS)
    school_presently_attending = models.CharField(max_length = 100, choices = SCHOOLS)
    guidance_counselor = models.CharField(max_length = 100)
    counselor_phone = models.CharField(validators=[phone_regex,] ,max_length = 100)
    choice_1 = models.CharField(max_length = 100, choices = MAJORS)
    choice_2 = models.CharField(max_length = 100, choices = MAJORS)
    choice_3 = models.CharField(max_length = 100, choices = MAJORS)

    def __str__(self):
		#Joey Greenleaf and Ian Dorman added logic to correctly format name without a middle initial 3/2/18
        if self.middle_letter == "":
            return self.first_name + " " + self.last_name

        elif self.middle_letter != "":
            return self.first_name + " " + self.middle_letter + ". " + self.last_name

