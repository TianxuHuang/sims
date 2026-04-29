from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .forms import StudentForm
from .models import Student
from classes.models import Class


def list_student(request):
    # 获取查询参数
    student_id = request.GET.get('student_id', '')
    name = request.GET.get('name', '')
    phone = request.GET.get('phone', '')
    gender = request.GET.get('gender', '')
    class_field = request.GET.get('class_field', '')
    
    # 构建查询
    students = Student.objects.all()
    
    # 按学号、姓名、电话进行模糊查询
    if student_id:
        students = students.filter(student_id__icontains=student_id)
    if name:
        students = students.filter(name__icontains=name)
    if phone:
        students = students.filter(phone__icontains=phone)
    
    # 按性别进行精确查询
    if gender:
        students = students.filter(gender=gender)
    
    # 按班级进行精确查询
    if class_field:
        students = students.filter(class_field_id=class_field)
    
    paginator = Paginator(students, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # 获取所有班级用于下拉选择
    classes = Class.objects.all()
    
    # 传递查询参数给模板
    context = {
        'page_obj': page_obj,
        'student_id': student_id,
        'name': name,
        'phone': phone,
        'gender': gender,
        'class_field': class_field,
        'classes': classes
    }
    
    return render(request, 'student/list_student.html', context)


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student:add_student')
    else:
        form = StudentForm()
    
    return render(request, 'student/add_student.html', {'form': form})


def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
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

