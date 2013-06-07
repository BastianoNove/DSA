#ifndef AVL_H
#define AVL_H

typedef struct avl_node {
  int key;
  int height;
  struct avl_node* left;
  struct avl_node* right;
  struct avl_node* parent;
} avl_node_t;

typedef enum { false, true } bool;

avl_node_t* search(avl_node_t* root, int key);
void insert(avl_node_t** root, avl_node_t* node);
avl_node_t* delete(int key);

void left_rotate(avl_node_t*);
void right_rotate(avl_node_t*);

avl_node_t* create_node(int);
void print_tree(avl_node_t*);
void build_tree(avl_node_t**, int[], int);
bool check_balance(avl_node_t*, int);
bool check_bst(avl_node_t*, int);
#endif
