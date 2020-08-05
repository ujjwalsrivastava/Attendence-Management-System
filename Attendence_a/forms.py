from django import forms
from .models import *
from django.core.validators import validate_email


class Signup_teacher_form(forms.ModelForm):
    first_n=forms.CharField(widget=forms.TextInput(
    attrs={'class':'form-control','placeholder':'First Name'})
    ,required=True,max_length=30)
    last_n=forms.CharField(widget=forms.TextInput(
    attrs={'class':'form-control','placeholder':'Last Name'})
    ,required=True,max_length=30)
    userid=forms.CharField(widget=forms.TextInput(
    attrs={'class':'form-control','placeholder':'User Id'})
    ,required=True,max_length=30)
    password=forms.CharField(widget=forms.PasswordInput(
    attrs={'class':'form-control','placeholder':'Password'})
    ,required=True,max_length=30)
    Cnf_password=forms.CharField(widget=forms.PasswordInput(
    attrs={'class':'form-control','placeholder':'Confirm Password'})
    ,required=True,max_length=30)
    email_id=forms.CharField(widget=forms.EmailInput(
    attrs={'class':'form-control','placeholder':'Email Id'})
    ,required=True,max_length=30)

    class Meta:
        model=Signup_teacher
        fields=['first_n','last_n','userid','password','email_id']
        
    def clean_userid(self):
        user=self.cleaned_data['userid']
        try:
            match=Signup_teacher.objects.get(userid=user)
        except:
            return self.cleaned_data['userid']
        raise forms.ValidationError('User name is Already Exist')
    def clean_email_id(self):
        email=self.cleaned_data['email_id']
        match=Signup_teacher.objects.filter(email_id=email)
        if(match):
            raise forms.ValidationError("Email already exist")
        else:
            try:
                mt=validate_email(email)
            except:
                return forms.ValidationError("Email is not in Correct format")
        return email

    def clean_Cnf_password(self):
        c_psw=self.cleaned_data['Cnf_password']
        psw=self.cleaned_data['password']
        MIN_LENGTH=8
        if psw and c_psw:
            if psw != c_psw:
                raise forms.ValidationError("Password and Confirm Password not Matched")
            else:
                if len(psw)<MIN_LENGTH:
                    raise forms.ValidationError("Password should have atleast %d Character" %MIN_LENGTH)
                if psw.isdigit():
                    raise forms.ValidationError("Password should not numeric")

class Teacher_login_form(forms.Form):
    userid=forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'User Id'}
    ),required=True,max_length=50)
    password=forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'form-control','placeholder':'Password'}
    ),required=True,max_length=10)

class Add_student_form(forms.ModelForm):
    first_n=forms.CharField(widget=forms.TextInput(
    attrs={'class':'form-control','placeholder':'First Name'})
    ,required=True,max_length=30)
    last_n=forms.CharField(widget=forms.TextInput(
    attrs={'class':'form-control','placeholder':'Last Name'})
    ,required=True,max_length=30)
    userid=forms.CharField(widget=forms.TextInput(
    attrs={'class':'form-control','placeholder':'User Id'})
    ,required=True,max_length=30)
    password=forms.CharField(widget=forms.PasswordInput(
    attrs={'class':'form-control','placeholder':'Password'})
    ,required=True,max_length=30)
    Cnf_password=forms.CharField(widget=forms.PasswordInput(
    attrs={'class':'form-control','placeholder':'Confirm Password'})
    ,required=True,max_length=30)
    email_id=forms.CharField(widget=forms.EmailInput(
    attrs={'class':'form-control','placeholder':'Email Id'})
    ,required=True,max_length=30)

    class Meta:
        model=Add_student
        fields=['first_n','last_n','userid','password','email_id']
        
    def clean_userid(self):
        user=self.cleaned_data['userid']
        try:
            match=Add_student.objects.get(userid=user)
        except:
            return self.cleaned_data['userid']
        raise forms.ValidationError('User name is Already Exist')
    def clean_email_id(self):
        email=self.cleaned_data['email_id']
        match=Add_student.objects.filter(email_id=email)
        if(match):
            raise forms.ValidationError("Email already exist")
        else:
            try:
                mt=validate_email(email)
            except:
                return forms.ValidationError("Email is not in Correct format")
        return email

    def clean_Cnf_password(self):
        c_psw=self.cleaned_data['Cnf_password']
        psw=self.cleaned_data['password']
        MIN_LENGTH=8
        if psw and c_psw:
            if psw != c_psw:
                raise forms.ValidationError("Password and Confirm Password not Matched")
            else:
                if len(psw)<MIN_LENGTH:
                    raise forms.ValidationError("Password should have atleast %d Character" %MIN_LENGTH)
                if psw.isdigit():
                    raise forms.ValidationError("Password should not numeric")

class Student_login_form(forms.Form):
    userid=forms.CharField(widget=forms.TextInput(
    attrs={'class':'form-control','placeholder':'User Id'})
    ,required=True,max_length=30)
    password=forms.CharField(widget=forms.PasswordInput(
    attrs={'class':'form-control','placeholder':'Password'})
    ,required=True,max_length=30)

class Teacher_subject_form(forms.ModelForm):
    subject=forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'subject'}
    ),required=True,max_length=40)
    teacher_id=forms.CharField(widget=forms.TextInput(
    attrs={'class':'form-control','placeholder':'Teacher Id'})
    ,required=True,max_length=30)
    class Meta():
        model=Add_subject
        fields=['subject','teacher_id']

class Teacher_class_form(forms.ModelForm):
    class_c=forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Class'}
    ),required=True,max_length=40)
    teacher_id=forms.CharField(widget=forms.TextInput(
    attrs={'class':'form-control','placeholder':'Teacher Id'})
    ,required=True,max_length=30)
    class Meta():
        model=Add_class
        fields=['class_c','teacher_id']
