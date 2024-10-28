from django.contrib import admin
from .models import BioQuestion, BioScienceCourse, UserProfile, AptitudeTestBIO, CommerceQuestion, CommerceCourse, \
    AptitudeTestCommerce, ChatMessage, AdminReply, HumanitiesQuestion, HumanitiesCourse, AptitudeTestHumanities, \
    ComputerQuestion, ComputerCourse, AptitudeTestComputer, StatisticQuestion, StatisticCourse, AptitudeTestStatistics, \
    Feedback, AptitudeTestBSCCOM, BSCCOMQuestion, BSCCOMCourse, BCACourse, BCAQuestion, AptitudeTestBCA, BBAQuestion, \
    BBACourse, AptitudeTestBBA, CHEMISTRYQuestion, CHEMISTRYCourse, AptitudeTestCHEMISTRY

admin.site.register(BioQuestion)

admin.site.register(BioScienceCourse)







admin.site.site_header = 'Career Guidance Admin'

admin.site.site_title = 'Career Guidance Admin'

admin.site.index_title = 'Career Guidance Admin'

# core/admin_panel.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Customize User Admin
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active')  # Add more fields as needed
    search_fields = ('username', 'email')

# Register User model with the customized admin_panel
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# Register UpdateProfile model if needed
class UpdateProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'qualification', 'age', 'location')  # Include fields from UpdateProfile
    search_fields = ('user__username', 'qualification')  # Add searchable fields

admin.site.register(UserProfile, UpdateProfileAdmin)



class AptitudeTestResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'score', 'start_time', 'end_time', 'comments')  # Display relevant fields in the admin_panel
    search_fields = ('user__username', 'comments')
    list_filter = ('score', 'start_time', 'end_time')
    ordering = ('start_time',)


admin.site.register(AptitudeTestBIO, AptitudeTestResultAdmin)

#----------------------------------------------------------------------------
admin.site.register(CommerceQuestion)

admin.site.register(CommerceCourse)

class AptitudeTestResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'score', 'start_time', 'end_time', 'comments')  # Display relevant fields in the admin_panel
    search_fields = ('user__username', 'comments')
    list_filter = ('score', 'start_time', 'end_time')
    ordering = ('start_time',)


admin.site.register(AptitudeTestCommerce, AptitudeTestResultAdmin)

#------------------------------------------------------------------------------------


class AdminReplyInline(admin.TabularInline):
    model = AdminReply
    extra = 0  # Number of empty forms to display for adding new replies

class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'timestamp', 'message')  # Display sender, timestamp, and message
    list_filter = ('sender', 'timestamp')  # Allow filtering by sender and timestamp
    search_fields = ('sender__username', 'message')  # Enable searching by username and message content
    inlines = [AdminReplyInline]  # Show admin replies inline

# Register the admin models
admin.site.register(ChatMessage, ChatMessageAdmin)
#----------------------------------------------------------------------------------------------------


admin.site.register(HumanitiesQuestion)

admin.site.register(HumanitiesCourse)

class AptitudeTestResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'score', 'start_time', 'end_time', 'comments')  # Display relevant fields in the admin_panel
    search_fields = ('user__username', 'comments')
    list_filter = ('score', 'start_time', 'end_time')
    ordering = ('start_time',)


admin.site.register(AptitudeTestHumanities, AptitudeTestResultAdmin)

#------------------------------------------------------------------------------------------------------

admin.site.register(ComputerQuestion)

admin.site.register(ComputerCourse)

class AptitudeTestResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'score', 'start_time', 'end_time', 'comments')  # Display relevant fields in the admin_panel
    search_fields = ('user__username', 'comments')
    list_filter = ('score', 'start_time', 'end_time')
    ordering = ('start_time',)


admin.site.register(AptitudeTestComputer, AptitudeTestResultAdmin)

#---------------------------------------------------------------------------------------

admin.site.register(StatisticQuestion)

admin.site.register(StatisticCourse)

class AptitudeTestResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'score', 'start_time', 'end_time', 'comments')  # Display relevant fields in the admin_panel
    search_fields = ('user__username', 'comments')
    list_filter = ('score', 'start_time', 'end_time')
    ordering = ('start_time',)


admin.site.register(AptitudeTestStatistics, AptitudeTestResultAdmin)
#---------------------------------------------------------------------------------------------------


from django.contrib import admin
from .models import Feedback
from django.core.mail import send_mail
from django.conf import settings

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('email', 'feedback_text', 'phone_number', 'admin_reply')  # Customize this as needed

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)  # Call the base class save method

        # If the admin is providing a reply, send an email
        if obj.admin_reply:
            send_mail(
                subject='Your Feedback Response',
                message=obj.admin_reply,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[obj.email],  # Send to the user's email
            )

admin.site.register(Feedback, FeedbackAdmin)
#------------------------------------------------------------------------------------------------


admin.site.register(BSCCOMQuestion)

admin.site.register(BSCCOMCourse)

class AptitudeTestResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'score', 'start_time', 'end_time', 'comments')  # Display relevant fields in the admin_panel
    search_fields = ('user__username', 'comments')
    list_filter = ('score', 'start_time', 'end_time')
    ordering = ('start_time',)


admin.site.register(AptitudeTestBSCCOM, AptitudeTestResultAdmin)
#-----------------------------------------------------------------------------------
admin.site.register(BCAQuestion)

admin.site.register(BCACourse)

class AptitudeTestResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'score', 'start_time', 'end_time', 'comments')  # Display relevant fields in the admin_panel
    search_fields = ('user__username', 'comments')
    list_filter = ('score', 'start_time', 'end_time')
    ordering = ('start_time',)


admin.site.register(AptitudeTestBCA, AptitudeTestResultAdmin)
#---------------------------------------------------------------------------------
admin.site.register(BBAQuestion)

admin.site.register(BBACourse)

class AptitudeTestResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'score', 'start_time', 'end_time', 'comments')  # Display relevant fields in the admin_panel
    search_fields = ('user__username', 'comments')
    list_filter = ('score', 'start_time', 'end_time')
    ordering = ('start_time',)


admin.site.register(AptitudeTestBBA, AptitudeTestResultAdmin)
#---------------------------------------------------------------------------------

admin.site.register(CHEMISTRYQuestion)

admin.site.register(CHEMISTRYCourse)

class AptitudeTestResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'score', 'start_time', 'end_time', 'comments')  # Display relevant fields in the admin_panel
    search_fields = ('user__username', 'comments')
    list_filter = ('score', 'start_time', 'end_time')
    ordering = ('start_time',)


admin.site.register(AptitudeTestCHEMISTRY, AptitudeTestResultAdmin)