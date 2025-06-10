import threading

# Global lock to block concurrent prints
print_lock = threading.Lock()

def log(message: str):
    with print_lock:
        print(message)
