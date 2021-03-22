from django import forms
from .models import Workout

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ('type', 'duration', 'intensity', 'steps', 'miles', 'profile')

        widgets = {
            'type': forms.TextInput(attrs={'class': 'form-control'}),
            'duration': forms.TextInput(attrs={'class': 'form-control'}),
            'intensity': forms.TextInput(attrs={'class': 'form-control'}),
            'steps': forms.TextInput(attrs={'class': 'form-control'}),
            'miles': forms.TextInput(attrs={'class': 'form-control'}),
        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['profile'].queryset = Workout.objects.none()