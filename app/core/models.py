"""
Database models.
"""
from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('user must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'



# class Master(models.Model):
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#     )
#     name = models.CharField(null=True)
#     code = models.CharField(null=True)
#     country_id = models.CharField(null=True)
#     company_id = models.CharField(null=True)
#     is_global = models.IntegerField(null=True)
#     is_active = models.IntegerField(null=True)
#     is_consignor = models.IntegerField(null=True)
#     is_consignee = models.IntegerField(null=True)
#     is_agent = models.IntegerField(null=True)
#     is_transporter = models.IntegerField(null=True)
#     is_broker = models.IntegerField(null=True)
#     is_service_provider = models.IntegerField(null=True)
#     is_acc_receivable = models.IntegerField(null=True)
#     is_acc_payable = models.IntegerField(null=True)
#     is_active_rem = models.IntegerField(null=True)
#     is_air_transport = models.IntegerField(null=True)
#     trans_airline_id = models.BigIntegerField(null=True)
#     is_sea_transport = models.IntegerField(null=True)
#     trans_sealine_id = models.BigIntegerField(null=True)
#     is_road_transport = models.IntegerField(null=True)
#     is_rail_transport = models.IntegerField(null=True)
#     location_id = models.BigIntegerField(null=True)
#     comp_type = models.CharField(null=True)
#     exptr_type = models.CharField(null=True)
#     kyc_details_present = models.CharField(null=True)
#     doc_status = models.CharField(null=True)
#     sales_person_id = models.BigIntegerField(null=True)
#     is_affiliate = models.IntegerField(null=True)
#     aff_company_id = models.BigIntegerField(null=True)
#     denied_party_status = models.CharField(null=True)
#     denied_party_checked_on = models.CharField(null=True)
#     sales_person_user_id = models.BigIntegerField(null=True)
#     global_org_id = models.BigIntegerField(null=True)
#     global_org = models.CharField(null=True)
#     pay_method = models.CharField(null=True)
#     org_edi_code = models.CharField(null=True)
#     exptr_status = models.CharField(null=True)
#     leid = models.CharField(null=True)
#     created_at = models.DateField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name


# class Branch(models.Model):
#     org = models.ForeignKey(Master, on_delete=models.CASCADE, null=True)
#     name = models.CharField(null=True)
#     code = models.CharField(null=True)
#     sr_no = models.IntegerField(null=True)
#     address = models.CharField(null=True)
#     city = models.CharField(null=True)
#     postal_code = models.IntegerField(null=True)
#     country = models.CharField(null=True)
#     telephone_no = models.CharField(null=True)
#     fax_no = models.IntegerField(null=True)
#     email = models.EmailField(null=True)
#     is_default = models.BigIntegerField(null=True)
#     default_seaport_id = models.IntegerField(null=True)
#     default_airport_id = models.IntegerField(null=True)
#     web_url = models.CharField(null=True)
#     branch_add_1 = models.CharField(null=True)
#     branch_add_2 = models.CharField(null=True)
#     branch_add_3 = models.CharField(null=True)
#     city_id = models.IntegerField(null=True)
#     state = models.CharField(null=True)
#     bank_add = models.CharField(null=True)
#     bank_acc_no = models.IntegerField(null=True)
#     dealer_code = models.IntegerField(null=True)
#     is_active = models.BigIntegerField(null=True)
#     amshpr_air = models.CharField(null=True)
#     amshpr_sea = models.CharField(null=True)
#     amcnee_air = models.CharField(null=True)
#     amcnee_sea = models.CharField(null=True)
#     sales_person = models.IntegerField(null=True)
#     collection_exec = models.CharField(null=True)
#     state_code = models.IntegerField(null=True)
#     taxable_type = models.CharField(null=True)
#     aeo_code = models.CharField(null=True)
#     aeo_country = models.CharField(null=True)
#     aeo_role = models.CharField(null=True)
#     branch_edi_code = models.CharField(null=True)
#     org_marks_nos = models.CharField(null=True)
#     created_at = models.DateField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name


# class Reg_Types(models.Model):
#     company_id = models.ForeignKey(Master, on_delete=models.CASCADE)
#     reg_name = models.CharField(null=True)
#     type = models.CharField(null=True)
#     size = models.CharField(null=True)
#     country_id = models.CharField(null=True)
#     is_mandatory = models.BigIntegerField(null=True)
#     sys_defined = models.BigIntegerField(null=True)
#     check_duplicate = models.BigIntegerField(null=True)
#     org_entity_type = models.CharField(null=True)
#     is_global = models.BigIntegerField(null=True)
#     comp_settings = models.BigIntegerField(null=True)
#     data_format = models.CharField(null=True)
#     allow_special_characters = models.BigIntegerField(null=True)
#     allow_unregistered = models.BigIntegerField(null=True)
#     created_at = models.DateField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.reg_name


# class RegNo_Details(models.Model):
#     org_id = models.ForeignKey(Master, on_delete=models.CASCADE)
#     reg_type_id = models.ForeignKey(Reg_Types, on_delete=models.CASCADE)
#     reg_date = models.DateField(auto_now_add=True)
#     valid_upto = models.DateField()
#     branch_id = models.DateField()
#     is_unregistered = models.DateField()
#     created_at = models.DateField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.org_id
