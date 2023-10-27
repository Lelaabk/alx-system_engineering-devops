#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

/**
 * infinite_while - sleeps indefinitely
 *
 * Return: Always returns 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Creates 5 zombie processes
 *
 * This program creates 5 child processes, turning them into zombies,
 * and prints their PIDs.
 *
 * Return: Always returns 0.
 */
int main(void)
{
	int x;
	pid_t child_pid;

	for (x = 0; x < 5; x++)
	{
		child_pid = fork();

		if (child_pid == 0)
		{
			/* Child process*/
			return (0);
		}
		else if (child_pid > 0)
		{
			/*Parent process*/
			printf("Zombie process created, PID: %d\n", child_pid);
		}
	}

	infinite_while();

	return (0);
}
