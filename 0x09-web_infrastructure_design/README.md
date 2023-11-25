# 0x09. Web Infrastructure Design

## Project Overview

This project, part of the ALX System Engineering and DevOps curriculum, focuses on understanding and implementing key concepts in web infrastructure design. It is to be completed in teams of 3 people, with a designated start and end date.

**Project Information:**
- **Author:** Sylvain Kalache, co-founder at Holberton School
- **Weight:** 1
- **Team:** Layla ABKARI
- **Project Start:** Nov 23, 2023, 4:00 AM
- **Project End:** Nov 27, 2023, 4:00 AM
- **Manual QA Review:** Mandatory upon project completion

## Concepts

This project covers the following key concepts:

- DNS
- Monitoring
- Web Server
- Network basics
- Load balancer
- Server

## Resources

Before starting the tasks, it is recommended to read or watch the following resources:

- [Network basics concept page](https://intranet.alxswe.com/concepts/33)
- [Server concept page](https://intranet.alxswe.com/concepts/67)
- [Web server concept page](https://intranet.alxswe.com/concepts/17)
- [DNS concept page](https://intranet.alxswe.com/concepts/12)
- [Load balancer concept page](https://intranet.alxswe.com/concepts/46)
- [Monitoring concept page](https://intranet.alxswe.com/concepts/13)
- [What is a database](https://www.oracle.com/ke/database/what-is-database/)
- [Difference between a web server and an app server](https://www.infoworld.com/article/2077354/app-server-web-server-what-s-the-difference.html)
- [DNS record types](https://www.site24x7.com/learn/dns-record-types.html)
- [Single point of failure](https://avinetworks.com/glossary/single-point-of-failure/)
- [Avoiding downtime when deploying new code](https://softwareengineering.stackexchange.com/questions/35063/how-do-you-update-your-production-codebase-database-schema-without-causing-downt#answers-header)
- [High availability cluster (active-active/active-passive)](https://docs.oracle.com/cd/E17904_01/core.1111/e10106/intro.htm#ASHIA714)
- [What is HTTPS](https://www.instantssl.com/http-vs-https)
- [What is a firewall](https://www.webopedia.com/definitions/firewall/)

## Learning Objectives

Upon completion of this project, you should be able to:

- Draw a diagram covering the web stack built with sysadmin/devops track projects.
- Explain the function of each component in the web infrastructure.
- Describe system redundancy.
- Understand and use acronyms: LAMP, SPOF, QPS.

## Copyright - Plagiarism

- Solutions for tasks must be developed independently.
- Plagiarism is strictly forbidden and will result in removal from the program.
- Do not publish any content of this project.

## Requirements

### General

- A `README.md` file at the root of the project folder is mandatory.
- For each task, provide a picture/screenshot of the whiteboard diagram.
- Project will be manually reviewed.
- URLs for completed tasks must be provided.
- Whiteboard each task in front of a mentor, staff, or student without computer or notes.
- Focus on the requirements and avoid unnecessary details.

## Tasks

### 0. Simple Web Stack

**Requirements:**
- Design a one-server web infrastructure for www.foobar.com.
- Components: 1 server, 1 Nginx web server, 1 application server, 1 MySQL database, 1 domain name.
- Explain the role of each component.
- Identify issues: SPOF, downtime during maintenance, scalability.

**Add URLs:**
- [GitHub Repository](https://github.com/Lelaabk/alx-system_engineering-devops/tree/main/0x09-web_infrastructure_design)
- [Screenshot of Whiteboard Diagram](https://github.com/Lelaabk/alx-system_engineering-devops/blob/main/0x09-web_infrastructure_design/Screenshots/Simple%20web%20stack.png)

### 1. Distributed Web Infrastructure

**Requirements:**
- Design a three-server web infrastructure for www.foobar.com.
- Components: 2 servers, 1 Nginx web server, 1 application server, 1 HAproxy load balancer, 1 MySQL database.
- Explain the purpose of each component.
- Discuss distribution algorithm, Active-Active vs. Active-Passive, and Primary-Replica cluster.

**Add URLs:**
- [GitHub Repository](https://github.com/Lelaabk/alx-system_engineering-devops/tree/main/0x09-web_infrastructure_design)
- [Screenshot of Whiteboard Diagram](https://github.com/Lelaabk/alx-system_engineering-devops/blob/main/0x09-web_infrastructure_design/Screenshots/Distributed%20web%20infrastructure.png)

### 2. Secured and Monitored Web Infrastructure

**Requirements:**
- Design a three-server web infrastructure for www.foobar.com with security, HTTPS, and monitoring.
- Components: 3 firewalls, SSL certificate, 3 monitoring clients.
- Explain the rationale behind each addition.
- Address issues: SSL termination, single writable MySQL server, uniform server components.

**Add URLs:**
- [GitHub Repository](https://github.com/Lelaabk/alx-system_engineering-devops/tree/main/0x09-web_infrastructure_design)
- [Screenshot of Whiteboard Diagram](#)
