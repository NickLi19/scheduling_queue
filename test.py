import LinkList

chaiin = LinkList.Linklist()
for i in range(10):
    chaiin.append(i)

chaiin.display()
print('---------------------')
chaiin.delete(chaiin.getIndex(7))
chaiin.display()
print('---------------------')
chaiin.pop()
chaiin.display()
print('---------------------')
chaiin.insert(6, 7)
chaiin.display()
print('---------------------')
chaiin.update(8, 12)
chaiin.display()
# print(chaiin.length)
# print('---------------------')
# print(chaiin.getItem(8))
