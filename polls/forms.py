from django import forms
from polls.models import Poll
from polls.models import Choice

class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
