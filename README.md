# pdf-openai-app

## Description and Background
The pdf-openai-app is a demo application crafted during a 48-hour hackathon. Developed entirely from scratch, this project involved an immersive journey into enhancing Python coding skills and integrating the OpenAI API within the limited timeframe. Its purpose is to modify PDF files, such as high school student materials, to make them more convenient according to the student's learning style. The app takes a PDF file as input, allows the user to choose a learning style, and upon pressing a button, sends the PDF to be processed using the OpenAI API. The app then displays the resulting text and a picture generated using DALL-E.

## Installation
1. Install Python (at least Python 3.x) on your system.
2. Install the required dependencies using the following command:
   ```bash
   pip install -r requirements.txt
3. Set the OpenAI API key (`API_KEY`) as an environment variable.

## Usage
1. Run the application using the following command:
    ```bash
   python main_app.py
&rarr;  The app will open a user-friendly interface for processing PDFs.

2. Choose a PDF file, select a learning style, and click the processing button.
&rarr;  The app will use the OpenAI API to modify the PDF and display the result text and generated image.

## Dependencies/Requirements
* Python (at least Python 3.x)
* openai
* PyPDF2
* os
* tkinter
* PIL (Pillow)
* requests

## Important note
Ensure that you have set up the OpenAI API key as an environment variable named OpenAI `API_KEY` before running the application.

## Other notes
There is AI-generated small pdf about frog's anatomy (`Frog_anatomy_example_material.pdf`) on this directory to be used as an example input file if needed.