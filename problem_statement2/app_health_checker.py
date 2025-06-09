import requests
import logging


logging.basicConfig(filename='app_health.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def check_application(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            status = "UP"
            print(f"{url} is UP")
        else:
            status = f"DOWN (Status code: {response.status_code})"
            print(f"{url} is DOWN")
        logging.info(f"Checked {url}: {status}")
    except requests.exceptions.RequestException as e:
        print(f"{url} is DOWN - Exception occurred: {e}")
        logging.error(f"Error checking {url}: {e}")

if __name__ == "__main__":
   
    app_url = "https://opensource-demo.orangehrmlive.com/"
    check_application(app_url)
