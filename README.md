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
- Google Cloud account with billing enabled
- Google Cloud SDK

### Steps

1. **Install [Google Cloud CLI](https://cloud.google.com/sdk/docs/downloads-snap)**

    ```sh
    snap install google-cloud-cli --classic
    gcloud init
    ```

    Afterward, you will be prompted to sign in. Sign in with your Google Cloud account. Now choose your billing-linked project or create a new project and link it with a billing-enabled account.

    ```sh
    gcloud auth application-default login
    ```

    You will be prompted to sign in with your Google Cloud account again. Complete the sign-in process.

2. **Clone the repository**

    ```sh
    git clone https://github.com/MeghashyamRavuru/AI-Powered-StoryTeller.git
    cd AI-Powered-StoryTeller
    ```

3. **Create and activate a virtual environment**

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. **Add your Project ID**

    In `main.py`, replace `XXXXXX` with your project ID:

    ```python
    PROJECT_ID = "XXXXXX"
    ```

5. **Install dependencies**

    ```sh
    pip install -r requirements.txt
    ```

6. **Run the application**

    ```sh
    python3 main.py
    ```

7. **Access the application**

    Open your browser and navigate to `http://localhost:8080`.

## Deployment

This project can be deployed using Google Cloud Run. Follow these steps:

1. **Build and deploy the service**

    In the Google Cloud terminal, run:

    ```sh
    cd AI-Powered-StoryTeller
    gcloud run deploy --source=.
    ```

    You will be prompted to enter a name for your service (e.g., "ai"). Choose the corresponding number for the region (e.g., "us-central1" or your preferred location). Say "y" when asked if you want to allow unauthenticated invocations. Note that we are allowing unauthenticated access here because this is a demo application. It is recommended to use appropriate authentication for enterprise and production applications.

2. **Access the deployed service**

    Once the deployment is complete, you should get a link similar to:

    ```
    https://ai-*****eua-uc.a.run.app/
    ```

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
