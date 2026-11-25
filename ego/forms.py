from django import forms
class GiveForm(forms.Form):
    namef=forms.CharField(label="Name", widget=forms.TimeInput, initial="UnDefined", help_text="Enter your name", required=True)
    agef=forms.IntegerField(min_value=1, max_value=150, required=True)
    emailf=forms.EmailField(required=False)
    datef=forms.DateField(label='Date', widget=forms.SelectDateWidget, required=False)
    filef=forms.FileField(label='ID', help_text='attach your ID', required=False)
    passwordf=forms.CharField(label="create a password please", min_length=8,widget=forms.PasswordInput() ,required=True)
