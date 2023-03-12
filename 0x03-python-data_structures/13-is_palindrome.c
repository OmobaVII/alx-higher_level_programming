#include "lists.h"
#include <stddef.h>

/**
 * is_palindrome - a function that checks if a singly linked list is 
 * a palindrome
 * @head: the singly linked list
 * Return: 1 if palindrome and 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp, *temp2, *temp3, *ptr;

	ptr = *head;
	temp2 = NULL;
	if (*head == NULL)
		return (1);
	while (*head != NULL)
	{
		temp = (*head)->next;
		(*head)->next = temp2;
		temp2 = *head;
		*head = temp;
	}	
	*head = temp2;
	temp3 = NULL;
	while (temp2 != NULL)
	{
		temp = temp2->next;
		temp2->next = temp3;
		temp3 = temp2;
		temp2 = temp;
	}
	temp2 = temp3;
	if (ptr == temp3)
	{
		return (1);
	}
	else
	{
		return (0);
	}
}
