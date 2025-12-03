#include <iostream>
#include <string>

using namespace std;

int main(){

    string fullName;
    cout << "Type your full name: ";
    getline (cin, fullName);
    cout << "Your name is: " << fullName;

    int myAge = 25;
    int votingAge = 18;
    if (myAge >= votingAge) {
    cout << "Old enough to vote!";
    } else {
    cout << "Not old enough to vote.";
    }

    int time = 22;
    if (time < 10) {
    cout << "Good morning.";
    } else if (time < 20) {
    cout << "Good day.";
    } else {
    cout << "Good evening.";
    }

    int day = 4;
    switch (day) {
        case 1:
            cout << "Monday";
            break;
        case 2:
            cout << "Tuesday";
            break;
        case 3:
            cout << "Wednesday";
            break;
        case 4:
            cout << "Thursday";
            break;
        case 5:
            cout << "Friday";
            break;
        case 6:
            cout << "Saturday";
            break;
        case 7:
            cout << "Sunday";
            break;
    }

    int x = 5;
    while (x>0)
    {
        cout << "Not happy new year!\n";
        --x;
    };
    cout << "Happy new year!\n";

    int i = 0;
    do {
    cout << i << "\n";
    i++;
    }
    while (i < 5);

    int number;
    do {
    cout << "Enter a natural number: ";
    cin >> number;
    
    // A variable to store the reversed number
    int revNumbers = 0;

    // Reverse and reorder the numbers
    while (number) {
    // Get the last number of 'numbers' and add it to 'revNumbers'
    revNumbers = revNumbers * 10 + number % 10;
    // Remove the last number of 'numbers'
    number /= 10;
    }

    cout << "Reversed numbers: " << revNumbers << "\n"; 

    } while (number >= 0);



    cout << "\n";
    return 0;
}