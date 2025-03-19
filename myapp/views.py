from django.shortcuts import render, HttpResponse
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings
import sys


# Now import PaperAnalysis from model
# from model import PaperAnalysis

def home(request):
    # analyzer = PaperAnalysis(os.path.join(settings.MEDIA_ROOT, "sample1.pdf"))
    return render(request, "home.html")

def resultHTML(request):
    return render(request, "result.html")

def about(request):
    return render(request, "about.html")

def future(request):
    return render(request, "future.html")


def uploadPdf(request):
    context = {}
    media_folder = os.path.join(settings.BASE_DIR, 'media')

    if request.method == 'POST' and request.FILES.get('pdf_file'):
        # Delete existing PDF files in the media folder
        for filename in os.listdir(media_folder):
            if filename.endswith('.pdf'):
                file_path = os.path.join(media_folder, filename)
                os.remove(file_path) 

        # Save the new file
        uploaded_file = request.FILES['pdf_file']
        fs = FileSystemStorage(location=media_folder)
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)

    return render(request, 'pdfUpload.html', context)