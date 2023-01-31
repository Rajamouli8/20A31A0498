days=int(input())
if days<=84:
    calls=int(input())
    msgs=int(input())
    data=float(input())
    print("remaining days:", 84-days)
    print("remaining calls:", 3000-calls) if calls<=3000 else print("kindly top-up")
    print("remaining msgs:", 100-msgs) if msgs<=100 else print("message failed")
    print("remaining data:", round((2-data),3)) if data<=2 else print("limit exceeded")
else:
    print("your plan expired")
