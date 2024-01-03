# Scanning


## Network Scanning

```sh
sudo nmap -T4 -p- -A 10.129.126.241
sudo nmap -p- -sV -sC # Scan often used in HTB
nmap -p- --min-rate=1000 -sV {target_IP} # HTB scan to speed things up
arp-scan -l # Gives you all the host in your current network via arp scan
```

## Vulnerability Scanning

- Nessus

```sh
nikto -h http://{ip_address} # Makes a Vulnerability Scan
```

## Vulnerability Research

```sh
msfconsole
```

## Directory busting

- dirbuster -> Has an actuall interface

```

```
