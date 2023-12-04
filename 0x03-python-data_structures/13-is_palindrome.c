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
	listint_t *a, *b, *c;
	size_t d = 0, e;

	if (*h == NULL || (*h)->next == NULL)
		return (1);

	a = *h;
	while (a)
	{
		d++;
		a = a->next;
	}
	a = *h;
	for (e = 0; e < (d / 2) - 1; e++)
		a = a->next;
	if ((d % 2) == 0 && a->n != a->next->n)
		return (0);
	a = a->next->next;
	b = rev(&a);
	c = b;

	a = *h;
	while (b)
	{
		if (a->n != b->n)
			return (0);
		a = a->next;
		b = b->next;
	}
	rev(&c);

	return (1);
}
