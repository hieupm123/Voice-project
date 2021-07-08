#include<bits/stdc++.h>
using namespace std;
#define double long double
#define int long long
vector<int> cnt;
void KMP(string s){
	int n = (int)s.size();
	cnt.resize(n + 100);
	for(int i = 1; i < n; ++i){
		int j = cnt[i - 1];
		while(j > 0 && s[i] != s[j]){
			j = cnt[j - 1];
		}
		if(s[i] == s[j]) ++j;
		cnt[i] = j;
	}
}
int32_t main(){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
   string s; cin>>s;
   int n = (int)s.size();
   string s1 = "", s2 = "";
   for(int i = 0; i < n - 1; ++i){
   	s1 += s[i];
   }
   for(int i = 1; i < n; ++i){
   	s2 += s[i];
   }
   s = s1 + "#" + s2;
   cout<<s<<"\n";
   KMP(s);
   int ans = 0;
   for(int i = 0; i < (int)s.size() + 100; ++i){
   	if(cnt[i] > ans){
   		ans = cnt[i];
   	}else if(cnt[i] < ans){
   		cout<<ans<<" ";
   		ans = cnt[i];
   	}
   	// cout<<cnt[i]<<" ";
   }
   return 0;
}