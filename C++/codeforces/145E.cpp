#include <iostream>
using namespace std;

int n, m, L, R, V;
char A[1000005];
class Node {
   public:
    int len4, len7, len47, len74;
    int val;
    int Left, Right;
};
Node T[4000020];

void pushup(int nd) {
    T[nd].len4 = T[nd * 2].len4 + T[nd * 2 + 1].len4;
    T[nd].len7 = T[nd * 2].len7 + T[nd * 2 + 1].len7;
    T[nd].len47 = max(T[nd * 2].len4 + T[nd * 2 + 1].len47, T[nd * 2].len47 + T[nd * 2 + 1].len7);
    T[nd].len74 = max(T[nd * 2].len7 + T[nd * 2 + 1].len74, T[nd * 2].len74 + T[nd * 2 + 1].len4);
}

void build(int nd, int lf, int rg) {
    int mid, lr, rr;
    T[nd].Left = lf;
    T[nd].Right = rg;
    T[nd].val = 0;
    if (lf == rg) {
        char tmp = A[lf - 1];
        if (tmp == '4') {
            T[nd].len4 = 1;
            T[nd].len47 = 1;
            T[nd].len74 = 1;
        } else {
            T[nd].len7 = 1;
            T[nd].len47 = 1;
            T[nd].len74 = 1;
        }
    } else {
        mid = (lf + rg) / 2;
        build(nd * 2, lf, mid);
        build(nd * 2 + 1, mid + 1, rg);
        pushup(nd);
        // cout <<  nd << ": 4 " << T[nd].len4 << " 7 " << T[nd].len7 << " 47 " << T[nd].len47 <<  " 74 " << T[nd].len74 << '\n';
    }
}

void pushdown(int nd) {
    if (T[nd].val) {
        T[nd * 2].val += T[nd].val;
        T[nd * 2 + 1].val += T[nd].val;
        if (T[nd].val & 1) {
            swap(T[nd * 2].len4, T[nd * 2].len7);
            swap(T[nd * 2].len47, T[nd * 2].len74);
            swap(T[nd * 2 + 1].len4, T[nd * 2 + 1].len7);
            swap(T[nd * 2 + 1].len47, T[nd * 2 + 1].len74);
        }
        T[nd].val = 0;
    }
}

void update(int nd, int lf, int rg) {
    if (lf <= T[nd].Left && rg >= T[nd].Right) {
        T[nd].val += 1;
        swap(T[nd].len4, T[nd].len7);
        swap(T[nd].len47, T[nd].len74);
    } else {
        int mid = (T[nd].Left + T[nd].Right) / 2;
        pushdown(nd);
        if( lf <= mid){
            update(nd * 2, lf, rg);
        }
        if( rg > mid){
            update(nd * 2 + 1, lf, rg);
        }
        pushup(nd);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int i,l,r;
    cin >> n >> m;
    cin >> A;
    build(1, 1, n);
    string in;
    for (i = 0; i < m; i++) {
        cin >> in;
        if(in[0]=='s'){
            cin >> l >> r;
            update(1, l, r);
        } else{
            cout << T[1].len47 << '\n';
        }
    }
}