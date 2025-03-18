import pdfplumber
import openai
import os
import django
from dotenv import load_dotenv
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iWiH_Django.settings')
django.setup()
class GenderDisease():
    def __init__(self, pdf_path):
        self.pdf_path = os.path.join(settings.MEDIA_ROOT, pdf_path)
        self.title = "Title not found"
    def extract_title_with_largest_font(self, pdf_path):
        with pdfplumber.open(pdf_path) as pdf:
            first_page = pdf.pages[0]
            words = first_page.extract_words()

            for word in words[:5]:
                print(word)

            words_sorted = sorted(words, key=lambda x: -x['bottom'] + x['top'])

            possible_title = [word['text'] for word in words_sorted[:10]]  
            self.title = ' '.join(possible_title)
            print(self.title)
            return self.title 
    
    def open_AI_classification(self):
        load_dotenv()
        openai.api_key = os.getenv("OPEN_AI_KEY")
        self.extract_title_with_largest_font(self.pdf_path)
        messages = [
            {"role": "user", "content": f"Classify the gender orientation of the research paper based ON ONLY the diseases on the title (not the gender). The title is: '{self.title}'. The options are 'male', 'female', or 'neutral'."}
        ]
        response = openai.ChatCompletion.create(
        model="gpt-4",  
        messages=messages,
        max_tokens=10, 
        temperature=0  
        )
        return response['choices'][0]['message']['content'].strip()
    

if __name__ == "__main__":
    genderDisease = GenderDisease("HotFlashes.pdf")
    print(genderDisease.open_AI_classification())
