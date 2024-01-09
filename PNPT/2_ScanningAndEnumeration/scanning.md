# Scanning


## Network Scanning

```sh
sudo nmap -T4 -p- -A {target_IP}
sudo nmap -p- -sV -sC # Scan often used in HTB
nmap -p- --min-rate=1000 -sV {target_IP} # HTB scan to speed things up
arp-scan -l # Gives you all the host in your current network via arp scan
```

## Vulnerability Scanning

For Web Vulnerabilities
- Nessus

```sh
nikto -h {ip_address} -p {port_1,port_2} -Format csv -o bla.csv # Makes a Vulnerability Scan on the requested ports in csv format. Storing output in bla.csv

```

## Vulnerability Research

```sh
msfconsole
```

## Directory busting

- dirbuster -> Has an actuall interface
- sublisst3r
- Amass
- Gobuster


## Subdomain hunting

```sh
wfuzz -c -f sub-fighter -w top5000.txt -u 'http://cmess.thm' -H "Host: FUZZ.cmess.thm" #Fuzzing subdomains -> See tldr page for more info
```


## Web Proxies

- BurpSuite
- ZAP (Zed Attack Proxy)
