//
//  main.c
//  PROG1_CW8_120A_50985
//
//  Created by Hubert Jakubiak on 09/12/2021.
//

#include <stdio.h>
#include <stdlib.h>

int main() {
    int i;
    FILE *odczyt;
    odczyt=fopen("/Users/hubertjakubiak/Desktop/programy/PROG1_CW8_120A_50985/odczyt.txt","r");
    if(odczyt == 0) {
        perror("fopen");
        exit(1);
    }
    int liczba= 1;
    int sume =0;
    while((liczba != 0)&&(odczyt != EOF))
    {
        rewind(odczyt);
        for(i=0;i<=sume;i++)
        {
            fscanf(odczyt,"%d",&liczba);
        }
        sume += liczba;
    }
    
    printf("%d",sume);
    fclose(odczyt);
    return 0;
}
