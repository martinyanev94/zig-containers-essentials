struct Car myCar;
#include <stdio.h>
#include <string.h>

struct Car {
    char make[50];
    char model[50];
    int year;
    char color[30];
};

int main() {
    struct Car myCar;

    strcpy(myCar.make, "Toyota");
    strcpy(myCar.model, "Camry");
    myCar.year = 2020;
    strcpy(myCar.color, "Blue");

    printf("Car Make: %s\n", myCar.make);
    printf("Car Model: %s\n", myCar.model);
    printf("Car Year: %d\n", myCar.year);
    printf("Car Color: %s\n", myCar.color);

    return 0;
}
