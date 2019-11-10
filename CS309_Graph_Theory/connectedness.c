#include<stdio.h>
#include<stdlib.h>
#define SIZE 10

int adj_mtx[SIZE][SIZE],r,done[SIZE];
struct vertices *ver_arr[SIZE];

struct vertices{
  int id;
  struct vertices *adj[SIZE];
};

void initialize(struct vertices *ptr,int id){
  int i;
  ptr->id = id;
  for(i=0;i<SIZE;i++)
    ptr->adj[i] = NULL;
}

void connectedness_DFS(struct vertices *ptr){
  int i=0;
  printf("%d -> ", ptr->id);
  done[ptr->id] = 1;
  while(ptr->adj[i]!=NULL){
    if(done[ptr->adj[i]->id] == 0)
      connectedness_DFS(ptr->adj[i]);
    i++;
  }
}

void main(){
  int i,j,adj_ptr,conn_grh_count = 0;
  printf("Enter the graph as adjacent matrix(LIMIT: %d x %d)\n",SIZE,SIZE);
  printf("No of rows/clmn: ");
  scanf("%d",&r);

  //initializing done
  for(i=0;i<r;i++){
    done[i]=0;
  }

  //inserting adj matrix & initializing pointers
  for(i=0;i<r;i++){
    ver_arr[i] = (struct vertices*)malloc(sizeof(struct vertices));
    initialize(ver_arr[i],i);
    for(j=0;j<r;j++){
      scanf("%d",&adj_mtx[i][j]);
    }
  }


  //constructing graph using adj matrix
  for(i=0;i<r;i++){
    adj_ptr = 0;
    for(j=0;j<r;j++){
      if(adj_mtx[i][j] == 1){
        ver_arr[i]->adj[adj_ptr] = ver_arr[j];
        adj_ptr+=1;
      }
    }
  }

  //connectedness
  for(i=0;i<r;i++){
    if(done[i]==0){
      printf("\n");
      conn_grh_count += 1;
      connectedness_DFS(ver_arr[i]);
    }
  }
  printf("\nno of connected graphs: %d\n",conn_grh_count);


}

/*
sample: 1
0 0 0 1 1 0 0 0 0
0 0 1 0 1 0 0 0 0
0 1 0 0 1 0 0 0 0
1 0 0 0 1 0 0 0 0
1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 1 0
0 0 0 0 0 0 0 1 0
0 0 0 0 0 1 1 0 1
0 0 0 0 0 0 0 1 0

*/
