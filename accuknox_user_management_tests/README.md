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
git clone https://github.com/your-username/AccuKnox-user-management-tests.git
cd AccuKnox-user-management-tests
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

Running in Headed Mode (GUI browser)

```bash
pytest --headed
```

Running with Slow Motion (for debugging)

```bash
pytest --headed --slowmo 1000
```
---

##  Project Structure

```
accuknox_user_management_tests/
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   └── admin_page.py
├── tests/
│   ├── test_add_user.py
│   ├── test_edit_user.py
│   ├── test_search_user.py
│   ├── test_validate_user.py
│   └── test_delete_user.py
├── test_data/
├── conftest.py
├── README.md

```

---

## 🔧 Playwright Version

This project uses:

```
playwright==1.52.0
pytest-playwright==0.4.4
```







