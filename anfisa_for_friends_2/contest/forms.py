from django import forms

from .models import Contest
class ContestForm(forms.ModelForm):
    class Meta:
        model = Contest
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows':5, 'cols':22}),
            'comment': forms.Textarea(attrs={'rows':5, 'cols':22}),
        }
