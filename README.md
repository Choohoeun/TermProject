# T5-Based Korean Text Summarization Program

This project is a Flask web application that uses a T5-based Korean text summarization model to summarize lengthy documents into concise and clear summaries.

## Features

- Generate concise summaries from lengthy Korean texts
- Utilizes T5 model (paust/pko-t5-base)
- Provides a user-friendly web interface built on Flask

## Installation and Setup

### 1. Requirements
To run this project, you need the following:

Python 3.8 or higher
PyTorch
Transformers
Flask

### 2. Installation

Run the following commands to set up the project:

```sh
# Clone the repository
git clone <repository_link>
cd <project_directory>

# (Optional) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
```

### 3. Run the Application
You can run the application using one of the following files:

#### Single File (main.py):

```sh
python main.py
```
#### Modular Version (app.py):
```sh
python app.py
```

### 4. Access the Application
Open your browser and navigate to http://127.0.0.1:5000. Enter your text and click the "Summarize" button.

## Code Structure

### 1. main.py
Initializes the T5 model
Defines functions for text summarization
Runs the web application

### 2. app.py
Calls summarization functions from main.py to serve a Flask web application

## Notes

Input documents are limited to a maximum of 512 tokens. Longer texts are truncated automatically.
Summary generation may take some time depending on model parameters.

## Contribution

To contribute to this project, fork the repository and submit your improvements via a Pull Request.

## License

This project is distributed under the Apache 2.0 License.
