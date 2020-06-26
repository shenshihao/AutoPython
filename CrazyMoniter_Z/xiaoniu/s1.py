from django.shortcuts import HttpResponse


def index(request):
    return HttpResponse('一米')
