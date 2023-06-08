#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
* insert_node - inserts a new node to a sorted linked list
* @head: linked list
* @number: value to be added
* Return: Always 0
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;


	if (*head == NULL || number < (*head)->n)
		*head = new;
	else
	{
		current = *head;
		while (current->next != NULL && current->next->n < number)
		{
			current = current->next;
		}

		new->next = current->next;
		current->next = new;
	}

	return (current->next);
}
