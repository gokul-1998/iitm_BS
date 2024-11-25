
# Custom Authentication Flask Application

This project implements a custom authentication mechanism with two main components:
1. A **Flask Backend Server** to handle authentication requests.
2. A **Desktop Client** to send requests to the backend server.

## Key Features

- Authentication via `SEEK-CUSTOM-AUTH` header containing `username`, `password`, and `machine ID`.
- Each machine ID is uniquely associated with a user upon first authentication.
- Users can only authenticate with their associated machine IDs.

---

## Setup Instructions

### Prerequisites

- **Python 3** installed on your system.
- **pip** (Python package manager) installed.

---

### Steps to Run the Project

1. **Clone the repository:**

   ```bash
   git clone https://github.com/gokul-1998/iitm_BS
   cd https://github.com/gokul-1998/iitm_BS
   ```

2. **Create and activate a virtual environment:**

   **On Linux/Mac:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   **On Windows:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask Backend Server:**

   Navigate to the `app` directory and start the server:
   ```bash
   flask run
   ```

5. **Use the Desktop Client:**

   Run the `client.py` file to interact with the server:
   ```bash
   python client.py
   ```


---

### Backend Command Line Utilities

The backend includes the following CLI commands to manage users:
- **To see list of commands**
  ```bash
   flask --help
   ```


- **Add a user:**
  ```bash
  flask add_user
  ```

- **Update a user's password:**
  ```bash
  flask update_user
  ```

---

## Directory Structure

```plaintext
.
├── app.py                  # Main Flask app
├── client.py               # Desktop client script
├── client_utils.py         # Helper utilities for the client
├── config.py               # Configuration settings
├── docs
│   └── clarifications
│       └── extras.md       # Additional clarifications
├── instance
│   ├── app.db              # Application database
│   └── test.db             # Test database
├── migrations              # Database migration files
├── project
│   ├── auth_utils.py       # Authentication utilities
│   ├── checks              # Additional functionality
│   └── models.py           # Database models
├── scripts
│   ├── format_check.py     # Script for formatting checks
│   └── lint.py             # Linter script
├── tests                   # Automated test cases
│   ├── functional          # Functional tests
│   ├── unit                # Unit tests
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies
└── Todo.md                 # Pending tasks
```

---

## Testing

Automated tests are included to validate the application's functionality. To run tests:

```bash
pytest tests
```

To run with coverage:
  ```bash
  pytest --cov=project tests
  ```

---

## How It Works

1. **First-Time Authentication:**
   - The backend associates the `machine ID` with the provided `username` and `password`.

2. **Subsequent Requests:**
   - Requests succeed only if the `machine ID` matches the one associated with the `username`.

3. **Reassociation of Machine ID:**
   - Machine IDs cannot be reassigned once linked to a user.

---

## Notes

- **Unique Machine ID:** Ensure the `machine ID` generated is tied to the specific computer and cannot be transferred.
- **Incremental Commits:** Code was committed incrementally with meaningful messages.

---

## Contributing

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature-name`).
3. Commit changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

---

## License

This project is licensed under the MIT License.

