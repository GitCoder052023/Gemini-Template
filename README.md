# Introduction

Are you eager to explore the incredible capabilities of Gemini models? Look no further than this versatile Python template, designed to empower you to create engaging text-based and image-driven conversations with AI! It seamlessly integrates with Google's cutting-edge Gemini Pro and Gemini Pro Vision models, unlocking a realm of possibilities for meaningful interactions.

# Key Features:

- **Text-based Chat**: Converse naturally with the model through text-based prompts, diving into open-ended discussions or exploring a vast range of topics.
- **Image-Driven Chat**: Enhance conversations by incorporating visual elements. Share images and receive insightful responses that blend understanding of text and visuals.
- **Video-Enhanced Chat**: Engage in interactive dialogues based on video content. The model meticulously analyzes frames, extracting context and generating responses that align with both the video and your queries.
- **Customization**: Tailor the code to your specific needs, adjusting model preferences, voice settings, and conversation prompts.

# Get Started:

# How to import template?

All you need to do that first download the template and then create a new python file and then simply open template in same directory in which you want to use this template then go to you main file and paste this python line to initiate Gemini_template and use Gemini models:
```Python
from Gemini_Template import *

gemini = Gemini(key="YOUR GEMINI API KEY")

gemini.Gemini_Pro_chat() # REPLACE THE MODEL NAME AS PER YOUR NEED
```
# Setup API Key:

1 - **Obtain a Gemini API Key**: Visit this official website to acquire your API key: https://makersuite.google.com/app/apikey

2 - **Install Necessary Libraries**: Utilize Python's package manager to install the required libraries: 

- google-generativeai, 
- PIL,
- pyttsx3,
- cv2

**You can use this pip command to install required modules:**
```bash
pip install google-generativeai pillow pyttsx3 cv2
```

3 - **Incorporate Your API Key**: Within the code, replace "YOUR GEMINI API KEY" with your actual API key.

4 - **Initiate Conversations**: Choose your preferred interaction mode:

- **Gemini_Pro_chat()** for text-based conversations
- **Gemini_Pro_Vision_chat()** for image-based interactions
- **Gemini_Vision_Video_chat()** for video-based dialogues
