import psutil
import time
import requests
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env.server_local")

send_api = os.getenv("NODEJS_SERVER_URL")+"update-memory-usage"

while True:
    # memory_usage = psutil.virtual_memory().used
    
    memory_info = psutil.virtual_memory()
    total_memory = memory_info.total
    used_memory = memory_info.used
    memory_usage = memory_info.percent

    response = requests.post(send_api, json={"memory_used": memory_usage})
    
    time.sleep(1)