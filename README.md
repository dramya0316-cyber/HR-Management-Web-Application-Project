# 🚀 OrangeHRM Management Application – Test Automation Framework

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Selenium](https://img.shields.io/badge/Selenium-Automation-brightgreen?logo=selenium)
![Pytest](https://img.shields.io/badge/Pytest-Framework-orange?logo=pytest)
![Allure](https://img.shields.io/badge/Reporting-Allure-purple)
![GitHub](https://img.shields.io/badge/Git-Version%20Control-black?logo=github)

## 📖 Project Overview

The **OrangeHRM Management Application Test Automation Framework** is a robust end-to-end automation solution built using **Python, Selenium WebDriver, and Pytest**. The framework follows the **Page Object Model (POM)** design pattern to improve maintainability, scalability, and code reusability.

It automates critical business workflows of the OrangeHRM application, including Login, User Management, Leave, Claims, Recruitment, Employee Management, and My Info modules.

---

## ✨ Key Features

* ✅ Page Object Model (POM) Architecture
* ✅ Pytest Test Framework
* ✅ Cross-Browser Testing (Chrome, Firefox & Edge)
* ✅ Explicit & Implicit Wait Strategies
* ✅ Data-Driven Testing using Excel (OpenPyXL)
* ✅ Comprehensive Logging
* ✅ Allure & HTML Reporting
* ✅ Screenshot Capture on Test Failure
* ✅ Reusable Utility Classes
* ✅ Configurable Test Execution
* ✅ Scalable & Easy-to-Maintain Framework

---

## 🛠️ Technology Stack

| Technology         | Purpose                  |
| ------------------ | ------------------------ |
| Python             | Programming Language     |
| Selenium WebDriver | Web Automation           |
| Pytest             | Test Framework           |
| Allure Reports     | Interactive Test Reports |
| HTML Report        | Test Execution Report    |
| OpenPyXL           | Data-Driven Testing      |
| Git & GitHub       | Version Control          |
| VS Code / PyCharm  | Development Environment  |

---

## 📂 Project Structure

```text
HR_Management_Test_Automation/
│
├── pages/                 # Page Object Classes
├── tests/                 # Test Cases
├── Utilities/             # Utility Classes
├── TestData/              # Excel Test Data
├── Reports/               # HTML & Allure Reports
├── Logs/                  # Execution Logs
├── Screenshots/           # Failure Screenshots
├── conftest.py            # Pytest Fixtures
├── config.py              # Configuration File
├── pytest.ini             # Pytest Configuration
├── requirements.txt       # Project Dependencies
└── README.md
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone git clone https://github.com/umashankarm15071993-spec/OrangeHRM_Management_Application_project.git
```

### Navigate to the Project Directory

```bash
cd OrangeHRM_Management_Application_project
```

### Install Required Packages

```bash
pip install -r requirements.txt
```

---

## ▶️ Test Execution

### Run All Tests

```bash
pytest
```

### Run Tests in Chrome

```bash
pytest --browser Chrome
```

### Run Tests in Firefox

```bash
pytest --browser Firefox
```

### Run Tests in Edge

```bash
pytest --browser Edge
```

### Run a Specific Test

```bash
pytest tests/test_loginpage.py
```

---

## 📊 Test Reports

### Generate Allure Report

```bash
pytest --alluredir=Reports/allure-results
```

```bash
allure serve Reports/allure-results
```

### Generate HTML Report

```bash
pytest --html=Reports/report.html --self-contained-html
```

---

## ✅ Automated Test Coverage

* 🔐 Login
* 📋 Dashboard
* 👥 User Management
* 👨‍💼 Employee Management
* 🗓️ Leave Management
* 💰 Claim Management
* 👤 My Information
* 🔍 Search & Validation
* 🚪 Logout

---

## 🏗️ Framework Design

The framework is designed using industry best practices:

* Page Object Model (POM)
* Base Page Implementation
* Reusable Utility Classes
* Centralized Configuration
* Logging Mechanism
* Pytest Fixtures
* Modular Test Design

---

## 📈 Framework Highlights

* Clean & Maintainable Architecture
* Easy to Extend with New Test Cases
* Reduced Code Duplication
* Faster Test Execution
* Better Reporting & Debugging
* Easy CI/CD Integration

---

## 📸 Reports & Screenshots

The framework automatically generates:

* 📊 Allure Interactive Report
* 📄 HTML Report
* 📸 Failure Screenshots
* 📝 Execution Logs
---

## 👨‍💻 Author

### **D Ramya**

**Python Selenium Automation Test Engineer**

* Python
* Selenium WebDriver
* Pytest
* Page Object Model (POM)
* Data-Driven Testing
* Allure Reporting
* Git & GitHub
* SQL


---

⭐ **If you found this project useful, don't forget to Star the repository!**
