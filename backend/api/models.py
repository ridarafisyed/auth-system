from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


# Create your models here.

# when user register these field must be store

# class User(models.Model):
#     f_name = models.CharField(max_length=80)
#     l_name = models.CharField(max_length=80)
#     m_name = models.CharField(max_length=80)
#     company = models.CharField(max_length=80, default="")
#     uname = models.CharField(max_length=80, unique=True)
#     pword = models.CharField(max_length=80) #should be encrypt 
#     created_at = models.DateTimeField(auto_now_add = True)
# when a user register the profile will build with default values and user_id
# user can edit their profile later.
#  user profile 
class Profile (models.Model):
    # p_id = models.IntegerField()[pk, increment]
    f_name = models.CharField(max_length=80)
    l_name = models.CharField(max_length=80)
    m_name = models.CharField(max_length=80)
    company = models.CharField(max_length=80, default="")
    user_id = models.IntegerField(default= 0)
    emp_pers_email = models.CharField(max_length=80, default="")
    emp_ssn = models.IntegerField(default= 0)
    user = models.IntegerField() # user model ref 
    job_title = models.CharField(max_length=80, default="")
    bar_no = models.IntegerField(default= 0)
    role = models.CharField(max_length=80, default="")
    group = models.CharField(max_length=80, default="")
    timezone = models.DateTimeField()
    rate = models.FloatField(max_length=10, default=0.00)
    company_email = models.CharField(max_length=80, default="")
    round_enteries = models.IntegerField()
    add_street = models.CharField(max_length=80, default="")
    add_suite = models.CharField(max_length=80,default="")
    add_city = models.CharField(max_length=80,default="")
    add_state = models.CharField(max_length=80, default="")
    add_zip = models.CharField(max_length=80,default="")
    mobile_no = models.IntegerField(default= 0)
    work_no = models.IntegerField(default=0)
    home_no = models.IntegerField(default=0) 
    extention  = models.IntegerField(default=0)

class Country(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=80)
    continent_name = models.CharField(max_length=80)
    timezone = models.DateTimeField()

class County_Recorder (models.Model):
    # id int [pk, increment]
    cnty_plus_4 = models.IntegerField()
    cnty_add = models.CharField(max_length=80)
    cnty_city = models.CharField(max_length=80)
    cnty_email = models.CharField(max_length=80)
    cnty_phone = models.IntegerField()
    cnty_state = models.CharField(max_length=80)
    cnty_suite = models.CharField(max_length=80)
    cnty_website = models.CharField(max_length=80)
    cnty_zip = models.CharField(max_length=80)

class Company(models.Model):
    comp_name = models.CharField(max_length=80)
    comp_email = models.CharField(max_length=80)
    comp_address = models.CharField(max_length=80)
    comp_suite = models.CharField(max_length=80)
    comp_city = models.CharField(max_length=80)
    comp_state = models.CharField(max_length=80)
    comp_zip = models.CharField(max_length=80)
    comp_county = models.CharField(max_length=80) # ref to country 
    comp_attorneys = models.CharField(max_length=80)
    comp_emp = models.CharField(max_length=80)
    comp_office = models.CharField(max_length=80)

class Office (models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default="")
    off_name = models.CharField(max_length=80)
    off_rep_id = models.IntegerField() #[ref: > users.id]
    off_add = models.CharField(max_length=80)
    off_add_suite = models.CharField(max_length=80)
    off_add_city = models.CharField(max_length=80)
    off_add_state = models.CharField(max_length=80)
    off_add_zip = models.CharField(max_length=80)
    off_add_country = models.IntegerField() #[ref: > countries.code]
    off_contact_mobile = models.IntegerField()
    off_contact_home = models.IntegerField()
    off_contact_work = models.IntegerField()
    off_fax = models.IntegerField()
    off_email1 = models.CharField(max_length=80)
    off_email2 = models.CharField(max_length=80)
    off_email3 = models.CharField(max_length=80)
    off_ssn = models.IntegerField()

class Contact (models.Model):
    # contact_id = models.IntegerField()
    office_id = models.ForeignKey(Office, on_delete=models.CASCADE)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)

# invoice model 
class Invoice(models.Model):
    # inv_client_id = models.IntegerField()
    inv_created_at = models.DateField(max_length=8)
    inv_payed_at = models.DateField(max_length=8)
    inv_client_name = models.CharField(max_length=50)
    inv_disputed = models.CharField(max_length=200)
    inv_due_at = models.DateField(max_length=8)
    inv_interest_due_at = models.DateField(max_length=8)
    inv_status = models.CharField(max_length=10)
    inv_matter_id = models.CharField(max_length=50) # ref to matter
    inv_note = models.TextField(max_length=500)
    inv_date_period = models.DateField(max_length=8)
    inv_term_contidion = models.TextField(max_length=1000)
    inv_void = models.CharField(max_length=200)
    inv_amount =models.FloatField(max_length=20)
    inv_disc = models.FloatField(max_length=20)
    inv_fees = models.IntegerField()
    inv_misc_fees = models.IntegerField()
    
class Matter (models.Model):
    matter_id = models.IntegerField() # used as a ref
    matter_name = models.CharField(max_length=80)
    matter_type = models.CharField(max_length=80)
    matter_source = models.CharField(max_length=80)
    matter_status = models.CharField(max_length=80)
    assign_to = models.IntegerField() # ref to user 

class Court_Record (models.Model):
    # id int [pk, increment]
    court_plus_4 = models.IntegerField()
    court_add = models.CharField(max_length=80)
    court_cnty = models.CharField(max_length=80)
    court_email = models.CharField(max_length=80)
    court_house_name = models.CharField(max_length=80)
    court_phone_no = models.IntegerField() 
    court_room = models.CharField(max_length=80)
    court_state = models.CharField(max_length=80)
    court_type = models.CharField(max_length=80)
    court_website = models.CharField(max_length=80)
    court_zip = models.IntegerField() 
    court_efile_id = models.IntegerField() # [ref: > efile_serveices.court_efile_id]
    proc_server_id = models.IntegerField()# [ref: > process_servers.proc_server_id]
    sheriff_id = models.IntegerField()# [ref: > sheriff_details.sheriff_id]

class EFIle_Services (models.Model):
    court_efile_id = models.IntegerField()#  [pk, increment]
    court_efile_plus_4 = models.IntegerField()# 
    court_efile_add = models.CharField(max_length=80)
    court_efile_city = models.CharField(max_length=80)
    court_efile_unit = models.CharField(max_length=80)
    court_efile_county = models.CharField(max_length=80)
    court_efile_state = models.CharField(max_length=80)
    court_efile_zip = models.CharField(max_length=80)
    court_efile_website = models.CharField(max_length=80)
    count_efile_phone_no = models.IntegerField() 
    court_efile_email = models.CharField(max_length=80)
    court_efile_cmpy_name = models.CharField(max_length=80)
    court_efile_cont_person = models.CharField(max_length=80)
    court_efile_cust_rating = models.CharField(max_length=80)
    court_efile_rate_sheet = models.CharField(max_length=80)# // file path

class Lead (models.Model):
    # id = models.IntegerField()[pk, increment]
    lead_add = models.CharField(max_length=80)
    lead_city = models.CharField(max_length=80)
    lead_state = models.CharField(max_length=80)
    lead_unit = models.CharField(max_length=80)
    lead_zip = models.IntegerField()
    lead_event_date = models.DateField(max_length=8)
    lead_country = models.IntegerField() #[ref: > countries.code]
    lead_email = models.CharField(max_length=80)
    lead_fname = models.CharField(max_length=80)
    lead_lname = models.CharField(max_length=80)
    lead_phone = models.IntegerField()
    lead_relation = models.CharField(max_length=80)
    lead_Matter_Type = models.CharField(max_length=80)
    lead_vic_atty_Email = models.CharField(max_length=80)
    lead_vic_4 = models.IntegerField()
    lead_vic_add = models.CharField(max_length=80)
    lead_vic_atty = models.CharField(max_length=80)
    lead_vic_atty_fn = models.CharField(max_length=80)
    lead_vic_atty_ln = models.CharField(max_length=80)
    lead_vic_atty_phone = models.IntegerField()
    lead_vic_atty_4 = models.IntegerField()
    lead_vic_atty_add = models.CharField(max_length=80)
    lead_vic_atty_cty = models.CharField(max_length=80)
    lead_vic_atty_cnty = models.IntegerField()# [ref: > countries.code]
    lead_vic_atty_st  = models.CharField(max_length=80)
    lead_vic_atty_unit = models.IntegerField()
    lead_vic_atty_zip = models.IntegerField()
    lead_vic_dob = models.DateField(max_length=8)
    lead_vic_fname = models.CharField(max_length=80)
    lead_vic_lname = models.CharField(max_length=80)
    lead_vic_gen = models.CharField(max_length=80)
    lead_vic_st = models.CharField(max_length=80)
    lead_vic_unit = models.IntegerField()
    lead_vic_zip = models.IntegerField()
    lead_vic_cty = models.CharField(max_length=80)
    lead_vic_cnty = models.IntegerField() #[ref: > countries.code]

class Client_Vic_Atty (models.Model):
    client_id = models.IntegerField() # [ref: > users.id]
    cl_vic_atty_id = models.IntegerField() # [pk, increment]
    cl_vic_atty_plus_4 = models.IntegerField()
    cl_vic_atty_add = models.CharField(max_length=80)
    cl_vic_atty_cty = models.CharField(max_length=80)
    cl_vic_atty_cnty = models.CharField(max_length=80)
    cl_vic_atty_fn = models.CharField(max_length=80)
    cl_vic_atty_ln = models.CharField(max_length=80)
    cl_vic_atty_phone = models.IntegerField()
    cl_vic_atty_st = models.CharField(max_length=80)
    cl_vic_atty_unit = models.CharField(max_length=80)
    cl_vic_atty_zip = models.IntegerField()

class Job_Board (models.Model):
    #id int [pk, increment]
    user_id = models.IntegerField(default= 0)
    act_srch  = models.BooleanField()
    bar_pass_date = models.DateField(max_length=8)
    gpa = models.FloatField(max_length=4)
    grad_date = models.DateField(max_length=8) 
    lschool = models.CharField(max_length=80)
    lic_st = models.CharField(max_length=80)
    pass_srch = models.BooleanField()
    salary = models.FloatField(max_length=20)
    ug_degree = models.CharField(max_length=80)
    ug_school = models.CharField(max_length=80)
    relocate = models.BooleanField()

class Sheriff_Detail (models.Model):
    # sheriff_id = models.IntegerField() [pk, increment]
    sheriff_plus_4 = models.IntegerField()
    sheriff_add = models.CharField(max_length=80)
    sheriff_city = models.CharField(max_length=80)
    sheriff_county = models.CharField(max_length=80)
    sheriff_state = models.CharField(max_length=80)
    sheriff_unit = models.CharField(max_length=80)
    sheriff_zip = models.IntegerField()
    sheriff_email = models.CharField(max_length=80)
    sheriff_phone_no = models.CharField(max_length=80)
    sheriff_website = models.CharField(max_length=80)

# client victom information table relate back to client table
class Client_Vic_Info (models.Model):
    client_id = models.IntegerField()# [ref: > users.id]
    cl_vic_atty_email = models.CharField(max_length=80)
    cl_vic_plus_4 = models.IntegerField()
    cl_vic_add = models.CharField(max_length=80)
    cl_vic_cty = models.CharField(max_length=80)
    cl_vic_cnty = models.CharField(max_length=80)
    cl_vic_dob = models.DateField(max_length=8)
    cl_vic_fname = models.CharField(max_length=80)
    cl_vic_gen = models.CharField(max_length=80)
    cl_vic_lname = models.CharField(max_length=80)
    cl_vic_st = models.CharField(max_length=80)
    cl_vic_unit = models.CharField(max_length=80)
    cl_vic_zip = models.IntegerField()
    cl_vic_atty = models.CharField(max_length=80)
    cl_vic_atty_id = models.IntegerField() 

# debtor models 
class Debtor(models.Model):
    # id = models.IntegerField()[pk, increment]
    jdg_type = models.CharField(max_length=80)
    jdg_date = models.DateField(max_length=8)
    dbt_fname = models.CharField(max_length=80)
    dbt_lname = models.CharField(max_length=80)
    dbt_hair = models.CharField(max_length=80)
    dbt_height = models.FloatField(max_length=10)
    dbt_mname = models.CharField(max_length=80)
    dbt_phone = models.IntegerField()
    dbt_gender = models.CharField(max_length=80)
    dbt_bod = models.DateField(max_length=8)
    dbt_ethnicity = models.CharField(max_length=80)
    dbt_eye = models.CharField(max_length=80)
    dbt_skill = models.CharField(max_length=80)
    dbt_ssn = models.IntegerField() 
    dbt_weight = models.IntegerField() 
    dbt_4 = models.IntegerField()
    dbt_add = models.CharField(max_length=80)
    dbt_bank = models.CharField(max_length=80)
    dbt_unit = models.CharField(max_length=80)
    dbt_city = models.CharField(max_length=80)
    dbt_county = models.CharField(max_length=80)
    dbt_state = models.CharField(max_length=80)
    dbt_zip = models.IntegerField()
    dbt_license_no = models.CharField(max_length=80)
    dbt_license = models.CharField(max_length=80)
    dbt_emp_4 = models.IntegerField()
    dbt_emp_add = models.CharField(max_length=80)
    dbt_emp_city = models.CharField(max_length=80)
    dbt_emp_state = models.CharField(max_length=80)
    dbt_emp_unit = models.CharField(max_length=80)
    dbt_emp_zip = models.IntegerField()
    dbt_emp_website = models.CharField(max_length=80)
    dbt_emp_county = models.CharField(max_length=80)
    dbt_emp_email = models.CharField(max_length=80)
    dbt_emp_phone = models.IntegerField()