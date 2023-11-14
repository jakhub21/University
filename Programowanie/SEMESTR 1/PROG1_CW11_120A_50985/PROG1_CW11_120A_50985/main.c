//
//  main.c
//  PROG1_CW11_120A_50985
//
//  Created by Hubert Jakubiak on 02/02/2022.
//

#include <stdio.h>
#include <stdlib.h>

typedef union date{
    int idate;
    float fdate;
    char sdate[100];
}TDana;

struct structElement{
    int idate;
    float fdate;
    char sdate[100];
    char typ;
    struct structElement * poprzedni;
    TDana date;
};



struct structElement *top =NULL;
void push(TDana date,char typ){
     struct structElement *elem =(struct structElement *)malloc(sizeof(struct structElement));
    elem ->date = date;
    elem -> poprzedni = top;
    top = elem;
    elem -> typ = typ;
};

struct elem* pop(struct structElement **top){
    if (*top==NULL){
        printf("Stos jest pusty");
        return -1;
    }
    
    struct structElement *elem = *top;
    int tmp = elem -> date;
    (*top) = (*top) -> poprzedni;
    free(elem);
    return tmp;
}

int peek(struct structElement *top){
    if(top != NULL){
        printf("%d",top->date);
    }
    else{
    printf("Stos jest pusty");
    }
    return -1;
}

void print(TDana date,char typ){
    switch(typ){
        case 1:
            print("%d", date.idate);
            break;
        case 2:
            print("%d", date.fdate);
            break;
        case 3:
            print("%s", date.sdate);
            break;
            
    }
}

int main() {
    int option = -1;
    int number = -1;
    while (option != 0) {
        printf("\n MENU\n");
        printf("1.PUSH\n");
        printf("2.POP\n");
        printf("3.PEEK\n");
        printf("4.KONIEC\n");
        scanf("%i",&option);
        switch(option){
            case 1:
                printf("Jaka liczbe chcesz dodac:\n");
                scanf("%i", &number);
                push(number);
                break;
            case 2:
                pop(&top);
                break;
            case 3:
                peek(top);
                break;
            case 4:
                exit(0);
            default:
                printf("Podaj wlasciwa opcje!");
                break;
            }
        
    }
    
    return 0;
}
