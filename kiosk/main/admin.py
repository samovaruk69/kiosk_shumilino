from django.contrib import admin
from .models import price, timelimitsforappeal, RightsAndObligations,\
    ProceduresOneWindow, WorkAndMeeting, Leadership_Polotsk, Leadership_Vitebsk,\
    Leadership_Beltop, Leadership_Minenergo, Videos, Statements_for_writing_off_penalties, Liquefied_Petroleum_Gas_Supply_Statement,\
    Application_for_the_reconstruction_of_the_gas_supply_system, Large_family_statement, Application_for_registration_of_a_discount_on_payment_for_consumed_gas,\
    Extension_Statement, Statement_for_the_reconstruction_of_the_gas_supply_system, Recalculation_statement,\
    Statement_on_the_consolidation_of_personal_accounts, Gas_startup_application, Application_for_issuance_of_a_certificate_of_payments_for_consumed_natural_gas,\
    Application_for_payment, Excavation_permit_application, Sidebar_application, Application_for_TU, Application_for_liquidation_of_the_registered_IBU,\
    Application_for_cylinder_acceptance, Application_for_financing_construction_and_installation_works, Application_for_funding_design_and_survey_work,\
    Absence_notice, Command, Order, Law, Directive, Ruling, Decree, Other, Services, Leadership_Shumilino, gas_potreb, prikaz,Gazification,Stroy_gaz,Stroy_vvod,Your_save,Metan
# Register your models here.

admin.site.register(price)
admin.site.register(timelimitsforappeal)
admin.site.register(RightsAndObligations)
admin.site.register(ProceduresOneWindow)
admin.site.register(WorkAndMeeting)
admin.site.register(Leadership_Shumilino)
admin.site.register(Leadership_Polotsk)
admin.site.register(Leadership_Vitebsk)
admin.site.register(Leadership_Beltop)
admin.site.register(Leadership_Minenergo)
admin.site.register(Videos)


admin.site.register(Statements_for_writing_off_penalties)
admin.site.register(Liquefied_Petroleum_Gas_Supply_Statement)
admin.site.register(Application_for_the_reconstruction_of_the_gas_supply_system)
admin.site.register(Large_family_statement)
admin.site.register(Application_for_registration_of_a_discount_on_payment_for_consumed_gas)
admin.site.register(Extension_Statement)
admin.site.register(Statement_for_the_reconstruction_of_the_gas_supply_system)
admin.site.register(Recalculation_statement)
admin.site.register(Statement_on_the_consolidation_of_personal_accounts)
admin.site.register(Gas_startup_application)
admin.site.register(Application_for_issuance_of_a_certificate_of_payments_for_consumed_natural_gas)
admin.site.register(Application_for_payment)
admin.site.register(Excavation_permit_application)
admin.site.register(Sidebar_application)
admin.site.register(Application_for_TU)
admin.site.register(Application_for_liquidation_of_the_registered_IBU)
admin.site.register(Application_for_cylinder_acceptance)
admin.site.register(Application_for_financing_construction_and_installation_works)
admin.site.register(Application_for_funding_design_and_survey_work)
admin.site.register(Absence_notice)


admin.site.register(Command)
admin.site.register(Order)
admin.site.register(Law)
admin.site.register(Directive)
admin.site.register(Ruling)
admin.site.register(Decree)
admin.site.register(Other)
admin.site.register(Services)

admin.site.register(gas_potreb)
admin.site.register(prikaz)

admin.site.register(Gazification)
admin.site.register(Stroy_gaz)
admin.site.register(Stroy_vvod)
admin.site.register(Your_save)
admin.site.register(Metan)

