from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='home'),
    path('price/', views.price_home, name='price'),
    path('Videos/', views.Videos_home, name='Videos'),
    path('onewindow/', views.onewindow, name='onewindow'),
    path('onewindow/belarusbank/', views.belarusbank, name='belarusbank'),
    path('onewindow/timelimitsforappeal/', views.timelimitsforappeal_home, name='timelimitsforappeal'),
    path('onewindow/claimbook/', views.claimbook, name='claimbook'),
    path('onewindow/RightsAndObligations/', views.RightsAndObligations_home, name='RightsAndObligations'),
    path('onewindow/ProceduresOneWindow/', views.ProceduresOneWindow_home, name='ProceduresOneWindow'),
    path('onewindow/WorkAndMeeting/', views.WorkAndMeeting_home, name='WorkAndMeeting'),
    path('onewindow/Leadership/', views.Leadership, name='Leadership'),
    path('onewindow/Leadership_Shumilino', views.Leadership_Shumilino_home, name='Leadership_Shumilino'),
    path('onewindow/Leadership_Polotsk', views.Leadership_Polotsk_home, name='Leadership_Polotsk'),
    path('onewindow/Leadership_Vitebsk', views.Leadership_Vitebsk_home, name='Leadership_Vitebsk'),
    path('onewindow/Leadership_Beltop', views.Leadership_Beltop_home, name='Leadership_Beltop'),
    path('onewindow/Leadership_Minenergo', views.Leadership_Minenergo_home, name='Leadership_Minenergo'),
    path('bot/', views.bot, name='bot'),
    path('Services/', views.Services_home, name='Services'),

    path('onewindow/Forms', views.Forms, name='Forms'),
    path('onewindow/Forms/Statements_for_writing_off_penalties', views.Statements_for_writing_off_penalties_home, name='Statements_for_writing_off_penalties'),
    path('onewindow/Forms/Liquefied_Petroleum_Gas_Supply_Statement', views.Liquefied_Petroleum_Gas_Supply_Statement_home, name='Liquefied_Petroleum_Gas_Supply_Statement'),
    path('onewindow/Forms/Application_for_the_reconstruction_of_the_gas_supply_system', views.Application_for_the_reconstruction_of_the_gas_supply_system_home, name='Application_for_the_reconstruction_of_the_gas_supply_system'),
    path('onewindow/Forms/Large_family_statement', views.Large_family_statement_home, name='Large_family_statement'),
    path('onewindow/Forms/Application_for_registration_of_a_discount_on_payment_for_consumed_gas', views.Application_for_registration_of_a_discount_on_payment_for_consumed_gas_home, name='Application_for_registration_of_a_discount_on_payment_for_consumed_gas'),
    path('onewindow/Forms/Extension_Statement', views.Extension_Statement_home, name='Extension_Statement'),
    path('onewindow/Forms/Statement_for_the_reconstruction_of_the_gas_supply_system', views.Statement_for_the_reconstruction_of_the_gas_supply_system_home, name='Statement_for_the_reconstruction_of_the_gas_supply_system'),
    path('onewindow/Forms/Recalculation_statement', views.Recalculation_statement_home, name='Recalculation_statement'),
    path('onewindow/Forms/Statement_on_the_consolidation_of_personal_accounts', views.Statement_on_the_consolidation_of_personal_accounts_home, name='Statement_on_the_consolidation_of_personal_accounts'),
    path('onewindow/Forms/Gas_startup_application', views.Gas_startup_application_home, name='Gas_startup_application'),
    path('onewindow/Forms/Application_for_issuance_of_a_certificate_of_payments_for_consumed_natural_gas', views.Application_for_issuance_of_a_certificate_of_payments_for_consumed_natural_gas_home, name='Application_for_issuance_of_a_certificate_of_payments_for_consumed_natural_gas'),
    path('onewindow/Forms/Application_for_payment', views.Application_for_payment_home, name='Application_for_payment'),
    path('onewindow/Forms/Excavation_permit_application', views.Excavation_permit_application_home, name='Excavation_permit_application'),
    path('onewindow/Forms/Sidebar_application', views.Sidebar_application_home, name='Sidebar_application'),
    path('onewindow/Forms/Application_for_TU', views.Application_for_TU_home, name='Application_for_TU'),
    path('onewindow/Forms/Application_for_liquidation_of_the_registered_IBU', views.Application_for_liquidation_of_the_registered_IBU_home, name='Application_for_liquidation_of_the_registered_IBU'),
    path('onewindow/Forms/Application_for_cylinder_acceptance', views.Application_for_cylinder_acceptance_home, name='Application_for_cylinder_acceptance'),
    path('onewindow/Forms/Application_for_financing_construction_and_installation_works', views.Application_for_financing_construction_and_installation_works_home, name='Application_for_financing_construction_and_installation_works'),
    path('onewindow/Forms/Application_for_funding_design_and_survey_work', views.Application_for_funding_design_and_survey_work_home, name='Application_for_funding_design_and_survey_work'),
    path('onewindow/Forms/Absence_notice', views.Absence_notice_home, name='Absence_notice'),

    path('onewindow/list_of_normative_documents', views.list_of_normative_documents, name='list_of_normative_documents'),
    path('onewindow/list_of_normative_documents/Command', views.Command_home, name='Command'),
    path('onewindow/list_of_normative_documents/Order', views.Order_home, name='Order'),
    path('onewindow/list_of_normative_documents/Law', views.Law_home, name='Law'),
    path('onewindow/list_of_normative_documents/Directive', views.Directive_home, name='Directive'),
    path('onewindow/list_of_normative_documents/Ruling', views.Ruling_home, name='Ruling'),
    path('onewindow/list_of_normative_documents/Decree', views.Decree_home, name='Decree'),
    path('onewindow/list_of_normative_documents/Other', views.Other_home, name='Other'),
    path('onewindow/list_of_normative_documents/prikaz', views.prikaz_home, name='prikaz'),

    path('onewindow/gas_potreb', views.gas_potreb_home, name='gas_potreb'),

    path('onewindow/gas_potreb/Gazification', views.Gazification_home, name='Gazification'),
    path('onewindow/gas_potreb/Stroy_gaz', views.Stroy_gaz_home, name='Stroy_gaz'),
    path('onewindow/gas_potreb/Stroy_vvod', views.Stroy_vvod_home, name='Stroy_vvod'),
    path('onewindow/gas_potreb/Your_save', views.Your_save_home, name='Your_save'),
    path('onewindow/gas_potreb/Metan', views.Metan_home, name='Metan'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)