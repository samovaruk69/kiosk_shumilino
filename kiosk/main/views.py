from django.shortcuts import render
from .models import price, timelimitsforappeal, RightsAndObligations,\
    ProceduresOneWindow, WorkAndMeeting, Leadership_Polotsk, Leadership_Vitebsk,\
    Leadership_Beltop, Leadership_Minenergo, Videos, Statements_for_writing_off_penalties, Liquefied_Petroleum_Gas_Supply_Statement,\
    Application_for_the_reconstruction_of_the_gas_supply_system, Large_family_statement, Application_for_registration_of_a_discount_on_payment_for_consumed_gas,\
    Extension_Statement, Statement_for_the_reconstruction_of_the_gas_supply_system, Recalculation_statement,\
    Statement_on_the_consolidation_of_personal_accounts, Gas_startup_application, Application_for_issuance_of_a_certificate_of_payments_for_consumed_natural_gas,\
    Application_for_payment, Excavation_permit_application, Sidebar_application, Application_for_TU, Application_for_liquidation_of_the_registered_IBU,\
    Application_for_cylinder_acceptance, Application_for_financing_construction_and_installation_works, Application_for_funding_design_and_survey_work,\
    Absence_notice, Command, Order, Law, Directive, Ruling, Decree, Other, Services, Leadership_Shumilino, gas_potreb, prikaz,Gazification,Stroy_gaz,Stroy_vvod,Your_save,Metan
# Create your views here.


def index(request):
    return render(request,'main/index.html')


def price_home(request):
    data = price.objects.all()
    return render(request,'main/price.html', {'data': data})

def onewindow(request):
    return render(request,'main/Onewindow.html')

def belarusbank(request):
    return render(request,'main/onewindow/belarusbank.html')

def timelimitsforappeal_home(request):
    data1 = timelimitsforappeal.objects.all()
    return render(request,'main/onewindow/timelimitsforappeal.html', {'data1': data1})

def claimbook(request):
    return render(request,'main/onewindow/claimbook.html')

def RightsAndObligations_home(request):
    data = RightsAndObligations.objects.all()
    return render(request,'main/onewindow/RightsAndObligations.html', {'data': data})

def ProceduresOneWindow_home(request):
    data = ProceduresOneWindow.objects.all()
    return render(request,'main/onewindow/ProceduresOneWindow.html', {'data': data})

def WorkAndMeeting_home(request):
    data = WorkAndMeeting.objects.all()
    return render(request,'main/onewindow/WorkAndMeeting.html', {'data': data})

def bot(request):
    return render(request, 'chatbot-master/index.html')

def Leadership(request):
    return render(request,'main/onewindow/Leadership.html')


def Leadership_Shumilino_home(request):
    data = Leadership_Shumilino.objects.all()
    return render(request,'main/onewindow/Leadership_Shumilino.html', {'data': data})

def Leadership_Polotsk_home(request):
    data = Leadership_Polotsk.objects.all()
    return render(request,'main/onewindow/Leadership_polotsk.html', {'data': data})

def Leadership_Vitebsk_home(request):
    data = Leadership_Vitebsk.objects.all()
    return render(request,'main/onewindow/Leadership_Vitebsk.html', {'data': data})

def Leadership_Beltop_home(request):
    data = Leadership_Beltop.objects.all()
    return render(request,'main/onewindow/Leadership_Beltop.html', {'data': data})

def Leadership_Minenergo_home(request):
    data = Leadership_Minenergo.objects.all()
    return render(request,'main/onewindow/Leadership_Minenergo.html', {'data': data})

def Videos_home(request):
    data = Videos.objects.all()
    return render(request,'main/Videos.html', {'data': data})



def Forms(request):
    return render(request,'main/onewindow/Forms.html')

def Statements_for_writing_off_penalties_home(request):
    data = Statements_for_writing_off_penalties.objects.all()
    return render(request,'main/statements/Statements_for_writing_off_penalties.html', {'data': data})

def Liquefied_Petroleum_Gas_Supply_Statement_home(request):
    data = Liquefied_Petroleum_Gas_Supply_Statement.objects.all()
    return render(request,'main/statements/Liquefied_Petroleum_Gas_Supply_Statement.html', {'data': data})

def Application_for_the_reconstruction_of_the_gas_supply_system_home(request):
    data = Application_for_the_reconstruction_of_the_gas_supply_system.objects.all()
    return render(request,'main/statements/Application_for_the_reconstruction_of_the_gas_supply_system.html', {'data': data})

def Large_family_statement_home(request):
    data = Large_family_statement.objects.all()
    return render(request,'main/statements/Large_family_statement.html', {'data': data})

def Application_for_registration_of_a_discount_on_payment_for_consumed_gas_home(request):
    data = Application_for_registration_of_a_discount_on_payment_for_consumed_gas.objects.all()
    return render(request,'main/statements/Application_for_registration_of_a_discount_on_payment_for_consumed_gas.html', {'data': data})

def Extension_Statement_home(request):
    data = Extension_Statement.objects.all()
    return render(request,'main/statements/Extension_Statement.html', {'data': data})

def Statement_for_the_reconstruction_of_the_gas_supply_system_home(request):
    data = Statement_for_the_reconstruction_of_the_gas_supply_system.objects.all()
    return render(request,'main/statements/Statement_for_the_reconstruction_of_the_gas_supply_system.html', {'data': data})

def Recalculation_statement_home(request):
    data = Recalculation_statement.objects.all()
    return render(request,'main/statements/Recalculation_statement.html', {'data': data})

def Statement_on_the_consolidation_of_personal_accounts_home(request):
    data = Statement_on_the_consolidation_of_personal_accounts.objects.all()
    return render(request,'main/statements/Statement_on_the_consolidation_of_personal_accounts.html', {'data': data})

def Gas_startup_application_home(request):
    data = Gas_startup_application.objects.all()
    return render(request,'main/statements/Gas_startup_application.html', {'data': data})

def Application_for_issuance_of_a_certificate_of_payments_for_consumed_natural_gas_home(request):
    data = Application_for_issuance_of_a_certificate_of_payments_for_consumed_natural_gas.objects.all()
    return render(request,'main/statements/Application_for_issuance_of_a_certificate_of_payments_for_consumed_natural_gas.html', {'data': data})

def Application_for_payment_home(request):
    data = Application_for_payment.objects.all()
    return render(request,'main/statements/Application_for_payment.html', {'data': data})

def Excavation_permit_application_home(request):
    data = Excavation_permit_application.objects.all()
    return render(request,'main/statements/Excavation_permit_application.html', {'data': data})

def Sidebar_application_home(request):
    data = Sidebar_application.objects.all()
    return render(request,'main/statements/Sidebar_application.html', {'data': data})

def Application_for_TU_home(request):
    data = Application_for_TU.objects.all()
    return render(request,'main/statements/Application_for_TU.html', {'data': data})

def Application_for_liquidation_of_the_registered_IBU_home(request):
    data = Application_for_liquidation_of_the_registered_IBU.objects.all()
    return render(request,'main/statements/Application_for_liquidation_of_the_registered_IBU.html', {'data': data})

def Application_for_cylinder_acceptance_home(request):
    data = Application_for_cylinder_acceptance.objects.all()
    return render(request,'main/statements/Application_for_cylinder_acceptance.html', {'data': data})

def Application_for_financing_construction_and_installation_works_home(request):
    data = Application_for_financing_construction_and_installation_works.objects.all()
    return render(request,'main/statements/Application_for_financing_construction_and_installation_works.html', {'data': data})

def Application_for_funding_design_and_survey_work_home(request):
    data = Application_for_funding_design_and_survey_work.objects.all()
    return render(request,'main/statements/Application_for_funding_design_and_survey_work.html', {'data': data})

def Absence_notice_home(request):
    data = Absence_notice.objects.all()
    return render(request,'main/statements/Absence_notice.html', {'data': data})

def list_of_normative_documents(request):
    return render(request,'main/onewindow/list_of_normative_documents.html')

def Command_home(request):
    data = Command.objects.all()
    return render(request,'main/list_of_normative_documents/Command.html', {'data': data})

def Order_home(request):
    data = Order.objects.all()
    return render(request,'main/list_of_normative_documents/Order.html', {'data': data})

def Law_home(request):
    data = Law.objects.all()
    return render(request,'main/list_of_normative_documents/Law.html', {'data': data})

def Directive_home(request):
    data = Directive.objects.all()
    return render(request,'main/list_of_normative_documents/Directive.html', {'data': data})

def Ruling_home(request):
    data = Ruling.objects.all()
    return render(request,'main/list_of_normative_documents/Ruling.html', {'data': data})

def Decree_home(request):
    data = Decree.objects.all()
    return render(request,'main/list_of_normative_documents/Decree.html', {'data': data})

def Other_home(request):
    data = Other.objects.all()
    return render(request,'main/list_of_normative_documents/Other.html', {'data': data})


def Services_home(request):
    data = Services.objects.all()
    return render(request,'main/Services.html', {'data': data})

def gas_potreb_home(request):
    data = gas_potreb.objects.all()
    return render(request,'main/onewindow/gas_potreb.html', {'data': data})

def prikaz_home(request):
    data = prikaz.objects.all()
    return render(request,'main/list_of_normative_documents/prikaz.html', {'data': data})


def Gazification_home(request):
    data = Gazification.objects.all()
    return render(request,'main/onewindow/Gazification.html', {'data': data})

def Stroy_gaz_home(request):
    data = Stroy_gaz.objects.all()
    return render(request,'main/onewindow/Stroy_gaz.html', {'data': data})

def Stroy_vvod_home(request):
    data = Stroy_vvod.objects.all()
    return render(request,'main/onewindow/Stroy_vvod.html', {'data': data})

def Your_save_home(request):
    data = Your_save.objects.all()
    return render(request,'main/onewindow/Your_save.html', {'data': data})

def Metan_home(request):
    data = Metan.objects.all()
    return render(request,'main/onewindow/Metan.html', {'data': data})