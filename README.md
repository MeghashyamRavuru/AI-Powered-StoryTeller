# AI-Powered Story Teller

AI-Powered Story Teller is a web application that generates educational stories tailored to different age groups and topics using Google's Gemini generative models and Google's Text-to-Speech and Speech-to-Text APIs.

## Features

- **Story Generation**: Generate stories based on the topic and age group of the user.
- **Speech-to-Text**: Convert spoken words to text to be used as the story topic.
- **Text-to-Speech**: Convert the generated story text into spoken words.

## Tech Stack

- **Frontend**: HTML, CSS (TailwindCSS), JavaScript
- **Backend**: Flask (Python)
- **APIs**: Google Cloud Vertex AI, Google Cloud Speech-to-Text, Google Cloud Text-to-Speech

## Setup and Installation

### Prerequisites

- Python 3.10 or higher
- Google Cloud account
- Google Cloud SDK

### Steps

1. **Clone the repository**

    ```sh
    git clone https://github.com/yourusername/AI-Powered-StoryTeller.git
    cd AI-Powered-StoryTeller
    ```

2. **Create and activate a virtual environment**

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**

    ```sh
    pip install -r requirements.txt
    ```

4. **Run the application**

    ```sh
    python3 main.py
    ```

5. **Access the application**

    Open your browser and navigate to `http://localhost:8080`.

## Deployment

This project can be deployed using Google Cloud Run. Follow these steps:

1. **Build and deploy the service**

    ```sh
    cd AI-Powered-StoryTeller
    gcloud run deploy --source=.
    ```

2. **Follow the command prompts to complete the deployment**

## Usage

1. **Generate a Story**

    - Enter a topic in the input field.
    - Select the age group and desired story length.
    - Click "Generate Story".

2. **Speech-to-Text**

    - Click the microphone icon to start recording your speech.
    - Speak the topic you want to generate a story about.
    - The text field will be automatically populated with the transcribed text.

3. **Text-to-Speech**

    - After generating a story, click the speaker icon to listen to the story.

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- [Google Cloud](https://cloud.google.com/) for providing the APIs used in this project.
- [TailwindCSS](https://tailwindcss.com/) for the UI styling.
