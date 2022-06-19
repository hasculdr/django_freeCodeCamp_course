from django.shortcuts import render

def index(request):
    test = {'key1': [1, 2], 'key2': 'value2'}
    return render(request, 'test_phonebook/index.html', test)
