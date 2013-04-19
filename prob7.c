#include <stdio.h>


void main() {
  int size = 150000;
  int lst [150000];
  int count = 0, i = 0, n;
  for(;i<size;i++){ lst[i] = 0;}
  for(i=2;i<size; i++){
    if(lst[i] ==0){
      for (n=i*2;n<size; n+= i){lst[n]+=1;}
      count +=1;
    }
    if (count ==10001){
      printf("%i \n", i);
      break;
    }
  }
}
