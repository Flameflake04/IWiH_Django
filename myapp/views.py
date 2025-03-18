from django.shortcuts import render, HttpResponse
from django.core.files.storage import FileSystemStorage
# Create your views here.


def home(request):
    return render(request, "home.html")

'''
def uploadPdf(request):
    return render(request, "pdfUpload.html")
'''
def resultHTML(request):
    pass

def uploadPdf(request):
    context = {}
    if request.method == 'POST' and request.FILES['pdf_file']:
        uploaded_file = request.FILES['pdf_file']
        fs = FileSystemStorage(location='media')  # Save to the media folder
        name = fs.save(uploaded_file.name, uploaded_file)  # Save the file
        context['url'] = fs.url(name)  # Get the URL to access the file
    return render(request, 'pdfUpload.html', context)