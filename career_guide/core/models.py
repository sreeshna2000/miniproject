from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


class Feedback(models.Model):
    email = models.EmailField()
    feedback_text = models.TextField()
    phone_number = models.CharField(max_length=10, blank=True, null=True)  # Optional field for phone number
    admin_reply = models.TextField(blank=True, null=True)  # Admin reply can be null or blank


    def __str__(self):
        return self.email


class BioQuestion(models.Model):
    subject = models.CharField(max_length=100)  # e.g., "Bio Science", "Computer Science"
    question_text = models.CharField(max_length=255)
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    option_c = models.CharField(max_length=100)
    option_d = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=1)  # Store A, B, C, or D

    def __str__(self):
        return self.question_text


class BioScienceCourse(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    subjects = models.TextField()  # Store subjects as a list of strings
    career_opportunities = models.TextField()  # Store career options as a list of strings
    study_tips = models.TextField()  # Store study tips as a list of strings
    future_studies = models.TextField()  # Store future study options as a list of strings

    def __str__(self):
        return self.title


class AptitudeTestBIO(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the User model
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(null=True, blank=True)
    score = models.IntegerField()  # Store the score or number of correct answers
    comments = models.TextField(blank=True, null=True)  # Optional field for any additional comments

    def __str__(self):
        return f"{self.user.username} - Score: {self.score} on {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}"

#--------------------------------------------------------------------------------------


class CommerceQuestion(models.Model):
    subject = models.CharField(max_length=100)  # e.g., "Bio Science", "Computer Science"
    question_text = models.CharField(max_length=255)
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    option_c = models.CharField(max_length=100)
    option_d = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=1)  # Store A, B, C, or D

    def __str__(self):
        return self.question_text

class CommerceCourse(models.Model):
    id = models.AutoField(primary_key=True)  # Custom ID field
    title = models.CharField(max_length=255)
    description = models.TextField()
    subjects = models.TextField()  # Store subjects as a list of strings
    career_opportunities = models.TextField()  # Store career options as a list of strings
    study_tips = models.TextField()  # Store study tips as a list of strings
    future_studies = models.TextField()  # Store future study options as a list of strings

    def __str__(self):
        return self.title


class AptitudeTestCommerce(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the User model
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(null=True, blank=True)
    score = models.IntegerField()  # Store the score or number of correct answers
    comments = models.TextField(blank=True, null=True)  # Optional field for any additional comments

    def __str__(self):
        return f"{self.user.username} - Score: {self.score} on {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}"

#---------------------------------------------------------------------------------------------



class ChatMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender} at {self.timestamp}"

class AdminReply(models.Model):
    message = models.ForeignKey(ChatMessage, on_delete=models.CASCADE, related_name='replies')
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_replies')
    reply = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reply to {self.message.sender.username} by {self.admin.username} at {self.timestamp}"
#-------------------------------------------------------------------------------------------------------

class HumanitiesQuestion(models.Model):
    subject = models.CharField(max_length=100)  # e.g., "Bio Science", "Computer Science"
    question_text = models.CharField(max_length=255)
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    option_c = models.CharField(max_length=100)
    option_d = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=1)  # Store A, B, C, or D

    def __str__(self):
        return self.question_text

class HumanitiesCourse(models.Model):
    id = models.AutoField(primary_key=True)  # Custom ID field
    title = models.CharField(max_length=255)
    description = models.TextField()
    subjects = models.TextField()  # Store subjects as a list of strings
    career_opportunities = models.TextField()  # Store career options as a list of strings
    study_tips = models.TextField()  # Store study tips as a list of strings
    future_studies = models.TextField()  # Store future study options as a list of strings

    def __str__(self):
        return self.title


class AptitudeTestHumanities(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the User model
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(null=True, blank=True)
    score = models.IntegerField()  # Store the score or number of correct answers
    comments = models.TextField(blank=True, null=True)  # Optional field for any additional comments

    def __str__(self):
        return f"{self.user.username} - Score: {self.score} on {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}"

#------------------------------------------------------------------------------------------------------------------

class ComputerQuestion(models.Model):
    subject = models.CharField(max_length=100)  # e.g., "Bio Science", "Computer Science"
    question_text = models.CharField(max_length=255)
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    option_c = models.CharField(max_length=100)
    option_d = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=1)  # Store A, B, C, or D

    def __str__(self):
        return self.question_text

class ComputerCourse(models.Model):
    id = models.AutoField(primary_key=True)  # Custom ID field
    title = models.CharField(max_length=255)
    description = models.TextField()
    subjects = models.TextField()  # Store subjects as a list of strings
    career_opportunities = models.TextField()  # Store career options as a list of strings
    study_tips = models.TextField()  # Store study tips as a list of strings
    future_studies = models.TextField()  # Store future study options as a list of strings

    def __str__(self):
        return self.title


class AptitudeTestComputer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the User model
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(null=True, blank=True)
    score = models.IntegerField()  # Store the score or number of correct answers
    comments = models.TextField(blank=True, null=True)  # Optional field for any additional comments

    def __str__(self):
        return f"{self.user.username} - Score: {self.score} on {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}"

#--------------------------------------------------------------------------------------------------------------

class StatisticQuestion(models.Model):
    subject = models.CharField(max_length=100)  # e.g., "Bio Science", "Computer Science"
    question_text = models.CharField(max_length=255)
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    option_c = models.CharField(max_length=100)
    option_d = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=1)  # Store A, B, C, or D

    def __str__(self):
        return self.question_text

class StatisticCourse(models.Model):
    id = models.AutoField(primary_key=True)  # Custom ID field
    title = models.CharField(max_length=255)
    description = models.TextField()
    subjects = models.TextField()  # Store subjects as a list of strings
    career_opportunities = models.TextField()  # Store career options as a list of strings
    study_tips = models.TextField()  # Store study tips as a list of strings
    future_studies = models.TextField()  # Store future study options as a list of strings

    def __str__(self):
        return self.title


class AptitudeTestStatistics(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the User model
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(null=True, blank=True)
    score = models.IntegerField()  # Store the score or number of correct answers
    comments = models.TextField(blank=True, null=True)  # Optional field for any additional comments

    def __str__(self):
        return f"{self.user.username} - Score: {self.score} on {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}"


#----------------------------------------------------------------------------------------------------------------

class BCAQuestion(models.Model):
    subject = models.CharField(max_length=100)  # e.g., "Bio Science", "Computer Science"
    question_text = models.CharField(max_length=255)
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    option_c = models.CharField(max_length=100)
    option_d = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=1)  # Store A, B, C, or D

    def __str__(self):
        return self.question_text


class BCACourse(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    subjects = models.TextField()  # Store subjects as a list of strings
    career_opportunities = models.TextField()  # Store career options as a list of strings
    study_tips = models.TextField()  # Store study tips as a list of strings
    future_studies = models.TextField()  # Store future study options as a list of strings

    def __str__(self):
        return self.title


class AptitudeTestBCA(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the User model
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(null=True, blank=True)
    score = models.IntegerField()  # Store the score or number of correct answers
    comments = models.TextField(blank=True, null=True)  # Optional field for any additional comments

    def __str__(self):
        return f"{self.user.username} - Score: {self.score} on {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}"

#----------------------------------------------------------------------------------------------------------------

class BSCCOMQuestion(models.Model):
    subject = models.CharField(max_length=100)  # e.g., "Bio Science", "Computer Science"
    question_text = models.CharField(max_length=255)
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    option_c = models.CharField(max_length=100)
    option_d = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=1)  # Store A, B, C, or D

    def __str__(self):
        return self.question_text


class BSCCOMCourse(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    subjects = models.TextField()  # Store subjects as a list of strings
    career_opportunities = models.TextField()  # Store career options as a list of strings
    study_tips = models.TextField()  # Store study tips as a list of strings
    future_studies = models.TextField()  # Store future study options as a list of strings

    def __str__(self):
        return self.title


class AptitudeTestBSCCOM(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the User model
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(null=True, blank=True)
    score = models.IntegerField()  # Store the score or number of correct answers
    comments = models.TextField(blank=True, null=True)  # Optional field for any additional comments

    def __str__(self):
        return f"{self.user.username} - Score: {self.score} on {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}"
#---------------------------------------------------------------------------------------------------------------------
class BBAQuestion(models.Model):
    subject = models.CharField(max_length=100)  # e.g., "Bio Science", "Computer Science"
    question_text = models.CharField(max_length=255)
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    option_c = models.CharField(max_length=100)
    option_d = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=1)  # Store A, B, C, or D

    def __str__(self):
        return self.question_text


class BBACourse(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    subjects = models.TextField()  # Store subjects as a list of strings
    career_opportunities = models.TextField()  # Store career options as a list of strings
    study_tips = models.TextField()  # Store study tips as a list of strings
    future_studies = models.TextField()  # Store future study options as a list of strings

    def __str__(self):
        return self.title


class AptitudeTestBBA(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the User model
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(null=True, blank=True)
    score = models.IntegerField()  # Store the score or number of correct answers
    comments = models.TextField(blank=True, null=True)  # Optional field for any additional comments

    def __str__(self):
        return f"{self.user.username} - Score: {self.score} on {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}"


#------------------------------------------------------------------------------------------------------------------

class CHEMISTRYQuestion(models.Model):
    subject = models.CharField(max_length=100)  # e.g., "Bio Science", "Computer Science"
    question_text = models.CharField(max_length=255)
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    option_c = models.CharField(max_length=100)
    option_d = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=1)  # Store A, B, C, or D

    def __str__(self):
        return self.question_text


class CHEMISTRYCourse(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    subjects = models.TextField()  # Store subjects as a list of strings
    career_opportunities = models.TextField()  # Store career options as a list of strings
    study_tips = models.TextField()  # Store study tips as a list of strings
    future_studies = models.TextField()  # Store future study options as a list of strings

    def __str__(self):
        return self.title


class AptitudeTestCHEMISTRY(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the User model
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(null=True, blank=True)
    score = models.IntegerField()  # Store the score or number of correct answers
    comments = models.TextField(blank=True, null=True)  # Optional field for any additional comments

    def __str__(self):
        return f"{self.user.username} - Score: {self.score} on {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}"

#-----------------------------------------------------------------------------------------------------------------

