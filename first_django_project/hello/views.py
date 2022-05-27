from django.http import HttpResponse

# Create your views here.
def diy(request):
    visits_counter = request.session.get('visits_counter', 0) + 1
    request.session['visits_counter'] = visits_counter
    resp = HttpResponse('view count='+str(visits_counter))
    resp.set_cookie('dj4e_cookie', '1a2d4440', max_age=10)
    return resp
