#include<bits/stdc++.h>
using namespace std;

vector<vector<int>> getval(string str)
{
    map<char, vector<int>> m;
    for (int i=0; i<str.size(); i++)
        m[str[i]].push_back(i);
        
    vector<vector<int>> res;

    for (map<char, vector<int>>::iterator i = m.begin(); i != m.end(); i++)
        {
            if (i->second.size() > 1)
                res.push_back(i->second);
        }
    sort(res.begin(), res.end());
    
    return res;
}

bool isIsomorphic(string &s, string &t)
{
    return (getval(s) == getval(t))? true : false;
}

bool isIsomorphic1(string &s, string &t)
{
    map<char, char> maps, mapt;
    for (int i=0; i<s.size(); i++)
    {
        if (maps[s[i]])
        {
            if (maps[s[i]] != t[i])
            {
                return false;
            }
        }

        else if (mapt[t[i]])
        {
            return false;
        }
        else
            {
                maps[s[i]] = t[i];
                mapt[t[i]] = s[i];
            }
    }
    return true;
}

int main()
{
    string s, t;
    cout<<"Enter first string : ";
    getline(cin, s);
    cout<<"Enter second string : ";
    getline(cin, t);
    cout<<isIsomorphic1(s, t);
    return 0;
}