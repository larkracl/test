#include <iostream>

using namespace std;

int main(){
    int N;
    cin >> N;

    int arr[10001] = {0,};

    int k;

    while(N--){
        cin >> k;
        arr[k]++;
    }

    for(int i = 0; i < 10001; i++){
        while(arr[i]-- > 0){
            cout << i << '\n';
        }
    }
    return 0;
}