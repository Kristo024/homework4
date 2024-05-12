immutable_var=2,4,6,True,'bom',[3,4]
print(immutable_var)
#immutable_var[0]=3 - Не доступно для изменений: сохраняем целостность кортежа, экономим память.
immutable_var[5][0]=1 # можно изменить список внутри кортежа.
print(immutable_var)
print(type(immutable_var))
#mutable_list=[immutable_var]
#print(mutable_list,type(mutable_list ))
#mutable_list[0][5][0]=200
mutable_list=[2,4,6,True,'bim',[3,4]]
mutable_list[1]=40
mutable_list.append(False)
print(mutable_list)