from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Course


def list_course(request):
    name = request.GET.get('name', '')
    courses = Course.objects.all()
    if name:
        courses = courses.filter(name__icontains=name)
    
    paginator = Paginator(courses, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'name': name
    }
    
    return render(request, 'course/list_course.html', context)


def add_course(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        credits = request.POST.get('credits')
        hours = request.POST.get('hours')
        description = request.POST.get('description')
        Course.objects.create(name=name, credits=credits, hours=hours, description=description)
        return redirect('course:list_course')
    return render(request, 'course/add_course.html')


def edit_course(request, pk):
    course_obj = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course_obj.name = request.POST.get('name')
        course_obj.credits = request.POST.get('credits')
        course_obj.hours = request.POST.get('hours')
        course_obj.description = request.POST.get('description')
        course_obj.save()
        return redirect('course:list_course')
    return render(request, 'course/edit_course.html', {'course': course_obj, 'pk': pk})


def delete_course(request, pk):
    course_obj = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course_obj.delete()
        return redirect('course:list_course')
    return render(request, 'course/delete_course.html', {'course': course_obj, 'pk': pk})
