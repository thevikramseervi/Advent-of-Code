// Day 03 - Part One
// ans = 173517243

#include <bits/stdc++.h>

using namespace std;

int fn(vector<char> str, int i) {
  int n = str.size();

  string f, s;
  f += str[i];
  i++;

  int j = 0;
  for (j = 1; j < 3; j++) {
    if (isdigit(str[i])) {
      f += str[i];
      i++;
      continue; // go to next digit
    }
    if (str[i] == ',') {
      i++;
      break; // stop if ,
    }
    return 0;
  }

  if (j == 3 && str[i] == ',') {
    i++;
  } else if (j == 3 && str[i] != ',') {
    return 0;
  }

  if (!isdigit(str[i])) {
    return 0;
  }

  s += str[i];
  i++;

  for (j = 0; j < 3; j++) {
    if (isdigit(str[i])) {
      s += str[i];
      i++;
      continue; // go to next digit
    }
    if (str[i] == ')') {
      i++;
      break;
    }
    return 0;
  }

  if (j == 3 && str[i] == ')') {
    i++;
  } else if (j == 3 && str[i] != ')') {
    return 0;
  }

  int res1 = stoi(f);
  int res2 = stoi(s);
  return res1 * res2;
}

int main() {

  ifstream f("input");

  char ch;
  vector<char> str;

  while (f.get(ch)) {
    str.push_back(ch);
  }

  long long ans = 0;

  int n = str.size();
  for (int i = 0; i < n - 4; i++) {
    string f, s, m;
    if (str[i] == 'm' && str[i + 1] == 'u' && str[i + 2] == 'l' &&
        str[i + 3] == '(' && isdigit(str[i + 4])) {
      ans += fn(str, i + 4);
    }
  }

  cout << ans << "\n";
  return 0;
}