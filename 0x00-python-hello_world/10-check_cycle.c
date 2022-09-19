#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle
 * @list: pointer to the head node
 *
 * Return: 1 if there is a cycle, 0 if otherwise
 */
int check_cycle(listint_t *list)
{
	const listint_t *current, *holder, *dummy;
	int n, i;

	current = holder = list;
	n = i = 0;
	while (current != NULL)
	{
		if (i)
		{
			dummy = holder;
			while (dummy)
			{
				if (current->next == dummy)
					return (1);
				else if (dummy->next == current)
					break;
				dummy = dummy->next;
			}
		}
		current = current->next;
		n++;
		i++;
	}
	return (0);
}
