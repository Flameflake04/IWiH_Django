from django.shortcuts import render, HttpResponse
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings
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
    media_folder = os.path.join(settings.BASE_DIR, 'media')

    if request.method == 'POST' and request.FILES.get('pdf_file'):
        # Delete existing PDF files in the media folder
        for filename in os.listdir(media_folder):
            if filename.endswith('.pdf'):
                file_path = os.path.join(media_folder, filename)
                os.remove(file_path)  # Remove the file

        # Save the new file
        uploaded_file = request.FILES['pdf_file']
        fs = FileSystemStorage(location=media_folder)
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)

    return render(request, 'pdfUpload.html', context)