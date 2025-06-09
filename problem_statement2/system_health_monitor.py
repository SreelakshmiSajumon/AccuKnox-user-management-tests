import psutil
import logging


logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s - %(message)s')


CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

def check_cpu():
    cpu = psutil.cpu_percent(interval=1)
    if cpu > CPU_THRESHOLD:
        logging.warning(f"High CPU usage detected: {cpu}%")
    return cpu

def check_memory():
    mem = psutil.virtual_memory().percent
    if mem > MEMORY_THRESHOLD:
        logging.warning(f"High Memory usage detected: {mem}%")
    return mem

def check_disk():
    disk = psutil.disk_usage('/').percent
    if disk > DISK_THRESHOLD:
        logging.warning(f"Low Disk space: {disk}% used")
    return disk

def check_processes():
    processes = len(psutil.pids())
    return processes

def main():
    cpu = check_cpu()
    memory = check_memory()
    disk = check_disk()
    processes = check_processes()

    print(f"CPU Usage: {cpu}%")
    print(f"Memory Usage: {memory}%")
    print(f"Disk Usage: {disk}%")
    print(f"Running Processes: {processes}")

if __name__ == "__main__":
    main()
