#include "lists.h"

listint_t *rev(listint_t **h);
int _pali(listint_t **h);

/**
 * rev - reverses list
 * @h: beginning of node
 *
 * Return: h
 */
listint_t *rev(listint_t **h)
{
	listint_t *a = *h, *b, *c = NULL;

	while (a)
	{
		b = a->next;
		a->next = c;
		c = a;
		a = b;
	}

	*h = c;

	return (*h);
}
/**
 * _pali - checks if list is palindrome
 * @h: beginning of node
 *
 * Return: h
 */
int _pali(listint_t **h)
{
	listint_t *a = *h, *b = *h, *c = *h, *d = NULL;

	if (*h == NULL || (*h)->next == NULL)
		return (1);

	while (1)
	{
		b = b->next->next;
		if (!b)
		{
			d = a->next;
			break;
		}
		if (!b->next)
		{
			d = a->next->next;
			break;
		}
		a = a->next;
	}
	rev(&d);

	while (d && c)
	{
		if (c->n == d->n)
		{
			d = d->next;
			c = c->next;
	}
		else
			return (0);
	if (!d)
		return (0);

	return (0);
}
