import psutil
import time


def getMemory():
    data = psutil.virtual_memory()
    memory = str(int(round(data.percent))) + "%"
    return memory


def getCpu():
    cpu = str(round(psutil.cpu_percent(interval=1), 2)) + "%"
    return cpu


def main():
    while (True):
        memory = getMemory()
        cpu = getCpu()
        print("CPU占用：%s \t 内存占用：%s" % (cpu, memory))
        time.sleep(0.2)


if __name__ == "__main__":
    main()