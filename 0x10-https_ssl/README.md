# HTTPS SSL Configuration Project

## Overview
This project focuses on configuring HTTPS SSL, DNS, and handling web stack debugging tasks to enhance the security and performance of a web infrastructure. It involves setting up subdomains, pointing them to specific IPs, and configuring HAProxy for SSL termination.

## Table of Contents
- [Tasks](#tasks)
  - [Task 0: World Wide Web](#task-0-world-wide-web)
  - [Task 1: HAProxy SSL Termination](#task-1-haproxy-ssl-termination)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Scripts](#scripts)

## Tasks

### Task 0: World Wide Web
The script `0-world_wide_web` configures domain zones and subdomains. It accepts a domain name and an optional subdomain as arguments, using `dig` and `awk` to display information about the subdomains.

**Example usage:**
```bash
./0-world_wide_web holberton.online
./0-world_wide_web holberton.online web-02
```

### Task 1: HAProxy SSL Termination
The script `1-haproxy_ssl_termination` sets up HAProxy to terminate SSL traffic for the subdomain www. It uses certbot to create a certificate and configures HAProxy to accept encrypted traffic on TCP port 443.

**Example usage:**
```bash
./1-haproxy_ssl_termination
```

## Prerequisites
- Ubuntu 16.04 LTS
- HAProxy 1.5 or higher
- Certbot
- Bash shell

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/Lelaabk/alx-system_engineering-devops.git
   cd alx-system_engineering-devops/0x10-https_ssl
   ```

2. Execute the scripts:
   ```bash
   ./0-world_wide_web holberton.online
   ./1-haproxy_ssl_termination
   ```

## Scripts
- [0-world_wide_web](0-world_wide_web): Configures domain zones and displays subdomain information.
- [1-haproxy_ssl_termination](1-haproxy_ssl_termination): Configures HAProxy for SSL termination.
