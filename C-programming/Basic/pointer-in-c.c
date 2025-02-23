#include <stdio.h>
#include <stdlib.h>

void update(int *a,int *b) {
    int x = *a;
    int z = *b;
    *a = x+z;
    *b = abs(x-z);
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;

    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}