from django.shortcuts import render, get_object_or_404, redirect

from cv.forms import BasicForm, EducationForm, WorkForm, GradeForm
from cv.models import Basic, Education, Work, Grade


def cv_list(request):
    basic = Basic.objects.order_by('id')
    education = Education.objects.order_by('id')
    work = Work.objects.order_by('id')
    grade = Grade.objects.order_by('id')
    return render(request, 'cv/cv_list.html', {'basic': basic, 'education': education, 'work': work, 'grade': grade})


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


def grade_edit(request, epk, gpk):
    grade = get_object_or_404(Grade, pk=gpk)
    if request.method == "POST":
        form = GradeForm(request.POST, instance=grade)
        if form.is_valid():
            grade = form.save(commit=False)
            grade.education=Education.objects.get(pk=epk)
            grade.save()
            return redirect('cv')
    else:
        form = GradeForm(instance=grade)
    return render(request, 'cv/form_edit.html', {'form': form, 'title': 'grade'})


def grade_new(request,epk):
    if request.method == "POST":
        form = GradeForm(request.POST)
        if form.is_valid():
            grade = form.save(commit=False)
            grade.education=Education.objects.get(pk=epk)
            grade.save()
            return redirect('cv')
    else:
        form = GradeForm()
    return render(request, 'cv/form_edit.html', {'form': form, 'title': 'grade'})
