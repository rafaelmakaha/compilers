#include <bits/stdc++.h>
using namespace std;

int main(){
    string buf;
    cin >> buf;
    stack<char> st;

    for (char i : buf){
        if(i == 'a'){
            if(st.empty()){
                st.push('A');
            }else if (st.top() == 'A'){
                st.push('A');
            }else if (st.top() == 'B'){
                st.pop();
            }
        }else if(st.empty()){
            st.push('B');
        }else if (st.top() == 'B'){
            st.push('B');
        }else if (st.top() == 'A'){
            st.pop();
        }
        if (st.empty()){
            cout << 'nil';
        }else{
            for(char j : st){
                printf('%c', st[j])
            }
        }
    }


    return 0;
}