from django.shortcuts import get_object_or_404, render


def index(request):

    data = {
        "ip": '192.168.1.1',
        "online": 'text'
    }
    return render(request, 'demo.html', {'data': data})
