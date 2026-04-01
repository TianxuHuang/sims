from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .forms import StudentForm
from .models import Student


def list_student(request):
    students = Student.objects.all()
    paginator = Paginator(students, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'student/list_student.html', {'page_obj': page_obj})


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student:add_student')
    else:
        form = StudentForm()
    
    return render(request, 'student/add_student.html', {'form': form})


def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student:list_student')
    else:
        form = StudentForm(instance=student)
    
    return render(request, 'student/edit_student.html', {'form': form})


def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student:list_student')
    return render(request, 'student/delete_student.html', {'student': student})

