#include "lists.h"

/**
 * check_cycle -  checks if a singly linked list has a cycle in it
 * @list: pointer to the first node
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *lst, *target;

	if (list == NULL || list->next ==NULL)
		return (0);

	lst = list->next;
	target = list->next->next;

	while (lst && target && target->next)
	{
		if (lst == target)
			return (1);

		lst = lst->next;
		target = target->next->next;
	}

	return (0);
}
