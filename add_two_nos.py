l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
l3 = list()
temp1 = 0
temp2 = 0
i = 0
j = 0
for i in l1[::-1]:
    temp1 = (temp1*10)+i
for j in l2[::-1]:
    temp2 = (temp2*10)+j

temp = temp1+temp2
while(temp>0):
    a = temp%10
    l3.append(a)
    temp = temp//10


print(temp1)
print(temp2)
print(l3)

#using linked list (leetcode problem)
'''class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = l1
        temp2 = l2
        temp = 0
        strg1 = ""
        strg2 = ""
        strg = ""
        res_list = None
        while(temp1!=None):
            strg1 += str(temp1.val)
            temp1 = temp1.next
        while(temp2!=None):
            strg2 += str(temp2.val)
            temp2 = temp2.next
        
        temp = int(strg1[::-1])+int(strg2[::-1])
        strg = str(temp)
        
        for i in range(len(strg)):
            res_list = ListNode(int(strg[i]),res_list)
            
        return res_list'''