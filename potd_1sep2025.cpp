/*
Sum of Mode
Difficulty: HardAccuracy: 54.2%Submissions: 14K+Points: 8Average Time: 20m
Given an array arr[] of positive integers and an integer k. You have to find the sum of the modes of all the subarrays of size k.
Note: The mode of a subarray is the element that occurs with the highest frequency. If multiple elements have the same highest frequency, the smallest such element is considered the mode.

Examples:

Input: arr[] = [1, 2, 3, 2, 5, 2, 4, 4], k = 3
Output: 13
Explanation: The mode of each k size subarray is [1, 2, 2, 2, 2, 4] and sum of all modes is 13.

Input: arr[] = [1, 2, 1, 3, 5], k = 2
Output: 6
Explanation: The mode of each k size subarray is [1, 1, 1, 3] and sum of all modes is 6.

Constraints:
1 ≤ k ≤ arr.size() ≤105
1 ≤ arr[i] ≤ 105

Time Complexity: O(n log k)
Auxiliary Space: O(k)

*/
#include <iostream>
#include <vector>
#include <unordered_map>
#include <set>
using namespace std;

int sumOfModes(vector<int> &arr, int k) {
    int n = arr.size();
    int sum = 0;

    // Stores frequency of elements 
    // in current window
    unordered_map<int, int> mp;

    // Stores (frequency, -value) to maintain
    // order of mode selection
    set<pair<int, int>> st;

    // Build frequency map for the first window
    for (int i = 0; i < k; i++) {
        mp[arr[i]]++;
    }

    // Populate the set with initial frequency pairs
    for (auto x : mp) {
        st.insert({x.second, -x.first});
    }

    // Add mode of the first window
    int mode = -st.rbegin()->second;
    sum += mode;

    // Slide the window across the array
    for (int i = k; i < n; i++) {
        int out = arr[i - k];
        int in = arr[i];

        // Remove the outgoing element's 
        // previous frequency pair
        st.erase({mp[out], -out});

        // Decrement frequency of 
        // outgoing element
        mp[out]--;

        // If frequency is still positive, 
        // reinsert updated pair
        if (mp[out] > 0) {
            st.insert({mp[out], -out});
        } else {
            mp.erase(out);
        }

        // Increment frequency of incoming element
        mp[in]++;

        // Insert updated frequency pair 
        // for incoming element
        st.insert({mp[in], -in});

        // Get current mode and add to sum
        mode = -st.rbegin()->second;
        sum += mode;
    }

    return sum;
}
//Driver code
int main() {
    vector<int> arr = {1, 2, 3, 2, 5, 2, 4, 4};
    int k = 3;

    int result = sumOfModes(arr, k);
    cout << result << endl;

    return 0;
}