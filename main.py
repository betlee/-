for i in range(10): ##縱軸10行
    if i%2 == 0:##判斷為偶數行
        for j in range(10):##橫軸10行
            print("*+", end='')##輸出
    else:##判斷為奇數行
        for j in range(10):##橫軸10行
            print("+*", end='')##輸出
    print()##換行