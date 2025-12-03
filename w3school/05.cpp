#include <iostream>
using namespace std;

void repeat(string text, int number){
    while (number >= 0){
        cout << text;
        --number;
    };
};

int main(){

for (int i = 0; i <= 10; ++i){
    cout << "\n";
    for (int j = 0; j <= 10; ++j){
        repeat(" ", 3 - to_string(j * i).length());
        cout << j * i;
    };
};

cout << "\n";
return 0;
};