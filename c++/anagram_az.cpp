#include<bits/stdc++.h>
using namespace std;

// sachin  output false
// abcdef....xyz true
// c++ map
// python set()
// java hashset

int main()
{
    string str;
    cout<<"Enter a string : ";
    getline(cin, str);
    map<char, int> m;
    for (char i : str)
        m[i] = 1;
    // for (map<char, int>::iterator i = m.begin(); i != m.end(); i++)
    //     cout<<i->first<<"\t";

    (m.size() == 26) ? cout<<true<<endl : cout<<false<<endl;
    return 0;
}