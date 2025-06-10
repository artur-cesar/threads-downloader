import threading

# Global lock to block concurrent prints
print_lock = threading.Lock()

#TODO: refactor using with
def log(message: str):
    print_lock.acquire()
    print(message)
    print_lock.release()
