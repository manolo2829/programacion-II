#include<stdlib.h>
#include<stdio.h>
#include<math.h>

int main(){
	int line1[3], line2[6], line3[9];
	int col1, col2, col31;
	int jug1, jug2;
	int ficha;
	int mov;
	printf("[%d]  [%d]  [%d]\n", line1[1], line1[2], line3[3]);
	printf("[%d]  [%d]  [%d]\n", line2[1], line2[2], line2[3]);
	printf("[%d]  [%d]  [%d]\n", line3[3], line3[2], line3[3]);
	
	printf("Que ficha queres ser jugador 1\n");
	printf("1 o 0?\n");
	scanf("%d",&ficha);
	if(ficha=1){
		jug1=1;
		jug2=0;
	}else{
		jug1=0;
		jug2=1;
	}
	printf("En que fila queres escribir jug1\n");
	printf("1, 2, 3\n");
	scanf("%d",&mov);
	if(mov=1){
		printf("que columna queres usar\n");
		printf("1, 2, 3\n");
		line1[3]=line1[col1];
		scanf("%d",&line1[col1]);
		printf("______________\n");
		printf("______________\n");
		printf("______________\n");
		printf("[%d]  [%d]  [%d]\n", line1[1], line1[2], line3[3]);
		printf("[%d]  [%d]  [%d]\n", line2[1], line2[2], line2[3]);
		printf("[%d]  [%d]  [%d]\n", line3[3], line3[2], line3[3]);
		
	}
}
