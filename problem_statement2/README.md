# Problem Statement 2 

This repository contains two Python scripts developed:

##  Project Structure

problem_statement2/
├── app_health_checker.py
├── system_health_monitor.py
└── README.md



## 1️ System Health Monitoring Script

###  File: `system_health_monitor.py`

This script monitors the health of a system. It checks:
-  **CPU Usage**
-  **Memory Usage**
-  **Disk Usage**
-  **Running Processes**

If any of these metrics exceed safe thresholds (e.g., CPU usage > 80%), it prints a **warning** in the console.

###  How to Run:

python system_health_monitor.py

## 2 Application Health Checker

###  File: `app_health_checker.py`

This script checks whether a web application is UP or DOWN by sending an HTTP request to the given URL.

It:

Sends a request to a specified URL.

Interprets the HTTP status code.

Prints the health status (UP/DOWN) based on the response.

 ### How to Run:

python app_health_checker.py

📦 Dependencies
Both scripts require the following Python packages:

psutil (for monitoring system resources)

requests (for checking web application health)

To install all dependencies:

pip install -r requirements.txt