from django.shortcuts import render, get_object_or_404, redirect

from cv.forms import BasicForm, EducationForm, WorkForm
from cv.models import Basic, Education, Work


def cv_list(request):
    basic = Basic.objects.order_by('id')
    education = Education.objects.order_by('id')
    work = Work.objects.order_by('id')
    return render(request, 'cv/cv_list.html', {'basic': basic, 'education': education, 'work': work})


def basic_edit(request, pk):
    basic = get_object_or_404(Basic, pk=pk)
    if request.method == "POST":
        form = BasicForm(request.POST, instance=basic)
        if form.is_valid():
            basic = form.save(commit=False)
            basic.save()
            return redirect('cv')
    else:
        form = BasicForm(instance=basic)
    return render(request, 'cv/form_edit.html', {'form': form, 'title': 'basic'})


def basic_new(request):
    if request.method == "POST":
        form = BasicForm(request.POST)
        if form.is_valid():
            basic = form.save(commit=False)
            basic.save()
            return redirect('cv')
    else:
        form = BasicForm()
    return render(request, 'cv/form_edit.html', {'form': form, 'title': 'basic'})


def education_edit(request, pk):
    education = get_object_or_404(Education, pk=pk)
    if request.method == "POST":
        form = EducationForm(request.POST, instance=education)
        if form.is_valid():
            education = form.save(commit=False)
            education.save()
            return redirect('cv')
    else:
        form = EducationForm(instance=education)
    return render(request, 'cv/form_edit.html', {'form': form, 'title': 'education'})


def education_new(request):
    if request.method == "POST":
        form = EducationForm(request.POST)
        if form.is_valid():
            education = form.save(commit=False)
            education.save()
            return redirect('cv')
    else:
        form = EducationForm()
    return render(request, 'cv/form_edit.html', {'form': form, 'title': 'education'})


def work_edit(request, pk):
    work = get_object_or_404(Work, pk=pk)
    if request.method == "POST":
        form = WorkForm(request.POST, instance=work)
        if form.is_valid():
            work = form.save(commit=False)
            work.save()
            return redirect('cv')
    else:
        form = WorkForm(instance=work)
    return render(request, 'cv/form_edit.html', {'form': form, 'title': 'Experience'})


def work_new(request):
    if request.method == "POST":
        form = WorkForm(request.POST)
        if form.is_valid():
            work = form.save(commit=False)
            work.save()
            return redirect('cv')
    else:
        form = WorkForm()
    return render(request, 'cv/form_edit.html', {'form': form, 'title': 'Experience'})
