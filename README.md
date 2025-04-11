# NextF1 API

## Overview
The NextF1 API provides access to the upcoming Formula 1 events, allowing users to fetch details about practice sessions, qualifying rounds, sprints, and races. This API is built using Python and utilizes the FastAPI framework for handling requests.

## Project Structure
```
NextF1-API
├── src
│   ├── main.py          # Main logic for fetching and displaying F1 events
│   ├── api.py           # API endpoints for accessing event data
│   └── utils
│       └── __init__.py  # Utility functions and classes
├── requirements.txt      # Project dependencies
├── Dockerfile             # Docker image instructions
├── .gitignore             # Files and directories to ignore in Git
├── README.md              # Project documentation
└── tests
    └── test_api.py       # Unit tests for the API
```

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/NextF1-API.git
   cd NextF1-API
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```bash
   uvicorn src.api:app --reload
   ```

## Usage
Once the application is running, you can access the API at `http://127.0.0.1:8000`. The following endpoints are available:

- **GET /events**: Retrieve a list of upcoming F1 events.
- **GET /events/{event_id}**: Retrieve details for a specific event.

## Testing
To run the tests, ensure your virtual environment is activated and execute:
```bash
pytest tests/test_api.py
```

## Docker
To build and run the application in a Docker container, use the following commands:

1. **Build the Docker Image**
   ```bash
   docker build -t nextf1-api .
   ```

2. **Run the Docker Container**
   ```bash
   docker run -p 8000:8000 nextf1-api
   ```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.