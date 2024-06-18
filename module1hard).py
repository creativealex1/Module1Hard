a = [5, 3, 3, 5, 4]
b = [2, 2, 2, 3]
c = [4, 5, 5, 2]
d = [4, 4, 3]
e = [5, 5, 5, 4, 5]
students = ({'Aaron' : sum(a)/len(a)} | {'Bilbo': sum(b)/len(b)} | {'Johnny' : sum(c)/len(c)} | {'Khednrik' : sum(d)/len(d)} | {'Steve' : sum(e)/len(e)})
print(students)