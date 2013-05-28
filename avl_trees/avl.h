#ifndef AVL_H
#define AVL_H

typedef struct avl_node {
  int key;
  int height;
  struct avl_node* left;
  struct avl_node* right;
} avl_node;

struct avl_node search(int key);
void insert(avl_node* root, avl_node* node);
avl_node* delete(int key);

#endif
