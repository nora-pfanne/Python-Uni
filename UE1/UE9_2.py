import re

''' 
Parser für die EBNF:
Exp  ::= '(' Exp Op Exp ')'
       | '[' Exps ']
       | '[' ']'
       | Num
Exps ::= Exp ',' Exps
       | Exp KommataExps
KommaExps ::= ',' Exps |
Op   ::= '+' | '*'
Num  ::= ( '1' | ... | '9' ){'0' | ... | '9'}
      | '0'
'''

def parse_exp(s,p) :

  if p<len(s) and s[p] == '(' :
    (e1,p1) = parse_exp(s,p+1)
    (op,p2) = parse_op(s,p1)
    (e2,p3) = parse_exp(s,p2)
    if p3<len(s) and s[p3] == ')' :
      return ([op,e1,e2],p3 + 1)
    else :
      raise Exception("')' expected")
  elif p<len(s) and s[p] == '[':

  else :
    return parse_num(s,p)

def parse_num(s,p) :

  m = re.match("[1-9][0-9]*|0",s[p:])
  if m==None :
    raise Exception('Number expected')
  else :
    return (int(m.group()), p + m.end())

def parse_op(s,p) :
  if p<len(s) and (s[p] == '+' or s[p] == '*') :
    return (s[p],p+1)
  else :
    raise Exception("operator expected")

def parse(s) :
  (e,p_end) = parse_exp(s,0)
  if p_end == len(s) :
    return e
  else :
    raise Exception("unexpected input in position: "+str(p_end))

#text = input("Bitte gib einen Ausdruck ein: ")

#print(parse(text))

# Parser für die BNF:
#
# S ::= 'a' S 'b' |
#

def parse_s(s,p) :
  if p<len(s) and s[p] == 'a' :
    (n,p1) = parse_s(s,p+1)
    if p1<len(s) and s[p1] == 'b' :
      return (n+1,p1+1)
    else :
      raise Exception("b expected")
  else :
    return (0,p)

def anbn(s) :
  (e,p_end) = parse_s(s,0)
  if p_end == len(s) :
    return e
  else :
    raise Exception("unexpected input in position: "+str(p_end))


text = input("Bitte gib Text ein: ")

print(anbn(text))