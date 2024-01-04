import pathlib
import google.generativeai as genai
import PIL.Image
import pyttsx3
import cv2



class Gemini:
    def __init__(self, key):
        self.key = key
        self.engine = pyttsx3.init()
        self.engine.setProperty('voice',
                                'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')

    def Gemini_Pro_chat(self):
        genai.configure(api_key=self.key)
        model = genai.GenerativeModel("gemini-pro")
        messages = []

        while True:
            user_input = input("You: ")
            messages.append({
                "role": "user",
                "parts": [user_input],
            })

            response = model.generate_content(messages)

            messages.append({
                "role": "model",
                "parts": [response.text],
            })

            print("Gemini: " + response.text)

    def Gemini_Pro_Vision_chat(self, path):
        genai.configure(api_key=self.key)
        model = genai.GenerativeModel("gemini-pro-vision")
        img = PIL.Image.open(path)

        messages = []

        while True:
            message = input("You: ")
            print("Recognizing...")
            messages.append({
                "role": "user",
                "parts": [message, [img]],
            })

            response = model.generate_content([message, img], stream=True)
            response.resolve()

            messages.append({
                "role": "model",
                "parts": [response.text],
            })

            print("Gemini: " + response.text)

    def Gemini_Vision_Video_chat(self, path, frame_path):
        genai.configure(api_key=self.key)
        model = genai.GenerativeModel("gemini-pro-vision")

        # Define video path and frame saving path
        video_path = path
        frame_path = frame_path  # Ensure this directory exists

        # Open the video capture
        cap = cv2.VideoCapture(video_path)

        messages = []

        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()

            if not ret:
                break  # End of video

            # Save the frame as a JPEG image
            frame_name = f"frame_{cap.get(cv2.CAP_PROP_POS_FRAMES)}.jpg"
            frame_path_full = pathlib.Path(frame_path) / frame_name
            cv2.imwrite(str(frame_path_full), frame)

            # Load the saved image
            img = PIL.Image.open(frame_path_full)

            # Get query from user
            message = input("You: ")
            print("Generating Answer sir, Please wait")
            messages.append({
                "role": "user",
                "parts": [message, [img]],
            })

            response = model.generate_content([message, img], stream=True)
            response.resolve()

            messages.append({
                "role": "model",
                "parts": [response.text],
            })

            print("Gemini: " + response.text)

        # Release video capture
        cap.release()


Note = '''
gemini = Gemini(key="YOUR GEMINI API KEY")

#Example usage:
gemini.Gemini_Pro_chat()
'''  # use this line when you want to initialize this template