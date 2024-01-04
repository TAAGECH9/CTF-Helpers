# HyperText Transfer Protocol


## Directory busting

```sh
sudo gobuster dir -w /usr/share/wordlists/dirb/common.txt -u {target_ip}
ffuf -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt:FUZZ -u http://{target_ip}/:FUZZ
dirb http://{target_ip}
ffuf -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt:FUZZ -u http://192.168.142.131/:FUZZ
```

## Fetching Data

```sh

wget -r -np http://example.com/directory # recursively download all the files from a web directory
```
