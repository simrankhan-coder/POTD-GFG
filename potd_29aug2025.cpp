/*Smallest window containing all characters
Difficulty: HardAccuracy: 30.19%Submissions: 186K+Points: 8Average Time: 30m
Given two strings s and p. Find the smallest substring in s consisting of all the characters (including duplicates) of the string p. Return empty string in case no such substring is present.
If there are multiple such substring of the same length found, return the one with the least starting index.

Examples:

Input: s = "timetopractice", p = "toc"
Output: "toprac"
Explanation: "toprac" is the smallest substring in which "toc" can be found.
Input: s = "zoomlazapzo", p = "oza"
Output: "apzo"
Explanation: "apzo" is the smallest substring in which "oza" can be found.
Input: s = "zoom", p = "zooe"
Output: ""
Explanation: No substring is present containing all characters of p.
Constraints: 
1 ≤ s.length(), p.length() ≤ 106
s, p consists of lowercase english letters */

#include <iostream>
#include <string>
#include <vector>
#include <climits>
using namespace std;

string smallestWindow(string s, string p){
    int len1 = s.length();
    int len2 = p.length();

    if (len1 < len2)
        return "";

    vector<int> countP(256, 0);
    vector<int> countS(256, 0);

    // Store occurrence of characters of P
    for (int i = 0; i < len2; i++)
        countP[p[i]]++;

    int start = 0, start_idx = -1, min_len = INT_MAX;

    int count = 0;

    for (int j = 0; j < len1; j++){
        // Count occurrence of characters 
        // of string S
        countS[s[j]]++;

        // If S's char matches with P's char,
        // increment count
        if (countP[s[j]] != 0 && countS[s[j]] <= countP[s[j]]){
            count++;
        }

        // If all characters are matched
        if (count == len2){
            // Try to minimize the window
            while (countS[s[start]] > countP[s[start]] || 
                   countP[s[start]] == 0){
                if (countS[s[start]] > countP[s[start]]){
                    countS[s[start]]--;
                }
                start++;
            }

            // Update window size
            int len = j - start + 1;
            if (min_len > len){
                min_len = len;
                start_idx = start;
            }
        }
    }

    if (start_idx == -1)
        return "";

    return s.substr(start_idx, min_len);
}

int main(){
    string s = "timetopractice";
    string p = "toc";

    string res = smallestWindow(s, p);
    cout << res;

    return 0;
}