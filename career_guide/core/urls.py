
from django.urls import path
from . import views
from .views import profile_view, update_profile_view, timeout_view, login_view, chat_view, send_message, \
    reply_to_message, Bsc_com_result, view_aptitude_results

urlpatterns = [
    path('', views.login_view, name='login'),  # Root URL shows login page
    path('register/', views.register, name='register'),
    path('accounts/login/', login_view, name='login'),  # Login URL
    path('index/', views.index, name='index'),  # Home page URL
    path('logout/', views.logout_view, name='logout'),  # Logout URL
    path('profile/', profile_view, name='profile'),
    path('update_profile/', update_profile_view, name='update_profile'),
    path('learn_more/', views.learn_more, name='learn_more'),
    path('contact/', views.contact_view, name='contact'),
    path('feedback/', views.feedback_view, name='feedback'),
    path('after_10/', views.after_10_view, name='after_10'),
    path('after_12/', views.after_12_view, name='after_12'),
    path('bio_science/',views.bio_science_view, name='bio_science'),
    path('aptitude_test/', views.aptitude_test, name='aptitude_test'),
    path('result/', views.result, name='result'),  # Add this line to define the result page
    path('submit-test/', views.submit_test, name='submit_test'),
    path('timeout/', timeout_view, name='timeout_page'),  # Add this line

    path('commerce/', views.commerce_view, name='commerce'),
    path('aptitude_commerce/', views.aptitude_commerce, name='aptitude_commerce'),
    path('commerce_result/', views.result, name='commerce_result'),  # Add this line to define the result page
    path('submit_commerce/', views.submit_commerce, name='submit_commerce'),
    path('chat/', chat_view, name='chat_view'),
    path('chat/send_message/', send_message, name='send_message'),
    path('chat/reply/<int:message_id>/', reply_to_message, name='reply_to_message'),  # Add this line
#-----------------------------------------------------------------------------------------------

    path('humanities/', views.hum_view, name='humanities'),
    path('aptitude_hum/', views.aptitude_hum, name='aptitude_hum'),
    path('hum_result/', views.hum_result, name='hum_result'),  # Add this line to define the result page
    path('submit-hum/', views.submit_hum, name='submit_hum'),
#----------------------------------------------------------------------------------------------------------------
    path('computer/', views.computer_view, name='computer'),
    path('aptitude_computer/', views.aptitude_computer, name='aptitude_computer'),
    path('hum_result/', views.hum_result, name='hum_result'),  # Add this line to define the result page
    path('submit_computer/', views.submit_computer, name='submit_computer'),

    path('statistic/', views.stati_view, name='statistic'),
    path('aptitude_stati/', views.aptitude_stati, name='aptitude_stati'),
    path('stati_result/', views.stati_result, name='stati_result'),  # Add this line to define the result page
    path('submit_stati/', views.submit_stati, name='submit_stati'),

#---------------------------------------------------------------------------------------------------------------
    path('bca/', views.BCA_view, name='bca'),
    path('aptitude_bca/', views.aptitude_BCA, name='aptitude_bca'),
    path('BCA_result/', views.BCA_result, name='result_bca'),  # Add this line to define the result page
    path('submit_BCA/', views.submit_BCA, name='submit_BCA'),

#----------------------------------------------------------------------------------------------

    path('bsc_com/', views.Bsc_com_view, name='bsc_com'),
    path('aptitude_bsccom/', views.aptitude_bsccom, name='aptitude_bsccom'),
    path('Bsc_com_result/', Bsc_com_result, name='Bsc_com_result'),  # Add this line to define the result page
    path('submit_BSC_COM/', views.submit_BSC_COM, name='submit_BSC_COM'),
#----------------------------------------------------------------------------------------------------

    path('bba/', views.bba_view, name='bba'),
    path('aptitude_bba/', views.aptitude_bba, name='aptitude_bba'),
    path('bba_result/', Bsc_com_result, name='bba_result'),  # Add this line to define the result page
    path('submit_bba/', views.submit_bba, name='submit_bba'),

    #---------------------------------------------------------------------
    path('chemistry/', views.chemistry_view, name='chemistry'),
    path('aptitude_chemistry/', views.aptitude_chemistry, name='aptitude_chemistry'),
    path('chemistry_result/', views.chemistry_result, name='chemistry_result'),  # Add this line to define the result page
    path('submit_chemistry/', views.submit_chemistry, name='submit_chemistry'),

    #-----------------------------------------------------------------------
    path('course_job/', views.course_job, name='course_job'),
    path('computer_job/', views.computer_job, name='computer_job'),
    path('commerece_job/', views.commerece_job, name='commerece_job'),
    path('bio_job/', views.bio_job, name='bio_job'),
    path('math_job/', views.math_job, name='math_job'),
    path('phyco_job/', views.phyco_job, name='phyco_job'),
    path('eng_job/', views.eng_job, name='eng_job'),
    path('term/', views.term, name='term'),
    path('privacy/', views.privacy, name='privacy'),

    path('dashboard/', views.admin_dashboard, name='dashboard'),
    path('view_users/', views.admin_view_users, name='view_users'),
    path('view_user_profile/<int:user_id>/', views.view_user_profile, name='view_user_profile'),
    path('edit_user_profile/<int:user_id>/', views.edit_user_profile, name='edit_user_profile'),
    path('delete_user_profile/<int:user_id>/', views.delete_user_profile, name='delete_user_profile'),
    path('view_feedback/', views.view_feedback, name='view_feedback'),
    path('admin_chat/', views.admin_chat_view, name='admin_chat'),
    path('admin_chat/reply/<int:message_id>/', views.admin_reply_to_message, name='admin_reply_to_message'),
    path('view_aptitude_results/', views.view_aptitude_results, name='view_aptitude_results'),
    # Ensure this line is present
]





