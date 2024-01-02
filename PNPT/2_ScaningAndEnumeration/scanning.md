# Scanning


## Basic Nmap Scanning

```sh
sudo nmap -T4 -p- -A 10.129.126.241
sudo nmap -p- -sV -sC # Scan often used in HTB
nmap -p- --min-rate=1000 -sV {target_IP} # HTB scan to speed things up
```
