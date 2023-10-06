def print_gugudan(n):
    for x in range(1,n+1):
        print(f" -----[{x}단] -----")
        for y in range(1,n+1):
            print(f"{x}*{y} ={x*y}")

num = int(input("몇단까지 출력할까요?"))
print_gugudan(num)
