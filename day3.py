# ------------
# def coinChange(self, coins: List[1, 5, 10, 25, 50], amount: 97) -> 97:
#     dp = [amount+1]* (amount+1)
#     dp[0]=0

#     for a in range(1, amount+1):
#         for c in coins:
#             if a - c >=0:
#                 dp[a]=min(dp[a], 1+dp[a - c])

#         return dp[amount] if dp[amount] != amount + 1 else -1

# print(coinChange)

# ------------

''' function minimumn change back required n= target value number, Denomination = type of coin'''
def minChangeBack(n, denominations):
    '''   float(inf)= default max-cap on number'''
    '''   for x in range(n+1)= finding list of numbers to iterate through'''
    change = [float('inf') for x in range(n+1)]
    '''minimum required coins to make chage of $0 = 0, sets a baseline'''
    change[0] = 0
    '''iterating through each single coin denomination possibility'''
    for denomination in denominations:
        '''looping in possible numbers/ amounts with the coin denominations'''
        for amount in range(len(change)):
            '''if the coin value is les or equal to change/amount'''
            if denomination <= amount:
                ''''''
                change[amount]= min(change[amount], 1+change[amount-denomination])

        return change[n] if change[n] != float('inf') else -1
print(minChangeBack(97, [1, 5, 10, 25, 50]))

# came up with 97 did not run as originally thought
# ------------

# def return_change( change, coins=[.01, .05, .10, .25]):
#     flag = None
#     for coin in coins:
#         if coin == change: return coin
#         if coin < change:
#             flag = c
#         return flag
#     return_change (.97)

# def removingDuplicates():
# names=['casey', 'kevin', 'tom', 'jerry']
# users= ['casey', 'kevin', 'tom','tom', 'jerry']

# for users in names:
#     names.append(users.remove()

# return names)


# cashier challenge
# int
# number under dollar
# ex2: 98c
# ex2: 27c

#output 1 quater + 2 pennys
#ex2: 3 quarters +2 times + 3 pennies

# quater 25, dime 10, nickel 5, penny 1
# def smallestChange(x):
#     if 


# create a for loop to subtract the greatest value of the listed change
# currency = ['quater','dime','nickel','penny']
# quater = 25
# dime = 10
# nickel = 5
# penny = 1
 
# input = 97

# currency.input
#  print (input.value)
