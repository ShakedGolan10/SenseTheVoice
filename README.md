# Grammar Correction and Transcription Service

Welcome to the **Grammar Correction and Transcription Service**! This Python-based server combines advanced speech-to-text transcription and grammar correction capabilities. You can upload an audio file along with its language, and the server will return the transcribed text and its corrected version.

---

## Features

- **Audio Transcription**: Converts speech in an audio file into text.
- **Grammar Correction**: Fixes grammatical mistakes in the transcribed text.
- **Output Structure**: The server returns a JSON response with both the raw transcription and the corrected text.

### Example Output

```json
{
  "transcription": " I am learn to walk again after high. Have a ninja by a car accident.",
  "fixed_text": "I am learning to walk again after high school. I was a ninja by "
}
```

---

## Installation and Setup

### Prerequisites

Ensure you have Python 3.10 or higher installed on your system.

### Step 1: Clone the Repository

```bash
git clone <repository_url>
cd <repository_folder>
```

### Step 2: Install Requirements

Install the required dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Step 3: Set Up Virtual Environment

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 4: Run the Server

Use Uvicorn to run the server locally:

```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

The server will be available at `http://127.0.0.1:8000`.

---

## Usage

### Endpoint: `/api/v1/transcribe-and-analyze`

**Method**: POST

Send a `formData` request to this endpoint with the following fields:

- `audio_file`: The audio file to transcribe (File).
- `language`: The language of the audio (string).

#### Example Request (using cURL)

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/transcribe-and-analyze" \
-H "Content-Type: multipart/form-data" \
-F "audio_file=@path_to_your_audio_file.wav" \
-F "language=en"
```

#### Example Response

```json
{
  "transcription": " I am learn to walk again after high. Have a ninja by a car accident.",
  "fixed_text": "I am learning to walk again after high school. I was a ninja by "
}
```

---

## Notes

- Ensure the audio file is in a supported format (e.g., WAV, MP3).
- Use the appropriate language code for the `language` field (e.g., `en` for English).

---

Thank you for using the **Grammar Correction and Transcription Service**! If you have any issues, feel free to report them. Happy transcribing and editing!
