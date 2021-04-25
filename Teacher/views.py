from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.db import connection
from django.views.generic import CreateView
from django.contrib import messages

# Create your views here.
from django.utils.datetime_safe import date


# get Section
def getSection():
    cursor = connection.cursor()
    cursor.execute("exec getSection ")
    columns = [column[0] for column in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


# Get Classes
def getClasses():
    cursor = connection.cursor()
    cursor.execute("exec getClasses ")
    columns = [column[0] for column in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


# Get Subjects As per Class
def load_Subjects(request):
    v_Dclass = request.GET.get('Selected')
    cursor = connection.cursor()
    cursor.execute("exec getListSubjects '" + v_Dclass + "'")
    columns = [column[0] for column in cursor.description]
    subjects = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return render(request, 'Subject_List_Option.html', {'subjects': subjects})


section = getSection()
getClass = getClasses()


# insert new Teacher
def addteacher(request):
    # UserData = request.user.first_name + ' ' + request.user.last_name
    if request.method == 'POST':
        myfile = request.FILES['myfile']
        imagename = myfile.name
        ext = imagename.split('.')[-1]
        imagename = '{}.{}'.format(8, ext)
        # print(imagename)
        fs = FileSystemStorage()
        filename = fs.save(imagename, myfile)
        # print(filename)
        uploaded_file_url = fs.url(filename)
        print(uploaded_file_url)

        if request.POST.get('fname') and request.POST.get('lname') and request.POST.get('govid'):
            v_username = request.POST.get('email')
            v_first_name = request.POST.get('fname')
            v_last_name = request.POST.get('lname')
            v_email = request.POST.get('email')
            v_is_active = 1
            v_date_joined = date.today()

            x = User.objects.create_user(password=123456,
                                         is_superuser=0,
                                         username=v_username,
                                         first_name=v_first_name,
                                         last_name=v_last_name,
                                         email=v_email,
                                         is_staff=1,
                                         is_active=v_is_active,
                                         date_joined=v_date_joined)
            x.save()
            v_id = x.id  # getting primary key

            # Image Upload COde
            myfile = request.FILES['myfile']
            imagename = myfile.name
            ext = imagename.split('.')[-1]
            imagename = '{}.{}'.format(v_id, ext)
            # print(imagename)
            fs = FileSystemStorage()
            filename = fs.save(imagename, myfile)
            # print(filename)
            uploaded_file_url = fs.url(filename)
            print(uploaded_file_url)

            # print(str(x.id)+","+str(request.user.id))

            v_gender = request.POST.get('txtSubject')
            v_DOB = request.POST.get('DOB')
            v_govid = request.POST.get('govid')
            v_Dbg = request.POST.get('Dbg')
            v_Dreligion = request.POST.get('Dreligion')
            v_Dclass = request.POST.get('Selected')
            v_Dsection = request.POST.get('Dsection')
            v_txtAddress = request.POST.get('txtAddress')
            v_txtPhone = request.POST.get('txtPhone')
            v_txtSbio = request.POST.get('txtSbio')
            v_subjects = request.POST.get('subjects')
            v_User = request.user.id
            cursor = connection.cursor()
            cursor.execute("exec saveAuthUser " + str(v_id) + ",'" + v_gender + "','" + str(v_DOB)
                           + "','" + v_govid + "','" + v_Dbg + "','" + v_Dreligion
                           + "','" + v_Dclass + "','" + v_Dsection + "','" + v_txtAddress
                           + "','" + v_txtPhone + "','" + v_txtSbio + "',5,NULL," + str(v_User)
                           + ",'" + uploaded_file_url + "','" + v_subjects + "'")

            # print(request, teacher.fn + " " + teacher.ln + " " + teacher.govid)
            # messages.success(request, teacher.fn + " " + teacher.ln + " " + teacher.govid)

            return render(request, 'AddTeacher.html', {'school': 'Donbosco', 'section': section, 'getClass': getClass})
    else:
        return render(request, 'AddTeacher.html', {'school': 'Donbosco', 'section': section, 'getClass': getClass})
    return render(request, 'AddTeacher.html', {'school': 'Donbosco', 'section': section, 'getClass': getClass})


# profile Data
def teacherdetails(request):
    # UserData = request.user.first_name + ' ' + request.user.last_name
    v_User = request.user.id
    cursor = connection.cursor()
    cursor.execute("exec getUser " + str(v_User))
    columns = [column[0] for column in cursor.description]
    row = dict(zip(columns, cursor.fetchone()))
    # row = dict(zip(zip(*cursor.description)[0], cursor.fetchone()))
    # row = cursor.fetchone()
    return render(request, 'teacherdetails.html', {'school': 'Donbosco', 'row': row})


# list of All teachers
def allteacher(request):
    # UserData = request.user.first_name + ' ' + request.user.last_name

    v_name = ''
    v_phone = ''
    v_id = 0

    if request.method == 'POST':
        v_name = request.POST.get('txtName')
        v_phone = request.POST.get('txtPhone')
        v_id = request.POST.get('txtId')

    cursor = connection.cursor()
    cursor.execute("exec getUsers " + str(v_id) + ",'" + v_name + "','" + v_phone + "'")
    columns = [column[0] for column in cursor.description]
    lists = [dict(zip(columns, row)) for row in cursor.fetchall()]
    # row = [dict(zip(zip(*cursor.description)[0], row)) for row in cursor.fetchall()]
    # row = cursor.fetchall()
    return render(request, 'AllTeachers.html', {'school': 'Donbosco', 'row': lists})


def updateacher(request, id):
    # v_User = id
    cursor = connection.cursor()
    cursor.execute("exec getUser " + str(id))
    columns = [column[0] for column in cursor.description]
    row = dict(zip(columns, cursor.fetchone()))
    if request.method == 'POST':
        v_first_name = request.POST.get('fname')
        v_last_name = request.POST.get('lname')
        v_gender = request.POST.get('Dgender')
        v_DOB = request.POST.get('DOB')
        v_govid = request.POST.get('govid')
        v_Dbg = request.POST.get('Dbg')
        v_Dreligion = request.POST.get('Dreligion')
        v_Dclass = request.POST.get('Selected')
        v_Dsection = request.POST.get('Dsection')
        v_txtAddress = request.POST.get('txtAddress')
        v_txtPhone = request.POST.get('txtPhone')
        v_txtSbio = request.POST.get('txtSbio')
        v_subjects = request.POST.get('subjects')
        v_User = request.user.id
        cursor = connection.cursor()
        cursor.execute("exec saveAuthUser " + str(id) + ",'" + v_gender + "','" + str(v_DOB)
                       + "','" + v_govid + "','" + v_Dbg + "','" + v_Dreligion
                       + "','" + v_Dclass + "','" + v_Dsection + "','" + v_txtAddress
                       + "','" + v_txtPhone + "','" + v_txtSbio + "',5,NULL," + str(v_User)
                       + ",NULL,'" + v_subjects + "','" + v_first_name + "','" + v_last_name + "'")
        return redirect('/allteacher/')
    else:
        return render(request, 'updateTeacher.html', {'school': 'Donbosco', 'section': section,
                                                      'getClass': getClass, 'row': row})
