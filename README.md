# NextF1 API

## Overview
The NextF1 API is primarily made to simply get the where, date and time to sessions for the next race weekend. Will probably expand later. Built using Python and utilizes the Flask framework for handling requests, Fast-F1 library for data.
F1 clock hanged on the wall?

## Project Structure
```
NextF1-API
├── src
│   ├── main.py          # Main entry point for the Flask application
│   ├── routes
│   │   └── events.py    # Blueprint for handling event-related routes
│   ├── services
│   │   └── events_service.py  # Business logic for event-related operations
│   └── utils
│       └── __init__.py  # Utility functions and classes
├── requirements.txt      # Project dependencies
├── Dockerfile             # Docker image instructions
├── .gitignore             # Files and directories to ignore in Git
├── README.md              # Project documentation
└── tests
    └── test_events.py    # Unit tests for the events blueprint
```

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/0hscar/NextF1-API.git
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
   python src/main.py
   ```

## Usage
Once the application is running, you can access the API at `http://127.0.0.1:5000`. The following endpoint is available:

- **GET /events/next**: Retrieve date & time to the next F1 weekends events. 
- More to come.



## Testing
To run the tests, ensure your virtual environment is activated and execute:
```bash
pytest tests/test_events.py
```

## Docker
To build and run the application in a Docker container, use the following commands:
NOTE: NOT TESTED

1. **Build the Docker Image**
   ```bash
   docker build -t nextf1-api .
   ```

2. **Run the Docker Container**
   ```bash
   docker run -p 5000:5000 nextf1-api
   ```

3. **Alternatively run docker-compose**
   ```bash
   docker-compose up --build
   ```


## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.