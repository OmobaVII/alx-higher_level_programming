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

	original = *head;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	if (*head != NULL && (*head)->next == NULL)
		return (1);
	temp2 = NULL;
	while (original != NULL)
	{
		temp = original->next;
		original->next = temp2;
		temp2 = original;
		original = temp;
	}
	original = temp2;
	while (*head != NULL && temp2 != NULL)
	{
		if ((*head)->n != temp2->n)
		{
			return (0);
		}
		*head = (*head)->next;
		temp2 = temp2->next;
	}
	return (1);
}
