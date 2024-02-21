# Application Server Project

## Overview
This project focuses on setting up an application server using Python, Flask, Gunicorn, and Nginx. The goal is to deploy an application and ensure its proper functioning in both development and production environments. The project involves setting up the server, configuring Nginx to serve the application, managing dynamic content, and ensuring uninterrupted service during updates or reboots.

## Tasks

### 0. Set up development with Python
- Configure development environment for testing and debugging.
- Install necessary packages and clone the project repository.
- Configure Flask application to serve content from a specific route and port.

### 1. Set up production with Gunicorn
- Install Gunicorn and required libraries for production environment.
- Configure Gunicorn to serve content from the same route and port as in development.
- Verify functionality by binding Gunicorn instance to localhost and testing.

### 2. Serve a page with Nginx
- Configure Nginx to serve the application page both locally and on its public IP.
- Proxy requests to the process listening on the designated port.
- Ensure proper configuration for Nginx to serve the page.

### 3. Add a route with query parameters
- Expand the application by adding another service for Gunicorn to handle.
- Configure Nginx to proxy requests to the new route and the process listening on a different port.
- Ensure proper configuration to handle requests with query parameters.

### 4. Serve your AirBnB clone
- Deploy the AirBnB clone application on the server.
- Configure Nginx to serve content from the application.
- Ensure Nginx serves static assets properly for the website to render correctly.

### 5. Deploy it!
- Set up a systemd script to start the Gunicorn process on system boot.
- Configure Gunicorn to serve content with specific parameters.
- Ensure the systemd service is started and running.

### 6. No service interruption
- Write a Bash script to reload Gunicorn gracefully without downtime.
- Test the script to ensure proper functioning during updates or reboots.

## Files
- **README.md**: Documentation providing an overview of the project, tasks, and instructions for setup and execution.
- **0x1A-application_server**: Directory containing scripts and configuration files for the application server project.
- **4-reload_gunicorn_no_downtime**: Bash script for reloading Gunicorn without downtime.
- **gunicorn.service**: Systemd script for starting Gunicorn on system boot.
- **1-app_server-nginx_config**: Nginx configuration file for serving the application.
- **2-app_server-nginx_config**: Nginx configuration file for serving the application with added routes.
- **3-app_server-nginx_config**: Nginx configuration file for serving the application with query parameters.
- **4-app_server-nginx_config**: Nginx configuration file for serving AirBnB clone v3.
- **5-app_server-nginx_config**: Nginx configuration file for serving AirBnB clone v4.

## Resources
- [Application server vs web server](https://www.nginx.com/resources/glossary/application-server-vs-web-server/)
- [How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-16-04)
- [Running Gunicorn](https://docs.gunicorn.org/en/latest/run.html)
- [Upstart documentation](https://doc.ubuntu-fr.org/upstart)

---
