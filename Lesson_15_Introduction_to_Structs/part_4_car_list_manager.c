struct Car {
    char make[50];
    char model[50];
    int year;
    struct Car *next; // Pointer to the next car in the list
};
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Car {
    char make[50];
    char model[50];
    int year;
    struct Car *next; // Pointer to the next car in the list
};

void printCars(struct Car *head) {
    struct Car *current = head;
    while (current != NULL) {
        printf("Make: %s, Model: %s, Year: %d\n", current->make, current->model, current->year);
        current = current->next;
    }
}

int main() {
    struct Car *firstCar = malloc(sizeof(struct Car));
    strcpy(firstCar->make, "Toyota");
    strcpy(firstCar->model, "Camry");
    firstCar->year = 2020;

    struct Car *secondCar = malloc(sizeof(struct Car));
    strcpy(secondCar->make, "Honda");
    strcpy(secondCar->model, "Accord");
    secondCar->year = 2019;

    firstCar->next = secondCar;
    secondCar->next = NULL;

    printCars(firstCar);

    free(firstCar);
    free(secondCar);

    return 0;
}
