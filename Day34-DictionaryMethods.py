info={'Ananth':'22311a0411','Nithin':'22311a0425','JBK':'22311a0429','Arun':'22311a0464'}
print(info)
info.update({'Akshitha':'22311a0413'})
info.update({'Arun':'22311a0465'})
print(info)

#  info.clear()#Dictionary is cleared
# print(info)

info.pop('Arun')
print(info)

info.popitem()
print(info)
info.popitem()
print(info)#Removes last item from the dictionary

info={'Ananth':'22311a0411','Nithin':'22311a0425','JBK':'22311a0429','Arun':'22311a0464'}
del info['Nithin']
print(info)
del info
print(info)#NameError: name 'info' is not defined
