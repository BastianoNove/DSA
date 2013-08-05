#ifndef LINKEDLIST
#define LINKEDLIST

typedef struct node{
  struct node* next;
  struct node* prev;
  int key;
  int data;
}node_t;

#endif /* LINKEDLIST */
