import psutil
import requests
import time
from dotenv import load_dotenv
import os

cpu_percent = psutil.cpu_percent()
cpu_count = psutil.cpu_count()

print(cpu_count)
print(cpu_percent)

load_dotenv(dotenv_path=".env.server_local")

send_api = os.getenv("NODEJS_SERVER_URL")
print(send_api)
print("send_api1: "+send_api)

while True:
    cpu_percent = psutil.cpu_percent(interval=0.5)
    
    # Node.js 서버로 데이터 전송
    response = requests.post(send_api, json={"cpu_percent": cpu_percent})
    
    time.sleep(0.5)