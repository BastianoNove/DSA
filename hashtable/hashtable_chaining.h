#ifndef HASHTABLE_H
#define HASHTABLE_H
#define M 701

#include "linkedlist.h"

typedef node_t* hash_table_t[M];

int hash(int key);
void insert(hash_table_t*, int key, int data);
node_t* search(hash_table_t*, int key);
void delete(hash_table_t*, int key);

#endif /* HASHTABLE_H */
