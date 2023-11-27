#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

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
