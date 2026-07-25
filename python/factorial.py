n=int(input("Enter a number: ")) # factorial calculation
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print("Factorial of", n, "is", factorial(n))


#left and ryt diff
def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        le=[0]*len(nums)
        re=[0]*len(nums)
        for i in range(1,len(nums)):
            le[i]=nums[i-1]+le[i-1]
        for i in range(len(nums)-2,-1,-1):
            re[i]=nums[i+1]+re[i+1]
        ans=[]
        for i in range(len(nums)):
            ans.append(abs(le[i]-re[i]))
        return ans

#Buddy string
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s)!=len(goal):
            return False
        if s==goal:
            return len(set(s))<len(s)
        ls=[]
        for i in range(len(s)):
            if s[i]!=goal[i]:
                ls.append(i)
        if len(ls)!=2:
            return False
        i,j=ls
        return s[i]==goal[j] and s[j]==goal[i]

#max product
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ls=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                ls.append((nums[i]-1)*(nums[j]-1))
        return max(ls)

#smallest elements in an array
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                    if nums[i]>nums[j]:
                     count=count+1
            ans.append(count)
        return ans
#revrse array technique
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        target.sort()
        arr.sort()
        return target == arr

#Highest altitude
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        ans=[0]
        for i in range(len(gain)):
            su=ans[i]+gain[i]
            ans.append(su)
        return max(ans)

#Maximum Product Subarray
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = nums[0]
        max_p = nums[0]
        min_p = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                max_p, min_p = min_p, max_p

            max_p = max(nums[i], max_p * nums[i])
            min_p = min(nums[i], min_p * nums[i])

            ans = max(ans, max_p)

        return ans

#Reverse words in a string
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words=s.split()
        res=[]
        for word in words:
            res.append(word[::-1])
        return " ".join(res)

#Sum of Square Numbers
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for a in range(int(c ** 0.5) + 1):
            b = c - a * a
            left = 0
            right = int(b ** 0.5)
            while left <= right:
                mid = (left + right) // 2
                square = mid * mid
                if square == b:
                    return True
                elif square < b:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
#Number of steps to reduce to zero
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        count=0
        while(num>0):
            if (num&1)==0:
                num=num/2
                count=count+1
            else:
                num=num-1
                count=count+1
        return count

#ptriangle
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row=[1]
        for j in range(1,rowIndex+1):
            k=row[-1]*(rowIndex - j+ 1) // j
            row.append(k)
        return row

#longest substing repetative
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)<=1:
            return ""
        ans = ""
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                sub = s[i:j]
                flag = True
                for ch in sub:
                    if ch.islower():
                        if ch.upper() not in sub:
                            flag = False
                            break
                    else:
                        if ch.lower() not in sub:
                            flag = False
                            break
                if flag:
                    if len(sub) > len(ans):
                        ans = sub

        return ans

#k-beauty
    def divisorSubstrings(self, num, k):
        nums = str(num)
        count = 0
        for i in range(len(nums) - k + 1):
            z = 0
            for j in range(i, i + k):
                z = z * 10 + int(nums[j])
            if z != 0 and num % z == 0:
                count += 1
        return count
#Power n
    def myPow(self, x: float, n: int) -> float:

        def calc_power(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            
            res = calc_power(x, n // 2)
            res = res * res

            if n % 2 == 1:
                return res * x
            
            return res

        ans = calc_power(x, abs(n))

        if n >= 0:
            return ans
        
        return 1 / ans 

#trapping rain water
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l=0
        r=len(height)-1
        l1=0
        r2=0
        ans=0
        while l<r:
            if height[l]<=height[r]:
                l1=max(l1,height[l])
                ans+=l1-height[l]
                l+=1
            else:
                r2=max(r2,height[r])
                ans+=r2-height[r]
                r-=1
        return ans
    
#Max of a digit
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        li=[]
        while (n>0):
            s=n%10
            li.append(s)
            n=n//10
        ans=0
        for i in range(len(li)):
           for j in range(i + 1, len(li)):
                ans = max(ans, li[i] * li[j])
        return ans

#count primes
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0

        prime = [True] * n
        prime[0] = False
        prime[1] = False

        p = 2
        while p * p < n:
            if prime[p]:
                for i in range(p * p, n, p):
                    prime[i] = False
            p += 1

        return sum(prime)
   