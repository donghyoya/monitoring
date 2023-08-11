import psutil
cpu_percent = psutil.cpu_percent()
cpu_count = psutil.cpu_count()

print(cpu_count)
print(cpu_percent)