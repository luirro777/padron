from dataclasses import field, fields
from django import forms
from afiliados.models import Afiliado
#from captcha.fields import ReCaptchaField
try:
  from captcha.fields import ReCaptchaField
except ImportError:
  from captcha.fields import CaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class AfiliadoForm(forms.ModelForm):
    #captcha = ReCaptchaField()
    #captcha = ReCaptchaField(
    #    widget=ReCaptchaV2Checkbox()
    #)
    class Meta:
        model = Afiliado
        fields = (            
            'dni',
        )
