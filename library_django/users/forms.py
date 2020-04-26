from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import ReCaptchaField
import re
from django.utils.safestring import mark_safe
from django.core.validators import RegexValidator
from phonenumber_field.formfields import PhoneNumberField


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    name = forms.CharField()
    surname = forms.CharField()
    street = forms.CharField()
    city = forms.CharField()
    post_code = forms.CharField(validators=[RegexValidator(regex=re.compile(r'\d{2}-\d{3}'), message='Enter valid '
                                                                                                     'post-code '
                                                                                                     'XX-XXX')])

    # post_code = forms.CharField(validators=validate_post_code)
    # phone_number = PhoneNumberField()
    phone_number = forms.CharField(validators=[RegexValidator(regex=re.compile(r'\d{9}'), message='Enter valid phone number')])

    # Get phone as string from object field: user.phone.as_e164
    country = forms.CharField()
    birth_date = forms.DateField()
    profile_picture = forms.ImageField(required=False)
    pesel = forms.CharField(validators=[RegexValidator(regex=re.compile(r'\d{11}'), message='Enter valid pesel')])
    rules_agreement = forms.BooleanField(label=mark_safe('I have read and agree to the <a href="#">Terms and '
                                                         'Conditions</a> and <a href="#">Privacy Policy</a>'))

    class Meta:
        model = User
        fields = ["username", 'email', 'name', 'surname', 'street', 'city', 'post_code', 'phone_number', 'country',
                  'birth_date', 'profile_picture', 'pesel', 'rules_agreement', "password1", "password2"]
