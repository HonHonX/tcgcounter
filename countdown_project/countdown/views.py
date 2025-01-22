from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import Countdown
from django.utils.timezone import now

def counter_view(request):
    if request.method == 'POST' and 'username' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('counter')
    counter = Countdown.objects.last()
    context = {
        'counter': counter,
        'time_remaining': counter.time_remaining() if counter else None,
    }
    return render(request, 'countdown/counter.html', context)

@login_required
def admin_counter_view(request):
    if request.method == 'POST':
        duration = int(request.POST['duration'])
        Countdown.objects.create(admin=request.user, duration_minutes=duration)
        return redirect('counter')
    return render(request, 'countdown/admin_counter.html')

def home_view(request):
    return redirect('counter')

def csrf_failure(request, reason=""):
    return render(request, 'csrf_failure.html', status=403)
