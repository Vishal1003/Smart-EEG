from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

import EEG as eg
import pandas as pd



def index(request):
    return render(request, 'index.html')


def register(request):
    return render(request, 'form.html')


def data(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES.get('document')
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)

    return render(request, 'data.html', context)


def user(request):
    fname = request.GET['fname']
    lname = request.GET['lname']
    email = request.GET['email']
    age = request.GET['age']
    gender = request.GET['gender']
    phone = request.GET['phone']
    return render(request, 'data.html', {'fname': fname, 'lname': lname, 'email': email, 'age': age, 'gender': gender, 'phone': phone})


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        context['url'] = url
        data = eg.predict(pd.read_csv("/home/sjsingh/Desktop/Smart EEG/WebApp"+url))
        print(data)
    return render(request, 'result.html',{'data': data})
