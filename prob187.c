#include <stdio.h>
//this method doesn't work xD;;; I ran into a memory error. I need a better method.
void main() {
  unsigned int size = 10000000;
  unsigned int lst [10000000];
  int i = 0, n, blah, count = 0;
  for(;i<size;i++){ lst[i] = 0;}
  
  for(i=2;i<size; i++){
    if(lst[i] ==0){
      for (n=i*2;n<size; n+= i){lst[n]+=1;}
      blah = i* i;
      for (n=blah;n<size; n+= blah){lst[n]+=1;}
      blah = i*i* i;
      for (n=blah;n<size; n+= blah){lst[n]+=1;}
    }
  }
  for(i=4;i< size; i++){
    if(lst[i]==2){count += 1;}}
    
  printf("There are %i semiprimes under %u \n", count, size);
  
}
