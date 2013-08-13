#ifndef HASHTABLE_H
#define HASHTABLE_H
#define M 701

typedef struct hashtable_item {
    int key;
    int data;
    int deleted;
    int isnull;
} hashtable_item;

typedef hashtable_item hash_table_t[M];

int hash(int key, int index);
int insert(hash_table_t*, int key, int data);
int search(hash_table_t*, int key);
void delete(hash_table_t*, int key);

#endif
