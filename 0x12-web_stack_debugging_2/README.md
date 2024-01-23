# 0x12-web_stack_debugging_2

## Description

This repository contains scripts for debugging and configuring web stack components, addressing specific issues related to user permissions and Nginx configuration.

## Table of Contents

- [Files](#files)
- [Requirements](#requirements)
- [Usage](#usage)
- [Debugging Scripts](#debugging-scripts)
- [Issues Resolved](#issues-resolved)
- [Author](#author)

## Files

1. **[0-iamsomeoneelse](0x12-web_stack_debugging_2/0-iamsomeoneelse):**
   - Bash script to run the `whoami` command under a specified user.

2. **[1-run_nginx_as_nginx](0x12-web_stack_debugging_2/1-run_nginx_as_nginx):**
   - Bash script to configure Nginx to run as the `nginx` user and listen on all active IPs on port 8080.

## Requirements

- All scripts are intended to be executed on Ubuntu 20.04 LTS.
- Scripts should be executable (`chmod +x script_name`).
- Scripts should pass Shellcheck without any errors.
- Detailed requirements for each script are mentioned in their respective sections.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/Lelaabk/alx-system_engineering-devops.git
   cd alx-system_engineering-devops/0x12-web_stack_debugging_2
   ```

2. Execute the desired script:

   ```bash
   ./script_name [arguments]
   ```

## Debugging Scripts

### 0-iamsomeoneelse

- **Description:**
  - Accepts one argument (username).
  - Runs the `whoami` command under the specified user.

- **Usage:**
  ```bash
  ./0-iamsomeoneelse username
  ```

### 1-run_nginx_as_nginx

- **Description:**
  - Configures Nginx to run as the `nginx` user.
  - Ensures Nginx is listening on all active IPs on port 8080.

- **Usage:**
  ```bash
  ./1-run_nginx_as_nginx
  ```

## Issues Resolved

1. **0-iamsomeoneelse:**
   - Ensures the correct execution of the `whoami` command under a specified user.

2. **1-run_nginx_as_nginx:**
   - Configures Nginx to run as the `nginx` user.
   - Ensures Nginx is listening on all active IPs on port 8080.

## Author

- [Layla Abkari](https://github.com/Lelaabk)

