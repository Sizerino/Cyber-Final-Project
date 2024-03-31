import sys
import platform
import subprocess

def main():
    if platform.system() == "Windows":
        Process = subprocess.Popen('powershell.exe -ExecutionPolicy RemoteSigned -file "windows.ps1"', stdout = sys.stdout)
        Process.communicate()
        print("")
    elif platform.system() == "Linux":
        Process = subprocess.Popen(["/bin/bash", "./main/linux.bash"], stdout = sys.stdout)
        Process.communicate()
        print("")
    else:
        print("Can't identify OS")
    
if __name__ == "__main__":
    main()