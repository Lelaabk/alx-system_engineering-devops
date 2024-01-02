# Attack is the Best Defense - DevOps Project

## Overview
This project, developed by Sylvain Kalache, is designed to explore and understand various concepts related to network security, Docker, scripting, and hacking. The project encompasses two tasks with an optional nature, aiming to enhance your understanding of network basics and security practices.

## Concepts Covered
1. Network basics
2. Docker
3. Scripting
4. Hacking

## Background Context
This project is entirely optional. Completion of any part will contribute over 100% to your average project grade. While the project is not mandatory, it provides an opportunity to delve into essential concepts and have fun with the challenges presented.

## Resources
Read or watch materials related to:
- Network sniffing
- ARP spoofing
- Connecting to SendGrid’s SMTP relay using telnet
- Docker and its popularity
- Dictionary attack

Refer to the man or help pages for:
- tcpdump
- hydra
- telnet
- docker

## Tasks

### Task 0: ARP Spoofing and Sniffing Unencrypted Traffic
**Advanced Level**

Security is a crucial aspect of network systems, and this task focuses on the interception of unencrypted traffic. The project starts by sniffing unencrypted traffic and extracting information from it.

**Instructions:**
- Execute the provided script `user_authenticating_into_server` locally on your Ubuntu vagrant machine or any other Linux machine.
- Use `tcpdump` to sniff the network and find the password used in the authentication process.
- Paste the discovered password in your answer file.

*Note: The script will not work on Docker containers or Mac OS.*

**Repo:**
- GitHub Repository: [alx-system_engineering-devops](https://github.com/Lelaabk/alx-system_engineering-devops)
- Directory: `attack_is_the_best_defense`
- File: `0-sniffing`

### Task 1: Dictionary Attack
**Advanced Level**

This task explores the vulnerability of password-based authentication systems to dictionary attacks. The focus is on breaking an SSH account through a dictionary attack on a Docker container.

**Instructions:**
1. Install Docker on your Ubuntu machine.
2. Pull and run the Docker image `sylvainkalache/264-1` using the command: `docker run -p 2222:22 -d -ti sylvainkalache/264-1`
3. Find a password dictionary (you may need multiple).
4. Install and use `hydra` to attempt a brute force attack on the SSH account `sylvain` within the Docker container.
5. As the Docker container runs locally, use IP `127.0.0.1` and port `2222` for hydra access.
6. The password is 11 characters long. Once found, share it in your answer file.

**Repo:**
- GitHub Repository: [alx-system_engineering-devops](https://github.com/Lelaabk/alx-system_engineering-devops)
- Directory: `attack_is_the_best_defense`
- File: `1-dictionary_attack`

## Disclaimer
You may observe "Authentication failed: Bad username / password" in the tcpdump trace. This is normal, as the Sendgrid account user has been deleted for security reasons. The password cannot be verified via Sendgrid; only the correction system can.

**Copyright © 2024 ALX, All rights reserved.**
