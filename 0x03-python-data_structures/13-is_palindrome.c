#include "lists.h"
#include <stddef.h>
#include <stdlib.h>

/**
 * is_palindrome - a function that checks if a singly linked list is
 * a palindrome
 * @head: the singly linked list
 * Return: 1 if palindrome and 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *current, *reversed, *temp;
	int count = 0;
	int i;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	if ((*head)->next == NULL)
		return (1);
	for (current = *head; current != NULL; current = current->next)
	{
		count++;
	}
	current = *head;
	reversed = NULL;
	for (i = 0; i < (count / 2); i++)
	{
		temp = current->next;
		current->next = reversed;
		reversed = current;
		current = temp;
	}
	if (count % 2 != 0)
		current = current->next;

	while (reversed != NULL && current != NULL)
	{
		if (reversed->n != current->n)
		{
			return (0);
		}
		reversed = reversed->next;
		current = current->next;
	}
	return (1);
}
