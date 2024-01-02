# Passive Reconnaissance

## Physical/Social

### Location information
- Satellite images
- Drone recon
- Building layout (badge readers, break areas, security, fencing)

### Job information
- Employees (name, job title, phone number, manager, etc)
- Pictures (badge photos, desk photos, computer, photos, etc.)


## Web / Hosts

- Target Validation -> WHOIS, nslookup, dnsrecon
- Finding Subdomains -> Google Fu, dig, Nmap, Sublist3r
- Fingerprinting -> Nmap, Wappalyzer, WhatWeb, BuiltWith, Netcat
- Data Breaches -> HaveIBeenPwned, BreachParse, WeLeakInfo


## Discovering Email Addresses

- [Hunter IO](https://hunter.io/)
- [Phonebook.cz](https://phonebook.cz/)
- [Voilanorbert](https://www.voilanorbert.com/)
- [Clearbit Connect](https://clearbit.com/resources/tools/connect)
- [Email Verifier -> EmailHippo](https://tools.emailhippo.com/)
- [Email Verifier -> Email-checker.net](https://email-checker.net/)


## Breached Credentials

- [breach-parse script](https://github.com/hmaverickadams/breach-parse/blob/master/breach-parse.sh)
- [Dehashed](https://www.dehashed.com/)


## Subdomain Hunting

- [crt.sh](https://crt.sh/) -> Doing certificate fingerprinting

```
sublist3r -d tesla.com #
```

## Identify Website Technologies

- [BuiltWith](https://builtwith.com/)
- [Wappalyzer](https://www.wappalyzer.com/)

```sh
whatweb https://tesla.com # Will give you the info of what this page is built on
```
