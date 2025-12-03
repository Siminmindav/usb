#include <iostream>
#include <cmath>
using namespace std;//heheheee
/*
hihihihiiii
uhuhuhuuuu
*/

int main(){
    int egészSzám = -16;
    double racionálisSzám = 13.5;
    char karakter = 'A'; //NEM JÓ A "", mert miért is lenne jó?
    wchar_t sokBitesKarakter = L'ß'; //ehhez wcout kell, ami nem mükszi. :_( Csak használj stringet ha nem vagy mazoista.
    string szöveg = " sájßeee "; //amúgy a string object (juhééé!)
    bool igazHamis = 0;

    const int istenSzemélySzám = 3;
    // istenSzemélySzám = 1; //Eretnekség

    //rossz
    bool aigmf = 0;
    // jó
    bool atombombaIndítóGombMegnyomvaFontos = 0;

    int x = 3, y = 5, z = 7;
    x = y = z = 13;
    x = x + y + z;
    y = z = y == z;
    z = x % (y + 5);
    --x;
    ++y;

    //ugyanaz
    szöveg[8] = '\b';
    szöveg.at(8) = '\b';

    cout << egészSzám << racionálisSzám << karakter << szöveg << igazHamis << szöveg[4] << "\n";
    cout << egészSzám + racionálisSzám - igazHamis * egészSzám / racionálisSzám << "\n";


    cout << sqrt(x);
    cout << round(y/z);
    cout << log(z);
    cout << min(x, y);
    cout << max(y, z);
    cout << (x == y);
    cout << (z == z);

    szöveg.append(to_string(x + y + z));
    szöveg.append(" firewägen ");
    cout << (szöveg.length() == szöveg.size()) << szöveg << "\n";

    return 0;
}