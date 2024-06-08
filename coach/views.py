from django.shortcuts import render

# Create your views here.
def coach_view(request):
    return render(request, 'coach/coach.html')