import sys

def translate(fileName):
        
    #nombre del archivo sin extension
    name=fileName.split('.')[0]
    #ruta del archivo
    route=name+'/'+fileName
    file = open(route, 'r')

    # nombre del archivo sin la extension para las instrucciones static
    nameStatic = name.split('/')[0]
    # lee el archivo de entrada y lo limpia de comentarios y saltos de linea e ingresa las instrucciones a una lista
    ins = []
    # contador para las etiquetas
    label = 0

    for line in file.readlines():

        if line[0] is not '/' and (line is not "\n"):
            # print(line)
            ins.append(line.strip())

    # crea un nuevo archivo con la extencion .asm
    newFile = name+'/'+name + ".asm"
    file = open(newFile, 'w')

    # recorre la lista de instrucciones
    for i in ins:
        # separa la instruccion por argumentos
        args = i.split(" ")
        if args[0] == "push":
            # agurmentos para el push

            if args[1] == "constant":
                # print("asm para push constant ",i)
                out = "@" + args[2] + "\n" + "D=A\n" + "@SP\n" + "A=M\n" + "M=D\n" + "@SP\n" + "M=M+1\n"
                file.writelines(out)

            elif args[1] == "static":
                # print("asm para push static",i)
                out = "@" + nameStatic + "." + args[
                    2] + "\n" + "D=M\n" + "@SP\n" + "A=M\n" + "M=D\n" + "@SP\n" + "M=M+1\n"
                file.writelines(out)

            elif args[1] == "pointer":
                # print("asm para push pointer")
                out = "@" + args[
                    2] + "\n" "D=A\n" + "@3\n" + "A=A+D\n" + "D=M\n" + "@SP\n" + "A=M\n" + "M=D\n" + "@SP\n" + "M=M+1\n"
                file.writelines(out)

            elif args[1] == "argument":
                # print("asm para push arguments")
                out = "@" + args[
                    2] + "\n" + "D=A\n" + "@ARG\n" + "A=M+D\n" + "D=M\n" + "@SP\n" + "A=M\n" + "M=D\n" + "@SP\n" + "M=M+1\n"
                file.writelines(out)

            elif args[1] == "this":
                # print("asm para push this")
                out = "@" + args[
                    2] + "\n" + "D=A\n" + "@THIS\n" + "A=M+D\n" + "D=M\n" + "@SP\n" + "A=M\n" + "M=D\n" + "@SP\n" + "M=M+1\n"
                file.writelines(out)

            elif args[1] == "that":
                # print("asm para that")
                out = "@" + args[
                    2] + "\n" + "D=A\n" + "@THAT\n" + "A=M+D\n" + "D=M\n" + "@SP\n" + "A=M\n" + "M=D\n" + "@SP\n" + "M=M+1\n"
                file.writelines(out)

            elif args[1] == "temp":
                # print("asm para push temp")
                out = "@" + args[
                    2] + "\n" + "D=A\n" + "@5\n" + "A=A+D\n" + "D=M\n" + "@SP\n" + "A=M\n" + "M=D\n" + "@SP\n" + "M=M+1\n"
                file.writelines(out)

            elif args[1] == "local":
                # print("asm para push local")
                out = "@" + args[
                    2] + "\n" + "D=A\n" + "@LCL\n" + "A=M+D\n" + "D=M\n" + "@SP\n" + "A=M\n" + "M=D\n" + "@SP\n" + "M=M+1\n"
                file.writelines(out)

            else:
                print("entrada no valida", i)
                sys.exit()


        elif args[0] == "pop":
            # agurmentos para el pop

            if args[1] == "static":
                # print("asm para pop static")
                out = "@SP\n" + "AM=M-1\n" + "D=M\n" + "@" + nameStatic + "." + args[2] + "\n" + "M=D\n"
                file.writelines(out)

            elif args[1] == "this":
                # print("asm para pop this")
                out = "@" + args[
                    2] + "\n" + "D=A\n" + "@THIS\n" + "D=M+D\n" + "@R13\n" + "M=D\n" + "@SP\n" + "AM=M-1\n" + "D=M\n" + "@R13\n" + "A=M\n" + "M=D\n"
                file.writelines(out)

            elif args[1] == "that":
                # print("asm para pop that")
                out = "@" + args[
                    2] + "\n" + "D=A\n" + "@THAT\n" + "D=M+D\n" + "@R13\n" + "M=D\n" + "@SP\n" + "AM=M-1\n" + "D=M\n" + "@R13\n" + "A=M\n" + "M=D\n"
                file.writelines(out)

            elif args[1] == "pointer":
                # print("asm para pop pointer")
                out = "@" + args[
                    2] + "\n" + "D=A\n" + "@3\n" + "D=A+D\n" + "@R13\n" + "M=D\n" + "@SP\n" + "AM=M-1\n" + "D=M\n" + "@R13\n" + "A=M\n" + "M=D\n"
                file.writelines(out)

            elif args[1] == "argument":
                # print("asm para pop arguments")
                out = "@" + args[
                    2] + "\n" + "D=A\n" + "@ARG\n" + "D=M+D\n" + "@R13\n" + "M=D\n" + "@SP\n" + "AM=M-1\n" + "D=M\n" + "@R13\n" + "A=M\n" + "M=D\n"
                file.writelines(out)

            elif args[1] == "local":
                # print("asm para pop local")
                out = "@" + args[
                    2] + "\n" + "D=A\n" + "@LCL\n" + "D=M+D\n" + "@R13\n" + "M=D\n" + "@SP\n" + "AM=M-1\n" + "D=M\n" + "@R13\n" + "A=M\n" + "M=D\n"
                file.writelines(out)

            elif args[1] == "temp":
                # print("asm para temp")
                out = "@" + args[
                    2] + "\n" + "D=A\n" + "@5\n" + "D=A+D\n" + "@R13\n" + "M=D\n" + "@SP\n" + "AM=M-1\n" + "D=M\n" + "@R13\n" + "A=M\n" + "M=D\n"
                file.writelines(out)

            else:
                print("entrada no valida", i)
                sys.exit()

        # Operaciones Aritmeticas

        elif args[0] == "add":
            # print("asm para add")
            out = "@SP\n" + "AM=M-1\n" + "D=M\n" + "@SP\n" + "AM=M-1\n" + "M=D+M\n" + "@SP\n" + "M=M+1\n"
            file.writelines(out)

        elif args[0] == "sub":
            # print("asm para sub")
            out = "@SP\n" + "AM=M-1\n" + "D=M\n" + "@SP\n" + "AM=M-1\n" + "M=M-D\n" + "@SP\n" + "M=M+1\n"
            file.writelines(out)

        elif args[0] == "neg":
            # print("asm para neg")
            out = "@SP\n" + "A=M-1\n" + "M=-M\n"
            file.writelines(out)

        elif args[0] == "not":
            # print("asm para not")
            out = "@SP\n" + "A=M-1\n" + "M=!M\n"
            file.writelines(out)

        elif args[0] == "or":
            # print("asm para not")
            out = "@SP\n" + "AM=M-1\n" + "D=M\n" + "@SP\n" + "A=M-1\n" + "M=D|M\n"
            file.writelines(out)

        elif args[0] == "and":
            # print("asm para and")
            out = "@SP\n" + "AM=M-1\n" + "D=M\n" + "@SP\n" + "A=M-1\n" + "M=D&M\n"
            file.writelines(out)

        elif args[0] == "eq":
            label = int(label)
            label += 1
            label = str(label)
            out = "@SP\n" + "AM=M-1\n" + "D=M\n" + "@SP\n" + "A=M-1\n" + "D=M-D\n" + "M=-1\n" + "@eqTrue" + label + "\n" + "D;JEQ\n" + "@SP\n" + "A=M-1\n" + "M=0\n" + "(eqTrue" + label + ")\n"
            file.writelines(out)

        elif args[0] == "gt":
            label = int(label)
            label += 1
            label = str(label)

            out = "@SP\n" + "AM=M-1\n" + "D=M\n" + "@SP\n" + "A=M-1\n" + "D=M-D\n" + "M=-1\n" + "@gtTrue" + label + "\n" + "D;JGT\n" + "@SP\n" + "A=M-1\n" + "M=0\n" + "(gtTrue" + label + ")\n"
            file.writelines(out)

        elif args[0] == "lt":
            label = int(label)
            label += 1
            label = str(label)

            out = "@SP\n" + "AM=M-1\n" + "D=M\n" + "@SP\n" + "A=M-1\n" + "D=M-D\n" + "M=-1\n" + "@ltTrue" + label + "\n" + "D;JLT\n" + "@SP\n" + "A=M-1\n" + "M=0\n" + "(ltTrue" + label + ")\n"
            file.writelines(out)

        

        #project 8
        elif args[0]== "label":
            out='(' + args[1] + ')' + "\n"
            file.writelines(out)

        elif args[0] == "goto":
            out="@"+ args[1] +"\n" + "0;JMP" + "\n"
            file.writelines(out)

        elif args[0] =="if-goto":
            out="@SP\n" +  "M=M-1\n" + "A=M\n" + "D=M\n" + "@" + args[1] + "\n" + "D;JNE\n"
            file.writelines(out)

        elif args[0] =="function":
            #print("soy una funcion")
            out='(' + args[1] + ')' + "\n"
            aux =0
            while(aux < int(args[2])):
                out=out + pconstant()
                aux=aux+1
            #print(out)
            file.writelines(out)

        elif args[0]=="return":
           # print("soy un return")
            out = "@LCL\n" + "D=M\n" + "@R11\n" + "M=D\n" + "@5\n" + "A=D-A\n" + "D=M\n" + "@R12\n" + "M=D\n"
            out += popArg()
            out += "@ARG\n" + "D=M\n" + "@SP\n" + "M=D+1\n"
            out +=  frame("THAT") + frame("THIS") + frame("ARG") + frame("LCL")
            out +=    "@R12\n" + "A=M\n" + "0;JMP\n";
            #print(out)
            file.writelines(out)

        elif args== "CALL":
            label = int(label)
            label += 1
            label = str(label)
            R_Label='(' + args[1] + label + ')' + "\n"
            out="@"+ R_Label +'\n' + "D=A\n + @SP\n + A=M\n + M=D\n + @SP\n + M=M+1\n"
            #push local 0
            out += push("LCL",0)
            #push ARG 0
            out +=push("ARG",0)
            #push this
            out += push("THIS",0)
            #push that 0
            out += push("THAT",0)

            out += "@SP\n" + "D=M\n" + "@5\n" + "D=D-A\n" + "@" + args[2] + "\n"
            out += "D=D-A\n" + "@ARG\n" + "M=D\n" + "@SP\n" + "D=M\n" + "@LCL\n"
            out += "M=D\n" + "@" + args[1] + "\n" + "0;JMP\n" +"(" + R_Label + ")\n"
            file.writelines(out)

        else:
            print("instruccion no valida", i)
            sys.exit()


def pconstant():
    out = "@0" + "\n" + "D=A\n" + "@SP\n" + "A=M\n" + "M=D\n" + "@SP\n" + "M=M+1\n"
    return out

def frame(pointer):
    out = "@R11\n" + "D=M-1\n" + "AM=D\n" + "D=M\n" + "@" + pointer + "\n" + "M=D\n";
    return out
def popArg ():
    out="@0\n" + "D=A\n" + "@ARG\n" + "D=M+D\n" + "@R13\n" + "M=D\n" + "@SP\n" + "AM=M-1\n" + "D=M\n" + "@R13\n" + "A=M\n" + "M=D\n"
    return out
def push(segment,index):
    out="@" + str(index) + "\n" + "D=A\n" + "@"+ segment+ '\n' + "A=M+D\n" + "D=M\n" + "@SP\n" + "A=M\n" + "M=D\n" + "@SP\n" + "M=M+1\n"
    return out



#imprime la lista de parametros 
print(sys.argv)

#ejecuta el metodo translate para cada parametro empezando desde la pocision 1
i=1
length=len(sys.argv)
while(i<length):
    fileName=sys.argv[i]
    print(fileName)
    translate(fileName)
    i=i+1