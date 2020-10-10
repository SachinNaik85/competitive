#include<bits/stdc++.h>
using namespace std;

int main()
{
    vector<int> arr;
    cout<<"Enter number of elements : ";
    int n; 
    cin>>n;
    cout<<"Enter array elements separated by space : ";
    for (int i=0; i<n; i++)
        {
            int temp;
            cin>>temp;
            arr.push_back(temp);
        }

    int count = 0;
    int sum = 0;
    int mean = accumulate(arr.begin(), arr.end(), sum) / n;
    for (int i : arr)
        count += abs(i - mean);
    cout<<"Min steps required  : "<<count<<endl;
    return 0;
}
