#ifndef LISTS_H
#define LISTS_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* Define the structure for a doubly linked list node */
typedef struct dlistint_s {
int n;  /* Data element */
struct dlistint_s *prev;  /*Pointer to the previous node */
struct dlistint_s *next;  /* Pointer to the next node */
} dlistint_t;

/* Function prototype for printing a doubly linked list */
size_t print_dlistint(const dlistint_t *h);

#endif /* LISTS_H */

