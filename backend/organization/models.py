from django.db import models


class Master(models.Model):
    name = models.CharField()
    code = models.CharField()
    country_id = models.CharField()
    company_id = models.CharField()
    is_global = models.IntegerField()
    is_active = models.IntegerField()
    is_consignor = models.IntegerField()
    is_consignee = models.IntegerField()
    is_agent = models.IntegerField()
    is_transporter = models.IntegerField()
    is_broker = models.IntegerField()
    is_service_provider = models.IntegerField()
    is_acc_receivable = models.IntegerField()
    is_acc_payable = models.IntegerField()
    is_active_rem = models.IntegerField()
    is_air_transport = models.IntegerField()
    trans_airline_id = models.BigIntegerField()
    is_sea_transport = models.IntegerField()
    trans_sealine_id = models.BigIntegerField()
    is_road_transport = models.IntegerField()
    is_rail_transport = models.IntegerField()
    location_id = models.BigIntegerField()
    comp_type = models.CharField()
    exptr_type = models.CharField()
    kyc_details_present = models.CharField()
    doc_status = models.CharField()
    sales_person_id = models.BigIntegerField()
    is_affiliate = models.IntegerField()
    aff_company_id = models.BigIntegerField()
    denied_party_status = models.CharField()
    denied_party_checked_on = models.CharField()
    sales_person_user_id = models.BigIntegerField()
    global_org_id = models.BigIntegerField()
    global_org = models.CharField()
    pay_method = models.CharField()
    org_edi_code = models.CharField()
    exptr_status = models.CharField()
    leid = models.CharField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Branch(models.Model):
    org_id = models.ForeignKey(Master, on_delete=models.CASCADE)
    name = models.CharField()
    code = models.CharField()
    sr_no = models.IntegerField()
    address = models.CharField()
    city = models.CharField()
    postal_code = models.IntegerField()
    country = models.CharField()
    telephone_no = models.CharField()
    fax_no = models.IntegerField()
    email = models.EmailField()
    is_default = models.BigIntegerField()
    default_seaport_id = models.IntegerField()
    default_airport_id = models.IntegerField()
    web_url = models.CharField()
    branch_add_1 = models.CharField()
    branch_add_2 = models.CharField()
    branch_add_3 = models.CharField()
    city_id = models.IntegerField()
    state = models.CharField()
    bank_add = models.CharField()
    bank_acc_no = models.IntegerField()
    dealer_code = models.IntegerField()
    is_active = models.BigIntegerField()
    amshpr_air = models.CharField()
    amshpr_sea = models.CharField()
    amcnee_air = models.CharField()
    amcnee_sea = models.CharField()
    sales_person = models.IntegerField()
    collection_exec = models.CharField()
    state_code = models.IntegerField()
    taxable_type = models.CharField()
    aeo_code = models.CharField()
    aeo_country = models.CharField()
    aeo_role = models.CharField()
    branch_edi_code = models.CharField()
    org_marks_nos = models.CharField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Reg_Types(models.Model):
    company_id = models.ForeignKey(Master, on_delete=models.CASCADE)
    reg_name = models.CharField()
    type = models.CharField()
    size = models.CharField()
    country_id = models.CharField()
    is_mandatory = models.BigIntegerField()
    sys_defined = models.BigIntegerField()
    check_duplicate = models.BigIntegerField()
    org_entity_type = models.CharField()
    is_global = models.BigIntegerField()
    comp_settings = models.BigIntegerField()
    data_format = models.CharField()
    allow_special_characters = models.BigIntegerField()
    allow_unregistered = models.BigIntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class RegNo_Details(models.Model):
    org_id = models.ForeignKey(Master, on_delete=models.CASCADE)
    reg_type_id = models.ForeignKey(Reg_Types, on_delete=models.CASCADE)
    reg_date = models.DateField(auto_now_add=True)
    valid_upto = models.DateField()
    branch_id = models.DateField()
    is_unregistered = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
