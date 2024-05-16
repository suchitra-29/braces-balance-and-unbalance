s=input()
flag=0
stack=[]
for i in s:
  if i =="[" and "(" and "{":
    stack.append(i)
  elif i =="]" and ")" and "}":
      if len(stack) !=0:
         stack.pop()
      else:
        print("inbalanced")
        flag=1
        break
if len(stack) ==0 and flag == 0:
  print("balanced")
elif len(stack) !=0 and flag == 0:
  print("inbalanced")