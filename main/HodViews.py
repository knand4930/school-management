from datetime import datetime

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from main.models import CustomUser, Courses, Staffs, Subjects, Students


def admin_home(request):
    return render(request, 'index.html')


def add_staff(request):
    return render(request, 'add_staff_template.html')


def add_staff_save(request):
    if request.method != 'POST':
        return HttpResponse("Method Not Allowed")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email,
                                                  first_name=first_name, last_name=last_name, user_type=2)
            user.staffs.address = address
            user.save()
            messages.success(request, "Successfully Added Staff")
            return HttpResponseRedirect("/add_staff")
        except:
            messages.error(request, "Failed To Added Staff")
            return HttpResponseRedirect("/add_staff")


def add_course(request):
    return render(request, 'add_course_template.html')


def add_course_save(request):
    if request.method != 'POST':
        return HttpResponse("Method Not Allowed")
    else:
        course = request.POST.get("course")
        try:
            course_model = Courses(course_name=course)
            course_model.save()
            messages.success(request, "Successfully Added Course")
            return HttpResponseRedirect("/add_course")
        except:
            messages.error(request, "Failed To Added Staff")
            return HttpResponseRedirect("/add_course")


def add_student(request):
    courses = Courses.objects.all()
    return render(request, 'add_student_template.html', {'courses': courses})


def add_student_save(request):
    if request.method != 'POST':
        return HttpResponse("Method Not Allowed")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        session_start = request.POST.get('session_start')
        session_end = request.POST.get('session_end')
        course_id = request.POST.get("course")
        sex = request.POST.get("sex")
        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email,
                                                  first_name=first_name, last_name=last_name, user_type=3)
            user.students.address = address
            course_obj = Courses.objects.get(id=course_id)
            user.students.course_id = course_obj

            # start_date = datetime.datetime.strptime(session_start,"%d-%m-%y").strftime('%Y-%m-%d')
            # end_date = datetime.datetime.strptime(session_end,"%d-%m-%y").strftime('%Y-%m-%d')

            user.students.session_start_years = session_start
            user.students.session_end_years = session_end
            user.students.gender = sex
            user.students.profile_pic = ""
            user.save()
            messages.success(request, "Successfully Added Student")
            return HttpResponseRedirect("/add_student")
        except:
            messages.error(request, "Failed To Added Student")
            return HttpResponseRedirect("/add_student")


def add_subjects(request):
    courses = Courses.objects.all()
    staffs = CustomUser.objects.filter(user_type=2)
    return render(request, 'add_subjects_template.html', {'staffs': staffs, 'courses': courses})


def add_subjects_save(request):
    if request.method != 'POST':
        return HttpResponse("<h2>Method Not Allowed </h2>")
    else:
        subject_name = request.POST.get("subject_name")
        course_id = request.POST.get("course")
        course = Courses.objects.get(id = course_id)

        staff_id = request.POST.get("staff")
        staff = CustomUser.objects.get(id = staff_id)

        try:
            subject = Subjects(subject_name=subject_name, course_id=course, staff_id=staff)
            subject.save()
            messages.success(request, "Successfully Added Student")
            return HttpResponseRedirect("/add_subjects")
        except:
            messages.error(request, "Failed To Added Student")
            return HttpResponseRedirect("/add_subjects")


def manage_staff(request):
    staffs = Staffs.objects.all()
    return render(request, 'manage_staff_template.html', {'staffs':staffs})


def manage_student(request):
    students = Students.objects.all()

    return render(request, 'manage_student_template.html', {'students':students})


def manage_course(request):
    courses = Courses.objects.all()
    return render(request, 'manage_course_template.html', {'courses':courses})


def manage_subject(request):
    subjects = Subjects.objects.all()
    return render(request, 'manage_subject_template.html', {"subjects":subjects})