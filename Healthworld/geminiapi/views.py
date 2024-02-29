from django.shortcuts import render


from django.shortcuts import render
from .forms import ImageUploadForm

from PIL import Image


import google.generativeai as genai
genai.configure(api_key="AIzaSyDl1SfdgcHfha9YdGCmje9V8V88GzyMfGk")


def process_image(request):

    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            imagedata = Image.open(image)
            response = get_gemini_response(imagedata)
            return render(request, 'output.html', {'image_description': response})
    else:
        form = ImageUploadForm()
    return render(request, 'inputform.html')

def get_gemini_response(imagedata):
    input = """Reply only if image is related to food or not 
    if image is related to food 
    in first paragraph tell about the food in second paragraph give calories of the food and 
    in third paragraph tell how it helps or affects to health and affects to heart ,diabetes disease
    else reply give me only food related image"""
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input,imagedata])
    return response.text