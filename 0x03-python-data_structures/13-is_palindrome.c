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
	printf("LOL 1\n");
	for (len = 0; dummy; len++)
		dummy = dummy->next;
	printf("list_len: %d\n", len);
	dummy = *head;
	x = len - 1;
	printf("Dummy: %d\n", dummy->n);
	array = malloc((sizeof(int) * len) + 1);
	if (array == NULL)
		return (-1);
	printf("Malloc pass\n");
	for (i = 0; dummy; i++)
	{
		printf("%d ", i);
		array[i] = dummy->n;
		dummy = dummy->next;
	}
	array[i--] = '\0';
	printf("len: %d\n", i);
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
