#ifndef AVL_H
#define AVL_H

typedef struct avl_node {
  int key;
  int height;
  struct avl_node* left;
  struct avl_node* right;
  struct avl_node* parent;
} avl_node_t;

int max(int, int);
avl_node_t* search(avl_node_t* root, int key);
void insert(avl_node_t** root, avl_node_t* node);
avl_node_t* delete(int key);

void left_rotate(avl_node_t*);
void right_rotate(avl_node_t*);
#endif
