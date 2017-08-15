t = int(input())

def desenho(Mt,Nt,Lt,At,Bt):
    At *= Lt
    Bt *= Lt
    soma = At + Bt
    Nt = int(Nt/2)
    soma *= Nt
    return soma

def desenho2(Mt,Nt,Lt,At,Bt):
    At *= Lt
    Bt *= Lt
    soma = Bt + At
    Nt = int(Nt/2)
    soma *= Nt
    return soma


cond = 0
while cond < t :
   mt = int(input())
   nt = int(input())
   lt = int(input())
   at = input()
   bt = input()
   cond += 1

cond2 = 0
while cond2 < nt:
    print(desenho(mt,nt,lt,at,bt)"\n",*2)
    print(desenho2(mt,nt,lt,at,bt))
    cond2 += 1
