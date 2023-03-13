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
	listint_t *original, *temp2, *ptr;

	original = *head;
	ptr = NULL;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	temp2 = malloc(sizeof(listint_t));
	while (original != NULL)
	{
		temp2->n = original->n;
		temp2->next = ptr;
		ptr = temp2;
		original = original->next;
	}
	while (*head != NULL && ptr != NULL)
	{
		if ((*head)->n != ptr->n)
		{
			return (0);
		}
		*head = (*head)->next;
		ptr = ptr->next;
	}
	return (1);
}
