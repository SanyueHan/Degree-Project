from main.II_syntactic.node import ASTNode
from main.II_syntactic.node_types import ASTNodeType


class Asmgen:
    _root=ASTNode()

    _rspoffset = 0  # size of stack frame

    # temp var in the cal process, key- ASTNode, value-the address of node,can be register or stack
    _tempvar = dict()
    # local var, key-var, value-address of node, in the stack
    _localvar = dict()

    # registers can be used
    _registersl=["%eax", "%ebx", "%r10d", "%r11d", "%r12d", "%r13d", "%r14d", "%r15d"]
    _pararegisl=["%edi", "%esi", "%edx", "%ecx", "%r8d", "%r9d"]
    _pararegisq=["%rdi", "%rsi", "%rdx", "%rcx", "%r8", "%r9"]

    # code cache when scanning function
    _bodyAsm=""

    # string literals
    stringliteral=[]

    def __init__(self,node):
        self._root=node

    def generate(self):
        string = ""
        # head of code block
        string += "\t.section	__TEXT,__text,regular,pure_instructions\n"

        # function call
        # for node in :

        # generate "main"
        self.visitprogram(self._root)
        temp=self.generateprogram("main",string)
        string+=temp

        # text literals
        string+="\n# string literals\n\t.section	__TEXT,__cstring,cstring_literals\n"
        for i in range(len(self.stringliteral)):
            string=string+"L.str"+str(i)+":\n"+"\t.asciz\t\""+self.stringliteral[i]+"\"\n"

        stringliteral=[]

        return string


    def generateprogram(self,name,string):
        # add label
        string=string+"\n# "+name+"\n\t.glbl _"+name+"\n_"+name+":\n"

        string=string+"\n\tpushq\t%rbp\n\tmovq\t%rsp, %rbp\n"

        # set stack top, 16 bytes align
        if (self._rspoffset % 16) !=0:
            self._rspoffset=(self._rspoffset/16 +1)*16

        string=string+"\n\t# set stack top\n\tsubq\t$"+str(self._rspoffset)+", %rsp\n"

        # save the values in the registers we used
        self.saveregisters()

        # function body
        string=string+"\n\t# process body\n"+self._bodyAsm

        # recover the values in the registers we used
        self.restoreregisters()

        # recover stack top
        string=string+"\n\t# recover stack top\n\taddq\t$"+str(self._rspoffset)+", %rsp\n"

        if name=="main":
            string=string+"\n\t#return value\n\txorl\t%eax, %eax\n"

        string=string+"\n\t# end\n\tpopq\t%rbp\n\tretq\n"

        # reset temp vars
        self._rspoffset=0
        self._localvar=dict()
        self._tempvar=dict()
        self._bodyAsm=""

        return string


    def saveregisters(self):
        pass

    def restoreregisters(self):
        pass


    def visitprogram(self,root):
        string=""
        for child in root.get_children():
            string+=self.visitblockstat(child)
        return string

    def visitblockstat(self,node):
        string=""
        if node.get_type()==ASTNodeType.EXP_STMT:# 如果是赋值语句
            string+=self.visitassign(node)
        elif True:
            pass
        return string

    def visitassign(self,node):
        identifier=node.get_child(0).get_child(0)
        varaddress=self.visitassignid(identifier)# 该变量要存储到的寄存器或栈
        value=self.visitexpression(node.get_child(0).get_child(1))
        self._bodyAsm=self._bodyAsm+"\tmovl\t"+str(value)+", "+varaddress
        return varaddress

    def visitassignid(self,id):
        self._rspoffset+=4
        string="-"+str(self._rspoffset)+"(%rbp)"
        self._localvar[id]=string
        return string


    def visitexpression(self,node):
        string=""
        # if (node.get_child(0)!=None) and (node.get_child(1)!=None):
        if node.num_children() >= 2:
            left=self.visitexpression(node.get_child(0))
            right=self.visitexpression(node.get_child(1))
            if node.get_text()=="+":
                string=self.allocforexp(node)
                if string!=left:
                    self._bodyAsm = self._bodyAsm + "\tmovl\t" + left + ", " + string+"\n"
                self._bodyAsm = self._bodyAsm + "\taddl\t" + right + ", " + string+"\n"
            elif node.get_text()=="-":
                string = self.allocforexp(node)
                self._bodyAsm = self._bodyAsm + "\tmovl\t" + left + ", " + string + "\n"
                self._bodyAsm = self._bodyAsm + "\tsubl\t" + right + ", " + string + "\n"

        elif node.get_type()==ASTNodeType.NUMBER_LIT:
            string=string+"$"+node.get_text()#此处之后修改添加支持a=b+1，右边支持加变量

        return string

    def allocforexp(self,node):
        string=""
        availregis=self.getavailregis()
        if availregis!=-1:
            string=self._registersl[availregis]
        else:
            self._rspoffset+=4
            string="-"+str(self._rspoffset)+"(%rbp)"
        self._tempvar[node.get_text()]=string
        return string

    def getavailregis(self):
        res=-1
        for i in range(len(self._registersl)):
            r=self._registersl[i]
            if r in self._tempvar.values():
                res=i
                break
        return res










