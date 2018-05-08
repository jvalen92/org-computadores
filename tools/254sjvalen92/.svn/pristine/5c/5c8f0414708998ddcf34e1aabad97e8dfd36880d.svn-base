file = open("StaticTest.vm",'r')
#lee el archivo de entrada y lo limpia de comentarios y saltos de linea e ingresa las instrucciones a una lista
ins=[]
for line in file.readlines():
    if line[0] is not '/' and (line is not "\n"):
        #print(line)
        ins.append(line.strip())


#recorre la lista de instrucciones
for i in ins:
    if i[0]=='p':
        if i[:4] == "push":
            #haga el codigo push
            print("push",i[:4])
            print()
        elif i[:3]=="pop":
            print("pop",i[:3])