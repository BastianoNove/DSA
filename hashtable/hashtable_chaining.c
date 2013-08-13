#include <assert.h>
#include "hashtable_chaining.h"
#include "linkedlist.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int hash(int key) {
  return key % M;
}

void insert(hash_table_t* table, int key, int data) {
  node_t* curr_node = *table[hash(key)];
  node_t* new_node = malloc(sizeof(*new_node));
  new_node->prev = NULL;
  new_node->next = curr_node;
  new_node->key = key;
  new_node->data = data;
  if (curr_node) {
    printf("key collision %d. Previous element key %d\n", key, curr_node->key);
    curr_node->prev = new_node;
  }
  else {
    printf("no collision\n");
  }
  *table[hash(key)] = new_node;
}

node_t* search(hash_table_t* table, int key) {
  node_t* curr_node = *table[hash(key)];
  while (curr_node) {
    if (curr_node->key == key) {
      return curr_node;
    }
    curr_node->next;
  }
  return NULL;
}

void delete(hash_table_t* table, int key) {
  node_t* curr_node = *table[hash(key)];
  while (curr_node) {
    if (curr_node->key == key) {
      curr_node->prev->next = curr_node->next;
      curr_node->next->prev = curr_node->prev; 
      free(curr_node);
      return;
    }
    curr_node->next;
  }
}

hash_table_t* create_table() {
  hash_table_t* table = malloc(sizeof(hash_table_t));
  memset(*table, 0, M*sizeof(table[0]));
  return table;
}

void print_result(node_t* result) {
  if (!result) {
      printf("Result not found\n");
      return;
  }
  printf("key %d found. Value: %d\n", result->key, result->data); 
}

void test() {
 srand(time(NULL));
 int k, data, i, chain_length, chains;
 int NUM_INSERTIONS = 10000;
 node_t* result;
 node_t* node;
 hash_table_t* table = create_table();

 for(i = 0; i < NUM_INSERTIONS; i++) {
   k = rand();
   data = rand();
   insert(table, k, data);
   result = search(table, k);
   assert(result);
   assert(result->key == k);
   assert(result->data == data);
 }

 chains = 0;
 for(i = 0; i < M; i++) {
   chain_length = 0;
   node = *table[i];
   while(node) {
     chain_length++;
     node = node->next;
   }
   printf("chain length %d\n", chain_length);
   if (*table[i]) {
    chains++;
   }
 }
 printf("Number of chains: %d\n", chains);
 printf("Average chain length  for %d insertions and %d buckets: %f\n", NUM_INSERTIONS, M, (float)NUM_INSERTIONS/chains);
}

int main() {
  printf("hashtable test\n");
  test();
  return 0;
}
