from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.db import connection


def getClasses():
    cursor = connection.cursor()
    cursor.execute("exec getClasses ")
    columns = [column[0] for column in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


getClass = getClasses()


def subjects(request):
    cursor = connection.cursor()
    if request.method == 'POST':
        v_subject = request.POST.get('txtSubject')
        v_type = request.POST.get('dType')
        v_class = request.POST.get('dClass')
        v_code = request.POST.get('txtCode')
        cursor.execute("exec SaveSubject '" + v_subject + "'," + str(v_type) + "," + str(v_class)
                       + ",'" + v_code + "'")

    cursor.execute("exec getSubjects ")
    columns = [column[0] for column in cursor.description]
    subjects = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return render(request, 'AllSubject.html', {'subjects': subjects, 'getClass': getClass})
