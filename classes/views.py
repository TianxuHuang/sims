from django.shortcuts import render
from django.shortcuts import redirect
from .models import Class


from django.core.paginator import Paginator

def list_class(request):
    name = request.GET.get('name', '')
    classes = Class.objects.all()
    if name:
        classes = classes.filter(name__icontains=name)
    
    paginator = Paginator(classes, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'name': name
    }
    
    return render(request, 'classes/list_class.html', context)


def add_class(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Class.objects.create(name=name)
        return redirect('classes:list_class')
    return render(request, 'classes/add_class.html')


from django.shortcuts import get_object_or_404

def edit_class(request, pk):
    class_obj = get_object_or_404(Class, pk=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        class_obj.name = name
        class_obj.save()
        return redirect('classes:list_class')
    return render(request, 'classes/edit_class.html', {'class': class_obj, 'pk': pk})


def delete_class(request, pk):
    class_obj = get_object_or_404(Class, pk=pk)
    if request.method == 'POST':
        class_obj.delete()
        return redirect('classes:list_class')
    return render(request, 'classes/delete_class.html', {'class': class_obj, 'pk': pk})
