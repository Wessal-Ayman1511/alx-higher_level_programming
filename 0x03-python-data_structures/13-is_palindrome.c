#include "lists.h"
/**
 * is_palindrome- function to check is pal
 * @head: input
 * Return: 0 or 1
*/
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (pal_list, *head);
}
/**
 * pal_list- function to cheack
 * @start: head
 * @end: end
 * Return: 0 or 1
*/
int pal_list(listint_t **start, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (pal_list(start, end->next) && (*start)->n == end->n)
	{
		*start = (*start)->next;
		return (1);
	}
	return (0);
}

