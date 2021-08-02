from .models import Student
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

def index(request):
    student_list = Student.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(student_list, 2)
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'list.html', { 'students': students })


def enroll_student(request):
    pass