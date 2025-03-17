# Question
Given a string consisting of uppercase and lowercase letters, your task is to find the longest contiguous substring of vowels (both uppercase and lowercase). Then, you must enclose this substring within square brackets ([ ]) in the original string and print the modified string.
If there are multiple longest vowel substrings, the first occurrence should be enclosed. If the string contains no vowels, the entire string should be enclosed within brackets.

-> Input Format
- - - - - - - -
A single string S consisting of only uppercase and lowercase English letters.

-> Output Format
- - - - - - - - -
Print the modified string after enclosing the longest contiguous vowel substring in square brackets ([ ]).

Example 1
---------
Input:  'helloooWorld'

Output:  hell[ooo]World

Explanation:

The longest contiguous vowel substring is "ooo", which is enclosed within [ ].

Example 2
---------
Input:  'rhythm'

Output:  [rhythm]
