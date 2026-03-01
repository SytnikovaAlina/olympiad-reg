from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ParticipantForm
from .models import Participant


def index(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            participant = form.save()
            messages.success(request, f'✅ {participant.full_name} успешно зарегистрирован!')
            return redirect('register')  # Остаёмся на форме
        else:
            messages.error(request, '❌ Исправьте ошибки в форме')
    else:
        form = ParticipantForm()

    return render(request, 'registration/index.html', {'form': form})
