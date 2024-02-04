Get-WindowsCapability -Online | Where-Object Name -like "OpenSSH.Server*" | Add-WindowsCapability -Online
