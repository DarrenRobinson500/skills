from django.shortcuts import render,redirect
from .models import People, Skill, Score, File
from .forms import FileForm
import openpyxl as xl


def people_list(request):
    list = People.objects.all().order_by('name')
    return render(request, 'people_list.html', {'list': list})

def skill_list(request):
    list = Skill.objects.all().order_by('category')
    return render(request, 'skill_list.html', {'list': list})

def skill_upload(request):
    try:
        wb = xl.load_workbook('media/files/skills.xlsx')
        sheet = wb['Sheet1']
    except:
        list = Skill.objects.all().order_by('category')
        error = True
        return render(request, 'skill_list.html', {'list': list, 'error': error})
    for row in range(2, sheet.max_row + 1):
        category = sheet.cell(row, 1).value
        level = sheet.cell(row, 2).value
        description = sheet.cell(row, 3).value
        if Skill.objects.filter(description=description).count() == 0:
            new_item = Skill(category=category, level=level, description=description)
            new_item.save()
    return redirect('skill_list')



def file_list(request):
    list = File.objects.all().order_by('name')
    return render(request, 'file_list.html', {'list': list})

def file_upload(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = FileForm()
    return render(request, 'file_upload.html',{'form':form})

def file_delete(request, file_id):
    if request.method == 'POST':
        file = File.objects.get(pk=file_id)
        file.delete()
    return redirect('file_list')

