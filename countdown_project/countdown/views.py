from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Countdown
from django.utils.timezone import now

def counter_view(request):
    counter = Countdown.objects.last()
    context = {
        'counter': counter,
        'time_remaining': counter.time_remaining() if counter else None,
    }
    return render(request, 'countdown/counter.html', context)  # Ensure it points to counter.html in templates/countdown

@login_required
def admin_counter_view(request):
    if request.method == 'POST':
        duration = int(request.POST['duration'])
        Countdown.objects.create(admin=request.user, duration_minutes=duration)
        return redirect('counter')
    return render(request, 'countdown/admin_counter.html')  # Ensure it points to admin_counter.html in templates/countdown
