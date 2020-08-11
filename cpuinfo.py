import psutil

def cpu_info():
    print("="*20,"CPU Informations","="*20)
    # Commands for printing information about amount of cores
    print("Physical Cores: ",psutil.cpu_count(logical=False))
    print("Total Cores",psutil.cpu_count(logical=True))
    # Commands for printing information about frequencies
    cpufreq=psutil.cpu_freq()
    print(f"Max Frequency:{cpufreq.max:.2f}Mhz")
    print(f"Min Frequency:{cpufreq.min:.2f}Mhz")
    print(f"Current Frequency:{cpufreq.current:.2f}Mhz")
    # Commands for printing information about usage
    print("CPU Usage Per core")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True,interval=1)):
        print(f"Core {i}:{percentage}%")
    print(f"Total CPU Usage:{psutil.cpu_percent()}%")

if __name__ == "__main__":
    cpu_info()