#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - a function that inserts a number into a sorted
 * singly linked list.
 * @head: the linked list
 * @number: the data part of the linked list inserted
 * Return: the address of the new node or NULL if failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}
	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		new = *head;
		return (new);
	}
	if ((*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	current = *head;
	while (current->next != NULL && current->next->n < number)
	{
		current = current->next;
	}
	new->next = current->next;
	current->next = new;
	return (new);
}

