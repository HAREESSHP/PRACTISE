def strrev(str):                 #reverse string
    str2=str[::-1]
    print(str2)
str=input("enter the string:")
strrev(str)
print("*************************************************")

def palin(str1,str2):                                  #palindrome
    if str1==str2:
        print("The strings are palindrome")
    else:
        print("The strings are not palindrome")
        
str1=input("Enter first string:")
str2=input("Enter secound string:")
palin(str1,str2)
print("*************************************************")

def vowelscount(str,vowels):                   #vowels count
    count=0
    for s in str:
        if s in vowels:
            count=count+1
            print(s)
    print(count)
str=input("Enter a string:")
v="aeiou"
vowelscount(str,v)
print("*************************************************")

def constcount(str,vowels):                    #consonants count       
    count=0
    for s in str:
        if s not in vowels:
            count=count+1
            print(s)
    print(count)
str=input("Enter a string:")
v="aeiou"
constcount(str,v)
print("*************************************************")

#str last word length
def lenofLastword(str):
    words=str.split()
    return len(words[-1])
str=input("Enter a string:")
print(lenofLastword(str))

#rev of string
def revofstr(str):
    words=str.split()
    return " ".join(words[::-1])
str=input("enter a string:")
print(revofstr(str))

#vowel and constant count
def vowelconstcount(str):
    vowels="aeiou"
    vowel_count=0
    consonant_count=0
    for s in str:
        if s.isalpha():
            if s.lower() in vowels:
                vowel_count+=1
            else:
                consonant_count+=1
    return vowel_count, consonant_count

str=input("enter a string:")
vowels, consonants = vowelconstcount(str)
print(f"Vowels: {vowels}, Consonants: {consonants}" )

#missing number
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total=sum(nums)
        n=len(nums)
        expected=n*(n+1)//2
        return expected-total

#transform array by partiry
    def transformArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[i]=0
            else:
                nums[i]=1
        nums.sort()
        return nums

#max repating substring

    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        count=0
        while word*(count+1) in sequence:
            count = count+1
        return count

#stones and jewels 
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        li=list(jewels)
        count=0
        for i in stones:
            if i in li:
                count=count+1
        return count


    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        sta = []

        for i in s:
            if i == "*":
                sta.pop()
            else:
                sta.append(i)

        return "".join(sta)
        

    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i=0
        for x in range(1,len(nums)):
            if nums[i] != nums[x]:
                i=i+1
            else:
                break
        return nums[i]


    def countPrefixes(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        count=0
        for word in words:
            if s.startswith(word):
                count += 1
        return count
        

    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        lis =bin(n)[2:]
        count=0
        for ch in lis:
            if ch =="1":
                count=count+1
        return count
    
#Third max element
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=list(set(nums))
        nums.sort(reverse=True)
        if len(nums)>=3:
            return nums[2]
        return nums[0]
    
#richest customer wealth
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        maximum=max(sum(row) for row in accounts)
        return maximum
    
#nth highest salary
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        for i in range (len(arr)):
            for j in range (0,len(arr)):
                if i != j and arr[i] == 2 * arr[j]:
                    return True
        return False

#reversal of the array
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        i=0
        r=n
        stack=[]
        for i in range (n):
            stack.append(nums[i])
            stack.append(nums[r])
            i=i+1
            r=r+1
        return stack
    
#continuous ones
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        r=0
        for x in range(len(nums)):
            if nums[x]==1:
                i=i+1
                if i>r:
                    r=i
            else:i=0
        return r