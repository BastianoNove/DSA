#include <stdio.h>
#include <stdlib.h>

typedef struct node {
  struct node* l; // left child
  struct node* r; // right child 
  struct node* p; // parent
  int key;
} node;

int insert_node(node** root, node* i){
  int edges = 0;
  node *curnode = *root;
  node **tp = root; //trailing parent pointer
  
  while(NULL!=(curnode)){
    tp = &curnode;
    printf("curnode = %d\n", (curnode)->key);
    if (i->key < (curnode)->key){ printf("going left\n");  curnode = (curnode)->l; }
    else { printf("going right\n"); curnode = (curnode)->r; }
    edges++; 
  }
  if (NULL==(*root)){
     *tp = i; 
     return 0;
  }

  if ((*tp)->key < (curnode)->key) (*tp)->l = curnode;
  else (*tp)->r = curnode; 
  
  return edges;
}

int main(){
  int x, k, count;
  scanf("%d",&x);
  node *root = NULL;
  node *inode;

  while(x-->0){
   scanf("%d", &k);
   inode = (node *) malloc(sizeof(node));
   inode->key = k;
   inode->l = inode->r = NULL;
   count += insert_node(&root, inode); 
  }
  printf("count is %d\n", count);
  return 0; 
}
