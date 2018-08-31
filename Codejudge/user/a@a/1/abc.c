#include<stdio.h>
void main()
{
    int year, n, i;

    scanf("%d", &n);
    for (i = 0; i<n; i++){
        scanf("%d", &year);
        if ((year % 400) == 0)
            printf("1");
        else if ((year % 100) == 0)
            printf("0");
        else if ((year % 4) == 0)
            printf("1");
        else
            printf("0");
        printf("\n");
    }
}