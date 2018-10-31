from django.db import models
import datetime
# Create your models here.
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import re

global LEARNERSHIP_ID_CHOICES

LEARNERSHIP_ID_CHOICES = (
        
        ('436','436 - Certificate in General Nursing (Enrolled) Level 4'),
        ('437','437 - Diploma in General Nursing (Bridging) Level 5'),
        ('439','439 - FETC Phlebotomy Techniques NQF Level 4'),
        ('440','440 - Certificate in General Nursing (Auxiliary) Level 4'),
        ('442','442 - Post Basic Diploma in Medical/Surgical Nursing (Elective: Critical Care/Operating Theater Nursing) Level 6'),
        ('444','444 - FET Certificate in Social Auxiliary Work Level 4'),
        ('446','446 - Further Education and Training Certificate: Child and Youth Care Work Level 4'),
        ('448','448 - Health Promotion Officer NQF Level 3'),
        ('1117','1117 - National Certificate: Pharmacist Assistance Level 3'),
        ('1118','1118 - Ferther Education and Training Certificate: Pharmacist Assistance Level 4'),
        ('1357','1357 - Further Education and Training Certificate:  Early Childhood Development Level 4'),
        ('268','268 - L5 - Learnership for ECD Trainers Level 5'),
        ('6591', '6591 - University Diploma:Veterinary Nursing Level 6'),
        ('10809', '10809 - Post Basic Diploma: Operating  Theater Nursing Science Level 7'),
        ('21214', '21214 - Post Basic Diploma: Medical and Surgical Nursing Science Level 7'),
        ('16496', '16496 - Advance University Diploma: Midwifery and Neonatal Nursing Level 7'),
        ('17196', '17196 - Bridging Diploma: Nursing General Level 5'),
        ('97756', '97756 - Higher Certificate: Auxilliary Nursing Level 5'),
        ('72049', '72049 - National Certificate: Pharmacy Assistant Level 3'),
        ('72050', '72050 - Further Education and training Certificate: Pharmacy Assistant Level 4'),
        ('59345', '59345 - Further Education and training Certificate: Phlebotomy Technique Level 4'),
        ('60209', '60209 - Further Education and training Certificate: Child & Youthcare Level 4'),
        ('94597', '94597 - Occupational Certificate: Health Promotion Officer Level 3'),
        ('99510', '99510 - Occupational Certificate: Child and Youth care Worker Level 5'),
        ('98890', '98890 - Occupational Certificate: Social Auxiliary Worker Level 5'),
        ('1502', '1502 - National Certificate: Occupational Health, Safety and Environment: Mining and Minerals, Level 2'),
        ('1111','1111 - General Education and Training Certificate: Business Practice, Level 1'),
        ('1216','1216 - National Certificate: Public Administration: Leadership, Level 5'),
        ('1217','1217 - National Certificate: Public Administration: Procurement, Level 5'),
        ('797','797 - Office Administration Assistant, Level 2'),
        ('527','527 - National Certificate in People Centre Management, Level 2'),
        ('871','871 - Contact Centre Support, Level 2'),
        ('1063','1063 - National Certificate: Wholesale Retail: Visual Merchandising, Level 3'),
        ('61595', '61595 - Further Education and Training Certificate: Business Administration Services Level 4'),
        ('57712', 'Further Education and Training Certificate: Generic Management - level 4'),
        ('61591', 'National Certificate: Information Technology: End User Computing – level 3'),
        ('63969', 'National Certificate: Pharmaceutical Sales Representation – level 5'),
        ('61592', 'National Diploma: Human Resources Management and Practices - level 5'),
        ('66876', 'National Certificate: Management Assistant – N6'),
        ('66874', 'National Certificate: Financial Management Level 4'),
        ('6695543', 'National Certificate: Financial Management Level 5'),
        ('66998', 'National Certificate:  Financial Management Level 6'),
        ('66997', 'National Certificate: N6 Human Resource Management Level 6'),
        ('67000', 'National Certificate: N6 Public Management Level 6'),
        ('337059','Advance Certification: Monitoring & Evaluation - NQF 6 337059'),
        ('83546','Advance Project Management - NQF 6 83546'),
        ('90665','Advanced certificate in Management - NQF 6 90665'),
        ('49256','Advanced Councelling - nan 49256'),
        ('90559','Advanced Diploma in Accounting Sciences  - NQF 8 90559'),
        ('63669','Aerobic Instructor - NQF 4 63669'),
        ('90677','B Comm (Management Science) -  NQF 6 90677'),
        ('5563','B Comm in Accounting/HR - NQF 8 5563'),
        ('7765','B- Cur  (Operating Theatre) - NQF 7 765'),
        ('72052','B Eng Chemical - NQF 4 72052'),
        ('80128','B Medical and Surgery - NQF Level 7 80128'),
        ('12153','B Occupational Therapy  - NQF Level 7 12153'),
        ('57827','B Public Admin Hons - NQF 7 57827'),
        ('9703','B Social Science (Nursing) - NQF Level 7 9703'),
        ('71789','B Tech in Nursing - NQF 7 71789'),
        ('72375','B Tech Information Technology - NQF Level 7 72375'),
        ('91786','B Tech: Medical Orthotics and Prosthetics - NQF 4 91786'),
        ('65320','B Tech: Radiography - NQF 6 65320'),
        ('72843','B. Optometry - NQF Level 7 72843'),
        ('57827','BA Administration Public Sector Management and Administration - NQF Level 7 57827'),
        ('14169','BA Communication Science - NQF 6 14169'),
        ('79706','BA Community Development - NQF 8 79706'),
        ('91757','BA Development Studies - NQF 8 91757'),
        ('91932','BA Forensic Science and Technology - NQF 7 91932'),
        ('15932','BA Health Sciences and Social Services - NQF 5 15932'),
        ('15802','BA Honours Media Studies - N3 15802'),
        ('15859','BA Honours Psychology - NQF 8 15859'),
        ('21433','BA honours: Gender Studies - NQF 8 21433'),
        ('66509','BA Nursing Admin and Education  - NQF 7 66509'),
        ('61389','BA Psychology - NQF Level 7 61389'),
        ('23994','BA Social Work - NQF Level 7 23994'),
        ('21528','Baccalaureus Scientiae in Dietetics - NQF Level 7 21528'),
        ('49130','Bachelor  of Theology - NQF 7 49130'),
        ('21532','Bachelor of  Biokinetics - NQF Level 7 21532'),
        ('90622','Bachelor of Accounting Science in Taxation - NQF 7 90622'),
        ('23375','Bachelor of Arts - NQF 8 23375'),
        ('91757','Bachelor of Arts Honours Development Studies - NQF Level 7 91757'),
        ('71778','Bachelor of Commerce - NQF Level 7 71778'),
        ('98306','Bachelor of Commerce in Financial Management - NQF 7 98306'),
        ('62129','Bachelor of Commerce in HR - NQF 6 62129'),
        ('5563','Bachelor of Economics - NQF Level 7 5563'),
        ('20474','Bachelor of Education - NQF 7 20474'),
        ('63129','Bachelor of Emergency Medical Care (Ext) - NQF Level 7 63129'),
        ('72843','Bachelor of Optometry - NQF Level 7 72843'),
        ('65130','Bachelor of Pharmacy - NQF Level 7 65130'),
        ('22993','Bachelor of Laws - NQF 8 22993'),
        ('78108','Bachelor of Medicine and Bachelor of Surgery - NQF Level 7 78108'),
        ('66949', 'Bachelor of Radiography in Diagnostics - NQF Level 7  66949'),



    )

def validate_letters_special(value):
    if not re.match(r"(?=.*[ABCDEFGHIJKLMNOPQRTSUVWXYZ1234567890#&\(\)\/:\._`])",value):
        raise ValidationError(
                _("%(value)s should contain ABCDEFGHIJKLMNOPQRTSUVWXYZ1234567890#&()/\:._`"),
                params={'value': value},
            )

def validate_sixteen(value):
    sixteen_years = datetime.datetime.now() - datetime.timedelta(days=16*365)
    if value > sixteen_years.date():
        raise ValidationError(
                _("%(value)s - person is younger than 16!"),
                params={'value': value},
            )

def validate_eighteen_fifty(value):
    if datetime.date(1850, 1, 1) > value:
        raise ValidationError(
                _("%(value)s is less than 1850!"),
                params={'value': value},
            )

def nineteen_hundred(value):
    if datetime.date(1900, 1, 1) > value:
        raise ValidationError(
                _("%(value)s is less than 1900!"),
                params={'value': value},
            )

def validate_names(value):
    if not re.match(r"(?=.*[abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRTSUVWXYZ`'\-])",value):
        raise ValidationError(
                _("%(value)s should contain ABCDEFGHIJKLMNOPQRTSUVWXYZ`'\-"),
                params={'value': value},
            )


def validate_na_geen(value):
    illegal =['% UNKNOWN %', '% AS', 'ABOVE %','% SOOS', 'BO %', '% DELETE %', 'N / A', 'NA', 'U',
              'NONE', 'GEEN', '0', 'TEST', '% ONTBREEK %', 'NIL', '-', '–']
    if value in illegal:
        raise ValidationError(
            _('%(value)s cannot be UNKOWNW, AS ABOVE, SOOS, BO, DELETE, N / A, NA, U, NONE, GEEN, 0, TEST, ONTBREEK, NIL, - or ~'),
            params={'value': value},
        )

def validate_postcode(value):
    if not re.match(r"(?<!\d)\d{4,4}(?!\d)", value):
        raise ValidationError(
                _('%(value)s is not a valid postcode'),
                params={'value': value},
            )

def validate_phone_fax(value):
    try:
        int(value)
    except:
        raise ValidationError(
                _('%value)s is not a valid phone or fax number'),
                params={'value':value},
                )
    #if not re.match(r"(?<!\d)\d{20,20}(?!\d)", value):
    #    raise ValidationError(
    #            _('%(value)s is not a valid postcode'),
    #            params={'value': value},
    #        )


def validate_uppercase_letters_numbers_special(value):
    p = re.compile("[A-Z_0-9]")
    a = p.match(value)
    if a == None:
        raise ValidationError(
            _('%(value)s is not valid - only use the characters: ABCDEFGHIJKLMNOPQRTSUVWXYZ1234567890@#&+() /\:._- '),
            params={'value': value},
        )


def validateID(IDNum):
    def informinvalid():
        raise ValidationError(
            _('%(IDNum)s is not an ID'),
            params={'IDNum': IDNum},
        )

    xv = True
    if len(IDNum) != 13:
        informinvalid()
    if int(IDNum[10]) > 1:
        informinvalid()
    d = -1
    a = 0
    for i in range(0, 6):
        a += int(IDNum[2 * i])
    b = 0
    for i in range(0, 6):
        b = b * 10 + int(IDNum[2 * i + 1])
        b *= 2
    c = 0
    while b > 0:
        c += b % 10
        b = b / 10
        c += a
        d = 10 - (c % 10)
        if d == 10:
            d = 0
        xc = (str(d) == IDNum[12])
    if xv == False:
        informinvalid()


def validate_even(value):
    value = int(value)
    if value % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )

def validate_provider_start_end_date(value):
    if Provider.provider_start_date == Provider.provider_end_date or 1 == 1:
        raise ValidationError(
            # _('%(value)s is time travel'),
            _('%(Provider.provider_start_date)s is time travel'),
            params={'value': value},
        )

# QMR lookups

class Citizen_Resident_Status_Code(models.Model):
    lookup = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150)

    def __str__(self):
        return '%s' % (self.description)


class Alternate_Id_Type_Id(models.Model):
    lookup = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150)

    def __str__(self):
        return '%s' % (self.description)


class Communicating_Rating_Id(models.Model):
    lookup = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150)

    def __str__(self):
        return '%s' % (self.description)


class Country_Code(models.Model):
    lookup = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150)

    def __str__(self):
        return '%s' % (self.description)


class Designation_Id(models.Model):
    lookup = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150)

    def __str__(self):
        return '%s' % (self.description)


class Designation_Structure_Status_Id(models.Model):
    lookup = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150)

    def __str__(self):
        return '%s' % (self.description)


class Economic_Status_Id(models.Model):
    lookup = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150)

    def __str__(self):
        return '%s' % (self.description)


class Employer_Approval_Status_Id(models.Model):
    lookup = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150)

    def __str__(self):
        return '%s' % (self.description)


class Enrolment_Status_Id(models.Model):
    lookup = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150)

    def __str__(self):
        return '%s' % (self.description)


class Enrolment_Status_Reason_Id(models.Model):
    lookup = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150)

    def __str__(self):
        return '%s' % (self.description)


class Enrolment_Type_Id(models.Model):
    lookup = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150)

    def __str__(self):
        return '%s' % (self.description)


class Equity_Code(models.Model):
    lookup = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150)

    def __str__(self):
        return '%s' % (self.description)


class Funding_Id(models.Model):
    lookup = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150)

    def __str__(self):
        return '%s' % (self.description)


class Gender_Code(models.Model):
    lookup = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150)

    def __str__(self):
        return '%s' % (self.description)


class Hearing_Rating_Id(models.Model):
    lookup = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150)

    def __str__(self):
        return '%s' % (self.description)


class Home_Language_Code(models.Model):
    lookup = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150)

    def __str__(self):
        return '%s' % (self.description)


class Internship_Status_Id(models.Model):
    lookup = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150)

    def __str__(self):
        return '%s' % (self.description)


class Nationality_Code(models.Model):
    lookup = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150)

    def __str__(self):
        return '%s' % (self.description)


class Non_NQF_Interv_Status_Id(models.Model):
    lookup = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150)

    def __str__(self):
        return '%s' % (self.description)


class OFO_Code(models.Model):
    lookup = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150)

    def __str__(self):
        return '%s %s' % (self.lookup, self.description)


class Part_Of_Id(models.Model):
    lookup = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150)

    def __str__(self):
        return '%s' % (self.description)


class POPI_Act_Status_ID(models.Model):
    lookup = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150)

    def __str__(self):
        return '%s' % (self.description)


class Provider_class_Id(models.Model):
    lookup = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150)

    def __str__(self):
        return '%s' % (self.description)


class Provider_Status_Id(models.Model):
    lookup = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150)

    def __str__(self):
        return '%s' % (self.description)


class Provider_Type_Id(models.Model):
    lookup = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150)

    def __str__(self):
        return '%s %s' % (self.lookup, self.description)


class Province_Code(models.Model):
    lookup = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150)

    def __str__(self):
        return '%s' % (self.description)


class Remembering_Rating_Id(models.Model):
    lookup = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150)

    def __str__(self):
        return '%s' % (self.description)


class Seeing_Rating_Id(models.Model):
    lookup = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150)

    def __str__(self):
        return '%s' % (self.description)


class Self_Care_Rating_Id(models.Model):
    lookup = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150)

    def __str__(self):
        return '%s' % (self.description)


class SETA_Id(models.Model):
    lookup = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150)

    def __str__(self):
        return '%s' % (self.description)


class SIC_Code(models.Model):
    lookup = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150)

    def __str__(self):
        return '%s' % (self.description)


class STATSSA_Area_Code(models.Model):
    lookup = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150)

    def __str__(self):
        return '%s' % (self.description)


class Subfield_Id(models.Model):
    lookup = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150)

    def __str__(self):
        return '%s' % (self.description)


class Trade_Test_Result_Id(models.Model):
    lookup = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150)

    def __str__(self):
        return '%s' % (self.description)


class Trade_Test_Result_Reason_Id(models.Model):
    lookup = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150)

    def __str__(self):
        return '%s' % (self.description)


class Urban_Rural_ID(models.Model):
    lookup = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150)

    def __str__(self):
        return '%s' % (self.description)


class Walking_Rating_Id(models.Model):
    lookup = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150)

    def __str__(self):
        return '%s' % (self.description)


# Provider - 100
class Provider(models.Model):    
    provider_code = models.CharField(unique=True, max_length=20)
    provider_etqe_id = models.CharField(max_length=10)
    sic_code = models.ForeignKey(SIC_Code, blank=True, null=True, to_field='lookup', on_delete = models.CASCADE)
    provider_name = models.CharField(max_length=70, validators=[validate_na_geen])
    provider_type_id = models.ForeignKey(Provider_Type_Id, on_delete = models.CASCADE)
    provider_physical_address_1 = models.CharField(max_length=50)
    provider_physical_address_2 = models.CharField(max_length=50)
    provider_physical_address_3 = models.CharField(max_length=50, blank=True)
    provider_physical_address_code = models.CharField(max_length=4)
    provider_website_address = models.URLField(blank=True)    
    provider_postal_address_1 = models.CharField(max_length=50, validators=[validate_na_geen, validate_letters_special], blank=True)
    provider_postal_address_2 = models.CharField(max_length=50, validators=[validate_na_geen, validate_letters_special], blank=True)
    provider_postal_address_3 = models.CharField(max_length=50, blank=True, validators=[validate_na_geen, validate_letters_special])
    provider_postal_address_code = models.CharField(max_length=4, validators=[validate_postcode], blank=True)
    provider_phone_number = models.CharField(max_length=20, blank=True, validators=[validate_phone_fax])
    provider_fax_number = models.CharField(max_length=20, blank=True, validators=[validate_phone_fax])
    provider_sars_number = models.CharField(max_length=20, blank=True)
    provider_contact_name = models.CharField(max_length=20, blank=True)
    provider_contact_email_address = models.EmailField(max_length=50, blank=True)
    provider_contact_phone_number = models.CharField(max_length=20, blank=True, validators=[validate_phone_fax])
    provider_contact_cell_number = models.CharField(max_length=20, blank=True, validators=[validate_phone_fax])
    provider_accreditation_num = models.CharField(max_length=20, blank=True)
    # provider_start_date = models.DateField(validators=[validate_provider_start_end_date])
    provider_start_date = models.DateField()
    provider_end_date = models.DateField(blank=True, null=True)
    etqe_decision_number = models.CharField(max_length=20, blank=True)
    provider_class_id = models.ForeignKey(Provider_class_Id, to_field='lookup', on_delete = models.CASCADE)
    provider_status_id = models.ForeignKey(Provider_Status_Id, to_field='lookup', on_delete = models.CASCADE)
    province_code = models.ForeignKey(Province_Code, to_field='lookup', on_delete = models.CASCADE)
    country_code = models.ForeignKey(Country_Code, to_field='lookup', on_delete = models.CASCADE)
    latitude_degree = models.CharField(max_length=3, blank=True)
    latitude_minutes = models.CharField(max_length=2, blank=True)
    latitude_seconds = models.CharField(max_length=6, blank=True)
    longitude_degree = models.CharField(max_length=2, blank=True)
    longitude_minutes = models.CharField(max_length=2, blank=True)
    longitude_seconds = models.CharField(max_length=6, blank=True)    
    sdl_no = models.CharField(max_length=10, blank=True)
    date_stamp = models.DateField(default=datetime.datetime.now)

    def clean(self):
        if not self.provider_postal_address_1:
            self.provider_postal_address_1 = self.provider_physical_address_1
        if not self.provider_postal_address_2:
            self.provider_postal_address_2 = self.provider_physical_address_2
        if not self.provider_postal_address_3:
            self.provider_postal_address_3 = self.provider_physical_address_3
        if not self.provider_postal_address_code:
            self.provider_postal_address_code = self.provider_physical_address_code
        super(Provider, self).clean() 

    def save(self):
        if not self.provider_postal_address_1:
            self.provider_postal_address_1 = self.provider_physical_address_1
        if not self.provider_postal_address_2:
            self.provider_postal_address_2 = self.provider_physical_address_2
        if not self.provider_postal_address_3:
            self.provider_postal_address_3 = self.provider_physical_address_3
        if not self.provider_postal_address_code:
            self.provider_postal_address_code = self.provider_physical_address_code
        super(Provider, self).save() 



    def __str__(self):
        return '%s %s' % (self.provider_name, self.provider_code)


# Employer 200
class Employer(models.Model):
    sdl_no = models.CharField(max_length=10)
    #change all G & T numbers to L numbers
    site_no = models.CharField(max_length=10)
    seta_id = models.ForeignKey(SETA_Id, null=True, to_field='lookup', on_delete = models.CASCADE)
    sic_code = models.ForeignKey(SIC_Code, blank=True, null=True, to_field='lookup', on_delete = models.CASCADE)
    employer_registration_number = models.CharField(max_length=20, blank=True)
    employer_company_name = models.CharField(max_length=70)
    employer_trading_name = models.CharField(max_length=70)
    employer_physical_address_1 = models.CharField(max_length=50)
    employer_physical_address_2 = models.CharField(max_length=50)
    employer_physical_address_3 = models.CharField(max_length=50, blank=True)
    employer_physical_address_code = models.CharField(max_length=4)
    employer_postal_address_1 = models.CharField(max_length=50, blank=True)
    employer_postal_address_2 = models.CharField(max_length=50, blank=True)
    employer_postal_address_3 = models.CharField(max_length=50, blank=True)
    employer_postal_address_code = models.CharField(max_length=4, blank=True)    
    employer_phone_number = models.CharField(max_length=20, blank=True, validators=[validate_phone_fax])
    employer_fax_number = models.CharField(max_length=20, blank=True, validators=[validate_phone_fax])
    employer_contact_name = models.CharField(max_length=20, blank=True)
    employer_contact_email_address = models.EmailField(max_length=50, blank=True)
    employer_contact_phone_number = models.CharField(max_length=20, blank=True, validators=[validate_phone_fax])
    employer_contact_cell_number = models.CharField(max_length=20, blank=True, validators=[validate_phone_fax])
    employer_approval_status_id = models.CharField(max_length=10, blank=True)
    employer_approval_start_date = models.DateField()
    employer_approval_end_date = models.DateField()
    employer_approval_status_num = models.CharField(max_length=20, blank=True)
    province_code = models.ForeignKey(Province_Code, to_field='lookup', on_delete = models.CASCADE)
    country_code = models.ForeignKey(Country_Code, to_field='lookup', on_delete = models.CASCADE)
    latitude_degree = models.CharField(max_length=3, blank=True)
    latitude_minutes = models.CharField(max_length=2, blank=True)
    latitude_seconds = models.CharField(max_length=6, blank=True)
    longitude_degree = models.CharField(max_length=2, blank=True)
    longitude_minutes = models.CharField(max_length=2, blank=True)
    longitude_seconds = models.CharField(max_length=6, blank=True)
    main_sdl_no = models.CharField(max_length=10)
    date_stamp = models.DateField(default=datetime.datetime.now)

    def clean(self):
        if not self.employer_postal_address_1:
            self.employer_postal_address_1 = self.employer_physical_address_1
        if not self.employer_postal_address_2:
            self.employer_postal_address_2 = self.employer_physical_address_2
        if not self.employer_postal_address_3:
            self.employer_postal_address_3 = self.employer_physical_address_3
        if not self.employer_postal_address_code:
            self.employer_postal_address_code = self.employer_physical_address_code
        super(Employer, self).clean() 

    def save(self):
        if not self.employer_postal_address_1:
            self.employer_postal_address_1 = self.employer_physical_address_1
        if not self.employer_postal_address_2:
            self.employer_postal_address_2 = self.employer_physical_address_2
        if not self.employer_postal_address_3:
            self.employer_postal_address_3 = self.employer_physical_address_3
        if not self.employer_postal_address_code:
            self.employer_postal_address_code = self.employer_physical_address_code
        super(Employer, self).save() 

    def __str__(self):
        return '%s %s' % (self.employer_company_name, self.sdl_no)
    

PERSON_TITLES = (
    ('Mr', 'Mr'),
    ('Mrs', 'Mrs'),
    ('Ms', 'Ms'),
    ('Miss', 'Miss'),
    ('Dr', 'Dr'),
    ('Prof', 'Prof'),
)


# Person 400
class Person(models.Model):
    national_id = models.CharField(blank=True, max_length=15, validators=[validateID])    
    alternate_id_type_id = models.ForeignKey(Alternate_Id_Type_Id, to_field='lookup', on_delete = models.CASCADE)
    person_alternate_id = models.CharField(max_length=20, blank=True)
    equity_code = models.ForeignKey(Equity_Code, to_field='lookup', on_delete = models.CASCADE)
    nationality_code = models.ForeignKey(Nationality_Code, to_field='lookup', on_delete = models.CASCADE)
    home_language_code = models.ForeignKey(Home_Language_Code, to_field='lookup', on_delete = models.CASCADE)
    gender_code = models.ForeignKey(Gender_Code, to_field='lookup', on_delete = models.CASCADE)
    citizen_resident_status_code = models.ForeignKey(Citizen_Resident_Status_Code, to_field='lookup', on_delete = models.CASCADE)
    person_last_name = models.CharField(max_length=45, validators=[validate_na_geen, validate_names])
    person_first_name = models.CharField(max_length=26, validators=[validate_na_geen, validate_names])
    person_middle_name = models.CharField(max_length=50, validators=[validate_na_geen, validate_names])
    person_title = models.CharField(max_length=10, choices=PERSON_TITLES)
    person_birth_date = models.DateField(max_length=8, validators=[validate_sixteen, validate_eighteen_fifty])
    person_home_address_1 = models.CharField(max_length=50, validators=[validate_na_geen, validate_letters_special])
    person_home_address_2 = models.CharField(max_length=50, validators=[validate_na_geen, validate_letters_special])
    person_home_address_3 = models.CharField(max_length=50, blank=True, validators=[validate_na_geen, validate_letters_special])
    person_address_code = models.CharField(max_length=4)
    person_postal_address_1 = models.CharField(max_length=50, validators=[validate_na_geen, validate_letters_special], blank=True)
    person_postal_address_2 = models.CharField(max_length=50, validators=[validate_na_geen, validate_letters_special], blank=True)
    person_postal_address_3 = models.CharField(max_length=50, validators=[validate_na_geen, validate_letters_special], blank=True)
    person_postal_address_code = models.CharField(max_length=4, blank=True)    
    person_phone_number = models.CharField(max_length=20, blank=True, validators=[validate_phone_fax])
    person_cell_phone_number = models.CharField(max_length=20, blank=True, validators=[validate_phone_fax])
    person_fax_number = models.CharField(max_length=20, blank=True, validators=[validate_phone_fax])
    person_email_address = models.EmailField(max_length=50, blank=True)
    province_code = models.ForeignKey(Province_Code, to_field='lookup', on_delete = models.CASCADE)
    provider_code = models.ForeignKey(Provider, on_delete = models.CASCADE)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    # provider_etqe_id = models.CharField(max_length=10, blank=True)
    person_previous_last_name = models.CharField(max_length=45, blank=True)
    person_previous_alternate_id = models.CharField(max_length=20, blank=True)
    person_previous_alternate_id_type_id = models.CharField(max_length=3, blank=True)
    person_previous_provider_code = models.CharField(max_length=20, blank=True)
    person_previous_provider_etqe_id = models.CharField(max_length=10, blank=True)
    seeing_rating_id = models.ForeignKey(Seeing_Rating_Id, blank=True, null=True, to_field='lookup', on_delete = models.CASCADE)
    hearing_rating_id = models.ForeignKey(Hearing_Rating_Id, blank=True, null=True, to_field='lookup', on_delete = models.CASCADE)
    walking_rating_id = models.ForeignKey(Walking_Rating_Id, blank=True, null=True, to_field='lookup', on_delete = models.CASCADE)
    remembering_rating_id = models.ForeignKey(Remembering_Rating_Id, blank=True, null=True, to_field='lookup', on_delete = models.CASCADE)
    communicating_rating_id = models.ForeignKey(Communicating_Rating_Id, blank=True, null=True, to_field='lookup', on_delete = models.CASCADE)
    self_care_rating_id = models.ForeignKey(Self_Care_Rating_Id, blank=True, null=True, to_field='lookup', on_delete = models.CASCADE)
    last_school_emis_number = models.CharField(max_length=10, blank=True, null=True)
    last_school_year = models.CharField(max_length=4, blank=True, null=True)
    statssa_area_code = models.ForeignKey(STATSSA_Area_Code, blank=True, null=True, to_field='lookup', on_delete = models.CASCADE)
    popi_act_status_id = models.ForeignKey(POPI_Act_Status_ID, blank=True, null=True, to_field='lookup', on_delete = models.CASCADE)
    popi_act_status_date = models.DateField(blank=True, null=True)
    date_stamp = models.DateField(default=datetime.datetime.now)

    def clean(self):
        if not self.person_postal_address_1:
            self.person_postal_address_1 = self.person_home_address_1
        if not self.person_postal_address_2:
            self.person_postal_address_2 = self.person_home_address_2
        if not self.person_postal_address_3:
            self.person_postal_address_3 = self.person_home_address_3
        if not self.person_postal_address_code:
            self.person_postal_address_code = self.person_address_code
        super(Person, self).clean() 

    def save(self):
        if not self.person_postal_address_1:
            self.person_postal_address_1 = self.person_home_address_1
        if not self.person_postal_address_2:
            self.person_postal_address_2 = self.person_home_address_2
        if not self.person_postal_address_3:
            self.person_postal_address_3 = self.person_home_address_3
        if not self.person_postal_address_code:
            self.person_postal_address_code = self.person_address_code
        super(Person, self).save() 

    def __str__(self):
        return '%s %s %s' % (self.person_first_name, self.person_last_name, self.national_id)


# Person Designation 401
class Designation(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    #national_id = models.CharField(max_length=15, validators=[validateID])
    #person_alternate_id = models.CharField(max_length=20, blank=True)
    #alternate_id_type_id = models.ForeignKey(Alternate_Id_Type_Id, to_field='lookup', on_delete = models.CASCADE)
    #alternate_id_type_id = models.ForeignKey(Alternate_Id_Type_Id)
    designation_id = models.ForeignKey(Designation_Id, to_field='lookup', on_delete = models.CASCADE)
    designation_registration_number = models.CharField(max_length=20)
    designation_etqe_id = models.CharField(max_length=10)
    designation_start_date = models.DateField()
    designation_end_date = models.DateField(blank=True)
    designation_structure_status_id = models.ForeignKey(Designation_Structure_Status_Id, to_field='lookup', on_delete = models.CASCADE)
    etqe_decision_number = models.CharField(max_length=20, blank=True)
    provider_code = models.ForeignKey(Provider, on_delete = models.CASCADE)
    # provider_etqe_id = models.CharField(max_length=10)
    date_stamp = models.DateField(default=datetime.datetime.now)

    def __str__(self):
        return '%s %s' % (self.designation_id, self.designation_registration_number)




# Learnership 500
class Learnership(models.Model):
    #national_id = models.CharField(max_length=15, validators=[validateID])
    #person_alternate_id = models.CharField(max_length=20, blank=True)
    #alternate_id_type_id = models.CharField(max_length=3)
    #alternate_id_type_id = models.ForeignKey(Alternate_Id_Type_Id, to_field='lookup', on_delete = models.CASCADE)
    person = models.ForeignKey(Person, on_delete = models.CASCADE)
    #learnership_id = models.CharField(max_length=10)
    LEARNERSHIP_ID_CHOICES = (
        
        ('436','436 - Certificate in General Nursing (Enrolled) Level 4'),
        ('437','437 - Diploma in General Nursing (Bridging) Level 5'),
        ('439','439 - FETC Phlebotomy Techniques NQF Level 4'),
        ('440','440 - Certificate in General Nursing (Auxiliary) Level 4'),
        ('442','442 - Post Basic Diploma in Medical/Surgical Nursing (Elective: Critical Care/Operating Theater Nursing) Level 6'),
        ('444','444 - FET Certificate in Social Auxiliary Work Level 4'),
        ('446','446 - Further Education and Training Certificate: Child and Youth Care Work Level 4'),
        ('448','448 - Health Promotion Officer NQF Level 3'),
        ('1117','1117 - National Certificate: Pharmacist Assistance Level 3'),
        ('1118','1118 - Ferther Education and Training Certificate: Pharmacist Assistance Level 4'),
        ('1357','1357 - Further Education and Training Certificate:  Early Childhood Development Level 4'),
        ('268','268 - L5 - Learnership for ECD Trainers Level 5'),
        ('6591', '6591 - University Diploma:Veterinary Nursing Level 6'),
        ('10809', '10809 - Post Basic Diploma: Operating  Theater Nursing Science Level 7'),
        ('21214', '21214 - Post Basic Diploma: Medical and Surgical Nursing Science Level 7'),
        ('16496', '16496 - Advance University Diploma: Midwifery and Neonatal Nursing Level 7'),
        ('17196', '17196 - Bridging Diploma: Nursing General Level 5'),
        ('97756', '97756 - Higher Certificate: Auxilliary Nursing Level 5'),
        ('72049', '72049 - National Certificate: Pharmacy Assistant Level 3'),
        ('72050', '72050 - Further Education and training Certificate: Pharmacy Assistant Level 4'),
        ('59345', '59345 - Further Education and training Certificate: Phlebotomy Technique Level 4'),
        ('60209', '60209 - Further Education and training Certificate: Child & Youthcare Level 4'),
        ('94597', '94597 - Occupational Certificate: Health Promotion Officer Level 3'),
        ('99510', '99510 - Occupational Certificate: Child and Youth care Worker Level 5'),
        ('98890', '98890 - Occupational Certificate: Social Auxiliary Worker Level 5'),
        ('1502', '1502 - National Certificate: Occupational Health, Safety and Environment: Mining and Minerals, Level 2'),
        ('1111','1111 - General Education and Training Certificate: Business Practice, Level 1'),
        ('1216','1216 - National Certificate: Public Administration: Leadership, Level 5'),
        ('1217','1217 - National Certificate: Public Administration: Procurement, Level 5'),
        ('797','797 - Office Administration Assistant, Level 2'),
        ('527','527 - National Certificate in People Centre Management, Level 2'),
        ('871','871 - Contact Centre Support, Level 2'),
        ('1063','1063 - National Certificate: Wholesale Retail: Visual Merchandising, Level 3'),
        ('61595', '61595 - Further Education and Training Certificate: Business Administration Services Level 4'),
        ( '57712', 'Further Education and Training Certificate: Generic Management - level 4'),
        ('61591', 'National Certificate: Information Technology: End User Computing – level 3'),
        ('63969', 'National Certificate: Pharmaceutical Sales Representation – level 5'),

    )
    
    learnership_id = models.CharField(max_length=10, choices=LEARNERSHIP_ID_CHOICES)

    #LEARNERSHIP_TYPE_CHOICES = (
    #    ('Technical', 'Technical'),
    #    ('Academic', 'Academic'),
    #)
    #learnership_type = models.CharField(max_length=10, choices=LEARNERSHIP_TYPE_CHOICES)
    #enrolment_status_id = models.CharField(max_length=3)
    enrolment_status_id = models.ForeignKey(Enrolment_Status_Id, to_field='lookup', on_delete = models.CASCADE)
    assessor_registration_number = models.CharField(max_length=20, blank=True)
    enrolment_status_date = models.DateField()
    enrolment_date = models.DateField()
    provider = models.ForeignKey(Provider, on_delete = models.CASCADE)
    employer = models.ForeignKey(Employer, on_delete = models.CASCADE)
    # provider_etqe_id = models.CharField(max_length=10)
    assessor_etqe_id = models.CharField(max_length=10, blank=True)
    enrolment_status_reason_id = models.ForeignKey(Enrolment_Status_Reason_Id, null=True, blank=True, to_field='lookup', on_delete = models.CASCADE)
    most_recent_registration_date = models.DateField()
    certificate_number = models.CharField(max_length=30, blank=True)
    economic_status_id = models.ForeignKey(Economic_Status_Id, to_field='lookup', on_delete = models.CASCADE)
    funding_id = models.ForeignKey(Funding_Id, to_field='lookup', on_delete = models.CASCADE)
    cumulative_spend = models.CharField(max_length=10, blank=True)
    ofo_code = models.ForeignKey(OFO_Code, to_field='lookup', on_delete = models.CASCADE)
    # sdl_no = models.ForeignKey(Employer)
    urban_rural_id = models.ForeignKey(Urban_Rural_ID, to_field='lookup', on_delete = models.CASCADE)
    learning_programme_type_id = models.CharField(max_length=10)
    date_stamp = models.DateField(default=datetime.datetime.now)
    

    def __str__(self):
        return '%s (%s)' % (self.person, self.learnership_id)


# Qualification Enrolment 501
class Qualification(models.Model):
    #national_id = models.CharField(max_length=15, validators=[validateID])
    #person_alternate_id = models.CharField(max_length=20, blank=True)
    #alternate_id_type_id = models.CharField(max_length=3)
    person = models.ForeignKey(Person, on_delete = models.CASCADE)
    qualification_id = models.CharField(max_length=10)
    #enrolment_status_id = models.CharField(max_length=3)
    assessor_registration_number = models.CharField(max_length=20, blank=True)
    enrolment_type_id = models.ForeignKey(Enrolment_Type_Id, to_field='lookup', on_delete = models.CASCADE, default=4)
    #enrolment_status_date = models.DateField()
    #enrolment_date = models.DateField()
    #part_of_id = models.CharField(max_length=2)
    part_of_id = models.ForeignKey(Part_Of_Id, on_delete=models.CASCADE, to_field='lookup')
    #learnership_id = models.CharField(max_length=20, blank=True)
    provider = models.ForeignKey(Provider, on_delete = models.CASCADE)
    assessor_etqe_id = models.CharField(max_length=20, blank=True)
    enrolment_status_reason_id = models.CharField(max_length=10, blank=True)
    most_recent_registration_date = models.DateField()
    certificate_number = models.CharField(max_length=30, blank=True)
    #economic_status_id = models.CharField(max_length=10)
    economic_status_id = models.ForeignKey(Economic_Status_Id, on_delete=models.CASCADE, to_field='lookup')
    employer = models.ForeignKey(Employer, on_delete = models.CASCADE)
    practical_provider = models.CharField(max_length=20, blank=True)
    practical_etqe_id = models.CharField(max_length=10, blank=True)
    #funding_id = models.CharField(max_length=10)
    funding_id = models.ForeignKey(Funding_Id, on_delete=models.CASCADE, to_field="lookup")
    cumulative_spend = models.CharField(max_length=10, blank=True)
    #ofo_code = models.CharField(max_length=15, blank=True)
    ofo_code = models.ForeignKey(OFO_Code, on_delete=models.CASCADE, to_field="lookup")
    #urban_rural_id = models.CharField(max_length=3)
    urban_rural_id = models.ForeignKey(Urban_Rural_ID, on_delete=models.CASCADE, to_field="lookup")
    learning_programme_type_id = models.CharField(max_length=10, default='')
    date_stamp = models.DateField(default=datetime.datetime.now)

    def __str__(self):
        return '%s (%s)' % (self.person, self.qualification_id)

# Unit Standard Enrolment 503
class Unit_Standard(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    unit_standard_id = models.CharField(max_length=10)
    enrolment_status_id = models.ForeignKey(Enrolment_Status_Id, to_field='lookup', on_delete = models.CASCADE)
    assessor_registration_number = models.CharField(max_length=20, blank=True)
    enrolment_type_id = models.ForeignKey(Enrolment_Type_Id, to_field='lookup', on_delete = models.CASCADE)
    enrolment_status_date = models.DateField()
    enrolment_date = models.DateField()
    part_of_id = models.CharField(max_length=2)
    qualification_id = models.CharField(max_length=10, blank=True)
    learnership_id = models.CharField(max_length=10, blank=True)
    provider = models.ForeignKey(Provider, on_delete = models.CASCADE)
    assessor_etqe_id = models.CharField(max_length=20, blank=True)
    enrolment_status_reason_id = models.ForeignKey(Enrolment_Status_Reason_Id, to_field='lookup', on_delete = models.CASCADE)
    most_recent_registration_date = models.DateField()
    certificate_number = models.CharField(max_length=30, blank=True)
    economic_status_id = models.ForeignKey(Economic_Status_Id, to_field='lookup', on_delete = models.CASCADE)
    employer = models.ForeignKey(Employer, on_delete = models.CASCADE)
    non_nqf_interv_provider = models.CharField(max_length=20, blank=True)
    non_nqf_interv_etqe_id = models.CharField(max_length=10, blank=True)
    funding_id = models.ForeignKey(Funding_Id, to_field='lookup', on_delete = models.CASCADE)
    cumulative_spend = models.CharField(max_length=10, blank=True)
    ofo_code = models.ForeignKey(OFO_Code, to_field='lookup', on_delete = models.CASCADE)
    urban_rural_id = models.ForeignKey(Urban_Rural_ID, to_field='lookup', on_delete = models.CASCADE)
    date_stamp = models.DateField(default=datetime.datetime.now)

    def __str__(self):
        return '%s (%s)' % (self.person, self.unit_standard_id)

# Internship Placement 506
class Internship_Placement(models.Model):
    #national_id = models.CharField(max_length=15, validators=[validateID])
    #person_alternate_id = models.CharField(max_length=20, blank=True)
    #alternate_id_type_id = models.CharField(max_length=3)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    qualification_id = models.CharField(max_length=10)
    qualification_achievement_date = models.DateField()
    internship_status_id = models.ForeignKey(Internship_Status_Id, to_field='lookup',on_delete=models.CASCADE)
    enrolment_status_id = models.ForeignKey(Enrolment_Status_Id, to_field='lookup', on_delete = models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    employer = models.ForeignKey(Employer, on_delete = models.CASCADE)
    provider_code = models.ForeignKey(Provider, on_delete = models.CASCADE)
    funding_id = models.ForeignKey(Funding_Id, to_field='lookup', on_delete=models.CASCADE)
    cumulative_spend = models.CharField(max_length=10)
    ofo_code = models.ForeignKey(OFO_Code, to_field='lookup', on_delete=models.CASCADE)
    urban_rural_id = models.ForeignKey(Urban_Rural_ID, to_field='lookup', on_delete=models.CASCADE)
    date_stamp = models.DateField(default=datetime.datetime.now)

    def __str__(self):
        return str(self.person)+" ("+str(self.qualification_id)+")"

class Non_NQF_Intervention(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    non_nqf_intervention_code = models.CharField(max_length=10)
    non_nqf_intervention_name = models.CharField(max_length=10)
    subfield_id = models.ForeignKey(Subfield_Id, to_field='lookup', on_delete=models.CASCADE)
    non_nqf_registration_start_date = models.DateField()
    non_nqf_registration_end_date = models.DateField()
    non_nqf_intervention_etqe_id = models.CharField(max_length=10)
    non_nqf_status_id = models.ForeignKey(Non_NQF_Interv_Status_Id, to_field='lookup', on_delete=models.CASCADE)
    non_nqf_credit = models.CharField(max_length=10)
    learning_programme_type_id = models.CharField(max_length=10)
    date_stamp = models.DateField(default=datetime.datetime.now)

    def __str__(self):
        return str(self.person)+" ("+str(self.non_nqf_intervention_code)+")"

class Non_NQF_Placement(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    non_nqf_intervention_code = models.CharField(max_length=20)
    enrolment_status_id =  models.ForeignKey(Enrolment_Status_Id, on_delete=models.CASCADE)
    assessor_registration_number =  models.CharField(max_length=20)
    enrolment_type_id = models.ForeignKey(Enrolment_Type_Id, on_delete=models.CASCADE)
    enrolment_status_date = models.DateField()
    enrolment_date = models.DateField()
    part_of_id = models.ForeignKey(Part_Of_Id, on_delete=models.CASCADE)
    qualification_id = models.CharField(max_length=10)
    learnership_id = models.CharField(max_length=10, choices=LEARNERSHIP_ID_CHOICES)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    assessor_etqe_id = models.CharField(max_length=10)
    enrolment_status_reason_id = models.ForeignKey(Enrolment_Status_Reason_Id, on_delete=models.CASCADE)
    most_recent_registration_date = models.DateField()
    economic_status_id = models.ForeignKey(Economic_Status_Id, on_delete=models.CASCADE)
    funding_id = models.ForeignKey(Funding_Id, on_delete=models.CASCADE)
    cumulative_spend = models.CharField(max_length=10)
    ofo_code = models.ForeignKey(OFO_Code, on_delete=models.CASCADE)
    sdl_no = models.CharField(max_length=10)
    site_no = models.CharField(max_length=10)
    non_nqf_intervention_etqe_id = models.CharField(max_length=10)
    urban_rural_id = models.ForeignKey(Urban_Rural_ID, on_delete=models.CASCADE)
    date_stamp = models.DateField(default=datetime.datetime.now)

    def __str__(self):
        return str(self.person)+str(self.non_nqf_intervention_code)
        
#Non NQF Interv Code:
#*Non NQF Interv Name:
#*Subfield Id:
#*Non NQF Interv Reg Start Date:	#
    #yyyymmdd
#Non NQF Interv Reg End Date:
#    yyyymmdd
#*Non NQF Interv ETQE Id:
#*Non NQF Interv Status Id:
#*Non NQF Interv Credit:
#*Date Stamp:	20180116
#Submit
