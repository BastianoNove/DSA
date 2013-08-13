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
    if ((*table)[j].isnull) {
      (*table)[j]= node;
      return j;
    }
    else {
      i++;
    }
  }
  assert(i!=M); //Table is full
}

int search(hash_table_t* table, int key) {
  int i;
  int j;
  while (!(*table)[j].isnull || i!=M) {
    j = hash(j, i);
    if ((*table)[j].key == key) {
        return j;
    }
    else {
        i++;
    }
  }
  return -1;
}

void delete(hash_table_t* table, int key) {

}


int main() {
  printf("works\n");
  return 0;
}
