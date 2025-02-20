from django.shortcuts import render, redirect
from .forms import GoalForm, DreamForm, EventTimeCapsuleForm
from .models import Goal, Dream, EventTimeCapsule
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    goals = Goal.objects.filter(user=request.user)
    dreams = Dream.objects.filter(user=request.user)
    events = EventTimeCapsule.objects.filter(user=request.user)
    return render(request, 'vault/dashboard.html', {'goals': goals, 'dreams': dreams, 'events': events})

@login_required
def add_goal(request):
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            return redirect('dashboard')
    else:
        form = GoalForm()
    return render(request, 'vault/add_goal.html', {'form': form})

@login_required
def add_dream(request):
    if request.method == 'POST':
        form = DreamForm(request.POST)
        if form.is_valid():
            dream = form.save(commit=False)
            dream.user = request.user
            dream.save()
            return redirect('dashboard')
    else:
        form = DreamForm()
    return render(request, 'vault/add_dream.html', {'form': form})

@login_required
def add_event(request):
    if request.method == 'POST':
        form = EventTimeCapsuleForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return redirect('dashboard')
    else:
        form = EventTimeCapsuleForm()
    return render(request, 'vault/add_event.html', {'form': form})
