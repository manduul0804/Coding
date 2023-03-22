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
    int y =0;
    int x = 0;
    int count = 0;
    int size = 0;
    int num = 0;

    for(int i=0; i < height.size(); i++){
        cout << height.at(i) << endl;
        if(count == 0){
            y = height.at(i);
            x = height.at(i);
            count++;
            num++;
        }
        else if(count == 1){
            x = height.at(i);
            count++;
            num++;
        }
        else if(((x < y) ? (x*count): (y*count)) > size){
            cout << "size = ";
            cout << size << endl;
        }
    }
    return x;
}