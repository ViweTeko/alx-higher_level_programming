#include "lists.h"

/**
 * insert_node - inserts number into sorted singly linked list
 * @head: pointer to head of node
 * @number: number to insert
 *
 * Return: NULL if fails, or pointer to new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *a = *head, *b;

	b = malloc(sizeof(listint_t));
	if (b == NULL)
		return (NULL);
	b->n = number;

	if (a == NULL || a->n >= number)
	{
		b->next = a;
		*head = b;
		return (b);
	}

	while (a && a->next && a->next->n < number)
		a = a->next;
	b->next = a->next;
	a->next = b;

	return (b);
}
