import sys
import platform
import subprocess

def main():
    if platform.system() == "Windows":
        windowsProcess = subprocess.Popen('powershell.exe -ExecutionPolicy RemoteSigned -file "windows.ps1"', stdout = sys.stdout)
        windowsProcess.communicate()
        print("")
    elif platform.system() == "Linux":
        linuxProcess = subprocess.Popen("linux.bash", stdout = sys.stdout)
        linuxProcess.communicate()
        print("")
    else:
        print("Can't Identify OS")
    
if __name__ == "__main__":
    main()