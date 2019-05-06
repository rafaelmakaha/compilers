def main():
    n = int(input())
    a = set()
    for _ in range(n):
        st = input().split('@')
        st1 = ''.join(st[0].split('.'))
        st1 = st1.split('+')
        st2 = st[1]
        st = '@'.join([st1[0], st2])
        a.add(st)
    print(len(a))

main()