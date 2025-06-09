# OrangeHRM User Management Automation

This project automates various test scenarios of the **User Management module** in [OrangeHRM](https://opensource-demo.orangehrmlive.com/) using **Playwright (Python)**.

---

##  Automated Scenarios

The following test cases are automated:

1. **Login with valid credentials**
2. **Add a new user**
3. **Search the user by username**
4. **Edit the added user**
5. **Validate the updated user data**
6. **Delete the user**

---

##  Project Setup Steps

### Prerequisites

- Python 3.7 or above installed
- Git installed
- Node.js (Playwright internally uses it)
- Install Playwright dependencies

### Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/orangehrm-user-management-playwright.git
cd orangehrm-user-management-playwright
```

2. **Create virtual environment (recommended)**

```bash
python -m venv venv
source venv/bin/activate        # For Linux/macOS
venv\Scripts\activate           # For Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Install Playwright browsers**

```bash
playwright install
```

---

##  How to Run Test Cases

From the project root, run:

```bash
pytest tests/
```

Or run a specific test:

```bash
pytest tests/test_01_add_user.py
```

---

##  Project Structure

```
orangehrm-user-management-playwright/
│
├── tests/
│   ├── test_01_add_user.py
│   ├── test_02_search_user.py
│   ├── test_03_edit_user.py
│   ├── test_04_validate_user.py
│   └── test_05_delete_user.py
│
├── pages/
│   ├── login_page.py
│   └── admin_page.py
│
├── conftest.py
├── requirements.txt
└── README.md
```

---

## 🔧 Playwright Version

This project uses:

```
playwright==1.52.0
pytest-playwright==0.4.4
```







