#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

void dummy(void);

/**
 * insert_node - inserts a numver into a sorted singly linked list
 * @head: the head node
 * @number: the numer to be added to the linked list
 *
 * Return: address of the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *dummy, *new, *last = NULL;

	dummy = *head;
	while (dummy != NULL)
	{
		if (dummy->n >= number)
		{
			new = malloc(sizeof(listint_t));
			if (new == NULL)
				return (NULL);
			new->n = number;
			new->next = dummy;
			if (last)
			{
				last->next = new;
				break;
			}
			else
			{
				*head = new;
				return (*head);
			}
		}
		else if (dummy->next == NULL)
		{
			new = malloc(sizeof(listint_t));
			if (new == NULL)
				return (NULL);
			new->n = number;
			new->next = NULL;
			dummy->next = new;
			break;
		}
		last = dummy;
		dummy = dummy->next;
	}
	return (*head);
}

/**
 * dummy - bypass betty
 */
void dummy(void)
{
}
