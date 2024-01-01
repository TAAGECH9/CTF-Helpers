# Escalation Paths



## Kernel Explits
- [kernel-exploits Github](https://github.com/lucyoa/kernel-exploits)


## Password and File permissions

```bash
grep --color=auto -rnw '/' -ie "PASSWORD=" --color=always 2> /dev/null
locate password | less
find / -name id_rsa 2> /dev/null
find / -name authorized_keys 2> /dev/null
history
cat .bash_history # Prints out the complete history -> Here you can grep for usernames/passwords
unshadow passwd shadow # Where as the passwd is the content of /etc/passwd and shadow the content of /etc/shadow
```

## Sudo and Binaries

- [GTFOBins](https://gtfobins.github.io/)
- **Inteded Functionality**: If bin is not in GTFOBins do google search -> example "apache sudo privilege escalation"
- [LD_PRELOAD](https://book.hacktricks.xyz/linux-hardening/privilege-escalation#ld_preload-and-ld_library_path)

```bash
sudo -l # Gives you all the command that you can run without root
```

## SUID

- Use GTFOBins with `SUID`

```bash
find / -perm -u=s -type f 2>/dev/null # Shows all files owned by the root user
```

## Capabilities

- [Linux Privilege Escalation using Capabilities](https://www.hackingarticles.in/linux-privilege-escalation-using-capabilities/)
- [SUID vs. Capabilities](https://mn3m.info/posts/suid-vs-capabilities/)
- [Linux Capabilities Privilege Escalation via OpenSSL](https://int0x33.medium.com/day-44-linux-capabilities-privilege-escalation-via-openssl-with-selinux-enabled-and-enforced-74d2bec02099)


```bash
getcap -r / 2>/dev/null # Showing all the capabilities set
```

## Schedule Tasks - Cron Jobs

- [Payload all the Things - Scheduled tasks](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Linux%20-%20Privilege%20Escalation.md#scheduled-tasks)