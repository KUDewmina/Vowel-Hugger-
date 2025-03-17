string = input()
vowels = "AEIOUaeiou"
left,right=0,1 # Iterating points
left_flag,right_flag=0,0 # These flag points are the deciders where the brackets should add
max_length = 0
while left<len(string):  # Iterating with left pointer
    if string[left] in vowels: 
        right=left+1 
        while right<len(string): # Iterating with right pointer
            if string[right] in vowels:
                right+=1
            else:
                lenght = right-left
                if max_length<lenght:
                    max_length=lenght
                    right_flag,left_flag=right,left # Assigning pointers to flags
                left=right # Move left to the next non-vowel character
                break
    left+=1

if max_length==0: # Checking if there are no vowels
    print("["+string+"]")
else:
    print(string[:left_flag]+"["+string[left_flag:right_flag]+"]"+string[right_flag:])
