from django import forms
from .models import Participant


class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['full_name', 'school', 'phone', 'email']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form__input form-control',
                'placeholder': 'Иванов Иван Иванович',
                'autocomplete': 'name',
                'id': 'fullname',
                'name': 'fullname',
                'required': True
            }),
            'school': forms.TextInput(attrs={
                'class': 'form__input form-control',
                'placeholder': 'РГЭУ (РИНХ)',
                'autocomplete': 'organization',
                'id': 'institution',
                'name': 'institution',
                'required': True
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form__input form-control',
                'placeholder': '+7 (___) ___-__-__',
                'autocomplete': 'tel',
                'id': 'phone',
                'name': 'phone',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form__input form-control',
                'placeholder': 'example@mail.ru',
                'autocomplete': 'email',
                'id': 'email',
                'name': 'email',
                'required': True
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Убираем дефолтные Django ошибки, используем HTML5 validation
        self.fields['full_name'].required = False
        self.fields['school'].required = False
        self.fields['phone'].required = False
        self.fields['email'].required = False
