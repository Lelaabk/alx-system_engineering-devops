# 0x0E. Web stack debugging #1

## Project Overview

This project focuses on debugging and fixing issues with an Nginx installation on an Ubuntu 20.04 LTS container. The primary objective is to ensure that Nginx is running and listening on port 80 of all the server's active IPv4 IPs.

## Task Details

### Task 0: Nginx likes port 80

Using debugging skills, the task involves identifying and fixing the issue preventing Nginx from listening on port 80. The solution is automated through a Bash script (`0-nginx_likes_port_80`), and this README provides instructions on its usage.

### Task 1: Advanced - Debugging made short

Continuing from Task 0, this advanced task requires creating a short and sweet Bash script (`1-debugging_made_short`) to configure Nginx to listen on port 80. The script is limited to 5 lines, respecting Bash script requirements and without using `&&`.

## Project Structure

- `0-nginx_likes_port_80`: Bash script to configure Nginx to listen on port 80.
- `1-debugging_made_short`: Short and sweet Bash script for advanced debugging.
- `README.md`: Project documentation.

## Requirements

- Allowed editors: vi, vim, emacs
- Interpreted on Ubuntu 20.04 LTS
- Files end with a new line
- Bash script files must be executable
- Bash scripts must pass Shellcheck without any error
- Bash scripts must run without error
- First line of Bash scripts: `#!/usr/bin/env bash`
- Second line of Bash scripts: A comment explaining what the script is doing
- Not allowed to use wget

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/Lelaabk/alx-system_engineering-devops.git
    cd alx-system_engineering-devops/0x0E-web_stack_debugging_1
    ```

2. Task 0: Make the script executable:

    ```bash
    chmod +x 0-nginx_likes_port_80
    ```

    Run the script:

    ```bash
    ./0-nginx_likes_port_80 > /dev/null 2&>1
    ```

3. Task 1: Make the script executable:

    ```bash
    chmod +x 1-debugging_made_short
    ```

    Run the script:

    ```bash
    ./1-debugging_made_short
    ```

4. Verify Nginx is listening on port 80:

    ```bash
    curl 0:80
    ```

If successful, you should see the Nginx welcome page.
