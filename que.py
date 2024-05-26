import json
que = { }
res = 0
num = 1
e= open("que.txt",'r')
que = json.load(e)
e.close()
print("Enter t or f ")
name = input("Enter your name: ")
for i in que.keys():
    print("Question",num,": ", i)
    answer = input("The answer  ")
    if answer.lower() == que[i].lower():
        res = res + 1

    num = num + 1

result={name:res}
m = open("result.txt",'w')
final = json.dump(result,m)
m.close()