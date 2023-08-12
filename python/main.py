import subprocess
import os

def main():
    current_path = os.path.dirname(os.path.abspath(__file__))

    moni_cpu_path = os.path.join(current_path, "system","moni_cpu.py")
    moni_memory_path = os.path.join(current_path,"system","moni_memory.py")

    subprocess.Popen(["python", moni_cpu_path])

    subprocess.Popen(["python",moni_memory_path])

    print("start monitering..")
    

if __name__ == "__main__":
    main()