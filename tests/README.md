# ALX System Engineering & DevOps - SSH Project

## Project Overview

This project focuses on understanding and implementing secure communication with an Ubuntu server using SSH. The tasks involve creating and using SSH key pairs, configuring the SSH client, and enhancing security through Puppet automation.

### Background Context

In this project, you have been assigned an Ubuntu server accessible via SSH in a remote datacenter. The server is configured with an Ubuntu 20.04 LTS environment, and connection is secured using an RSA key. The goal is to complete various tasks related to SSH configuration and understand key concepts such as servers, SSH, and RSA key pairs.

### Learning Objectives

Upon completion of this project, you should be able to:

- Explain what a server is and where servers typically reside.
- Understand the basics of SSH, its advantages, and how to create an SSH RSA key pair.
- Connect to a remote host using an SSH RSA key pair.
- Comprehend the use of `#!/usr/bin/env bash` versus `/bin/bash`.
- Demonstrate knowledge of SSH client configuration.

### Resources

Make sure to review the following resources to enhance your understanding:

- What is a (physical) server - [text](https://en.wikipedia.org/wiki/Server_%28computing%29#Hardware_requirement) | [video](https://www.youtube.com/watch?v=B1ANfsDyjeA)
- [SSH essentials](https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys)
- [SSH Config File](https://www.ssh.com/academy/ssh/config)
- [Public Key Authentication for SSH](https://www.ssh.com/academy/ssh/public-key-authentication)
- [How Secure Shell Works](https://www.youtube.com/watch?v=ORcvSkgdA58)
- [SSH Crash Course](https://www.youtube.com/watch?v=hQWRp-FdTpc) (Watch at x1.25 speed or above)
- [Understanding the SSH Encryption and Connection Process] (https://www.digitalocean.com/community/tutorials/understanding-the-ssh-encryption-and-connection-process)
- [Secure Shell Wiki](https://en.wikipedia.org/wiki/Secure_Shell)
- [IETF RFC 4251](https://www.ietf.org/rfc/rfc4251.txt) (Description of the SSH Protocol)

### Project Structure

The project is organized into directories and files as follows:

1. **0x0B-ssh**
    - **0-use_a_private_key**
        - `0-use_a_private_key`: Bash script for connecting to the server using an RSA private key.
    - **1-create_ssh_key_pair**
        - `1-create_ssh_key_pair`: Bash script for creating an RSA key pair.
    - **2-ssh_config**
        - `2-ssh_config`: SSH client configuration file.
    - **3-remote_authorized_keys**
        - `3-remote_authorized_keys`: File containing the SSH public key for server access.
    - **100-puppet_ssh_config.pp**
        - `100-puppet_ssh_config.pp`: Puppet script for configuring the SSH client file.

### Requirements

- **Allowed Editors:** vi, vim, emacs
- **Interpreter:** Ubuntu 20.04 LTS
- **File Endings:** All files should end with a new line
- **Executable Bash Scripts:** All Bash scripts must be executable
- **Shebang:** The first line of all Bash scripts should be `#!/usr/bin/env bash`
- **Comments:** The second line of all Bash scripts should be a comment explaining the script's purpose

### Copyright and Plagiarism

Please be aware of the following:

- You are responsible for solving the tasks yourself to meet the learning objectives.
- Do not copy and paste solutions; plagiarism is strictly forbidden.
- Do not publish any content from this project.

### Tasks

#### 0. Use a Private Key

Write a Bash script to connect to the server using an RSA private key.

```bash
$ ./0-use_a_private_key
```

#### 1. Create an SSH Key Pair

Write a Bash script to create an RSA key pair.

```bash
$ ./1-create_ssh_key_pair
```

#### 2. Client Configuration File

Configure the local SSH client to use the private key and refuse password authentication.

```bash
$ ssh -v ubuntu@your_server_ip
```

#### 3. Let Me In!

Add the provided SSH public key to your server to enable connection using the ubuntu user.

#### 4. Client Configuration File (w/ Puppet)

Use Puppet to automate the configuration of the SSH client file.

```bash
$ sudo puppet apply 100-puppet_ssh_config.pp
```
