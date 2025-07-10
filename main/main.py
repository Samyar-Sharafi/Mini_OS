
import time
import random as r
import os
from tqdm import tqdm

def starter ():
    print("""
┏━┓┏━┓ ┏━━┓ ┏━┓︱┏┓ ┏━━┓           ┏━━━┓ ┏━━━┓
┃┃┗┛┃┃ ┗┫┣┛ ┃┃┗┓┃┃ ┗┫┣┛           ┃┏━┓┃ ┃┏━┓┃
┃┏┓┏┓┃ ︱┃┃︱ ┃┏┓┗┛┃ ︱┃┃︱        ┃︱┃┃ ┃┗━━┓
┃┃┃┃┃┃ ︱┃┃︱ ┃┃┗┓┃┃ ︱┃┃︱        ┃┃︱┃┃ ┗━━┓┃
┃┃┃┃┃┃ ┏┫┣┓ ┃┃︱┃┃┃ ┏┫┣┓           ┃┗━┛┃ ┃┗━┛┃
┗┛┗┛┗┛ ┗━━┛ ┗┛︱┗━┛ ┗━━┛           ┗━━━┛ ┗━━━┛
""")
    
    for i in tqdm(range(100), desc="BOOTING"):
        time.sleep(r.uniform(0.000000000000000000001, 0.10000000000000000000))
    try:
            os.system("python C:/Users/DELL/Documents/Python/WorkSpace/projects/Mini_OS/main/kernel.py")
    except Exception as e:
            print("ERROR FOUND: ")
            print(f"{e}")
            exit()

starter()

