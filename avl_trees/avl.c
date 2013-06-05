#include "avl.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
const Q_SIZE = 100;

int main() {
  avl_node_t* root = malloc(sizeof(*root));
  root->key = 3;
  root->left = NULL;
  root->right = NULL;

  avl_node_t* a = malloc(sizeof(*a));
  a->key = 4;
  a->left = NULL;
  a->right = NULL;
  
  avl_node_t* b = malloc(sizeof(*b));
  b->key = 5;
  b->left = NULL;
  b->right = NULL;
  
  insert(&root, a);
  insert(&root, b); 
  print_tree(root);
  return 0;
}

avl_node_t* search(avl_node_t* root, int key) {
  avl_node_t* cur = root;
  while(cur && cur->key != key) {
    if (key < cur->key) {
      cur = cur->left;
    }
    else {
      cur = cur->right;
    }
  }
  return cur;
}

void insert(avl_node_t** root, avl_node_t* node) {
  avl_node_t* bp;
  avl_node_t* cur;
  int hl, hr; //height left, height right;
  int balance;
  bp = cur = *root;

  if (!cur) {
    *root = node;
    (*root)->parent = NULL;
    return;
  }

  while(cur) {
    bp = cur;
    hr = cur->right ? (cur->right)->height : 0;
    hl = cur->left ? (cur->left)->height : 0;

    if (node->key < cur->key) {
      cur = cur->left;
      if (hl >= hr) {
        bp->height += hl + 1; 
      }
    }
    else {
      cur = cur->right;
      if (hr >= hl) {
        bp->height += hr + 1;
      }
    }
  }
  node->parent = bp;
  if (node->key < bp->key) { 
    bp->left = node;
  }
  else {
    bp->right = node;
  }
  
  bp = bp->parent;
  node = node->parent;
  while(bp) {
    balance = bp->right ? (bp->right)->height+1 : 0;
    balance -= bp->left ? (bp->left)->height+1 : 0;

    if (balance == 2 ) {
      balance = node->right ? (node->right)->height+1 : 0;
      balance -= node->left ? (node->left)->height+1 : 0;
      if (balance < 0) {
        // LR or Double left rotation
        right_rotate(node);
        node = bp->right;
      }
      left_rotate(bp);
      bp = bp->parent;
      node = bp->left;
    }
    else if (balance == -2) {
      balance = node->right ? (node->right)->height+1 : 0;
      balance -= node->left ? (node->left)->height+1 : 0;
      
      if (balance > 0) {
        // RL or Double right rotation
        left_rotate(node);
        node = bp->left;
      }
      right_rotate(bp);
      bp = bp->parent;
      node = node->right;
    }
    node = node->parent;
    bp = bp->parent;
  }

  *root = node;
}

avl_node_t* delete(int key) {
}

void left_rotate(avl_node_t* x) {
  avl_node_t* y = x->right;
  x->right = y->left;
  y->left = x;
  y->parent = x->parent;
  x->parent = y;
  if (y->parent) {
    if (y->parent->right == x) {
      y->parent->right = y;
    }
    else {
      y->parent->left = y;
    }
  }
}

void right_rotate(avl_node_t* y) {
  avl_node_t* x = y->left;
  y->left = x->right;
  x->right = y;
  x->parent = y->parent;
  y->parent = x;
  if (x->parent) {
    if (x->parent->right == y) {
      x->parent->right = x;
    }
    else {
      x->parent->left = x;
    }
  }
}

void print_tree(avl_node_t* root) { 
  avl_node_t* queue[Q_SIZE];
  memset(queue, 0, Q_SIZE);
  avl_node_t* cur = root;
  int i = 1, j = 0 ;
  int left, right;
  queue[0] = root;
  while(queue[j]) {
    cur = queue[j];
    printf("%d\n", cur->key);
    if (cur->left) {
      printf("left %d\n", cur->left->key);
      queue[i++] = cur->left;
    }
    else {
      printf("left empty\n");
    }
    if (cur->right) {
      printf("right %d\n", cur->right->key);
      queue[i++] = cur->right;
    }
    else {
      printf("right empty\n");
    }
    j++;
  }
}
