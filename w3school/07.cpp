#include <iostream>
using namespace std;

int main(){
    int szám;
    int szám2;
    cout << "méret \n";
    cin >> szám;
    cout << "kerekítés \n";
    cin >> szám2;

    for (int i = 1; i <= szám * 5; ++i){
        cout << "\n";
        for (int j = 1; j <= szám*8; ++j){
            if (j + i > i * j / szám2){
                cout << "@ ";
            } else {
                cout << ". ";
            };
        };
    };

    cout << "\n";
    return 0;
};