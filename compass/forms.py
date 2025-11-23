from django import forms
from .models import Instruction


class InstructionForm(forms.ModelForm):
    class Meta:
        model = Instruction
        fields = ['direction', 'distance', 'description', 'previous_instruction', 'risk_level']
        widgets = {
            'direction': forms.Select(attrs={'class': 'form-control'}),
            'distance': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'previous_instruction': forms.Select(attrs={'class': 'form-control'}),
            'risk_level': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'max': '100'}),
        }

    def clean_distance(self):
        distance = self.cleaned_data['distance']
        if distance <= 0:
            raise forms.ValidationError("Distance must be greater than zero")
        return distance

    def clean_risk_level(self):
        risk_level = self.cleaned_data['risk_level']
        if risk_level < 0 or risk_level > 100:
            raise forms.ValidationError("Risk level must be between 0 and 100")
        return risk_level