import time
import threading as thread

def download(sec):
    print(f"Downloading in {sec} seconds...")
    time.sleep(sec)
    print(f"Downloaded {sec}")
    
t1 = time.perf_counter();
# download(4)
# download(3)
# download(1)

d1 = thread.Thread(target=download, args=[4])
d2 = thread.Thread(target=download, args=[3])
d3 = thread.Thread(target=download, args=[1])

d1.start()
d2.start()
d3.start()

d1.join()
d2.join()
d3.join()

t2 = time.perf_counter()
print(f"Downloaded in {t2-t1} seconds")
