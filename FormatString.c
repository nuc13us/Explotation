#include <stdio.h>

int data;

int main(int argc, char **argv){

  data = 0;

  if(argc != 2){
    printf("Enter argument\n");
    return 0;
  }	

  char buf[100];
  strncpy(buf, argv[1],99);
  printf(buf);
  printf("\n");

  if(data == 0)
    printf("Data not changed\n");
  else
    printf("Data changed!!!\n");
    printf("Now it's value is %x",data);
  return 0;
}
