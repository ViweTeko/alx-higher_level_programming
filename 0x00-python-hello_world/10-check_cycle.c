#include "lists.h"

/**
 * _cycle - checks list containing cycle
 * @l: singly linked list
 *
 * Return: 0 or 1
 */
int _cycle(listint_t *l)
{
	listint_t *j, *k;

	if (l == NULL || l->next == NULL)
		return (0);

	j = k = l;
	while (1)
	{
		if (k->next && k->next->next)
		{
			k = k->next->next;
			j = j->next;
			if (j == k)
				return (1);
		}
		else	
			return (0);
	}
}
