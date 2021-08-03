from .models import Student
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, reverse
from django.http import request, HttpResponseRedirect
from .forms import StudentForm
from django.views.generic import CreateView, UpdateView


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


class StudentCreateView(CreateView):
    model = Student
    fields = "__all__"
    template_name = 'student_form.html'
    def get_success_url(self):
        return HttpResponseRedirect(reverse('student'))

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_form.html'
    def get_success_url(self):
        return reverse(index)
