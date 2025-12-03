#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

void min(vector<int> list) {
    if (list.empty()) {
        cout << "List is empty, no minimum value.\n";
        return;
    }
    int min = list[0];
    for (int i : list){
        if (i < min){
            min = i;
        }
    }
    cout << "Minimum: " << min << "\n";
}

void max(vector<int> list) {
    if (list.empty()) {
        cout << "List is empty, no maximum value.\n";
        return;
    }
    int max = list[0];
    for (int i : list){
        if (i > max){
            max = i;
        }
    }
    cout << "Maximum: " << max << "\n";
}

void sum(vector<int> list) {
    if (list.empty()) {
        cout << "List is empty, sum is 0.\n";
        return;
    }
    int sum = 0;
    for (int i : list){
        sum += i;
    }
    cout << "Szummma" << sum << "\n";
}

void geometriaiátlag(vector<int> list) {
    if (list.empty()) {
        cout << "List is empty, geometric mean is undefined.\n";
        return;
    }
    double product = 1.0;
    for (int i : list){
        product *= i;
    }
    double geom_mean = pow(product, 1.0 / list.size());
    cout << "Geometric mean: " << geom_mean << "\n";
}

void számtaniátlag(vector<int> list) {
    if (list.empty()) {
        cout << "List is empty, arithmetic mean is undefined.\n";
        return;
    }
    double sum = 0.0;
    for (int i : list){
        sum += i;
    }
    double arith_mean = sum / list.size();
    cout << "Arithmetic mean: " << arith_mean << "\n";
}

void printchildren(vector<int> list) {
    if (list.empty()) {
        cout << "List is empty, no children to print.\n";
        return;
    }
    for (int i : list) {
        cout << i << " ";
    }
    cout << "\n";
}

void medián(vector<int> list) {
    if (list.empty()) {
        cout << "List is empty, median is undefined.\n";
        return;
    }
    sort(list.begin(), list.end());
    double median;
    size_t size = list.size();
    if (size % 2 == 0) {
        median = (list[size / 2 - 1] + list[size / 2]) / 2.0;
    } else {
        median = list[size / 2];
    }
    cout << "Median: " << median << "\n";
}


int main(){
    vector<int> lista = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};    

    cout << "List: ";
    printchildren(lista);
    min(lista);
    max(lista);
    sum(lista);
    geometriaiátlag(lista);
    számtaniátlag(lista);
    medián(lista);

    return 0;
}