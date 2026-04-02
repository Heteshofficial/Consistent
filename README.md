# Hate Storyline Detector

## Overview
The Hate Storyline Detector is a sophisticated system designed to identify and analyze hate speech in various contexts.

## Features
- **Real-time Detection**: Monitors content for hate speech in real time.
- **Multi-language Support**: Capable of detecting hate speech in multiple languages.
- **Customizable Thresholds**: Users can set sensitivity levels for detection.
- **User-friendly Interface**: Intuitive GUI for easy navigation.

## Agents
- **Detection Agent**: Analyzes input text and identifies potential hate speech.
- **Reporting Agent**: Generates reports on detected hate speech instances.
- **Feedback Agent**: Allows users to provide feedback on detections for improving the model.

## Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Heteshofficial/Consistent.git
   cd Consistent
   ```
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the database:
   ```bash
   python setup_database.py
   ```

## Usage Examples
To run the detection system:
```bash
python detect_hate.py "sample text to analyze"
```
To view reports:
```bash
python view_reports.py
```

## API Endpoints
- `POST /detect`: Analyzes the input text for hate speech.
- `GET /reports`: Retrieves a list of reports on detected hate speech.

## Troubleshooting
- **Issue**: Detection fails with error code 500.
  - **Solution**: Check if the database is correctly set up and running.
  
- **Issue**: API endpoint returns a 404 error.
  - **Solution**: Ensure the server is running and the endpoint is correctly spelled.