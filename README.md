
# **End-to-End UI Automation Framework**

## Overview

This repository contains an end-to-end UI automation framework built using Playwright (Python).
The project follows modern automation testing practices including:

* Page Object Model (POM)
* Modular and maintainable folder structure
* Dedicated test data management
* Reusable page interaction methods
* Clear assertions and negative test coverage
* Structured reporting and tracing support

The automated tests currently include:

* Login & Logout
* Updating personal information
* Password reset (valid and invalid cases)
* Registration with invalid captcha

---

## Project Structure

```
QA Automation/
├── .github/                    
├── pageObjects/                
│   ├── InfoPage.py
│   ├── LoginPage.py
│   ├── LogoutPage.py
│   ├── pageDropDown.py
│   ├── POManager.py
│   ├── PwdResetPage.py
│   └── RegisterPage.py
│
├── test-results/               
│
├── testData/                  
│   ├── credentials.py
│   ├── duplicaInfo.py
│   ├── personInfo.py
│   └── registData.py
│
├── tests/                     
│   ├── conftest.py
│   ├── test_login_logout.py
│   ├── test_person_info.py
│   ├── test_pwd_reset.py
│   └── test_register_invalid_captcha.py
│
├── tests-examples/            
│
├── package.json
├── package-lock.json
├── playwright.config.js
├── .gitignore
└── README.md
```

---

## Clone the Repository

```
https://github.com/danielchen0079/End-to-End-UI-Automation-Framework.git
```

```bash
git clone https://github.com/danielchen0079/End-to-End-UI-Automation-Framework.git
cd End-to-End-UI-Automation-Framework/"QA Automation"
```

---

## Installation

### Install Node.js Dependencies

```bash
npm install
```

### Install Playwright Browsers

```bash
npx playwright install
```

---

## Configuration

### Test Data Location

All editable test data is stored under:

```
testData/
```

Examples:

**credentials.py**

```python
valid_user = {
    "username": "teacher2",
    "password": "111111"
}
```

**personInfo.py**

```python
user_info = {
    "realName": "Test User 1",
    "sex": "female",
    "idNum": "422201197809031346",
    "phone": "19320114162",
    ...
}
```

**registData.py**

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
pytest tests/
```

### Run a specific test file

```bash
pytest tests/test_login_logout.py
```

### Show Playwright HTML Report

```bash
npx playwright show-report
```

---

## Test Coverage Summary

### Login and Logout

* Valid login
* Logout action
* Assertion: redirected to login page

### Update Personal Information

* Edit profile with full dataset
* Assertion: success message
* Assertion: data persists after refresh

### Password Reset

* Valid email → success message
* Unknown email → validation failure

### Registration

* Invalid captcha → error under input field

---


