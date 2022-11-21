n = int(input())
st = input()
one = st.count("1")
zero = st.count("0")
if one>=zero:
    print(one-zero)
else:
    print(zero-one)
