import shlex
import subprocess

def run_cmd(cmd):
    result = []
    p = subprocess.Popen(shlex.split(cmd),
                         shell=False,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    while p.poll() is None:
        line = p.stdout.readline()
        line = line.strip()
        if line:
            # 下面两行代码等价
            line = str(line, encoding="gbk")
            # line = line.decode("gbk")
            print(line)
            result.append(line)
    if p.returncode == 0:
        print('\nSubprogram success\n')
    else:
        print('\nSubprogram failed\n')
    return result


if __name__ == "__main__":
    print(run_cmd("ping yxzl.top"))
