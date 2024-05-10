import sys
import platform
import subprocess


def main():
    if platform.system() == "Windows":
        process = subprocess.Popen('./powershell.exe -ExecutionPolicy RemoteSigned -file "windows.ps1"',stdout=sys.stdout)
        process.communicate()
        print("")

    elif platform.system() == "Linux":
        process = subprocess.Popen(["/bin/bash", "./linux.bash"], stdout=sys.stdout)
        process.communicate()
        print("")

    else:
        print("Can't identify OS")


if __name__ == "__main__":
    main()
