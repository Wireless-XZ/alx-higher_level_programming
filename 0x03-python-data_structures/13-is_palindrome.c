#include "lists.h"

/**
 * is_palindrome - Write a function in C that checks
 * if a singly linked list is a palindrome.
 * @head: head node of the list
 *
 * Return: 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	int len, i = 0, n;
	char *array;

	if (head == NULL)
		return (1);
	for (len = 0; *head; len++)
		*head = (*head)->next;
	n = len - 1;
	array = malloc(sizeof(int) * (len + 1));
	if (array == NULL)
		return (-1);
	for (i = 0; *head; i++)
		array[i] = (*head)->n;
	array[i] = '\0';
	for (i = 0; n > i; i++, n--)
	{
		if (array[i] != array[n])
		{
			free(array);
			return (0);
		}
	}

	free(array);
	return (1);
}
