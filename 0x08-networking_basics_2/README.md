# 0x08. Networking Basics #1

## Introduction
This project is part of the ALX School curriculum and is focused on Networking Basics. The project consists of a set of tasks designed to help you understand fundamental networking concepts and how to work with network configurations on an Ubuntu 20.04 LTS system. Below, you'll find an overview of the project, its tasks, and the associated learning objectives.

## Project Details
- **Project Name:** Networking Basics #1
- **Domain:** DevOps, Network, SysAdmin
- **Author:** Sylvain Kalache
- **Project Weight:** 1
- **Project Start Date:** November 1, 2023, 4:00 AM
- **Project End Date:** November 3, 2023, 4:00 AM
- **Checker Release Date:** November 3, 2023, 4:00 AM
- **Auto Review Deadline:** Upon project end

## Learning Objectives
By the end of this project, you are expected to be able to explain the following concepts without relying on external sources:

### General
- What is localhost (127.0.0.1)?
- What is 0.0.0.0?
- What is the /etc/hosts file?
- How to display your machine's active network interfaces.

## Copyright and Plagiarism
As a student working on this project, it is essential to come up with your solutions to meet the learning objectives. Plagiarism in any form is strictly forbidden and will result in removal from the program. Do not publish any content related to this project.

## Requirements
### General
- Allowed editors: vi, vim, emacs.
- All your files will be interpreted on Ubuntu 20.04 LTS.
- All your files should end with a new line.
- A README.md file, at the root of the project folder, is mandatory.
- All your Bash script files must be executable.
- Your Bash scripts must pass Shellcheck (version 0.7.0 via apt-get) without any errors.
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`.
- The second line of all your Bash scripts should be a comment explaining what the script is doing.

## Tasks

### 0. Change your home IP (Mandatory)
Write a Bash script that configures an Ubuntu server with the following requirements:

**Requirements:**
- localhost resolves to 127.0.0.2
- facebook.com resolves to 8.8.8.8.

Example:
```shell
$ ping localhost
PING localhost (127.0.0.1) 56(84) bytes of data.
64 bytes from localhost (127.0.0.1): icmp_seq=1 ttl=64 time=0.012 ms
...
$ ping facebook.com
PING facebook.com (157.240.11.35) 56(84) bytes of data.
64 bytes from edge-star-mini-shv-02-lax3.facebook.com (157.240.11.35): icmp_seq=1 ttl=63 time=15.4 ms
...
$ sudo ./0-change_your_home_IP
...
$ ping localhost
PING localhost (127.0.0.2) 56(84) bytes of data.
64 bytes from localhost (127.0.0.2): icmp_seq=1 ttl=64 time=0.012 ms
...
$ ping facebook.com
PING facebook.com (8.8.8.8) 56(84) bytes of data.
64 bytes from facebook.com (8.8.8.8): icmp_seq=1 ttl=63 time=8.06 ms
```

### 1. Show attached IPs (Mandatory)
Write a Bash script that displays all active IPv4 IPs on the machine it's executed on.

Example:
```shell
$ ./1-show_attached_IPs | cat -e
10.0.2.15$
127.0.0.1$
```

### 2. Port listening on localhost (Advanced)
Write a Bash script that listens on port 98 on localhost.

**Usage Example:**
```shell
# Terminal 0
$ sudo ./100-port_listening_on_localhost

# Terminal 1
$ telnet localhost 98
Trying 127.0.0.2...
Connected to localhost.
Escape character is '^]'.
Hello world
test

# Terminal 0
$ sudo ./100-port_listening_on_localhost
Hello world
test
```

This script allows you to establish a connection within localhost, which can be useful for debugging network-related issues, testing socket connections, or working with firewall rules.

## Repository Information
- GitHub Repository: [alx-system_engineering-devops](https://github.com/Lelaabk/alx-system_engineering-devops)
- Directory: 0x08-networking_basics_2

---
