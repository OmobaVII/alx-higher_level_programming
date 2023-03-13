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
	listint_t *original, *temp2, *temp;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	if ((*head)->next == NULL)
		return (1);
	original = *head;
	temp2 = NULL;
	while (original != NULL)
	{
		temp = original->next;
		original->next = temp2;
		temp2 = original;
		original = temp;
	}
	original = temp2;
	temp2 = NULL;
	while (*head != NULL && original != NULL)
	{
		if ((*head)->n != original->n)
		{
			return (0);
		}
		*head = (*head)->next;
		original = original->next;
	}
	return (1);
}
