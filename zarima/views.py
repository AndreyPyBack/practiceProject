from django.shortcuts import render


def index(request):
    data = {'one': 1,
            'two': 2,
            }
    return render(request,'test.html', {'data':data})