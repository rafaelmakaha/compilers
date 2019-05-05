#include <bits/stdc++.h>
using namespace std;

bool resolve(int atual, string buf, int bpos, map<int, map<char,vector<int>>> tabtran, int* finais, char* alfabeto){
    if (bpos == buf.length() && finais[atual] == 1){
        return true;
    }else if(bpos == buf.length() || tabtran[atual][buf[bpos]].size()){
        return false;
    }else{
        for(int i=0;i<tabtran[atual][buf[bpos]].size();i++){
            if (resolve(tabtran[atual][buf[bpos]][i], buf, bpos+1, tabtran, finais, alfabeto)){
                return true;
            }
        }
        return false;
    }
}

int main(){
    int estados;
    scanf("%d",&estados);
    char alfabeto[1000];
    int simbolos;
    scanf("%d",&simbolos);
    for(int i=0;i<simbolos;i++)
        scanf(" %c",&alfabeto[i]);

    // int tabtran[estados]['z'+1];
    map<int, map<char,vector<int>>> tabtran;
    for(int i=0;i<estados;i++)
    {
        int pos,len; char trig;
        map<char,vector<int>> aux;
        for(int j=0;j<simbolos;j++)
        {
        scanf("%d %c %d",&pos,&trig,&len);
        vector<int> vetor;
        for(int j=0;j<len;++j){
            scanf("%d ", vetor[j]);
        }
        aux[trig] = vetor;
        tabtran[pos] = aux;
        // tabtran[i][trig]=vetor;
        }
    }
    int inicial;
    scanf("%d",&inicial);
    int finaisct;
    scanf("%d",&finaisct);
    int finais[estados];

    for(int i=0;i<estados;i++)
        finais[i]=-1;

    for(int i=0;i<finaisct;i++)
    {
        int final;
        scanf("%d",&final);
        finais[final]=1;
    }

    int atual=inicial;
    string buf;
    scanf(" %s",buf);
    int bpos=0;

    if(atual!=-1 && finais[atual]==1)
        printf("Aceito\n");
    else
        printf("Rejeito\n");
    return 0;
}