# Generated by Django 2.0.2 on 2018-03-14 15:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_letter', models.CharField(blank=True, max_length=1)),
                ('last_name', models.CharField(max_length=100)),
                ('birth_month', models.IntegerField(choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')])),
                ('birth_date', models.IntegerField()),
                ('birth_year', models.IntegerField(choices=[(2000, '2000'), (2001, '2001'), (2002, '2002'), (2003, '2003'), (2004, '2004'), (2005, '2005')], default='2004')),
                ('mailing_address', models.CharField(max_length=100)),
                ('apartment_number', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(choices=[('AL', 'Allamuchy'), ('AT', 'Allamuchy Township'), ('ALP', 'Alpha'), ('BE', 'Belvidere'), ('BL', 'Blairstown'), ('BR', 'Broadway'), ('BU', 'Buttzville'), ('CH', 'Changewater'), ('CO', 'Columbia'), ('DE', 'Delaware'), ('DEP', 'Delaware Park'), ('GM', 'Great Meadows'), ('HAC', 'Hackettstown'), ('HAR', 'Hardwick'), ('HT', 'Harmony Township'), ('HO', 'Hope'), ('JO', 'Johnsonburg'), ('LO', 'Lopatcong'), ('OX', 'Oxford'), ('PH', 'Phillipsburg'), ('PM', 'Port Murray'), ('ST', 'Stewartsville'), ('VI', 'Vienna'), ('WA', 'Washington'), ('O', 'Others')], max_length=100)),
                ('state', models.CharField(choices=[('AK', 'Alaska'), ('AL', 'Alabama'), ('AR', 'Arkansas'), ('AS', 'American Samo'), ('AZ', 'Arizona'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DC', 'District of Columbia'), ('DE', 'Delaware'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), ('IA', 'Iowa'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('MA', 'Massachusetts'), ('MD', 'Maryland'), ('ME', 'Maine'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MO', 'Missouri'), ('MP', 'Northern Mariana Islands'), ('MS', 'Mississippi'), ('MT', 'Montana'), ('NA', 'National'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('NE', 'Nebraska'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NV', 'Nevada'), ('NY', 'New York'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VA', 'Virginia'), ('VI', 'Virgin Islands'), ('VT', 'Vermont'), ('WA', 'Washington'), ('WI', 'Wisconsin'), ('WV', 'West Virginia'), ('WY', 'Wyoming')], default='NJ', max_length=30)),
                ('zip_code', models.CharField(choices=[('07820', '07820 Allamuchy'), ('07840', '07840 Allamuchy Township'), ('08865', '08865 Alpha'), ('07823', '07823 Belvidere'), ('07825', '07825 Blairstown'), ('08808', '08808 Broadway'), ('07829', '07829 Buttzville'), ('07831', '07831 Changewater'), ('07832', '07832 Columbia'), ('07833', '07833 Delaware'), ('08865', '08865 Delaware Park'), ('07838', '07838 Great Meadows'), ('07840', '07840 Hackettstown'), ('07825', '07825 Hardwick'), ('08865', '08865 Harmony Township'), ('07844', '07844 Hope'), ('07846', '07846 Johnsonburg'), ('08865', '08865 Lopatcong'), ('07863', '07863 Oxford'), ('08865', '08865 Phillipsburg'), ('07865', '07865 Port Murray'), ('08886', '08886 Stewartsville'), ('07880', '07880 Vienna'), ('07882', '07882 Washington'), ('O', 'Others')], max_length=10)),
                ('student_home_phone', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(message='Phone number should be between 10 and 11 digits', regex='^\\d{0,1}[\\-]?\\d{3}[\\-]?\\d{3}[\\-]?\\d{4}$')])),
                ('township_municipality', models.CharField(choices=[('AT', 'Allamuchy Township'), ('AB', 'Alpha Borough'), ('TOB', 'Town of Belvidere'), ('BT', 'Blairstown Township'), ('FT_1', 'Franklin Township'), ('FT_2', 'Frelinghuysen Township'), ('GT', 'Greenwich Township'), ('H', 'Hackettstown'), ('HT_1', 'Hardwick Township'), ('HT_2', 'Harmony Township'), ('HT_3', 'Hope Township'), ('IT', 'Independence Township'), ('KT', 'Knowlton Township'), ('LT_1', 'Liberty Township'), ('LT_2', 'Lopatcong Township'), ('MT', 'Mansfield Township'), ('OT', 'Oxford Township'), ('TOP', 'Town of Phillipsburg'), ('PT', 'Pohatcong Township'), ('WB', 'Washington Borough'), ('WT_1', 'Washington Township'), ('WT_2', 'White Township'), ('O', 'Other')], max_length=100)),
                ('parent_name_1', models.CharField(max_length=100)),
                ('parent_cell_1', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(message='Phone number should be between 10 and 11 digits', regex='^\\d{0,1}[\\-]?\\d{3}[\\-]?\\d{3}[\\-]?\\d{4}$')])),
                ('parent_work_1', models.CharField(blank=True, max_length=100, validators=[django.core.validators.RegexValidator(message='Phone number should be between 10 and 11 digits', regex='^\\d{0,1}[\\-]?\\d{3}[\\-]?\\d{3}[\\-]?\\d{4}$')])),
                ('parent_1_email', models.EmailField(max_length=100)),
                ('parent_name_2', models.CharField(blank=True, max_length=100)),
                ('parent_cell_2', models.CharField(blank=True, max_length=100, validators=[django.core.validators.RegexValidator(message='Phone number should be between 10 and 11 digits', regex='^\\d{0,1}[\\-]?\\d{3}[\\-]?\\d{3}[\\-]?\\d{4}$')])),
                ('parent_work_2', models.CharField(blank=True, max_length=100, validators=[django.core.validators.RegexValidator(message='Phone number should be between 10 and 11 digits', regex='^\\d{0,1}[\\-]?\\d{3}[\\-]?\\d{3}[\\-]?\\d{4}$')])),
                ('parent_2_email', models.EmailField(blank=True, max_length=100)),
                ('parent_2_address', models.CharField(blank=True, max_length=100)),
                ('parent_2_apartment_number', models.CharField(blank=True, max_length=100)),
                ('parent_2_city', models.CharField(blank=True, choices=[('AL', 'Allamuchy'), ('AT', 'Allamuchy Township'), ('ALP', 'Alpha'), ('BE', 'Belvidere'), ('BL', 'Blairstown'), ('BR', 'Broadway'), ('BU', 'Buttzville'), ('CH', 'Changewater'), ('CO', 'Columbia'), ('DE', 'Delaware'), ('DEP', 'Delaware Park'), ('GM', 'Great Meadows'), ('HAC', 'Hackettstown'), ('HAR', 'Hardwick'), ('HT', 'Harmony Township'), ('HO', 'Hope'), ('JO', 'Johnsonburg'), ('LO', 'Lopatcong'), ('OX', 'Oxford'), ('PH', 'Phillipsburg'), ('PM', 'Port Murray'), ('ST', 'Stewartsville'), ('VI', 'Vienna'), ('WA', 'Washington'), ('O', 'Others')], max_length=100)),
                ('parent_2_state', models.CharField(blank=True, choices=[('AK', 'Alaska'), ('AL', 'Alabama'), ('AR', 'Arkansas'), ('AS', 'American Samo'), ('AZ', 'Arizona'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DC', 'District of Columbia'), ('DE', 'Delaware'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), ('IA', 'Iowa'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('MA', 'Massachusetts'), ('MD', 'Maryland'), ('ME', 'Maine'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MO', 'Missouri'), ('MP', 'Northern Mariana Islands'), ('MS', 'Mississippi'), ('MT', 'Montana'), ('NA', 'National'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('NE', 'Nebraska'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NV', 'Nevada'), ('NY', 'New York'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VA', 'Virginia'), ('VI', 'Virgin Islands'), ('VT', 'Vermont'), ('WA', 'Washington'), ('WI', 'Wisconsin'), ('WV', 'West Virginia'), ('WY', 'Wyoming')], max_length=100)),
                ('parent_2_zip', models.CharField(blank=True, choices=[('07820', '07820 Allamuchy'), ('07840', '07840 Allamuchy Township'), ('08865', '08865 Alpha'), ('07823', '07823 Belvidere'), ('07825', '07825 Blairstown'), ('08808', '08808 Broadway'), ('07829', '07829 Buttzville'), ('07831', '07831 Changewater'), ('07832', '07832 Columbia'), ('07833', '07833 Delaware'), ('08865', '08865 Delaware Park'), ('07838', '07838 Great Meadows'), ('07840', '07840 Hackettstown'), ('07825', '07825 Hardwick'), ('08865', '08865 Harmony Township'), ('07844', '07844 Hope'), ('07846', '07846 Johnsonburg'), ('08865', '08865 Lopatcong'), ('07863', '07863 Oxford'), ('08865', '08865 Phillipsburg'), ('07865', '07865 Port Murray'), ('08886', '08886 Stewartsville'), ('07880', '07880 Vienna'), ('07882', '07882 Washington'), ('O', 'Others')], max_length=100)),
                ('school_presently_attending', models.CharField(choices=[('ATS', 'Allamuchy Township School'), ('AS', 'Alpha School'), ('OSES', 'Oxford Street Elementary School'), ('NWRHS', 'North Warren Regional High School'), ('WHRMS', 'Warren Hills Regional Middle School'), ('SS', 'Stewarstville School'), ('HMS', 'Hackettstown Middle School'), ('HTES', 'Harmony Township Elementary School'), ('HTS', 'Hope Township School'), ('GMRMS', 'Great Meadows Regional Middle School'), ('LTMS', 'Lopatcong Township Middle School'), ('PMS', 'Phillipsburg Middle School'), ('PALS', 'Phillipsburg Alternative Learning School'), ('WTCS', 'White Township Consolidated School'), ('RVCS', 'Ridge and Valley Charter School'), ('WCSSSD', 'Warren County Special Services School District'), ('O', 'Other')], max_length=100)),
                ('guidance_counselor', models.CharField(max_length=100)),
                ('counselor_phone', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(message='Phone number should be between 10 and 11 digits', regex='^\\d{0,1}[\\-]?\\d{3}[\\-]?\\d{3}[\\-]?\\d{4}$')])),
                ('choice_1', models.CharField(choices=[('AT', 'Automotive Technology'), ('BT', 'Building Technology'), ('BM', 'Business Management'), ('CD', 'Child Development'), ('CVP', 'Cinematography Video Production'), ('CP', 'Computer Programming'), ('C', 'Cosmetology'), ('ERC', 'Electrician Residential Commercial'), ('ET', 'Electronics Technology'), ('GAPM', 'Graphic Arts Printing Management'), ('GE', 'General Engineering'), ('HS', 'Health Science'), ('HMCA', 'Hospitality Management Culinary Arts'), ('LPSS', 'Law Public Safety Security')], max_length=100)),
                ('choice_2', models.CharField(choices=[('AT', 'Automotive Technology'), ('BT', 'Building Technology'), ('BM', 'Business Management'), ('CD', 'Child Development'), ('CVP', 'Cinematography Video Production'), ('CP', 'Computer Programming'), ('C', 'Cosmetology'), ('ERC', 'Electrician Residential Commercial'), ('ET', 'Electronics Technology'), ('GAPM', 'Graphic Arts Printing Management'), ('GE', 'General Engineering'), ('HS', 'Health Science'), ('HMCA', 'Hospitality Management Culinary Arts'), ('LPSS', 'Law Public Safety Security')], max_length=100)),
                ('choice_3', models.CharField(choices=[('AT', 'Automotive Technology'), ('BT', 'Building Technology'), ('BM', 'Business Management'), ('CD', 'Child Development'), ('CVP', 'Cinematography Video Production'), ('CP', 'Computer Programming'), ('C', 'Cosmetology'), ('ERC', 'Electrician Residential Commercial'), ('ET', 'Electronics Technology'), ('GAPM', 'Graphic Arts Printing Management'), ('GE', 'General Engineering'), ('HS', 'Health Science'), ('HMCA', 'Hospitality Management Culinary Arts'), ('LPSS', 'Law Public Safety Security')], max_length=100)),
            ],
        ),
    ]
