//
//  main.c
//  PROG1_CW10_120A_50985
//
//  Created by Hubert Jakubiak on 13/01/2022.
//

#include <stdio.h>
#include "stdlib.h"

struct structElement{
    int data;
    int paramert;
    struct structElement * nastepnik;
};

struct structElement *head = NULL;
struct structElement *end = NULL;

void add(int parametr){
    struct structElement *eq =(struct structElement *)malloc(sizeof(struct structElement));
    eq -> data = parametr;
    if (head == NULL){
        eq -> nastepnik = NULL;
        head = eq;
        end = eq;
    }
    else{
        end -> nastepnik = eq;
        end = eq;
    }
   
};

int peek(struct structElement *head){
    if (head != NULL){
        printf("%d", head -> data);
    }
    else{
    printf("Stos jest pusty");
    }
    return -1;
}

int pool(struct structElement **head){
    if (*head == NULL){
        printf("Stos jest pusty");
        return -1;
        }
    else{
        int itmp = (*head) -> data;
        struct structElement *eqtmp =(struct structElement *)malloc(sizeof(struct structElement));
        eqtmp = (*head);
        (*head) = (*head) -> nastepnik;
        if(*head == NULL){
            end = NULL;
            free(eqtmp);
            printf("%d",itmp);
        }
    }
    return -1;
}

int main() {
    int option = -1;
    int number = -1;
    while (option != 0) {
        printf("\n MENU\n");
        printf("1.ADD\n");
        printf("2.POLL\n");
        printf("3.PEEK\n");
        printf("4.KONIEC\n");
        scanf("%i",&option);
        switch(option){
            case 1:
                printf("Jaka liczbe chcesz dodac:\n");
                scanf("%i", &number);
                add(number);
                break;
            case 2:
                pool(&head);
                break;
            case 3:
                peek(head);
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
