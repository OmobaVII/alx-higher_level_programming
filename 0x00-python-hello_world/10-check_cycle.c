#include "lists.h"

/**
 * check_cycle - a function that checks if there is a cycle in a singly linked list
 * @list: the singly linked list
 * Return: 0 if no cycle and 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *p;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}
	if (list->next == NULL || list->next->next == NULL)
	{
		return (0);
	}
	p = list->next->next;
	if (p->next != NULL && p->next->next != NULL)
		return (1);
	else
		return (0);
}
