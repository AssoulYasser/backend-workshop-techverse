# backend-workshop-techverse

## 1. Install Python 3.10

### Download and Install:
- **Windows:**
  1. Download the Python 3.10 installer for Windows: [Python 3.10 for Windows](https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe)
  2. Run the installer and ensure you check "Add Python 3.10 to PATH" during the installation.

- **MacOS:**
  ```bash
  brew install python@3.10
  ```

- **Linux:**
  ```bash
  sudo apt update
  sudo apt install -y python3.10 python3.10-venv python3.10-dev
  ```

### Verify Installation:
```bash
python --version
```

---

## 2. Create and Activate a Virtual Environment

### Create the virtual environment:
```bash
python -m venv venv
```

### Activate the virtual environment:
- **Windows:**
  ```bash
  .\venv\Scripts\activate
  ```
- **MacOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

---

## 3. Install Dependencies

### Install Django and Django REST framework:

Ensure you have the `requirements.txt` file provided in the project.

```bash
pip install -r requirements.txt
```

### Verify Installation:
```bash
python -m django --version
python -c "import rest_framework; print(rest_framework.__version__)"
```

---

## 4. Install Postman

### Download and Install:
- **Windows/MacOS/Linux:**
  Download Postman from the official website: [Postman Download](https://www.postman.com/downloads/)

---

## 5. Run the Project

### Start the Development Server:
1. Navigate to the project directory.
2. Run the following command:
   ```bash
   python manage.py runserver
   ```

### Access the Application:
- Visit `http://127.0.0.1:8000/` in your browser or Postman.

---

## 6. Testing APIs with Postman

1. Open Postman.
2. Import the Postman collection (if provided) or manually set up requests.
3. Use the API endpoints described in the project documentation.

---