#include<bits/stdc++.h>
using namespace std;

// finfing missing elements in two arrays 
// original = [100, 200, 300, 400, 400, 200, 150, 10, 10, 10]
// duplicate = [10, 200, 300, 150]
//output = [10, 100, 200, 400]

/*
m1 = {10 : 3, 100 : 1, 150 : 1, 200 : 2, 300 : 1, 400 : 2}
m2 = {10 : 1, 150 : 1, 200 : 1, 300 : 1}
after m2 - m1
m1 = {10 : 2, 100 : 1, 200 : 1, 400 : 2}
*/

void find_missing(int &o, int *original, int &d, int *duplicate)
{
    map<int, int> m1, m2;
    for(int i=0; i<o; i++)
    {
        if (m1[original[i]])
            m1[original[i]]++;
        else
            m1[original[i]] = 1;
    }

    for (int j=0; j<d; j++)
    {
        if (m2[duplicate[j]])
            m2[duplicate[j]]++;
        else
            m2[duplicate[j]] = 1;
    }

    // map reducing starts here
    for (map<int, int>::iterator i = m2.begin(); i != m2.end(); i++)
    {
        if (m1[i->first])
            m1[i->first] -= i->second;

        if (m1[i->first] == 0)
            m1.erase(i->first);
    }

    for(map<int, int>::iterator i = m1.begin(); i != m1.end(); i++)
        cout<<i->first<<" ";
}

int main()
{
    int original[] = {100, 200, 300, 400, 400, 200, 150, 10, 10};
    int duplicate[] = {10, 200, 300, 150};
    int o = sizeof(original) / sizeof(*original);
    int d = sizeof(duplicate) / sizeof(*duplicate);
    find_missing(o, original, d, duplicate);
    return 0;
}