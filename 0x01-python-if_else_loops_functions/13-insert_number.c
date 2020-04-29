#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - function that inserts a number into a sorted linked list.
 * @head: double pointer that points to the first element of the linked list.
 * @number: number to insert.
 * Return: The new node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *i = NULL;
	listint_t *j = *head;

	i = malloc(sizeof(listint_t));
	if (i == NULL)
		return (NULL);
	if (*head == NULL || j->n >= number)
	{
		i->n = number;
		i->next = *head;
		*head = i;
		return (i);
	}

	while (j->next != NULL && j->next->n < number)
	{
		j = j->next;
	}
	i->n = number;
	i->next = j->next;
	j->next = i;

	return (i);
}
