#include <stdlib.h>
#include "lists.h"

/**
 * _cycle - checks list containig cycle
 * @l: singly linked list
 *
 * Return: 0 or 1
 */
int _cycle(listint_t *l)
{
	listint_t *j, *k;

	if (l == NULL || l->next == NULL)
		return (0);

	j = l->next;
	k = l->next->next;

	while (j && k && k->next)
	{
		if (j == k)
			return (1);
		j = j->next;
		k = k->next->next;
	}
	return (0);
}
