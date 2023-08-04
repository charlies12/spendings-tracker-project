# spendings-tracker-project

Supposed to keep track of expenses. So far the script works but it is very cumbersome and takes too many steps to input information. Validation could be a problem especially if the key-value pairs don't match. Such as only entering a key but not a value and vice versa. I was able to finally fix the issue where I would have to input item names and item prices two times. I was calling a function twice without saving the return value to a variable to later reuse.
