from django.shortcuts import render

from cv.models import Basics


def cv_list(request):
    basics = Basics.objects.order_by('id')
    return render(request, 'cv/cv_list.html', {'info': basics})
