def inp():
  global i,j
  i = int(input("i를 입력해주세요 : "))
  j = int(input("j를 입력해주세요 : "))
  return

def add(i,j):
  print("{0} + {1} = {2}".format(i,j,i+j))

def sub(i,j):
  print("{0} - {1} = {2}".format(i,j,i-j))

def mul(i,j):
  print("{0} * {1} = {2}".format(i,j,i*j))

def div(i,j):
  print("{0} / {1} = {2}".format(i,j,i/j))

def rem(i,j):
  print("{0} % {1} = {2}".format(i,j,i%j))

while(True):
    print("사칙연산을 받아와 사칙연산이 아니면 종료하는 프로그램입니다.")
    print("사칙 연산의 '+', '-','*','/','%'로 입력하여 주세요.")
    ao = input("사칙연산을 입력해주세요 : ")
    if (ao == "+"):
        inp()
        add(i,j)
    elif (ao == "-"):
        inp()
        sub(i,j)
    elif (ao == "*"):
        inp()
        mul(i,j)
    elif (ao == "/"):
        inp()
        div(i,j)
    elif (ao == "%"):
        inp()
        rem(i,j)
    else:
        print("사칙 연산이 아니므로 종료합니다.")
        break
