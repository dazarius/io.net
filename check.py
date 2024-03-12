import requests 
import os
import subprocess
import time
import json
import  os
import datetime
from datetime import datetime 





def  check():
    response = requests.get(url, headers={"Token": acc})

    return response.json()


def up():
    command = "./launch_binary_linux --device_id=16d63c38-4270-405d-ad5a-1ff73f305d9a --user_id=c1e6cd3a-3a69-4f19-8b77-c2ad65ae4784 --operating_system=Linux --usegpus=false --device_name=worker"
    if subprocess.call(command, shell=True) == 0:
        return True
    else:
        return False
def main():   
    
    up()



if __name__ == "__main__":
    while True:
        
        time.sleep()
    main()