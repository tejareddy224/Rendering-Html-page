from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def http_Response(request):
    return HttpResponse('<center><h1>this response is from  app2 </h1></center>')

def render_html2(request):
    return render(request,'render_html2.html')
