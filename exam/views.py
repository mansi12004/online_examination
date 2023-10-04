from django.shortcuts import render
from django.http import HttpResponse
from .models import Test,TestResult
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required
def test(request):
    ques = Test.objects.all()
    return render(request, 'test.html', {"ques": ques})
@login_required
def result(request):
    if request.method == 'POST':
        # Calculate the test result as you did before
        total_questions = len(request.POST) - 1
        questions_attempted = 0
        questions_correct = 0
        questions_wrong = 0
        questions_not_attempted = 0

        for que in Test.objects.all():
            user_answer = request.POST.get(f'options{que.pk}', None)

            if user_answer is None:
                questions_not_attempted += 1
            elif user_answer == que.answer:
                questions_correct += 1
                questions_attempted += 1
            else:
                questions_wrong += 1
                questions_attempted += 1

        # Calculate the total score or any other relevant data
        total_score = questions_correct  # You can modify this as per your scoring logic

        # Create a new TestResult instance and save it to the database
        test_result = TestResult(
            user=request.user,  # Assuming you are using Django's built-in User model
            test=Test.objects.first(),  # Replace with the actual test instance
            total_score=total_score,
            # Add other fields as needed
        )
        test_result.save()

        # Render the result to the user
        return render(
            request,
            'result.html',
            {
                'total_questions': total_questions,
                'questions_attempted': questions_attempted,
                'questions_correct': questions_correct,
                'questions_wrong': questions_wrong,
                'questions_not_attempted': questions_not_attempted,
            },
        )
    else:
        return HttpResponse("Invalid request method")
