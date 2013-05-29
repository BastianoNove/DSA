#ifndef AVL_H
#define AVL_H

typedef struct avl_node {
  int key;
  int height;
  struct avl_node* left;
  struct avl_node* right;
  struct avl_node* parent;
} avl_node;

int max(int, int);
avl_node* search(avl_node* root, int key);
void insert(avl_node** root, avl_node* node);
avl_node* delete(int key);

void left_rotate(avl_node*);
void right_rotate(avl_node*);
#endif
