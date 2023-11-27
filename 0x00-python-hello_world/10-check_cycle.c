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

/**
 * print_lint - prints all elements of a linked list
 * @h: pointer to head of file
 *
 * Return: num of nodes
 */
size_t print_lint(const listint_t *h)
{
        const listint_t *a;
        unsigned int b;

        a = h;

        for (b = 0; a != NULL; b++)
        {
                printf("%i\n", a->n);
                a = a->next;
        }
        return (b);
}
