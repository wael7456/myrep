#from django.contrib.auth.forms import UserCreationForm
from django import forms 
 
#from django.contrib.auth.models import RegistarionForm


from users.models import CustomUser



class RegistarionForm(forms.ModelForm):
    class Meta :
        model= CustomUser
        fields=('username','email','first_name','last_name','password')






class LoginForm(forms.ModelForm):
    class Meta :
        model = CustomUser 
        fields = ('username', 'password' )



