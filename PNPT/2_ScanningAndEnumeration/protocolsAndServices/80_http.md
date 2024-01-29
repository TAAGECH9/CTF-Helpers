# HyperText Transfer Protocol


## Directory busting

```sh
sudo gobuster dir -w /usr/share/wordlists/dirb/common.txt -u {target_ip}
ffuf -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt:FUZZ -u http://{target_ip}/:FUZZ
dirb http://{target_ip}
ffuf -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt:FUZZ -u http://192.168.142.131/:FUZZ
dirsearch --url "http://blablabla" --format=simple # When using the simple format you get as an output a list of urls -> This you can use with EyeWithness
```

## Checking URL's found with busting in an automated fashion

```sh
/opt/EyeWitness/Python/EyeWitness.py -f <filename> # Cool stuff -> It will create you an amazing report at the end
```


## Fetching Data

```sh
wget -r -np http://example.com/directory # recursively download all the files from a web directory
```
