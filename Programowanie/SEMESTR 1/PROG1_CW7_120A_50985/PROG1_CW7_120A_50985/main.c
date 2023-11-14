//
//  main.c
//  PROG1_CW7_120A_50985
//
//  Created by Hubert Jakubiak on 02/12/2021.
//

#include <stdio.h>
#include <stdlib.h>

int main() {

    int **A;
    int **B;
    int **C;
    int k,w,n,m,i,j,l;
    FILE *odczyt;
    FILE *zapis;
    
    odczyt=fopen("/Users/hubertjakubiak/Desktop/programy/PROG1_CW7_120A_50985/macierze.txt","r");
    if(odczyt == 0) {
        perror("fopen");
        exit(1);
    }
    else{
    fscanf(odczyt,"%d %d %d %d",&m,&n,&w,&k);
    printf("%d %d %d %d",m,n,w,k);
    }
    printf("\n");
    A=(int**)malloc(m*sizeof(int*));
    C=(int**)malloc(m*sizeof(int*));
    for(i =0; i<m;i++)
    {
        A[i]=(int*)malloc(n*sizeof(int));
        C[i]=(int*)malloc(w*sizeof(int));
    }
    
    B=(int**)malloc(w*sizeof(int*));
    for(i =0; i<w;i++)
    {
        B[i]=(int*)malloc(k*sizeof(int));
    }
    
    
    if (n != w) {
        printf("Wartosci sa inne mnozenie nie moze zajsc!\n");
        exit(1);
    }
    printf("\n");
    for (i= 0; i<m; i++) {
        for (j=0;j<n;j++){
            fscanf(odczyt,"%d",&A[i][j]);
            printf("%d",A[i][j]);
            printf("\n");
        }
    }
    printf("\n");
    for (i= 0; i<w; i++) {
        for (j=0;j<k;j++){
            fscanf(odczyt,"%d",&B[i][j]);
            printf("%d",B[i][j]);
            printf("\n");
        }
    }
    
    zapis=fopen("/Users/hubertjakubiak/Desktop/programy/PROG1_CW7_120A_50985/wynik.txt","w");
    for (i =0; i<m;i++){
        for(j=0;j<k;j++){
            C[i][j] =0;
            for(l=0;l<w;l++){
                C[i][j]+=A[i][l]*B[l][j];
                
            }
            fprintf(zapis,"%d", C[i][j]);
            
        }
        fprintf(zapis,"\n");
    }

    for(i=0;i<m;i++){
        free(A[i]);
        free(C[i]);
    }
    free(A);
    free(C);
    
    for(i=0;i<w;i++){
        free(B[i]);
    }
    free(B);
    
    fclose(odczyt);
    fclose(zapis);
    
    return 0;
    
}

