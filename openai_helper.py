# API_KEY = 'insert here the real key if not setting the environment variable'

import openai
import PyPDF2
import os

# Uncomment next line (and comment the next below that) if not setting the environment variable
# openai.api_key = API_KEY 
openai.api_key = os.getenv('API_KEY')
image_prompt = ''

def extract_text_from_pdf(file_path):
    pdf_file_obj = open(file_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file_obj)
    text = ""
    for page_num in range(len(pdf_reader.pages)):
        page_obj = pdf_reader.pages[page_num]
        text += page_obj.extract_text()
    pdf_file_obj.close()
    return text

def rewrite_text(text, learning_type):
    global image_prompt
    response = openai.chat.completions.create(model="gpt-4",
    messages=[
          {"role": "system", "content": "You are a helpful assistant and great pedagogy."},
          {"role": "user", "content": text},
          {"role": "user", "content": "Convert this to learning material for high school student, whos learning type is " + learning_type},
      ]).choices[0].message.content
    
    response2 = openai.chat.completions.create(model="gpt-3.5-turbo",
    messages=[
          {"role": "system", "content": "You are a helpful assistant and great pedagogy."},
          {"role": "user", "content": response},
          {"role": "user", "content": "What would be the best prompt to get the best image to visualize this content when giving the prompt to dall-e-3?"}
      ])
    image_prompt = response2.choices[0].message.content
    return response

def generate_image():
    global image_prompt
    response = openai.images.generate(
        model="dall-e-3",
        prompt=image_prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    return response.data[0].url
