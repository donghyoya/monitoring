import subprocess
import os
import atexit

subprocesses = []

def terminate_subprocesses():
    for proc in subprocesses:
        proc.terminate()

def main():
    current_path = os.path.dirname(os.path.abspath(__file__))

    moni_cpu_path = os.path.join(current_path, "system","moni_cpu.py")
    moni_memory_path = os.path.join(current_path,"system","moni_memory.py")

    cpu_proc= subprocess.Popen(["python", moni_cpu_path])

    memory_proc = subprocess.Popen(["python",moni_memory_path])

    subprocesses.extend([cpu_proc, memory_proc])

    print("start monitering..")
    

if __name__ == "__main__":
    main()
    #각각 프로세스로 동작하던 파이썬 파일 종료
    atexit.register(terminate_subprocesses)