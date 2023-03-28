#include <iostream>
#include <stdlib.h>
using namespace std;

//Documentaciones

//Ejercicio14 Muestra Los bordes de una cuadrado que se dibujan con *
/*Ejercicio7 Muestra la suma entre dos rangos elejidos por el usuario
Ejemplo: 3 y 6 -> 3+4+5+6 = 18*/

/*Ejercicio25 Determina en un rango de numeros elejidos por el usuario varias cosas:
cuales son pareas e impares
cuales son primeos
cuales hay en rango de 1 a 30
cuales hay en rango de 31 a 50
cuales hay en rango de 51 a 100
cuales son pares o impares entre 1 y 30
porcentaje de numeros pares e impares*/


void menu();

void menu(){
    bool enter = true
    int opcion = 0;
    do {
        cout<<"Menu de opciones\n";
        cout<<"1. Ejercicio7\n";
        cout<<"2. Ejercicio14\n";
        cout<<"3. Ejercicio25\n";
        cout<<"4. Salir";
        cout<<"Elije una opcion: "; cin>>opcion;

        switch (opcion) {
            case 1: ejercicio7(); break;
            case 2: ejercicio14(); break;
            case 3: ejercicio25(); break;
            case 4: enter = false
            default: cout<<"Opicion inexistente, vuelve a intentarlo\n\n"
        }
    }while(enter != False);
}


int main() {


    cout<<endl;
    system("pause");
    return 0;
}
