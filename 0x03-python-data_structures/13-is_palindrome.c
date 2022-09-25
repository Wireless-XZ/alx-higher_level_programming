#include "lists.h"
#include <string.h>
#include <stdio.h>

/**
 * is_palindrome - Write a function in C that checks
 * if a singly linked list is a palindrome.
 * @head: head node of the list
 *
 * Return: 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	int len, i, x;
	char *array = NULL;
	listint_t *dummy;

	dummy = *head;
	if (*head == NULL)
		return (1);
	for (len = 0; dummy; len++)
		dummy = dummy->next;
	dummy = *head;
	x = len - 1;
	array = malloc((sizeof(int) * len) + 1);
	if (array == NULL)
		return (-1);
	for (i = 0; dummy; i++)
	{
		array[i] = dummy->n;
		dummy = dummy->next;
	}
	array[i--] = '\0';
	for (x = 0; i > x; x++, i--)
	{
		if (array[x] != array[i])
		{
			free(array);
			return (0);
		}
	}
	free(array);
	return (1);
}
