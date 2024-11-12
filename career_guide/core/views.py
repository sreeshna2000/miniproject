
from django.contrib.auth.decorators import login_required, user_passes_test

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse


from .models import UserProfile, Feedback, BioQuestion, BioScienceCourse, \
    AptitudeTestBIO, BioQuestion, CommerceQuestion, AptitudeTestCommerce, CommerceCourse, ChatMessage, AdminReply, \
    HumanitiesCourse, HumanitiesQuestion, AptitudeTestHumanities, ComputerCourse, AptitudeTestComputer, \
    ComputerQuestion, AptitudeTestStatistics, StatisticQuestion, StatisticCourse, BCAQuestion, AptitudeTestBCA, \
    BCACourse, BSCCOMQuestion, AptitudeTestBSCCOM, BSCCOMCourse, BBACourse, AptitudeTestBBA, BBAQuestion, \
    CHEMISTRYQuestion, AptitudeTestCHEMISTRY, CHEMISTRYCourse
from .forms import CustomUserCreationForm
from django.core.mail import send_mail
from django.conf import settings
from .forms import FeedbackForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login



# Registration View
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()  # This ensures the form is always defined

    return render(request, 'core/register.html', {'form': form})

# Login View

def login_view(request):
    # Redirect already authenticated users to the home page
    if request.user.is_authenticated:
        return redirect('index')  # Change 'index' to the home page URL

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')  # Redirect to your home page after successful login
        else:
            messages.error(request, 'Invalid username or password')  # Error message

    return render(request, 'core/login.html')



def index(request):
    return render(request, 'core/index.html')  # Ensure the template path is correct



def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')  # Redirect to login page after logout





def profile_view(request):
    user = request.user

    profile, created = UserProfile.objects.get_or_create(user=user)

    if request.method == 'POST':
        # Update the profile fields from the form data
        profile.qualification = request.POST.get('qualification')
        profile.age = request.POST.get('age')
        profile.location = request.POST.get('location')
        profile.save()
        return redirect('profile')  # Redirect to the same profile page after update

    return render(request, 'core/profile.html', {'profile': profile})

def learn_more(request):
    return render(request, 'core/learn_more.html')


@login_required
def update_profile_view(request):
    user = request.user
    profile, created = UserProfile.objects.get_or_create(user=user)

    if request.method == 'POST':
        # Update User model (username, email)
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.save()

        # Update UserProfile model (qualification, age, location)
        profile.qualification = request.POST.get('qualification')
        profile.age = request.POST.get('age')
        profile.location = request.POST.get('location')
        profile.save()

        return redirect('profile')  # Redirect to the profile page after updating

    return render(request, 'core/update_profile.html', {
        'user': user,
        'profile': profile
    })





def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Process the form data (e.g., send an email)
        send_mail(
            f"Contact Form Submission from {name}",
            f"name: {name}\nMessage: {message}\nPhone: {phone}",
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )
        return render(request, 'core/contact.html', {'success': True})
    return render(request, 'core/contact.html')


def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)  # Save feedback without committing immediately
            feedback.save()  # Now save to the database

            send_mail(
                subject='Thank You for Your Feedback',
                message='We appreciate your feedback and will get back to you shortly.',
                from_email=settings.EMAIL_HOST_USER,  # Ensure EMAIL_HOST_USER is set in settings.py
                recipient_list=[feedback.email],  # Send to the user's email
            )

            return HttpResponse(
                "<script>alert('Feedback submitted successfully!');window.location='/feedback/';</script>"
            )
    else:
        form = FeedbackForm()

    return render(request, 'core/feedback.html', {'form': form})

def after_10_view(request):
    return render(request, 'courses/after_10.html')

def after_12_view(request):
    return render(request, 'courses/after_12.html')





def aptitude_test(request):
    questions = BioQuestion.objects.all()

    request.session['start_time'] = timezone.now().isoformat()

    return render(request, 'bio/aptitude_bio.html', {'questions': questions})




def submit_test(request):
    if request.method == 'POST':
        total_marks = 0
        total_questions = BioQuestion.objects.count()
        correct_answers = 0
        submitted_answers = []

        start_time = timezone.datetime.fromisoformat(request.session.get('start_time'))
        end_time = timezone.now()
        time_taken = end_time - start_time

        minutes, seconds = divmod(time_taken.total_seconds(), 60)
        formatted_time_taken = f"{int(minutes)}m {int(seconds)}s"

        questions = BioQuestion.objects.all()

        for question in questions:
            field_name = f'q{question.id}'
            selected_answer = request.POST.get(field_name)
            submitted_answers.append({
                'question': question,
                'selected_answer': selected_answer,
                'is_correct': selected_answer == question.correct_option
            })
            if selected_answer == question.correct_option:
                correct_answers += 1

        total_marks = correct_answers

        if total_marks == total_questions:
            comments = "Excellent! You've answered all questions correctly. Well done!"
        elif total_marks >= total_questions * 0.75:
            comments = "Great job! You've got most of the answers correct. Keep it up!"
        elif total_marks >= total_questions * 0.5:
            comments = "Good effort! You can improve with a bit more practice."
        else:
            comments = "It seems you need to study a bit more. Don't worry, keep trying!"

        AptitudeTestBIO.objects.create(
            user=request.user,
            start_time=start_time,
            end_time=end_time,  # Set end_time here
            score=total_marks,
            comments='Answers submitted'
        )

        return render(request, 'bio/result.html', {
            'correct_answers': correct_answers,
            'total_marks': total_marks,
            'total_questions': total_questions,
            'submitted_answers': submitted_answers,
            'comments': comments,
            'time_taken': formatted_time_taken
        })

def result(request):
    return render(request, 'bio/result.html')




def bio_science_view(request):
    courses = BioScienceCourse.objects.all()

    for course in courses:
        course.subjects = course.subjects.split(',')
        course.career_opportunities = course.career_opportunities.split(',')
        course.study_tips = course.study_tips.split('.')
        course.future_studies = course.future_studies.split(',')

    return render(request, 'bio/bio_science.html', {'courses': courses})


def timeout_view(request):
    return render(request, 'courses/timeout.html')  # Create a new template for timeout



#---------------------------------------------------------------------------------------------------------------------

def aptitude_commerce(request):
    questions = CommerceQuestion.objects.all()

    return render(request, 'commerce/aptitude_commerce.html', {'questions': questions})


from django.utils import timezone
from datetime import datetime

def submit_commerce(request):
    if request.method == 'POST':
        total_marks = 0
        total_questions = CommerceQuestion.objects.count()
        correct_answers = 0
        submitted_answers = []  # Store submitted answers to pass to template

        start_time_str = request.session.get('start_time')
        if start_time_str:
            try:
                start_time = datetime.fromisoformat(start_time_str)
            except ValueError:
                start_time = timezone.now()  # fallback in case of invalid format
        else:
            start_time = timezone.now()  # fallback if start_time is missing

        end_time = timezone.now()
        time_taken = end_time - start_time

        minutes, seconds = divmod(time_taken.total_seconds(), 60)
        formatted_time_taken = f"{int(minutes)}m {int(seconds)}s"

        questions = CommerceQuestion.objects.all()

        for question in questions:
            field_name = f'q{question.id}'  # Dynamically create field name like 'q1', 'q2', etc.
            selected_answer = request.POST.get(field_name)
            submitted_answers.append({
                'question': question,
                'selected_answer': selected_answer,
                'is_correct': selected_answer == question.correct_option
            })
            if selected_answer == question.correct_option:
                correct_answers += 1

        total_marks = correct_answers  # Each question can be 1 mark
        if total_marks == total_questions:
            comments = "Excellent! You've answered all questions correctly. Well done!"
        elif total_marks >= total_questions * 0.75:
            comments = "Great job! You've got most of the answers correct. Keep it up!"
        elif total_marks >= total_questions * 0.5:
            comments = "Good effort! You can improve with a bit more practice."
        else:
            comments = "It seems you need to study a bit more. Don't worry, keep trying!"

        AptitudeTestCommerce.objects.create(
            user=request.user,
            score=total_marks,
            start_time=start_time,
            end_time=end_time,
            comments=comments  # Save specific feedback as comments
        )

        return render(request, 'commerce/commerce_result.html', {
            'correct_answers': correct_answers,
            'total_marks': total_marks,
            'total_questions': total_questions,
            'submitted_answers': submitted_answers,  # Pass all the details to the template
            'comments': comments,
            'formatted_time_taken': formatted_time_taken
        })

def commerce_result(request):
    return render(request, 'commerce/commerce_result.html')




def commerce_view(request):
    courses = CommerceCourse.objects.all()

    # Process each course's fields to split the text into lists
    for course in courses:
        course.subjects = course.subjects.split(',')
        course.career_opportunities = course.career_opportunities.split(',')
        course.study_tips = course.study_tips.split('.')
        course.future_studies = course.future_studies.split(',')

    return render(request, 'commerce/commerce.html', {'courses': courses})

#------------------------------------------------------------------------------------------------


@login_required
def chat_view(request):
    messages = ChatMessage.objects.filter(sender=request.user).order_by('-timestamp')

    replies = {message.id: message.replies.all() for message in messages}

    return render(request, 'chat/chat.html', {'messages': messages, 'replies': replies})

@login_required
def send_message(request):
    if request.method == 'POST':
        message_text = request.POST.get('message')
        if message_text:
            ChatMessage.objects.create(sender=request.user, message=message_text)
        return redirect('chat_view')

@login_required
def reply_to_message(request, message_id):
    if request.method == 'POST':
        reply_text = request.POST.get('reply')
        message = get_object_or_404(ChatMessage, id=message_id)  # Get the original message
        if reply_text:
            AdminReply.objects.create(message=message, admin=request.user, reply=reply_text)

            print(f"Admin reply created: {AdminReply.reply}")

            try:
                # Send email notification to the user
                send_mail(
                    subject='New Reply to Your Message',
                    message=f'Admin replied to your message: "{message.message}"\n\nReply: "{reply_text}"',
                    from_email=settings.ADMIN_EMAIL,
                    recipient_list=[message.sender.email],
                    fail_silently=False,
                )
                print(f"Email sent to: {message.sender.email}")
            except Exception as e:
                print(f"Error sending email: {e}")
            return redirect('admin_chat_view')

#--------------------------------------------------------------------------------------------------
def aptitude_hum(request):
    questions = HumanitiesQuestion.objects.all()

    return render(request, 'humanities/aptitude_hum.html', {'questions': questions})


def submit_hum(request):
    if request.method == 'POST':
        total_marks = 0
        total_questions = HumanitiesQuestion.objects.count()
        correct_answers = 0
        submitted_answers = []  # Store submitted answers to pass to template

        start_time = timezone.datetime.fromisoformat(request.session.get('start_time'))
        end_time = timezone.now()
        time_taken = end_time - start_time

        minutes, seconds = divmod(time_taken.total_seconds(), 60)
        formatted_time_taken = f"{int(minutes)}m {int(seconds)}s"

        questions = HumanitiesQuestion.objects.all()

        for question in questions:
            field_name = f'q{question.id}'  # Dynamically create field name like 'q1', 'q2', etc.
            selected_answer = request.POST.get(field_name)
            submitted_answers.append({
                'question': question,
                'selected_answer': selected_answer,
                'is_correct': selected_answer == question.correct_option
            })
            if selected_answer == question.correct_option:
                correct_answers += 1

        total_marks = correct_answers  # Each question can be 1 mark
        if total_marks == total_questions:
            comments = "Excellent! You've answered all questions correctly. Well done!"
        elif total_marks >= total_questions * 0.75:
            comments = "Great job! You've got most of the answers correct. Keep it up!"
        elif total_marks >= total_questions * 0.5:
            comments = "Good effort! You can improve with a bit more practice."
        else:
            comments = "It seems you need to study a bit more. Don't worry, keep trying!"

        AptitudeTestHumanities.objects.create(
            user=request.user,
            score=total_marks,
            start_time=start_time,
            end_time=end_time,
            comments='Answers submitted'  # You can modify this to include additional comments if needed
        )

        return render(request, 'humanities/hum_result.html', {
            'correct_answers': correct_answers,
            'total_marks': total_marks,
            'total_questions': total_questions,
            'submitted_answers': submitted_answers,  # Pass all the details to the template
            'comments': comments
        })

def hum_result(request):
    return render(request, 'humanities/hum_result.html')




def hum_view(request):
    courses = HumanitiesCourse.objects.all()

    for course in courses:
        course.subjects = course.subjects.split(',')
        course.career_opportunities = course.career_opportunities.split(',')
        course.study_tips = course.study_tips.split('.')
        course.future_studies = course.future_studies.split(',')

    return render(request, 'humanities/humanities.html', {'courses': courses})
#--------------------------------------------------------------------------------------------------------

def aptitude_computer(request):
    questions = ComputerQuestion.objects.all()

    return render(request, 'computer/aptitude_computer.html', {'questions': questions})


def submit_computer(request):
    if request.method == 'POST':
        total_marks = 0
        total_questions = ComputerQuestion.objects.count()
        correct_answers = 0
        submitted_answers = []  # Store submitted answers to pass to template

        # Retrieve start_time from session, or use current time as fallback
        start_time_str = request.session.get('start_time')
        if start_time_str and isinstance(start_time_str, str):
            start_time = timezone.datetime.fromisoformat(start_time_str)
        else:
            start_time = timezone.now()

        end_time = timezone.now()
        time_taken = end_time - start_time

        minutes, seconds = divmod(time_taken.total_seconds(), 60)
        formatted_time_taken = f"{int(minutes)}m {int(seconds)}s"

        questions = ComputerQuestion.objects.all()

        for question in questions:
            field_name = f'q{question.id}'  # Dynamically create field name like 'q1', 'q2', etc.
            selected_answer = request.POST.get(field_name)
            submitted_answers.append({
                'question': question,
                'selected_answer': selected_answer,
                'is_correct': selected_answer == question.correct_option
            })
            if selected_answer == question.correct_option:
                correct_answers += 1

        total_marks = correct_answers  # Each question can be 1 mark
        if total_marks == total_questions:
            comments = "Excellent! You've answered all questions correctly. Well done!"
        elif total_marks >= total_questions * 0.75:
            comments = "Great job! You've got most of the answers correct. Keep it up!"
        elif total_marks >= total_questions * 0.5:
            comments = "Good effort! You can improve with a bit more practice."
        else:
            comments = "It seems you need to study a bit more. Don't worry, keep trying!"

        AptitudeTestComputer.objects.create(
            user=request.user,
            score=total_marks,
            start_time=start_time,
            end_time=end_time,
            comments=comments  # Save the comments to the database
        )

        return render(request, 'computer/computer_result.html', {
            'correct_answers': correct_answers,
            'total_marks': total_marks,
            'total_questions': total_questions,
            'submitted_answers': submitted_answers,  # Pass all the details to the template
            'comments': comments,
            'formatted_time_taken': formatted_time_taken  # Optional formatted time
        })

def computer_result(request):
    return render(request, 'computer/computer_result.html')




def computer_view(request):
    courses = ComputerCourse.objects.all()

    for course in courses:
        course.subjects = course.subjects.split(',')
        course.career_opportunities = course.career_opportunities.split(',')
        course.study_tips = course.study_tips.split('.')
        course.future_studies = course.future_studies.split(',')

    return render(request, 'computer/computer.html', {'courses': courses})

#----------------------------------------------------------------------------------------------

def aptitude_stati(request):
    questions = StatisticQuestion.objects.all()

    return render(request, 'statistic/aptitude_stati.html', {'questions': questions})


def submit_stati(request):
    if request.method == 'POST':
        total_marks = 0
        total_questions = StatisticQuestion.objects.count()
        correct_answers = 0
        submitted_answers = []

        start_time = timezone.datetime.fromisoformat(request.session.get('start_time'))
        end_time = timezone.now()
        time_taken = end_time - start_time

        minutes, seconds = divmod(time_taken.total_seconds(), 60)
        formatted_time_taken = f"{int(minutes)}m {int(seconds)}s"


        questions = StatisticQuestion.objects.all()

        for question in questions:
            field_name = f'q{question.id}'
            selected_answer = request.POST.get(field_name)
            submitted_answers.append({
                'question': question,
                'selected_answer': selected_answer,
                'is_correct': selected_answer == question.correct_option
            })
            if selected_answer == question.correct_option:
                correct_answers += 1

        total_marks = correct_answers

        if total_marks == total_questions:
            comments = "Excellent! You've answered all questions correctly. Well done!"
        elif total_marks >= total_questions * 0.75:
            comments = "Great job! You've got most of the answers correct. Keep it up!"
        elif total_marks >= total_questions * 0.5:
            comments = "Good effort! You can improve with a bit more practice."
        else:
            comments = "It seems you need to study a bit more. Don't worry, keep trying!"

        AptitudeTestStatistics.objects.create(
            user=request.user,
            start_time=start_time,
            end_time=end_time,  # Set end_time here
            score=total_marks,
            comments='Answers submitted'
        )

        return render(request, 'statistic/stati_result.html', {
            'correct_answers': correct_answers,
            'total_marks': total_marks,
            'total_questions': total_questions,
            'submitted_answers': submitted_answers,
            'comments': comments,
            'time_taken': formatted_time_taken
        })
def stati_result(request):
    return render(request, 'statistic/stati_result.html')




def stati_view(request):
    courses = StatisticCourse.objects.all()

    for course in courses:
        course.subjects = course.subjects.split(',')
        course.career_opportunities = course.career_opportunities.split(',')
        course.study_tips = course.study_tips.split('.')
        course.future_studies = course.future_studies.split(',')

    return render(request, 'statistic/statistics.html', {'courses': courses})
#------------------------------------------------------------------------------------------------
def aptitude_BCA(request):
    questions = BCAQuestion.objects.all()

    request.session['start_time'] = timezone.now().isoformat()

    return render(request, 'after_12/aptitude_bca.html', {'questions': questions})




def submit_BCA(request):
    if request.method == 'POST':
        total_marks = 0
        total_questions = BCAQuestion.objects.count()
        correct_answers = 0
        submitted_answers = []

        start_time = timezone.datetime.fromisoformat(request.session.get('start_time'))
        end_time = timezone.now()
        time_taken = end_time - start_time

        minutes, seconds = divmod(time_taken.total_seconds(), 60)
        formatted_time_taken = f"{int(minutes)}m {int(seconds)}s"

        questions = BCAQuestion.objects.all()

        for question in questions:
            field_name = f'q{question.id}'
            selected_answer = request.POST.get(field_name)
            submitted_answers.append({
                'question': question,
                'selected_answer': selected_answer,
                'is_correct': selected_answer == question.correct_option
            })
            if selected_answer == question.correct_option:
                correct_answers += 1

        total_marks = correct_answers

        if total_marks == total_questions:
            comments = "Excellent! You've answered all questions correctly. Well done!"
        elif total_marks >= total_questions * 0.75:
            comments = "Great job! You've got most of the answers correct. Keep it up!"
        elif total_marks >= total_questions * 0.5:
            comments = "Good effort! You can improve with a bit more practice."
        else:
            comments = "It seems you need to study a bit more. Don't worry, keep trying!"

        AptitudeTestBCA.objects.create(
            user=request.user,
            start_time=start_time,
            end_time=end_time,  # Set end_time here
            score=total_marks,
            comments='Answers submitted'
        )

        return render(request, 'after_12/result_bca.html', {
            'correct_answers': correct_answers,
            'total_marks': total_marks,
            'total_questions': total_questions,
            'submitted_answers': submitted_answers,
            'comments': comments,
            'time_taken': formatted_time_taken
        })

def BCA_result(request):
    return render(request, 'after_12/result_bca.html')




def BCA_view(request):
    courses = BCACourse.objects.all()

    # Process each course's fields to split the text into lists
    for course in courses:
        course.subjects = course.subjects.split(',')
        course.career_opportunities = course.career_opportunities.split(',')
        course.study_tips = course.study_tips.split('.')
        course.future_studies = course.future_studies.split(',')

    return render(request, 'after_12/bca.html', {'courses': courses})


#---------------------------------------------------------------------------------------------------------
def aptitude_bsccom(request):
    questions = BSCCOMQuestion.objects.all()

    request.session['start_time'] = timezone.now().isoformat()

    return render(request, 'after_12/aptitude_bca.html', {'questions': questions})
def submit_BSC_COM(request):
    if request.method == 'POST':
        total_marks = 0
        total_questions = BSCCOMQuestion.objects.count()
        correct_answers = 0
        submitted_answers = []

        # Calculate start_time from session and current time for end_time
        start_time = timezone.datetime.fromisoformat(request.session.get('start_time'))
        end_time = timezone.now()
        time_taken = end_time - start_time

        # Format the time taken into minutes and seconds (optional)
        minutes, seconds = divmod(time_taken.total_seconds(), 60)
        formatted_time_taken = f"{int(minutes)}m {int(seconds)}s"

        questions = BSCCOMQuestion.objects.all()

        for question in questions:
            field_name = f'q{question.id}'
            selected_answer = request.POST.get(field_name)
            submitted_answers.append({
                'question': question,
                'selected_answer': selected_answer,
                'is_correct': selected_answer == question.correct_option
            })
            if selected_answer == question.correct_option:
                correct_answers += 1

        total_marks = correct_answers

        if total_marks == total_questions:
            comments = "Excellent! You've answered all questions correctly. Well done!"
        elif total_marks >= total_questions * 0.75:
            comments = "Great job! You've got most of the answers correct. Keep it up!"
        elif total_marks >= total_questions * 0.5:
            comments = "Good effort! You can improve with a bit more practice."
        else:
            comments = "It seems you need to study a bit more. Don't worry, keep trying!"

        # Create the AptitudeTestBIO object with start_time and end_time
        AptitudeTestBSCCOM.objects.create(
            user=request.user,
            start_time=start_time,
            end_time=end_time,  # Set end_time here
            score=total_marks,
            comments='Answers submitted'
        )

        return render(request, 'after_12/result_bca.html', {
            'correct_answers': correct_answers,
            'total_marks': total_marks,
            'total_questions': total_questions,
            'submitted_answers': submitted_answers,
            'comments': comments,
            'time_taken': formatted_time_taken
        })

def Bsc_com_result(request):
    return render(request, 'after_12/result_bca.html')




def Bsc_com_view(request):
    courses = BSCCOMCourse.objects.all()

    # Process each course's fields to split the text into lists
    for course in courses:
        course.subjects = course.subjects.split(',')
        course.career_opportunities = course.career_opportunities.split(',')
        course.study_tips = course.study_tips.split('.')
        course.future_studies = course.future_studies.split(',')

    return render(request, 'after_12/bca.html', {'courses': courses})
#---------------------------------------------------------------------------------------
def aptitude_bba(request):
    # Fetch all questions from the database
    questions = BBAQuestion.objects.all()

    # Store the start time in the session
    request.session['start_time'] = timezone.now().isoformat()

    # Pass the questions to the template
    return render(request, 'after_12/aptitude_bba.html', {'questions': questions})
def submit_bba(request):
    if request.method == 'POST':
        total_marks = 0
        total_questions = BBAQuestion.objects.count()
        correct_answers = 0
        submitted_answers = []

        # Calculate start_time from session and current time for end_time
        start_time = timezone.datetime.fromisoformat(request.session.get('start_time'))
        end_time = timezone.now()
        time_taken = end_time - start_time

        # Format the time taken into minutes and seconds (optional)
        minutes, seconds = divmod(time_taken.total_seconds(), 60)
        formatted_time_taken = f"{int(minutes)}m {int(seconds)}s"

        questions = BBAQuestion.objects.all()

        for question in questions:
            field_name = f'q{question.id}'
            selected_answer = request.POST.get(field_name)
            submitted_answers.append({
                'question': question,
                'selected_answer': selected_answer,
                'is_correct': selected_answer == question.correct_option
            })
            if selected_answer == question.correct_option:
                correct_answers += 1

        total_marks = correct_answers

        if total_marks == total_questions:
            comments = "Excellent! You've answered all questions correctly. Well done!"
        elif total_marks >= total_questions * 0.75:
            comments = "Great job! You've got most of the answers correct. Keep it up!"
        elif total_marks >= total_questions * 0.5:
            comments = "Good effort! You can improve with a bit more practice."
        else:
            comments = "It seems you need to study a bit more. Don't worry, keep trying!"

        # Create the AptitudeTestBIO object with start_time and end_time
        AptitudeTestBBA.objects.create(
            user=request.user,
            start_time=start_time,
            end_time=end_time,  # Set end_time here
            score=total_marks,
            comments='Answers submitted'
        )

        return render(request, 'after_12/result_bba.html', {
            'correct_answers': correct_answers,
            'total_marks': total_marks,
            'total_questions': total_questions,
            'submitted_answers': submitted_answers,
            'comments': comments,
            'time_taken': formatted_time_taken
        })

def bba_result(request):
    return render(request, 'after_12/result_bba.html')




def bba_view(request):
    courses = BBACourse.objects.all()

    # Process each course's fields to split the text into lists
    for course in courses:
        course.subjects = course.subjects.split(',')
        course.career_opportunities = course.career_opportunities.split(',')
        course.study_tips = course.study_tips.split('.')
        course.future_studies = course.future_studies.split(',')

    return render(request, 'after_12/bba.html', {'courses': courses})

#----------------------------------------------------------------------------------------

def aptitude_chemistry(request):
    questions = CHEMISTRYQuestion.objects.all()

    request.session['start_time'] = timezone.now().isoformat()

    return render(request, 'after_12/aptitude_chemistry.html', {'questions': questions})
def submit_chemistry(request):
    if request.method == 'POST':
        total_marks = 0
        total_questions = CHEMISTRYQuestion.objects.count()
        correct_answers = 0
        submitted_answers = []

        start_time = timezone.datetime.fromisoformat(request.session.get('start_time'))
        end_time = timezone.now()
        time_taken = end_time - start_time

        # Format the time taken into minutes and seconds (optional)
        minutes, seconds = divmod(time_taken.total_seconds(), 60)
        formatted_time_taken = f"{int(minutes)}m {int(seconds)}s"

        questions = CHEMISTRYQuestion.objects.all()

        for question in questions:
            field_name = f'q{question.id}'
            selected_answer = request.POST.get(field_name)
            submitted_answers.append({
                'question': question,
                'selected_answer': selected_answer,
                'is_correct': selected_answer == question.correct_option
            })
            if selected_answer == question.correct_option:
                correct_answers += 1

        total_marks = correct_answers

        if total_marks == total_questions:
            comments = "Excellent! You've answered all questions correctly. Well done!"
        elif total_marks >= total_questions * 0.75:
            comments = "Great job! You've got most of the answers correct. Keep it up!"
        elif total_marks >= total_questions * 0.5:
            comments = "Good effort! You can improve with a bit more practice."
        else:
            comments = "It seems you need to study a bit more. Don't worry, keep trying!"

        # Create the AptitudeTestBIO object with start_time and end_time
        AptitudeTestCHEMISTRY.objects.create(
            user=request.user,
            start_time=start_time,
            end_time=end_time,  # Set end_time here
            score=total_marks,
            comments='Answers submitted'
        )

        return render(request, 'after_12/result_chemistry.html', {
            'correct_answers': correct_answers,
            'total_marks': total_marks,
            'total_questions': total_questions,
            'submitted_answers': submitted_answers,
            'comments': comments,
            'time_taken': formatted_time_taken
        })

def chemistry_result(request):
    return render(request, 'after_12/result_chemistry.html')




def chemistry_view(request):
    courses = CHEMISTRYCourse.objects.all()

    for course in courses:
        course.subjects = course.subjects.split(',')
        course.career_opportunities = course.career_opportunities.split(',')
        course.study_tips = course.study_tips.split('.')
        course.future_studies = course.future_studies.split(',')

    return render(request, 'after_12/chemistry.html', {'courses': courses})

#-------------------------------------------------------------------------------------


def course_job(request):
    return render(request, 'job/course_job.html')  # Ensure the template path is correct

def computer_job(request):
    return render(request, 'job/computer_job.html')  # Ensure the template path is correct

def commerece_job(request):
    return render(request, 'job/commerece_job.html')  # Ensure the template path is correct

def bio_job(request):
    return render(request, 'job/bio_job.html')  # Ensure the template path is correct

def math_job(request):
    return render(request, 'job/math_job.html')  # Ensure the template path is correct

def phyco_job(request):
    return render(request, 'job/phyco_job.html')  # Ensure the template path is correct

def eng_job(request):
    return render(request, 'job/phyco_job.html')  # Ensure the template path is correct

#------------------------------------------------------------------------------------------
def term(request):
    return render(request, 'core/terms.html')  # Ensure the template path is correct


def privacy(request):
    return render(request, 'core/privacy.html')  # Ensure the template path is correct


def admin_check(user):
    return user.is_superuser

@user_passes_test(admin_check)
def admin_dashboard(request):
    return render(request, 'admin/dasboard.html')

def admin_view_users(request):
    users = User.objects.all().select_related('userprofile')  # Fetch related UserProfile data
    return render(request, 'admin/view_users.html', {'users': users})


from .models import Feedback

def view_feedback(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'admin/view_feedback.html', {'feedbacks': feedbacks})

#------------------------------------------------------------------------------

def is_admin(user):
    return user.is_staff


@login_required
@user_passes_test(is_admin)
def admin_chat_view(request):
    messages = ChatMessage.objects.all().order_by('-timestamp')
    replies = {message.id: message.replies.all() for message in messages}
    return render(request, 'admin/admin_chat.html', {'messages': messages, 'replies': replies})


def admin_reply_to_message(request, message_id):
    if request.method == 'POST':
        reply_text = request.POST.get('reply')
        message = get_object_or_404(ChatMessage, id=message_id)  # Get the original message
        if reply_text:
            reply = AdminReply.objects.create(message=message, admin=request.user, reply=reply_text)

            try:
                send_mail(
                    subject='New Reply to Your Message',
                    message=f'Admin replied to your message please check career website',
                    from_email=settings.ADMIN_EMAIL,
                    recipient_list=[message.sender.email],
                    fail_silently=False,
                )
            except Exception as e:
                print(f"Error sending email: {e}")

            return redirect('admin_chat')

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserEditForm, UserProfileEditForm

def view_user_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user_profile = get_object_or_404(UserProfile, user=user)
    return render(request, 'admin/view_user_profile.html', {'user': user, 'user_profile': user_profile})

def edit_user_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user_profile = get_object_or_404(UserProfile, user=user)

    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=user)
        profile_form = UserProfileEditForm(request.POST, instance=user_profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('view_users')
    else:
        user_form = UserEditForm(instance=user)
        profile_form = UserProfileEditForm(instance=user_profile)

    return render(request, 'admin/edit_user_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'user': user,
    })

def delete_user_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()  # This will also delete the UserProfile due to cascade delete
        return redirect('view_users')
    return render(request, 'admin/delete_user_profile.html', {'user': user})


from django.shortcuts import render
from .models import AptitudeTestBIO, AptitudeTestCommerce, AptitudeTestHumanities, AptitudeTestComputer, \
    AptitudeTestStatistics, AptitudeTestBCA, AptitudeTestBBA, AptitudeTestCHEMISTRY, AptitudeTestBSCCOM


def view_aptitude_results(request):
    bio_results = AptitudeTestBIO.objects.all()
    commerce_results = AptitudeTestCommerce.objects.all()
    humanities_results = AptitudeTestHumanities.objects.all()
    computer_results = AptitudeTestComputer.objects.all()
    statistics_results = AptitudeTestStatistics.objects.all()
    bca_results = AptitudeTestBCA.objects.all()
    bba_results = AptitudeTestBBA.objects.all()
    chemistry_results = AptitudeTestCHEMISTRY.objects.all()
    bscc_com_results = AptitudeTestBSCCOM.objects.all()

    context = {
        'bio_results': bio_results,
        'commerce_results': commerce_results,
        'humanities_results': humanities_results,
        'computer_results': computer_results,
        'statistics_results': statistics_results,
        'bca_results': bca_results,
        'bba_results': bba_results,
        'chemistry_results': chemistry_results,
        'bscc_com_results': bscc_com_results,
    }

    return render(request, 'admin/view_aptitude_results.html', context)

