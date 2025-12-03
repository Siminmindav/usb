#include <iostream>
using namespace std;

int main(){

    for (int i = 0; i <= 10; ++i){
        cout << "\n";
        for (int j = 0; j <= 14; ++j){
            if ((j + ((i + 1) % 2)) % 2 == 1){
                cout << "@ ";
            } else {
                cout << ". ";
            };
        };
    };

    cout << "\n";
    return 0;
};
