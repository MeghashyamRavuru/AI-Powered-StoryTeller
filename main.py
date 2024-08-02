import io
import os
import random
from flask import Flask, render_template, request, jsonify, send_file
import vertexai
from vertexai.generative_models import GenerativeModel
import vertexai.preview.generative_models as generative_models
from google.cloud import speech
import google.cloud.texttospeech as tts

app = Flask(__name__)

PROJECT_ID = "XXXXX"          #Rename with your project ID
LOCATION = "us-central1"      #You can use any other location also

#Initiating the Vertex AI
vertexai.init(project=PROJECT_ID, location=LOCATION)

#System Instructions for the model
textsi_1 = """<<Role>>
You are a person who explains any topic with a story.

<<Level of Expertise>>
You are an expert storyteller who knows which story is best to explain a specific topic based on the educational level of the end user.

<<Objective>>
The objective of this story generation is to help students of different educational levels learn about different topics by using storytelling methods.

<<GUIDELINES>>
You have to generate a story based on the level of the student.
You should not generate a story if a user asks about a person unless he is a famous person, you have to say like \\\"I don\\\'t know who is <name>, sorry for the inconvenience ask me about something else\\\".
If you cannot generate a story that adheres to your constraints, never generate a random story. Instead, politely inform the user that you are unable to create a story that meets their specific requirements.\"\"\""""

model = GenerativeModel(
    model_name="gemini-1.5-flash-001",
    system_instruction=[textsi_1],
)

generation_config = {
    "max_output_tokens": 8192,
    "temperature": 1,
    "top_p": 0.95,
}

safety_settings = {
    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    topic = request.form.get('topic')
    age_group = request.form.get('age')
    length = request.form.get('length')

    prompt = topic + f". For {age_group if age_group else 'all'} years old students." + f" Generated story should be {length if length else 'medium'} in length."

    try:
        responses = model.generate_content(
            [prompt],
            generation_config=generation_config,
            safety_settings=safety_settings,
            stream=True,
        )

        response_text = ""

        for i in responses:
            response_text += i.text

        return jsonify({"text": response_text})
    except Exception as e:
        error_texts = ["Please try again after sometime.", "Gemini Overloaded.", "Due to high traffic Gemini took rest.", "It's not you, It's us!!", "Can you comeback after sometime?", "We are with limited resources, so can you wait some time for us!!"]
        selected_error = random.choice(error_texts)
        # print(e)
        return jsonify({"text": selected_error})

@app.route('/speech-to-text', methods=['POST'])
def speech_to_text_route():
    audio_data = request.files['audio_data'].read()

    client = speech.SpeechClient()
    audio = speech.RecognitionAudio(content=audio_data)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.WEBM_OPUS,
        sample_rate_hertz=48000,
        language_code="en-US",
    )

    response = client.recognize(config=config, audio=audio)

    if not response.results:
        return jsonify({"text": "Could not transcribe audio"}), 400

    transcript = response.results[0].alternatives[0].transcript

    return jsonify({"text": transcript})

@app.route('/text-to-speech', methods=['POST'])
def text_to_speech_route():
    text = request.json['text']
    voice_name = "en-US-Standard-C"
    
    language_code = "-".join(voice_name.split("-")[:2])
    text_input = tts.SynthesisInput(text=text)
    voice_params = tts.VoiceSelectionParams(
        language_code=language_code, name=voice_name
    )
    audio_config = tts.AudioConfig(audio_encoding=tts.AudioEncoding.MP3)
    
    client = tts.TextToSpeechClient()
    response = client.synthesize_speech(
        input=text_input,
        voice=voice_params,
        audio_config=audio_config,
    )
    
    audio_content = io.BytesIO(response.audio_content)
    audio_content.seek(0)
    
    return send_file(audio_content, mimetype="audio/mp3")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
