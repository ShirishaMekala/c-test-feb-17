#include<stdio.h>
#include<stdlib.h>
struct Student{
	int id;
	char name[1000];
	int age;
};
void write_f(struct Student S1 ){
	FILE *fpr=fopen("siri.txt","w");
	if(fpr==NULL){
		printf("file will not open ");
		exit(3);
	}
	printf("write  id,name and age of the Student\n");
	scanf("%d",&S1.id);
	fflush(stdin);
	gets(S1.name);
	scanf("%d",&S1.age);
	fwrite(&S1,sizeof(S1),1,fpr);
	fclose(fpr);
}
void readd2_f(struct Student S2){
	FILE *fpr1=fopen("apple.txt","r");
	if(fpr1==NULL){
		printf("cant open the file");
		exit(3);
	}
	fread(&S2,sizeof(S2),1,fpr1);
	printf("*************************\n");
	printf(" Student read  mode file\n\n\n");
	printf("%d\t",S2.id);
	printf("%s\t",S2.name);
	printf("%d\t",S2.age);
	fclose(fpr1);
}
int main(){
	struct Student S1,S2;
	write_f(S1);
	readd2_f(S2);
}
