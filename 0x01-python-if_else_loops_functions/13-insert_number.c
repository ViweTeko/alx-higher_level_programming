#include "lists.h"

/**
 * in_node - inserts number into sorted singly linked list
 * @h: pointer to head of node
 * @num: number to insert
 *
 * Return: NULL if fails, or pointer to new node
 */
listint_t *in_node(listint_t **h, int num)
{
	listint_t *a = *h, *b;

	b = malloc(sizeof(listint_t));
	if (b == NULL)
		return (NULL);
	b->n = num;

	if (a == NULL || a->n >= num)
	{
		b->next = a;
		*h = b;
		return (b);
	}

	while (a && a->next && a->next->n < num)
		a = a->next;
	b->next = a->next;
	a->next = b;

	return (b);
}
