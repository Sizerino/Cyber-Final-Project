import sys
import platform
import subprocess


def main():
    if platform.system() == "Windows":
        process = subprocess.Popen(
            './powershell.exe -ExecutionPolicy RemoteSigned -file "windows.ps1"',
            stdout=sys.stdout
        )
        
        process.communicate()
        print("")

    else:
        print("The Host OS Is Not Windows")


if __name__ == "__main__":
    main()
