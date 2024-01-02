# Main

## Linux

### System Enumeration
```bash
uname -a # Infos about the system
cat /proc/version # Similar
cat /etc/issue
lscpu # Listing cpu informations

ps aux # Services
```

### User Enumeration
```bash
whoami # name
id # What is our user id an what groups are we member
sudo -l # Listing what we can do with sudo
cat /etc/passwd # Shows you all the users
cat /etc/shadow # List with the hashes for all the users
history # Check if some juicy stuff is in history
```

### Network Enumeration
```bash
ip a # Shows all the network configuration
ip route # Shows you all the routes also to different networks ;)
ip neigh # Checks for arp tables
netstat -ano # What ports are open and what communication does exist?
```

## Windows

### System
```command
systeminfo
systeminfo | findstry /B /C:"OS Name" /C:"Os Version" /C:"System Type"
hostname
wmic qfe #Windows Management Instrumentation -> Shows you about patching
wmic qfe get Caption,Description,HotFixID,InstalledOn
wmic logicaldisk
wmic logicaldisk get caption,description,providername
```

### User
```cmd
whoami # Shows you the user
whoami /priv # Shows you the privileges of the current user
whoami /groups # Shows groups you are member of
net user
net user <username> # Infos about User
net localgroup
net localgroup <groupname> # infos about a group
```

### Network
```cmd
ipconfig
ipconfig /all # ipconfig with more infos
arp -a # Shows you arp table
route print # Shows you the route table
netstat -ano # Shows you all the listening ports
```

### Password Hunting
```cmd
findstr /si password *.txt *.ini *.config
```

### Antivirus and Firewall
```cmd
sc query windefend #sc is for service
sc queryex type= service # Shows you all the services running on this machine
netsh advfirewall firewall dump
netsh firewall show state
netsh firewall show config
```
