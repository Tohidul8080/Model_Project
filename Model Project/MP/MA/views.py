from django.shortcuts import render
from django.http import HttpResponse
from MA.models import student, shart

# Create your views here.

def index(request):
    student_list=student.objects.order_by('First_name')
    shart_list=shart.objects.order_by('shart_name')
    diction={'student':student_list, 'shart':shart_list,}
    return render(request, 'index.html', context=diction)
