# Password/Hash cracking


## Commands
```sh
# Using John the ripper
john -w=/usr/share/wordlists/rockyou.txt hash.txt

# Using hashcat
hashcat -m 0 {hash2crack} -a 0 /usr/share/wordlists/rockyou.txt --show # Cracking hash. Module 0 stands for md5
```

## Wordlists

- [SecLists](https://github.com/danielmiessler/SecLists)
