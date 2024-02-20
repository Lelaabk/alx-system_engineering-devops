# Project Title: Web Stack Debugging #4

## Description
This project focuses on debugging and improving the performance of a web server setup featuring Nginx. The task involves identifying and resolving issues causing a high rate of failed requests under pressure. The debugging process utilizes tools like ApacheBench and involves modifying server configurations to achieve optimal performance.

## Curriculum
- **SE Foundations**
  - Average: 127.0%
  - Web stack debugging #4
- **DevOps**
- **SysAdmin**
- **Scripting**
- **Debugging**

## Requirements
### General
- All files interpreted on Ubuntu 14.04 LTS
- Files should end with a new line
- Mandatory `README.md` file at the root of the project folder
- Puppet manifests must pass `puppet-lint` version 2.1.1 without errors
- Puppet manifests must run without errors
- Puppet manifests' first line must be a comment explaining their purpose
- Puppet manifests files must end with the extension `.pp`
- Files will be checked with Puppet v3.4
### Install puppet-lint
```bash
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
```

## Tasks
### 0. Sky is the limit, let's bring that limit higher (mandatory)
- Benchmarking reveals a high rate of failed requests.
- ApacheBench is used to simulate HTTP requests.
- Nginx server setup is modified to reduce failed requests to 0.

### 1. User limit (advanced)
- OS configuration is changed to allow login with the `holberton` user without encountering error messages regarding open files.

## Usage
1. Clone the GitHub repository: `alx-system_engineering-devops`
2. Navigate to directory: `0x1B-web_stack_debugging_4`
3. Run Puppet manifests:
   ```bash
   $ puppet apply <filename>.pp
   ```

## Repository
- **GitHub Repository**: [alx-system_engineering-devops](https://github.com/Lelaabk/alx-system_engineering-devops)
- **Directory**: `0x1B-web_stack_debugging_4`
- **Files**:
  - `0-the_sky_is_the_limit_not.pp`
  - `1-user_limit.pp`
