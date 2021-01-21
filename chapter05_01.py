# Chapter05-1
# 파이썬 함수 및 중요성
# 파이썬 함수식 및 람다(lambda)


# 함수 정의 방법
# def fuction_name(parameter):
#     code

# 예제1
def first_func(w):
    print("Hello,", w)

word = "Goodboy"
first_func(word)
print()

# 예제2
def return_func(w1):
    return "Hello, " + str(w1)

x = return_func('Goodboy2')
print(x)
print()

# 예제3(다중반환)
def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3

x, y, z = func_mul(10)
print(x, y, z)
print()

# 튜플 리턴
def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return (y1, y2, y3)

q = func_mul2(20)
print(type(q), q, list(q))
print()

# 리스트 리턴
def func_mul3(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1, y2, y3]

p = func_mul3(20)
print(type(p), p, set(p))
print()

# 딕셔너리 리턴
def func_mul4(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return {'v1':y1, 'v2':y2, 'v3':y3}

d = func_mul4(30)
print(type(d), d, d.get('v2'), d.items(), d.keys())
print()