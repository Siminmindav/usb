#include <iostream>
using namespace std;
using ll = long long;

int main() {
    char answer;

    cout << "Do you like cats? (y/n): ";
    cin >> answer;
    switch (answer) {
        case 'y':
        case 'Y':
            cout << "Great! Cats are awesome.\n";
            break;
        case 'n':
        case 'N':{
            cout << "Well then. I CAST MEMORY LEAK!\n";
            while (1){
                cout << "HAHAHAHAHA! I WILL LEAK YOUR MEMORY FOREVER!\n";
                ll size = 1024*1024*1024/8; //1GB memóriafoglalás, ami nem lesz felszabadítva, így memóriaszivárgást okoz
                ll* leak = new ll[size]; 
                for (ll i = 0; i < size; ++i) {
                    leak[i] = i; //a memória helyek feltöltése értékekkel, hogy ne legyen üres memóriafoglalás
                }
            }
            break;
            }
        default:
            cout << "Invalid input. Please enter 'y' or 'n'.\n";
    }

    return 0;
}