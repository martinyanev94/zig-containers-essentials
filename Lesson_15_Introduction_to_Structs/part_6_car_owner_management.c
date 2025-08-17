struct Owner {
    char name[50];
    char address[100];
};

struct Car {
    char make[50];
    char model[50];
    int year;
    struct Owner owner; // Embedded struct
};
#include <stdio.h>
#include <string.h>

struct Owner {
    char name[50];
    char address[100];
};

struct Car {
    char make[50];
    char model[50];
    int year;
    struct Owner owner; // Embedded struct
};

void displayCar(struct Car car) {
    printf("Car Make: %s\n", car.make);
    printf("Car Model: %s\n", car.model);
    printf("Car Year: %d\n", car.year);
    printf("Owner Name: %s\n", car.owner.name);
    printf("Owner Address: %s\n", car.owner.address);
}

int main() {
    struct Car myCar;
    
    strcpy(myCar.make, "Tesla");
    strcpy(myCar.model, "Model S");
    myCar.year = 2021;
    
    strcpy(myCar.owner.name, "John Doe");
    strcpy(myCar.owner.address, "123 Elm St, Springfield");

    displayCar(myCar);

    return 0;
}
