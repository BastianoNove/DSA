#include <assert.h>
#include "hashtable_probing.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int hash(int key, int index) {
    return ((key % M) + index) % M;
}

hash_table_t* create_table() {
  int i;
  hash_table_t* table = malloc(sizeof(hash_table_t));
  for(i = 0; i < M; i++) {
    (*table)[i].isnull = 1;
  }
  return table;
}

int insert(hash_table_t* table, int key, int data) {
  int i = 0;
  int j;
  hashtable_item node = { .key = key, .data = data, .deleted = 0};
  while (i != M) {
    j = hash(key, i);
    if ((*table)[j].isnull || (*table)[j].deleted) {
      (*table)[j]= node;
      return j;
    }
    else {
      i++;
    }
  }
  assert(i!=M && "Table is full");
}

int search(hash_table_t* table, int key) {
  int i;
  int j = hash(key, 0);
  while (!(*table)[j].isnull || !(*table)[j].deleted ||  i!=M) {
    if ((*table)[j].key == key) {
        return j;
    }
    else {
        i++;
        j = hash(key, i);
    }
  }
  return -1;
}

void delete(hash_table_t* table, int key) {
  int j = search(table, key);
  if (j < 0) {
    return;
  }
  (*table)[j].deleted = 1;
}

void test() {
 srand(time(NULL));
 int k, data, i, j;
 hashtable_item result;
 hash_table_t* table = create_table();

 for(i = 0; i < 701; i++) {
   k = rand();
   data = rand();
   insert(table, k, data);
   j = search(table, k);
   assert( j >= 0);
   result = (*table)[j];
   assert(result.key == k);
   assert(result.data == data);
 }
 printf("Test passes\n");
}

int main() {
  test();
  return 0;
}
