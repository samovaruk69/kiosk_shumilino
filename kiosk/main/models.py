from django.db import models

# Create your models here.

class price(models.Model):
    title = models.CharField(max_length=150)
    price_doc = models.FileField(upload_to='price/')
    times = models.DateField()

    def __str__(self):
        return self.title

class timelimitsforappeal(models.Model):
    title1 = models.CharField(max_length=150)
    timelimitsforappeal_photo = models.ImageField(upload_to='timelimitsforappeal/')
    times1 = models.DateField()

    def __str__(self):
        return self.title1

class RightsAndObligations(models.Model):
    title = models.CharField(max_length=150)
    RightsAndObligations_photo = models.ImageField(upload_to='RightsAndObligations/')
    times = models.DateField()

    def __str__(self):
        return self.title

class ProceduresOneWindow(models.Model):
    title = models.CharField(max_length=150)
    ProceduresOneWindow_doc = models.FileField(upload_to='ProceduresOneWindow/')
    times = models.DateField()

    def __str__(self):
        return self.title

class WorkAndMeeting(models.Model):
    title = models.CharField(max_length=150)
    WorkAndMeeting_photo = models.FileField(upload_to='WorkAndMeeting.html/')
    times = models.DateField()

    def __str__(self):
        return self.title

class Leadership_Shumilino(models.Model):
    title = models.CharField(max_length=150)
    Leadership_Shumilino_photo = models.FileField(upload_to='Leadership_Shumilino/')
    times = models.DateField()

    def __str__(self):
        return self.title


class Leadership_Polotsk(models.Model):
    title = models.CharField(max_length=150)
    Leadership_Polotsk_photo = models.FileField(upload_to='Leadership_Polotsk/')
    times = models.DateField()

    def __str__(self):
        return self.title

class Leadership_Vitebsk(models.Model):
    title = models.CharField(max_length=150)
    Leadership_Vitebsk_photo = models.FileField(upload_to='Leadership_Vitebsk/')
    times = models.DateField()

    def __str__(self):
        return self.title

class Leadership_Beltop(models.Model):
    title = models.CharField(max_length=150)
    Leadership_Beltop_photo = models.FileField(upload_to='Leadership_Beltop/')
    times = models.DateField()

    def __str__(self):
        return self.title

class Leadership_Minenergo(models.Model):
    title = models.CharField(max_length=150)
    Leadership_Minenergo_photo = models.FileField(upload_to='Leadership_Minenergo/')
    times = models.DateField()

    def __str__(self):
        return self.title

class Videos(models.Model):
    title = models.CharField(max_length=150)
    Videos_video = models.FileField(upload_to='Videos/')
    times = models.DateField()

    def __str__(self):
        return self.title



class Statements_for_writing_off_penalties(models.Model):
    title = models.CharField(max_length=150)
    Statements_for_writing_off_penalties_doc = models.FileField(upload_to='Forms/')
    times = models.DateField()

    def __str__(self):
        return self.title

class Liquefied_Petroleum_Gas_Supply_Statement(models.Model):
    title = models.CharField(max_length=150)
    Liquefied_Petroleum_Gas_Supply_Statement_doc = models.FileField(upload_to='Forms/')
    times = models.DateField()

    def __str__(self):
        return self.title

class Application_for_the_reconstruction_of_the_gas_supply_system(models.Model):
    title = models.CharField(max_length=150)
    Application_for_the_reconstruction_of_the_gas_supply_system_doc = models.FileField(upload_to='Forms/')
    times = models.DateField()

    def __str__(self):
        return self.title

class Large_family_statement(models.Model):
    title = models.CharField(max_length=150)
    Large_family_statement_doc = models.FileField(upload_to='Forms/')
    times = models.DateField()

    def __str__(self):
        return self.title

class Application_for_registration_of_a_discount_on_payment_for_consumed_gas(models.Model):
    title = models.CharField(max_length=150)
    Application_for_registration_of_a_discount_on_payment_for_consumed_gas_doc = models.FileField(upload_to='Forms/')
    times = models.DateField()

    def __str__(self):
        return self.title

class Extension_Statement(models.Model):
    title = models.CharField(max_length=150)
    Extension_Statement_doc = models.FileField(upload_to='Forms/')
    times = models.DateField()

    def __str__(self):
        return self.title

class Statement_for_the_reconstruction_of_the_gas_supply_system(models.Model):
    title = models.CharField(max_length=150)
    Statement_for_the_reconstruction_of_the_gas_supply_system_doc = models.FileField(upload_to='Forms/')
    times = models.DateField()

    def __str__(self):
        return self.title

class Recalculation_statement(models.Model):
    title = models.CharField(max_length=150)
    Recalculation_statement_doc = models.FileField(upload_to='Forms/')
    times = models.DateField()

    def __str__(self):
        return self.title

class Statement_on_the_consolidation_of_personal_accounts(models.Model):
    title = models.CharField(max_length=150)
    Statement_on_the_consolidation_of_personal_accounts_doc = models.FileField(upload_to='Forms/')
    times = models.DateField()

    def __str__(self):
        return self.title

class Gas_startup_application(models.Model):
    title = models.CharField(max_length=150)
    Gas_startup_application_doc = models.FileField(upload_to='Forms/')
    times = models.DateField()

    def __str__(self):
        return self.title

class Application_for_issuance_of_a_certificate_of_payments_for_consumed_natural_gas(models.Model):
    title = models.CharField(max_length=150)
    Application_for_issuance_of_a_certificate_of_payments_for_consumed_natural_gas_doc = models.FileField(upload_to='Forms/')
    times = models.DateField()

    def __str__(self):
        return self.title

class Application_for_payment(models.Model):
    title = models.CharField(max_length=150)
    Application_for_payment_doc = models.FileField(upload_to='Forms/')
    times = models.DateField()

    def __str__(self):
        return self.title

class Excavation_permit_application(models.Model):
    title = models.CharField(max_length=150)
    Excavation_permit_application_doc = models.FileField(upload_to='Forms/')
    times = models.DateField()

    def __str__(self):
        return self.title

class Sidebar_application(models.Model):
    title = models.CharField(max_length=150)
    Sidebar_application_doc = models.FileField(upload_to='Forms/')
    times = models.DateField()

    def __str__(self):
        return self.title

class Application_for_TU(models.Model):
    title = models.CharField(max_length=150)
    Application_for_TU_doc = models.FileField(upload_to='Forms/')
    times = models.DateField()

    def __str__(self):
        return self.title

class Application_for_liquidation_of_the_registered_IBU(models.Model):
    title = models.CharField(max_length=150)
    Application_for_liquidation_of_the_registered_IBU_doc = models.FileField(upload_to='Forms/')
    times = models.DateField()

    def __str__(self):
        return self.title

class Application_for_cylinder_acceptance(models.Model):
    title = models.CharField(max_length=150)
    Application_for_cylinder_acceptance_doc = models.FileField(upload_to='Forms/')
    times = models.DateField()

    def __str__(self):
        return self.title

class Application_for_financing_construction_and_installation_works(models.Model):
    title = models.CharField(max_length=150)
    Application_for_financing_construction_and_installation_works_doc = models.FileField(upload_to='Forms/')
    times = models.DateField()

    def __str__(self):
        return self.title

class Application_for_funding_design_and_survey_work(models.Model):
    title = models.CharField(max_length=150)
    Application_for_funding_design_and_survey_work_doc = models.FileField(upload_to='Forms/')
    times = models.DateField()

    def __str__(self):
        return self.title

class Absence_notice(models.Model):
    title = models.CharField(max_length=150)
    Absence_notice_doc = models.FileField(upload_to='Forms/')
    times = models.DateField()

    def __str__(self):
        return self.title




class Command(models.Model):
    title = models.CharField(max_length=150)
    Command_doc = models.FileField(upload_to='list_of_normative_documents/')
    times = models.DateField()

    def __str__(self):
        return self.title

class Order(models.Model):
    title = models.CharField(max_length=150)
    Order_doc = models.FileField(upload_to='list_of_normative_documents/')
    times = models.DateField()

    def __str__(self):
        return self.title


class Law(models.Model):
    title = models.CharField(max_length=150)
    Law_doc = models.FileField(upload_to='list_of_normative_documents/')
    times = models.DateField()

    def __str__(self):
        return self.title


class Directive(models.Model):
    title = models.CharField(max_length=150)
    Directive_doc = models.FileField(upload_to='list_of_normative_documents/')
    times = models.DateField()

    def __str__(self):
        return self.title


class Ruling(models.Model):
    title = models.CharField(max_length=150)
    Ruling_doc = models.FileField(upload_to='list_of_normative_documents/')
    times = models.DateField()

    def __str__(self):
        return self.title


class Decree(models.Model):
    title = models.CharField(max_length=150)
    Decree_doc = models.FileField(upload_to='list_of_normative_documents/')
    times = models.DateField()

    def __str__(self):
        return self.title


class Other(models.Model):
    title = models.CharField(max_length=150)
    Other_doc = models.FileField(upload_to='list_of_normative_documents/')
    times = models.DateField()

    def __str__(self):
        return self.title


class Services(models.Model):
    title = models.CharField(max_length=150)
    Services_doc = models.FileField(upload_to='Services/')
    times = models.DateField()

    def __str__(self):
        return self.title

class gas_potreb(models.Model):
    title = models.CharField(max_length=150)
    gas_potreb_doc = models.FileField(upload_to='gas_potreb/')
    times = models.DateField()

    def __str__(self):
        return self.title


class prikaz(models.Model):
    title = models.CharField(max_length=150)
    prikaz_doc = models.FileField(upload_to='prikaz/')
    times = models.DateField()

    def __str__(self):
        return self.title