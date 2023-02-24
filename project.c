#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int main(){
    int number,guess;
    int guessed;
    srand(time(0));
    number=rand()%100;
    guess=0;
    do{
        printf("enter the value from 1-100\n");
        scanf("%d",&guessed);
        guess++;
    }while(guessed!=number);
    printf("youre guess was correct and it took you only %d tries",guess);
    return 0;
}