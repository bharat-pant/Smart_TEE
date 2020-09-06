b1=b2=b3=b4=0
l=list()
while True:
    b4=b2
    b3=b2
    b2=b1
    a1=int(input())
    a2=int(input())
    a3=int(input())
    a4=int(input())
    s={'lane_1':a1,'lane_2':a2,'lane_3':a3,'lane_4':a4}
    sort_orders = sorted(s.items(), key=lambda x: x[1])
    # For sorted list
    for i in sort_orders:
        l.append(i[0])
    #   print(i[0], i[1])
    print(l)
    c=l[0]
    b1=c
    if((b1==b2)and (b1==b3)and (b1==b3)):
        print('no')
