from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['student_id'].widget.attrs['readonly'] = True
            self.fields['student_id'].widget.attrs['class'] = 'form-control bg-light'

    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'student_id': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'student_id': '学号',
            'name': '姓名',
            'birthday': '生日',
            'gender': '性别',
            'phone': '电话',
            'email': '邮箱',
            'address': '家庭地址',
            'avatar': '头像',
        }
