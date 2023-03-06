#include "lists.h"

/**
 * check_cycle - a function that checks if there is a cycle in a singly linked list
 * @list: the singly linked list
 * Return: 0 if no cycle and 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}
	fast = list->next;
	slow = list;
	while (fast != NULL && fast->next != NULL)
	{
		if (slow == fast)
		{
			return (1);
		}
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
