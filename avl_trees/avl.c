#include "avl.h"
#include <stdio.h>
#include <stdlib.h>

int main() {
  avl_node* root = malloc(sizeof(*root));
  root->key = 5;
  root->left = NULL;
  root->right = NULL;

  avl_node* a = malloc(sizeof(*a));
  a->key = 4;
  a->left = NULL;
  a->right = NULL;
  
  avl_node* b = malloc(sizeof(*b));
  b->key = 6;
  b->left = NULL;
  b->right = NULL;
  
  insert(&root, a);
  insert(&root, b); 
  return 0;
}

avl_node* search(avl_node* root, int key) {
  avl_node* cur = root;
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

void insert(avl_node** root, avl_node* node) {
  avl_node* bp;
  avl_node* cur;
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
        bp->height = hl + 1; 
      }
    }
    else {
      cur = cur->right;
      if (hr >= hl) {
        bp->height = hr + 1;
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
  while(node && bp) {
    balance = bp->right ? (bp->right)->height : 0;
    balance -= bp->left ? (bp->left)->height : 0;

    if (balance == 2 ) {
      balance = node->right ? (node->right)->height : 0;
      balance -= node->left ? (node->left)->height : 0;
      if (balance == -2) {
        // LR or Double left rotation
        right_rotate(node);
        left_rotate(bp);
      }
      else {
        left_rotate(bp);
      }
    }
    else if (balance == -2) {
      balance = node->right ? (node->right)->height : 0;
      balance -= node->left ? (node->left)->height : 0;
      
      if (balance == 2) {
        // RL or Double right rotation
        right_rotate(node);
        left_rotate(bp);
      }
      else {
        right_rotate(bp);
      }
    }
    node = node->parent;
  }
}

avl_node* delete(int key) {
}

void left_rotate(avl_node* x) {
  avl_node* y = x->right;
  x->right = y->left;
  y->left = x;
  y->parent = x->parent;
  x->parent = y;
}

void right_rotate(avl_node* y) {
  avl_node* x = y->left;
  y->left = x->right;
  x->right = y;
  x->parent = y->parent;
  y->parent = x;
}
