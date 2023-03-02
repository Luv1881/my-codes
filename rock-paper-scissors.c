#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int rockpaperscissors(char you,char comp){
    if (you==comp){
        return 0;
    }
    // rp
    // ps
    // sr
    if (you=='r' && comp=='p'){
        return -1;
    }
    else if (you=='p' && comp=='r'){
        return 1;
    }
    if (you=='p' && comp=='s'){
        return -1;
    }
    else if (you=='s' && comp=='p'){
        return 1;
    }
    if (you=='s' && comp=='r'){
        return -1;
    }
    else if (you=='r' && comp=='s'){
        return 1;
    }
}

int main(){
    int number;
    srand(time(0));
    number=rand()%100+1;
    char you,comp;
    if (number<33){
        comp='r';
    }
    else if (number>=33 && number<66){
        comp='p';
    }
    else{
        comp='s';
    }
    printf("enter r for rock, p for paper or s for scissors \n");
    scanf("%c",&you);
    printf("You chose %c and the computer chose %c so ",you,comp);
    int result = rockpaperscissors(you,comp);
    if (result==1){
        printf("you won!");
    }
    else if (result==-1){
        printf("you lost!");
    }
    else{
        printf("the game was a draw!");
    }

}