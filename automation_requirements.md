# Requirement list for automation



ip given:
  - Nmap scan -> Write result to nmap_scan.txt

nmap scan given:
  - Based on Used Technology Framework identify possible exploits
    - Using Searchsploit
    - Using exploit-db
  - based on discovered Ports execute stanard procedures
    - 21 ftp -> Check if anonymous login is possible or not
    - 80 http ->
      - Trigger directory busting (ffuf, gobuster, dirbuster, dirb)
        - Provide screenshots based on discovered pages (bustin directory)
      - Start Vulnerability scan
        - Nikto Scan
        - Nessus Scan
