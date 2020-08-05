from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from .forms import *
from Attendence_a.views import *
from Attendence_a import *
from django.core.exceptions import ObjectDoesNotExist

def Signup_teacher_r(request):
    if request.method=='POST':
        form=Signup_teacher_form(request.POST)
        if form.is_valid():
            form.save()
            userid=form.cleaned_data['userid']
            request.session['user']=userid
            return render(request,'Teacher_account.htm')
    else:
        form=Signup_teacher_form()
        redirect(Signup_teacher_r)
    return render(request,'Signup_teacher.htm',{'form':form})

def Teacher_account(request):
    if request.session.has_key('teacher'):
        return render(request,'Teacher_account.htm')
    elif request.session.has_key('student'):
        return render(request,'Studentaccount.htm')
    else:
        return redirect(Login_teacher)

def Login_teacher(request):
    if request.method=='POST':
        form=Teacher_login_form(request.POST)
        if form.is_valid():
            userid=form.cleaned_data['userid']
            password=form.cleaned_data['password']
            match=Signup_teacher.objects.filter(userid=userid)
            if(match):
                matchh=Signup_teacher.objects.filter(userid=userid,password=password)
                if(matchh):
                    request.session['teacher']=userid
                    return redirect(Teacher_account)
                else:
                    form=Teacher_login_form()
                    return render(request,'Login_teacher.htm',{'error':'Password is Incorrect','form':form})
            else:
                form=Teacher_login_form()
                return render(request,'Login_teacher.htm',{'error':'User Id is not Registered','form':form})
        else:
            form=Teacher_login_form()
            return render(request,'Login_teacher.htm',{'error':'Enter Correctly','form':form})
    else:
        form=Teacher_login_form()
    if request.session.has_key('teacher'):
        return render(request,'Teacher_account.htm')
    elif request.session.has_key('Student'):
        return render(request,'Student_account.htm')
    else:
        return render(request,'Login_teacher.htm',{'form':form})

def New_student(request):
    if request.session.has_key('teacher'):
        if request.method=='POST':
            form_student=Add_student_form(request.POST)
            if form_student.is_valid():
                user=form_student.cleaned_data['userid']
                form_student.save()
                subject=request.POST['subject']
                class_c=request.POST['class']
                teacheruserid=request.session['teacher']
                Add_student.objects.filter(userid=user).update(teacher_id=teacheruserid,subject=subject,class_c=class_c)
                form_student=Add_student_form()
                valuees=Add_subject.objects.filter(teacher_id=teacheruserid)
                valueec=Add_class.objects.filter(teacher_id=teacheruserid)
                return render(request,'New_student.htm',{'message':'Student Added Successfully','form_student':form_student,'valuees':valuees,'valueec':valueec})
            else:
                form_student=Add_student_form()
                teacheruserid=request.session['teacher']
                valuees=Add_subject.objects.filter(teacher_id=teacheruserid)
                valueec=Add_class.objects.filter(teacher_id=teacheruserid)
                return render(request,'New_student.htm',{'form_student':form_student,'valuees':valuees,'valueec':valueec})
        else:
                form_student=Add_student_form()
                teacheruserid=request.session['teacher']
                valuees=Add_subject.objects.filter(teacher_id=teacheruserid)
                valueec=Add_class.objects.filter(teacher_id=teacheruserid)
                return render(request,'New_student.htm',{'form_student':form_student,'valuees':valuees,'valueec':valueec})
    elif request.session.has_key('student'):
        return render(request,'Student_account.htm')
    else:
        form=Signup_teacher_form()
        return render(request,'Signup_teacher.htm',{'form':form})

def logout(request):
    if request.session.has_key('teacher'):
        del request.session['teacher']
        form=Teacher_login_form()
        return render(request,'Login_teacher.htm',{'form':form})
    elif request.session.has_key('student'):
        del request.session['student']
        form_student=Add_student_form()
        return render(request,'Login_student.htm',{'form_student':form_student})
    else:
        form=Signup_teacher_form()
        return render(request,'Signup_teacher.htm',{'form':form})

def Login_student(request):
    if request.method=='POST':
        form_student=Student_login_form(request.POST)
        if form_student.is_valid():
            userid=form_student.cleaned_data['userid']
            password=form_student.cleaned_data['password']
            match=Add_student.objects.filter(userid=userid)
            if(match):
                matchh=Add_student.objects.filter(userid=userid,password=password)
                if(matchh):
                    request.session['student']=userid
                    return render(request,'Student_account.htm')
                else:
                    form_student=Student_login_form()
                    return render(request,'Login_student.htm',{'error':'Password not matched','form_student':form_student})
            else:
                form_student=Student_login_form()
                return render(request,'Login_student.htm',{'error':'Userid not Found','form_student':form_student})
        else:
            form_student=Student_login_form()
            return render(request,'Login_student.htm',{'error':'Enter Correctly','form_student':form_student})
    else:
        form_student=Student_login_form()
    if request.session.has_key('teacher'):
        return render(request,'Teacher_account.htm')
    elif request.session.has_key('student'):
        return render(request,'Student_account.htm')
    else:
        return render(request,'Login_student.htm',{'form_student':form_student})


def Student_account(request):
    if request.session.has_key('teacher'):
        return render(request,'Teacher_account.htm')
    elif request.session.has_key('student'):
        return render(request,'Student_account.htm')
    else:
        form_student=Student_login_form()
        return render(request,'Login_student.htm',{'form_student':form_student})

def Add_subjectt(request):
    if request.session.has_key('teacher'):
        if request.method=='POST':
            form_subject=Teacher_subject_form(request.POST)
            if form_subject.is_valid():
                subject=form_subject.cleaned_data['subject']
                teacherid=form_subject.cleaned_data['teacher_id']
                ok=request.session['teacher']
                if(ok==teacherid):
                    match=None
                    try:
                        match=Add_subject.objects.get(teacher_id=ok,subject=subject)
                    except:
                        pass
                    if(match):
                        form_subject=Teacher_subject_form()
                        return render(request,'Addsubject.htm',{'message':"You already added this Subject!",'form_subject':form_subject})
                    else:
                        form_subject.save()
                        form_subject=Teacher_subject_form()
                        return render(request,'Addsubject.htm',{'message':"Subject Added Successfully!",'form_subject':form_subject})
                else:
                    form_subject=Teacher_subject_form()
                    return render(request,'Addsubject.htm',{'message':"You entered Wrong User Name!",'form_subject':form_subject})
            else:
                form_subject=Teacher_subject_form()
                return render(request,'Addsubject.htm',{'message':"Please Enter valid detail!",'form_subject':form_subject})
        else:
            form_subject=Teacher_subject_form()
            return render(request,'Addsubject.htm',{'form_subject':form_subject})
    elif request.session.has_key('student'):
        return render(request,'Student_account.htm')
    else:
        form=Teacher_login_form()
        return render(request,'Login_teacher.htm',{'form':form})

def Add_classs(request):
    if request.session.has_key('teacher'):
            if request.method=='POST':
                form_class=Teacher_class_form(request.POST)
                if form_class.is_valid():
                    class_c=form_class.cleaned_data['class_c']
                    teacherid=form_class.cleaned_data['teacher_id']
                    ok=request.session['teacher']
                    if(ok==teacherid):
                        match=None
                        try:
                            match=Add_class.objects.get(teacher_id=ok,class_c=class_c)
                        except:
                            pass
                        if(match):
                            form_class=Teacher_class_form()
                            return render(request,'Addclass.htm',{'message':"You have already added this Class!",'form_class':form_class})
                        else:
                            form_class.save()
                            form_class=Teacher_class_form()
                            return render(request,'Addclass.htm',{'message':"Class Added Successfully!",'form_class':form_class})
                    else:
                        form_class=Teacher_class_form()
                        return render(request,'Addclass.htm',{'message':"You entered Wrong User Name!",'form_class':form_class})
                else:
                    form_class=Teacher_class_form()
                    return render(request,'Addclass.htm',{'message':"Please Enter valid detail!",'form_class':form_class})
            else:
                form_class=Teacher_class_form()
                return render(request,'Addclass.htm',{'form_class':form_class})
    elif request.session.has_key('student'):
        return render(request,'Student_account.htm')
    else:
        form=Teacher_login_form()
        return render(request,'Login_teacher.htm',{'form':form})


def All_student(request):
    if request.session.has_key('teacher'):
        datas=Add_student.objects.filter(teacher_id=request.session['teacher'])
        return render(request,'All_student.htm',{'datas':datas})
    if request.session.has_key('student'):
        return redirect(Student_account)
    else:
        form=Teacher_login_form()
        return render(request,'Login_teacher.htm',{'form':form})

def Select(request):
    if request.session.has_key('teacher'):
            if request.method=='POST':
                subject=request.POST['subject']
                class_c=request.POST['class']
                try:
                    data=Teacher_subject_class.objects.filter(teacher_id=request.session['teacher'])
                except:
                    data=None
                if data:
                    Teacher_subject_class.objects.filter(teacher_id=request.session['teacher']).delete()
                Teacher_subject_class(subject=subject,teacher_id=request.session['teacher'],class_c=class_c).save()
                data=Add_student.objects.filter(teacher_id=request.session['teacher'],subject=subject,class_c=class_c)
                return render(request,'Add_attendencec.htm',{'data':data})
            else:
                    datas=Add_subject.objects.filter(teacher_id=request.session['teacher'])
                    datac=Add_class.objects.filter(teacher_id=request.session['teacher'])
                    return render(request,'Select.htm',{'datas':datas,'datac':datac})
    if request.session.has_key('student'):
            return redirect(Student_account)
    else:
        form=Teacher_login_form()
        return render(request,'Login_teacher.htm',{'form':form})

def Mark(request):
    if request.session.has_key('teacher'):
            if request.method=='POST':
                if request.POST.get('attendence'):
                    vi=request.POST.get('attendence')
                    print(vi)
                    vi=str(vi)
                    l=len(vi)
                    vii=vi[0:l-1]
                    present=vii.split(",")
                    li=[]
                    data=Teacher_subject_class.objects.get(teacher_id=request.session['teacher'])
                    dataa=Add_student.objects.filter(subject=data.subject,class_c=data.class_c)
                    for i in dataa:
                        li.append(i.userid)
                    absent1=list(set(li)-set(present))
                    absent2=list(set(present)-set(li))
                    absent=absent1+absent2
                    date=request.POST['date']
                    for i in present:
                        try:
                            Attendence.objects.get(userid=i,teacher_id=request.session['teacher'],date=date)
                        except:
                            Attendence(userid=i,teacher_id=request.session['teacher'],date=date,present_absent="P").save()
                    for j in absent:
                        try:
                            Attendence.objects.get(userid=i,teacher_id=request.session['teacher'],date=date)
                        except:
                            Attendence(userid=j,teacher_id=request.session['teacher'],date=date,present_absent="A").save()
    return render(request,'Teacher_account.htm',{'data':'Attendence Marked Successfully'})

def Delete(request,pk):
    if request.session.has_key('teacher'):
            Add_student.objects.get(id=pk).delete()
            return redirect(All_student)
    if request.session.has_key('student'):
            return redirect(Student_account)
    else:
        form=Teacher_login_form()
        return render(request,'Login_teacher.htm',{'form':form})



def Student_view_attendence(request):
    if request.session.has_key('teacher'):
            return redirect(Teacher_account)
    if request.session.has_key('student'):
            return render(request,'Student_view_attendence.htm')
    else:
        form=Teacher_login_form()
        return render(request,'Login_teacher.htm',{'form':form})

def Student_mark_attendence(request):
    if request.session.has_key('teacher'):
            return redirect(Teacher_account)
    if request.session.has_key('student'):
            if request.method=='POST':
                datef=request.POST['datef']
                datet=request.POST['datet']
                try:
                    t=Attendence.objects.filter(userid=request.session['student'],date__lte=datet,date__gte=datef)
                except:
                    t=None
                return render(request,'Display_attendence.htm',{'t':t})
            else:
                return redirect(Student_account)
    else:
        form=Teacher_login_form()
        return render(request,'Login_teacher.htm',{'form':form})
