//
//  main.c
//  PROG1_CW5_120A_50985
//
//  Created by Hubert Jakubiak on 11/11/2021.
//

#include <stdio.h>

int* sort(int n,int t1[]){
    int flaga =1;
    int tmp;
    while (flaga == 1) {
        flaga = 0;
        for (int i =0;i<n;i++) {
            for (int j=0;j<n-1;j++ ) {
                if(t1[j]>t1[j+1]){
                    tmp = t1[j];
                    t1[j]=t1[j+1];
                    t1[j+1] = tmp;
                    flaga =1;
                }
            }
        }
    }
    return t1;
}
int main() {
    int t[100];
    int x,n,i;
    printf("wprowadz ilosc liczb do sortowania: \n");
    scanf("%d",&n);
    
    for (i= 0; i<n; i++) {
        printf("Wpisz watrosci do tablicy: \n");
        scanf("%d",&x);
        t[i]= x;
        }
    printf("Twoje liczby: \n");
    for (i = 0;i<n;i++)
    {
        printf("\n");
        printf("%d",t[i]);
    }
    
    sort(n,t);
    
    printf("\n\nLiczby po sortowaniu: \n");
    for (i = 0;i<n;i++)
    {
        printf("\n");
        printf("%d",t[i]);
    }
    printf("\n");
    return 0;
}
