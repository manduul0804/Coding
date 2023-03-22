#include <iostream>
#include <vector>

using namespace std;

int maxArea(vector<int>& height);
int main(){

    vector<int> height{1,8,6,2,5,4,8,3,7};

    int h =1;

    h = maxArea(height);
    return 0;
}

int maxArea(vector<int>& height){
    int x = 0;
    for(int i=0; i < height.size(); i++){
        cout << height.at(i);
    }
    return x;
}