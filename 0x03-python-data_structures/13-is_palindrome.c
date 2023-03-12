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
	listint_t *original, *temp, *temp2, *ptr;

	original = *head;
	ptr = NULL;
	temp = original;

	while (temp != NULL)
	{
		temp2 = malloc(sizeof(listint_t));
		temp2->n = temp->n;
		temp2->next = ptr;
		ptr = temp2;
		temp = temp->next;
	}
	while (original != NULL && ptr != NULL)
	{
		if (original->n != ptr->n)
		{
			return (0);
		}
		original = original->next;
		ptr = ptr->next;
	}
	return (1);
}
