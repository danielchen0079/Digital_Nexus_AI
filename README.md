Automated UI Testing Project

## Overview

This repository contains automated end-to-end UI tests for the Digital Nexus AI web application.
The project is implemented using Playwright (Python), following modern automation principles such as:

* Page Object Model (POM)
* Modular and reusable components
* Layered architecture (tests, page objects, data, fixtures)
* Clear assertions and error-handling
* Positive and negative scenarios

The automated tests currently cover:

* Login
* Logout
* Updating personal information
* Password reset (valid and invalid email)
* Registration (invalid captcha)

---

## Project Structure

```
Digital_Nexus_AI/
├── pageObjects/               # Page Object Model classes
│   ├── login_page.py
│   ├── logout_page.py
│   ├── info_page.py
│   ├── pwd_reset_page.py
│   └── register_page.py
│
├── testData/                  # Test data files
│   ├── credentials.py
│   ├── personInfo.py
│   ├── duplicaInfo.py
│   └── registData.py
│
├── tests/                     # Test scripts
│   ├── test_login_and_logout.py
│   ├── test_person_info_edit.py
│   ├── test_reset_password_and_verify.py
│   └── test_register_with_invalid_captcha.py
│
├── playwright.config.js
├── package.json
├── requirements.txt
└── README.md
```

---

## Prerequisites

The following tools must be installed:

* Node.js >= 14.x
* Python >= 3.8
* Playwright (installed via npm)
* pytest (for running Python tests)

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/Digital_Nexus_AI.git
cd Digital_Nexus_AI
```

### 2. Install Node.js dependencies

```bash
npm install
```

### 3. Install Playwright browsers

```bash
npx playwright install
```

### 4. (Optional) Set up Python environment

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

---

## Configuration

Update test data in the `testData` folder.

### Example (credentials.py)

```python
valid_user = {
    "username": "teacher2",
    "password": "111111"
}
```

### Example (personInfo.py)

```python
user_info = {
    "realName": "Test User 1",
    "sex": "female",
    "idNum": "422201197809031346",
    "phone": "19320114162",
    ...
}
```

### Example (registData.py)

```python
regist_data = {
    "email": "test_invalid_captcha@example.com",
    "username": "test_invalid_captcha",
    "password": "Test123456!",
    "captcha": "0000"
}
```

---

## Running Tests

### Run all tests

```bash
pytest
```

### Run a specific test

```bash
pytest tests/test_login_and_logout.py
```

### Run Playwright tests (JavaScript version)

```bash
npx playwright test
```

---

## Test Coverage

### 1. Login & Logout

* Valid login
* Logout successful
* Assertion: redirected to login page

### 2. Update Personal Information

* Update full user profile
* Assert success message
* Assert data persists after refresh

### 3. Reset Password

* Valid email → success message
* Unknown email → negative scenario

### 4. Registration

* Invalid captcha → error message
* Assert account is not created

---

## Test Design Approach

This project follows several key principles:

* Clear test names and actions
* Separate test logic from page objects
* Consistent assertions
* Error handling with waits and visibility checks
* Edge cases included (invalid captcha, unknown email)

---

## Reports and Debugging

Playwright generates:

* `playwright-report/` — HTML report
* `test-results/` — screenshots, traces, videos

To open report:

```bash
npx playwright show-report
```

---

