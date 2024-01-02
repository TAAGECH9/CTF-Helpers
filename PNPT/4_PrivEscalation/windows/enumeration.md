# Windows - Enumeration for PrivEsc


## System
```command
systeminfo
systeminfo | findstry /B /C:"OS Name" /C:"Os Version" /C:"System Type"
hostname
wmic qfe #Windows Management Instrumentation -> Shows you about patching
wmic qfe get Caption,Description,HotFixID,InstalledOn
wmic logicaldisk
wmic logicaldisk get caption,description,providername
```

## User
```cmd
whoami # Shows you the user
whoami /priv # Shows you the privileges of the current user
whoami /groups # Shows groups you are member of
net user
net user {username} # Infos about User
net localgroup
net localgroup {groupname} # infos about a group
```

## Network
```cmd
ipconfig
ipconfig /all # ipconfig with more infos
arp -a # Shows you arp table
route print # Shows you the route table
netstat -ano # Shows you all the listening ports
```

## Password Hunting
```cmd
findstr /si password *.txt *.ini *.config
```

## Antivirus and Firewall
```cmd
sc query windefend #sc is for service
sc queryex type= service # Shows you all the services running on this machine
netsh advfirewall firewall dump
netsh firewall show state
netsh firewall show config
```
