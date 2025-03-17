from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello World")

def uploadPdf(request):
    return render(request, "pdfUpload.html")

def resultHTML(request):
    pass

