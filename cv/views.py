from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from cv.forms import BasicForm
from cv.models import Basic


def cv_list(request):
    basics = Basic.objects.order_by('id')
    return render(request, 'cv/cv_list.html', {'info': basics})


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
    return render(request, 'cv/basic_edit.html', {'form': form})


def basic_new(request):
    if request.method == "POST":
        form = BasicForm(request.POST)
        if form.is_valid():
            basic = form.save(commit=False)
            basic.save()
            return redirect('cv')
    else:
        form = BasicForm()
    return render(request, 'cv/basic_edit.html', {'form': form})
