# Linux - Enumeration for PrivEsc

## System Enumeration
```bash
uname -a # Infos about the system
cat /proc/version # Similar
cat /etc/issue
lscpu # Listing cpu informations

ps aux # Services
```

## User Enumeration
```bash
whoami # name
id # What is our user id an what groups are we member
sudo -l # Listing what we can do with sudo
cat /etc/passwd # Shows you all the users
cat /etc/shadow # List with the hashes for all the users
history # Check if some juicy stuff is in history
```

## Network Enumeration
```bash
ip a # Shows all the network configuration
ip route # Shows you all the routes also to different networks ;)
ip neigh # Checks for arp tables
netstat -ano # What ports are open and what communication does exist?
```
