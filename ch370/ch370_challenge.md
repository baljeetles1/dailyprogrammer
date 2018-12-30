# [2018-12-17] Challenge #370 [Easy] UPC check digits

The Universal Product Code (UPC-A) is a bar code used in many parts of the world. The bars encode a 12-digit number used to identify a product for sale, for example:
```
042100005264
```
The 12th digit (4 in this case) is a redundant check digit, used to catch errors. Using some simple calculations, a scanner can determine, given the first 11 digits, what the check digit must be for a valid code. (Check digits have previously appeared in this subreddit: see Intermediate 30 and Easy 197.) UPC's check digit is calculated as follows (taken from Wikipedia):
1. Sum the digits at odd-numbered positions (1st, 3rd, 5th, ..., 11th). *If you use 0-based indexing, this is the even-numbered positions (0th, 2nd, 4th, ... 10th).*
2. Multiply the result from step 1 by 3.
3. Take the sum of digits at even-numbered positions (2nd, 4th, 6th, ..., 10th) in the original number, and add this sum to the result from step 2.
4. Find the result from step 3 modulo 10 (i.e. the remainder, when divided by 10) and call it *M*
5. If *M* is 0, then the check digit is 0; otherwise the check digit is 10 - *M*.

## Challenge

Given an 11-digit number, find the 12th digit that would make a valid UPC. You may treat the input as a string if you prefer, whatever is more convenient. If you treat it as a number, you may need to consider the case of leading 0's to get up to 11 digits. That is, an input of `12345` would correspond to a UPC start of `00000012345`.
