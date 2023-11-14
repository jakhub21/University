//
//  main.c
//  PROG1_CW4_120A_50985
//
//  Created by Hubert Jakubiak on 04/11/2021.
//

#include <stdio.h>

int main() {
    int t[100];
    int x,n,i,j,tmp;
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
    
    for (i =0;i<n;i++) {
        for (j=0;j<n-1;j++ ) {
            if(t[j]>t[j+1]){
                tmp = t[j];
                t[j]=t[j+1];
                t[j+1] = tmp;
            }
        }
    }
    printf("\n\nLiczby po sortowaniu: \n");
    for (i = 0;i<n;i++)
    {
        printf("\n");
        printf("%d",t[i]);
    }
    printf("\n");
    return 0;
}
