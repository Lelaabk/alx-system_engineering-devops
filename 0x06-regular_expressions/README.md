# Project Title: 0x06 Regular Expression

## Overview

This project is part of the "0x06. Regular expression" series and focuses on working with regular expressions using the Oniguruma library, which is the default regular expression library for Ruby. The project's objective is to create Ruby scripts that utilize regular expressions to perform various pattern matching tasks.

## Project Details

- **Project Name**: 0x06 Regular Expression
- **Project Weight**: 1
- **Project Start Date**: October 31, 2023, 4:00 AM
- **Project End Date**: November 1, 2023, 4:00 AM
- **Checker Release Date**: October 31, 2023, 10:00 AM
- **Auto Review Deadline**: Deadline

## Concepts

For this project, you will be working with the following concept:

- **Regular Expression**: Understanding and using regular expressions for pattern matching.

## Project Background

In this project, you will be required to build regular expressions using the Oniguruma library, which is the default regular expression library for Ruby. Please note that different regular expression libraries may have varying properties, so it's essential to stick to Oniguruma as per project requirements.

The primary focus of this exercise is to work with regular expressions, and you will be provided with Ruby code that you should modify by replacing the regular expression part in the code.

Here is the template Ruby code that you should use:

```ruby
#!/usr/bin/env ruby
puts ARGV[0].scan(/your-regular-expression-here/).join
```

## Resources

Before starting the project, you can review the following resources to get a better understanding of regular expressions:

- [Regular expressions - basics](https://www.slideshare.net/neha_jain/introducing-regular-expressions)
- [Regular expressions - advanced](https://www.slideshare.net/neha_jain/advanced-regular-expressions-80296518)
- [Rubular](https://rubular.com/): An online tool for testing and experimenting with regular expressions.
- "Use a regular expression against a problem: now you have 2 problems"
- [Learn Regular Expressions with simple, interactive exercises](https://regexone.com/)

## Requirements

### General

- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 20.04 LTS
- All your files should end with a new line
- A `README.md` file at the root of the project folder is mandatory
- All your Bash script files must be executable
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env ruby`
- All regular expressions must be built for the Oniguruma library

## Tasks

### 0. Simply matching School

Create a Ruby script that matches the regular expression "School" and accepts one argument to pass to the regular expression matching method. Example:

```shell
$ ./0-simply_match_school.rb School | cat -e
School$
$ ./0-simply_match_school.rb "Best School" | cat -e
School$
$ ./0-simply_match_school.rb "School Best School" | cat -e
SchoolSchool$
$ ./0-simply_match_school.rb "Grace Hopper" | cat -e
$
```

### 1. Repetition Token #0

Find the regular expression that matches specified cases and create a Ruby script that accepts one argument to pass to the regular expression matching method.

### 2. Repetition Token #1

Find the regular expression that matches specified cases and create a Ruby script that accepts one argument to pass to the regular expression matching method.

### 3. Repetition Token #2

Find the regular expression that matches specified cases and create a Ruby script that accepts one argument to pass to the regular expression matching method.

### 4. Repetition Token #3

Find the regular expression that matches specified cases and create a Ruby script that accepts one argument to pass to the regular expression matching method. Your regex should not contain square brackets.

### 5. Not quite HBTN yet

Create a regular expression that matches a string that starts with "h," ends with "n," and can have any single character in between. Create a Ruby script that accepts one argument to pass to the regular expression matching method. Example:

```shell
$ ./5-beginning_and_end.rb 'hn' | cat -e
$
$ ./5-beginning_and-end.rb 'hbn' | cat -e
hbn$
$ ./5-beginning-and-end.rb 'hbtn' | cat -e
$
$ ./5-beginning-and-end.rb 'h8n' | cat -e
h8n$
```

### 6. Call me maybe

Create a regular expression that matches a 10-digit phone number and create a Ruby script that accepts one argument to pass to the regular expression matching method. Example:

```shell
$ ./6-phone_number.rb 4155049898 | cat -e
4155049898$
$ ./6-phone_number.rb " 4155049898" | cat -e
$
$ ./6-phone_number.rb "415 504 9898" | cat -e
$
$ ./6-phone_number.rb "415-504-9898" | cat -e
$
```

### 7. OMG WHY ARE YOU SHOUTING?

Create a regular expression that only matches capital letters and create a Ruby script that accepts one argument to pass to the regular expression matching method. Example:

```shell
$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "I realLy hOpe VancouvEr posseSs Yummy Soft vAnilla Dupper Mint Ice Nutella cream" | cat -e
ILOVESYSADMIN$
$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "WHAT do you SAY?" | cat -e
WHATSAY$
$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "cannot read you" | cat -e
$
```
### 8. Textme
**Advanced**

This exercise was prepared for you by Guillaume Plessis, VP of Infrastructure at TextMe. It is something he uses daily. You can thank Guillaume for his project on Twitter.

For this task, you’ll be taking over Guillaume’s responsibilities: one afternoon, a TextMe VoIP Engineer comes to you and explains she wants to run some statistics on the TextMe app text messages transactions.

**Requirements:**

- Your script should output: [SENDER],[RECEIVER],[FLAGS]

- The sender phone number or name (including country code if present)

- The receiver phone number or name (including country code if present)

- The flags that were used

- You can find a [log file here].

**Example:**

```shell
$ ./100-textme.rb 'Feb 1 11:00:00 ip-10-0-0-11 mdr: 2016-02-01 11:00:00 Receive SMS [SMSC:SYBASE1] [SVC:] [ACT:] [BINF:] [FID:] [from:Google] [to:+16474951758] [flags:-1:0:-1:0:-1] [msg:127:This planet has - or rather had - a problem, which was this: most of the people on it were unhappy for pretty much of the time.] [udh:0:]'
Google,+16474951758,-1:0:-1:0:-1
$
$
$ ./100-textme.rb 'Feb 1 11:00:00 ip-10-0-64-10 mdr: 2016-02-01 11:00:00 Receive SMS [SMSC:SYBASE2] [SVC:] [ACT:] [BINF:] [FID:] [from:+17272713208] [to:+19172319348] [flags:-1:0:-1:0:-1] [msg:136:Orbiting this at a distance of roughly ninety-two million miles is an utterly insignificant little blue green planet whose ape-descended] [udh:0:]'
+17272713208,+19172319348,-1:0:-1:0:-1
$
$ ./100-textme.rb 'Feb 1 11:00:00 ip-10-0-64-11 mdr: 2016-02-01 11:00:00 Sent SMS [SMSC:SYBASE1] [SVC:backendtextme] [ACT:] [BINF:] [FID:] [from:18572406905] [to:14022180266] [flags:-1:0:-1:-1:-1] [msg:136:Far out in the uncharted backwaters of the unfashionable end of the western spiral arm of the Galaxy lies a small unregarded yellow sun.] [udh:0:]'
18572406905,14022180266,-1:0:-1:-1:-1
$
$
$ ./100-textme.rb 'Feb 1 11:00:00 ip-10-0-64-11 mdr: 2016-02-01 11:00:00 Sent SMS [SMSC:SYBASE1] [SVC:backendtextme] [ACT:] [BINF:] [FID:] [from:12392190384] [to:19148265919] [flags:-1:0:-1:-1:-1] [msg:99:life forms are so amazingly primitive that they still think digital watches are a pretty neat idea.] [udh:0:]'
12392190384,19148265919,-1:0:-1:-1:-1
$
```

## Project Repository

- **GitHub Repository**: [alx-system_engineering-devops](https://github.com/Lelaabk/alx-system_engineering-devops/tree/main/0x06-regular_expressions)
- **Directory**: 0x06-regular_expressions


## Author
This project was prepared by Layla ABKARI for the ALX System Engineering & DevOps program.

- **LinkedIn Profile**: [Layla ABKARI](https://www.linkedin.com/in/layla-abkari-5505301a3/)

Acknowledgments
Special thanks to Guillaume Plessis, VP of Infrastructure at TextMe, and Neha Jain, Senior Software Engineer at LinkedIn, for their contributions to this project.
---

Please feel free to reach out if you have any questions or need further assistance with the project. Good luck with your regular expression tasks!
