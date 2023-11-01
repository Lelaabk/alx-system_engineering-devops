# Networking Basics #0

![DevOps](https://img.shields.io/badge/DevOps-Networking-blue)
![Author](https://img.shields.io/badge/Author-Sylvain%20Kalache-green)
![Weight](https://img.shields.io/badge/Weight-1-lightgrey)

**Project Start Date:** November 1, 2023, 4:00 AM  
**Project End Date:** November 3, 2023, 4:00 AM  
**Checker Release:** November 3, 2023, 4:00 AM  
**Auto Review Deadline:** [Insert Deadline]

## Resources

### Read or watch:
- [OSI model](https://en.wikipedia.org/wiki/OSI_model)
- [Different types of network](https://www.lifewire.com/lans-wans-and-other-area-networks-817376)
- [LAN network](https://en.wikipedia.org/wiki/Local_area_network)
- [WAN network](https://en.wikipedia.org/wiki/Wide_area_network)
- [Internet](https://en.wikipedia.org/wiki/Internet)
- [MAC address](https://whatismyipaddress.com/mac-address)
- [What is an IP address](https://www.bleepingcomputer.com/tutorials/ip-addresses-explained/)
- [Private and public address](https://www.iplocation.net/public-vs-private-ip-address)
- [IPv4 and IPv6](https://www.webopedia.com/insights/ipv6-ipv4-difference/)
- [Localhost](https://en.wikipedia.org/wiki/Localhost)
- [TCP and UDP](https://www.howtogeek.com/190014/htg-explains-what-is-the-difference-between-tcp-and-udp/)
- [TCP/UDP ports List](https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers)
- [What is ping / ICMP](https://en.wikipedia.org/wiki/Ping_%28networking_utility%29)
- [Positional parameters](https://www.adminschoice.com/bash-positional-parameters)

### Man or help:
- `netstat`
- `ping`

## Learning Objectives

Upon completion of this project, you are expected to be able to explain the following without the help of Google:

- OSI Model
  - What it is
  - How many layers it has
  - How it is organized
- What is a LAN
  - Typical usage
  - Typical geographical size
- What is a WAN
  - Typical usage
  - Typical geographical size
- What is the Internet
- What is an IP address
  - What are the 2 types of IP addresses
- What is localhost
- What is a subnet
- Why IPv6 was created
- TCP/UDP
  - What are the 2 mainly used data transfer protocols for IP (transfer level on the OSI schema)
  - What is the main difference between TCP and UDP
- What is a port
  - Memorize SSH, HTTP, and HTTPS port numbers
- What tool/protocol is often used to check if a device is connected to a network

## Copyright and Plagiarism

You are tasked to come up with solutions for the tasks below yourself to meet the above learning objectives. You will not be able to meet the objectives of this or any following project by copying and pasting someone else's work. Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements

### General
- Allowed editors: vi, vim, emacs
- All your Bash script files will be interpreted on Ubuntu 20.04 LTS
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass shellcheck without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what the script is doing

## Tasks

### 0. OSI model
- [0-OSI_model](0-OSI_model) - Script that answers questions about the OSI model.

### 1. Types of network
- [1-types_of_network](1-types_of_network) - Script that answers questions about types of networks.

### 2. MAC and IP address
- [2-MAC_and_IP_address](2-MAC_and_IP_address) - Script that answers questions about MAC and IP addresses.

### 3. UDP and TCP
- [3-UDP_and_TCP](3-UDP_and_TCP) - Script that answers questions about UDP and TCP.

### 4. TCP and UDP ports
- [4-TCP_and_UDP_ports](4-TCP_and_UDP_ports) - Bash script that displays listening ports and the associated program to which each socket belongs.

### 5. Is the host on the network
- [5-is_the_host_on_the_network](5-is_the_host_on_the_network) - Bash script that pings an IP address passed as an argument.

---

**GitHub Repository:** [alx-system_engineering-devops](https://github.com/Lelaabk/alx-system_engineering-devops)  
**Directory:** 0x07-networking_basics

This project covers the fundamentals of networking and serves as an introduction to the OSI model, network types, MAC and IP addresses, UDP and TCP, and network port management. Please follow the instructions for each task to gain a deeper understanding of these networking concepts.
