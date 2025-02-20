from django import forms
from .models import Goal, Dream, EventTimeCapsule

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['title', 'description', 'target_date', 'progress']

class DreamForm(forms.ModelForm):
    class Meta:
        model = Dream
        fields = ['title', 'description']

class EventTimeCapsuleForm(forms.ModelForm):
    class Meta:
        model = EventTimeCapsule
        fields = ['event_name', 'event_date', 'messages']
