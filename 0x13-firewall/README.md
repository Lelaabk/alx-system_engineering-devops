# 0x13-firewall

This repository contains scripts and configurations related to implementing firewall rules on servers.

## Overview

In this project, we focus on configuring firewall settings using UFW (Uncomplicated Firewall) on the `web-01` server. The main objectives include blocking all incoming traffic except for specific TCP ports and implementing port forwarding.

## Files

### 0-block_all_incoming_traffic_but

This script installs UFW on the `web-01` server and configures it to block all incoming traffic, except for the following TCP ports:
- 22 (SSH)
- 443 (HTTPS SSL)
- 80 (HTTP)

#### Usage:

```bash
./0-block_all_incoming_traffic_but


### 100-port_forwarding

This configuration file modifies UFW settings on `web-01` to implement port forwarding. It redirects incoming traffic on port 8080/TCP to port 80/TCP.

#### Usage:

Apply the changes using:

```bash
sudo ufw reload
```

## Verification

To verify the changes, you can use tools like `netstat` and `curl`. The `netstat` command shows the active connections and the ports on which the server is listening. Additionally, the `curl` commands from `web-02` demonstrate that the firewall is forwarding ports correctly.

## Notes

- Be cautious when working with firewall rules to avoid accidental lockout.
- Follow the provided instructions in the comments of the scripts for proper execution.

## Repository Information

- **GitHub Repository:** [alx-system_engineering-devops](https://github.com/Lelaabk/alx-system_engineering-devops)
- **Directory:** 0x13-firewall
