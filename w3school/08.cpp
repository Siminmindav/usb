#include <iostream>
#include <vector>
using namespace std;

int main(){
    vector l2 = {"alma", "korte", "szilva", "barack"};
    for (string i : l2){cout << i << ", ";};
    cout << "\n";
    l2.push_back("szilva");
    for (string i : l2){cout << i << ", ";};
    cout << "\n";

    string l[10] = {"alma", "korte", "szilva", "barack", "cseresznye", "szőlő", "málna", "eper", "citrom", "narancs"};
    for (string gyümölcs : l){
        cout << gyümölcs << "\n";
        for (char betü : gyümölcs){
            cout << betü << "\n";
        }
    }

    cout << sizeof(l) << sizeof(l2) << l->size() << l2.size() << "\n";
    cout << sizeof(l)/sizeof(l[0]) << l->size() << "\n";

    return 0;
}