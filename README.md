# Custom SSO Implementation

## Development Setup

> **Note:** Don’t forget to create a `.env` file and populate it with the required environment variables.

### 1. Clone the project

```bash
git clone https://github.com/Amit4218/my_own_oauth.git
cd my_own_oauth
```

### 2. Create and activate a virtual environment

#### on windows

```bash
python -m venv .venv

.venv\Scripts\activate.bat
```

#### on Linux / Macos

```bash
python3 -m venv .venv

source .venv/bin/activate
```

- install the requirements

```bash
pip install -r requirements.txt
```

- run the application

```bash
flask --app main run
```

#### Notes

- By default, the application runs at http://127.0.0.1:5000

- Update your .env file with any required credentials or configuration before running the app.
