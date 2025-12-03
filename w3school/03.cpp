#include <iostream>
#include <cmath>
using namespace std;

int main(){
    int szám1;
    int szám2;

    cout << "Írj be egy számot!\n";
    cin >> szám1;
    cout << "Még egyet!\n";
    cin >> szám2;

    if (szám1 == szám2){cout << "A két szám egyenlő.\n";};
    if (szám1 != szám2){cout << "A két szám nem egyenlő.\n";};
    if (szám1 < szám2){cout << "Az első szám kisebb.\n";};
    if (szám1 > szám2){cout << "Az első szám nagyobb.\n";};
    if (szám1 <= szám2){cout << "Az első szám kisebb bagy egyenlő.\n";};
    if (szám1 >= szám2){cout << "Az első szám nagyobb vagy egyenlő.\n";};
    if (((szám1 == 69) || (szám1 == 420)) && ((szám2 == 69) || (szám2 = 420))){cout << "Érdekes számok...\n";} else
    if (!(((szám1 == 69) || (szám1 == 420)) && ((szám2 == 69) || (szám2 = 420)))){cout << "Írhattál volna jobb számokat is.\n";};

    int x = 3;
    while (x > 0, --x){
        cout << "\n";
    };

    return 0;
}