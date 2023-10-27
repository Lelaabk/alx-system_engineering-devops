# 0x05. Processes and Signals

This repository contains a series of Bash scripts to help you understand and work with processes and signals in Linux. Each script is designed to achieve specific learning objectives. Make sure to follow the requirements for each script to ensure compatibility and correctness.

## Learning Objectives
By completing the tasks in this project, you will be able to:

- Understand what a PID (Process ID) is.
- Identify and manage processes in a Linux environment.
- Work with signals in Linux.
- Create Bash scripts to achieve various process-related tasks.

## Resources
Before you start working on the tasks, it's recommended to familiarize yourself with the following resources:

- [Linux PID](https://en.wikipedia.org/wiki/Process_identifier)
- [Linux process](https://en.wikipedia.org/wiki/Process_(computing))
- [Linux signal](https://en.wikipedia.org/wiki/Signal_(IPC))
- [Process management in Linux](https://linux.die.net/man/1/ps)

## Task Descriptions
1. **What is my PID**
   - Write a Bash script that displays its own PID.
   - Example usage:
     ```bash
     ./0-what-is-my-pid
     ```

2. **List your processes**
   - Write a Bash script that displays a list of currently running processes.
   - Requirements:
     - Must show all processes for all users, including those without a TTY.
     - Display in a user-oriented format with process hierarchy.
   - Example usage:
     ```bash
     ./1-list_your_processes | head -50
     ```

3. **Show your Bash PID**
   - Create a Bash script to display lines containing the word "bash" and its PID.
   - You cannot use pgrep.
   - Example usage:
     ```bash
     ./2-show_your_bash_pid
     ```

4. **Show your Bash PID made easy**
   - Write a Bash script to display the PID and process name of all processes containing the word "bash."
   - You cannot use the `ps` command.
   - Example usage:
     ```bash
     ./3-show_your_bash_pid_made_easy
     ```

5. **To infinity and beyond**
   - Create a Bash script that displays "To infinity and beyond" indefinitely with a sleep interval.
   - Use `sleep 2` between each iteration.
   - Example usage:
     ```bash
     ./4-to_infinity_and_beyond
     ```

6. **Don't stop me now!**
   - Write a Bash script that stops the process created by the 4-to_infinity_and_beyond script.
   - Use the `kill` command.
   - Example usage:
     ```bash
     ./5-dont_stop_me_now
     ```

7. **Stop me if you can**
   - Create a Bash script to stop the process created by the 4-to_infinity_and_beyond script.
   - You cannot use the `kill` or `killall` command.
   - Example usage:
     ```bash
     ./6-stop_me_if_you_can
     ```

8. **Highlander**
   - Write a Bash script that displays "To infinity and beyond" indefinitely with a sleep interval.
   - Display "I am invincible!!!" when receiving a SIGTERM signal.
   - Create a copy of your 6-stop_me_if_you_can script, name it 67-stop_me_if_you_can, and use it to kill the 7-highlander process instead of the 4-to_infinity_and_beyond one.
   - Example usage:
     ```bash
     ./7-highlander
     ```

9. **Beheaded process**
   - Create a Bash script to kill the 7-highlander process.
   - Example usage:
     ```bash
     ./8-beheaded_process
     ```

Remember to follow the requirements for each script, and ensure they are executable and free of errors when checked with Shellcheck.

**Note:** Avoid plagiarism and refrain from publishing project content.
