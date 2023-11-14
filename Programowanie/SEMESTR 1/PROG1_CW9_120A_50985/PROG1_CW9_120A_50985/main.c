//
//  main.c
//  PROG1_CW9_120A_50985
//
//  Created by Hubert Jakubiak on 16/12/2021.
//

#include <stdio.h>
#include <stdlib.h>

struct structElement{
    int date,tmp;
    struct structElement * poprzedni;
};

struct structElement *top =NULL;
void push(int date){
     struct structElement *elem =(struct structElement *)malloc(sizeof(struct structElement));
    elem ->date = date;
    elem -> poprzedni = top;
    top = elem;
    
};

int pop(struct structElement **top){
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
