from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def render_html(request):
    return render(request,'render_html.html')

def http_Response(request):
    return HttpResponse('this response is returned by http_Response')