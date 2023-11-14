//
//  main.c
//  PROG1_CW2_120A_50985
//
//  Created by Hubert Jakubiak on 14/10/2021.
//

#include <stdio.h>
#include <stdlib.h>

int main() {

    int **A;
    int **B;
    int **C;
    int k,w,n,m,i,j,l;
    printf("Wpisz wymiary macierzy A i B: \n");
    printf("Wprowadz liczbe kolumn A: \n");
    scanf("%d",&k);
    printf("Wprowadz liczbe wierszy A: \n");
    scanf("%d",&w);
    printf("Wprowadz liczbe kolumn B: \n");
    scanf("%d",&n);
    printf("Wprowadz liczbe wierszy B: \n");
    scanf("%d",&m);
    
    A=(int**)malloc(k*sizeof(int*));
    C=(int**)malloc(k*sizeof(int*));
    for(i =0; i<k;i++)
    {
        A[i]=(int*)malloc(w*sizeof(int));
        C[i]=(int*)malloc(m*sizeof(int));
    }
    
    B=(int**)malloc(n*sizeof(int*));
    for(i =0; i<n;i++)
    {
        B[i]=(int*)malloc(m*sizeof(int));
    }
    
    
    if (w != n) {
        printf("Wartosci sa inne mnozenie nie moze zajsc!\n");
        exit(1);
    }

    for (i= 0; i<k; i++) {
        for (j=0;j<w;j++){
            printf("Wpisz watrosci A: \n");
            scanf("%d",&A[i][j]);
        }
    }
        
    for (i= 0; i<n; i++) {
        for (j=0;j<m;j++){
            printf("Wpisz watrosci B: \n");
            scanf("%d",&B[i][j]);
        }
    }
        
        
    printf("\n Wynik macierza C:\n");
    for (i =0; i<k;i++){
        for(j=0;j<m;j++){
            C[i][j] =0;
            for(l=0;l<n;l++){
                C[i][j]+=A[i][l]*B[l][j];
                printf("\n");
            }
        printf("%d",C[i][j]);
        }
    
    }
    printf("\n");
    for(i=0;i<k;i++){
        free(A[i]);
        free(C[i]);
    }
    free(A);
    free(C);
    
    for(i=0;i<m;i++){
        free(B[i]);
    }
    free(B);
    
    return 0;
}

