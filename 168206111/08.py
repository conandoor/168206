a_true,b_true,c_true,d_true = 0,0,0,0

def speak(a,b,c,d):

    a_steal,b_steal,c_steal,d_steal = 0,0,0,0
    
    if a == 1:
        print("A说的是真话")
        c_steal = 1
    if b == 1:
        print("B说的是真话")
        
        d_steal = 1
        
    if c == 1:
        print("C说的是真话")
        
        b_steal = 1
    if d == 1:
    
        print("D说的是真话")
        
        a_steal = 1
        
    return a_steal,b_steal,c_steal,d_steal

def abcd(a,b,c,d):

    if  a == 1 and b == 0 and c == 0 and d == 0:
    
        print("A: 我没有偷钻石。")
        
        print("B: D不是罪犯")
        
        print("C: B不是盗取钻石的罪犯")
        
        print("D: B没有诬陷我")
        a_true ,b_true ,c_true ,d_true= 0,0,0,0
        return a_true,b_true,c_true,d_true
    if  a == 0 and b == 1 and c == 0 and d == 0:
        print("A: 我偷了钻石。")
        print("B: D就是罪犯")
        print("C: B不是盗取钻石的罪犯")
        print("D: B没有诬陷我")
        a_true,d_true = 1,1
        b_true,c_true = 0,0
        return a_true,b_true,c_true,d_true
    if  a == 0 and b == 0 and c == 1 and d == 0:
        print("A: 我偷了钻石。")
        print("B: D不是罪犯")
        print("C: B是盗取钻石的罪犯")
        print("D: B没有诬陷我")
        a_true,b_true = 1,1
        c_true ,d_true= 0,0
        return a_true,b_true,c_true,d_true
    if  a == 0 and b == 0 and c == 0 and d == 1:
        print("A: 我偷了钻石。")
        print("B: D不是罪犯")
        print("C: B不是盗取钻石的罪犯")
        print("D: B诬陷我")
        a_true,b_true,c_true = 0,0,0
        d_true = 1
        return a_true,b_true,c_true,d_true

def judge():
    a_speek_true,b_speek_true,c_speek_true,d_speek_true = 1,1,1,1

    if a_speek_true == 1:
    
        print("假设A说了真话")
        b_speek_true ,c_speek_true,d_speek_true= 0,0,0
        a,b,c,d=abcd(a_speek_true,b_speek_true,c_speek_true,d_speek_true)
        num = a+b+c+d
        if num ==1:
        
            a_steal, b_steal, c_steal, d_steal = speak(a, b, c, d)
        else:
            print("A说了假话\n")
            b_speek_true ,c_speek_true,d_speek_true= 1,1,1

    if b_speek_true == 1:
    
        print("假设B说了真话")
        a_speek_true,c_speek_true,d_speek_true = 0,0,0
        a,b,c,d=abcd(a_speek_true,b_speek_true,c_speek_true,d_speek_true)
        num = a + b + c + d
        if num == 1:
        
            a_steal, b_steal, c_steal, d_steal = speak(a, b, c, d)
        else:
        
            print("B说了假话\n")
            
            a_speek_true ,c_speek_true,d_speek_true= 1,1,1

    if c_speek_true == 1:
    
        print("假设C说了真话")
        
        b_speek_true ,a_speek_true,d_speek_true= 0,0,0
        
        a,b,c,d=abcd(a_speek_true,b_speek_true,c_speek_true,d_speek_true)
        
        num = a + b + c + d
        if num == 1:
        
            a_steal, b_steal, c_steal, d_steal = speak(a, b, c, d)
        else:
        
            print("C说了假话\n")
            
            b_speek_true,a_speek_true,d_speek_true = 1,1,1

    if d_speek_true == 1:
    
        print("假设D说了真话")
        
        b_speek_true ,c_speek_true,a_speek_true= 0,0,0
        
        a,b,c,d=abcd(a_speek_true,b_speek_true,c_speek_true,d_speek_true)
        num = a + b + c + d
        
        if num == 1:
        
            a_steal,b_steal,c_steal,d_steal = speak(a,b,c,d)
        else:
            print("D说了假话\n")
    if a_steal == 1:
        print("\n\nA偷取了钻石")
    if b_steal == 1:
        print("\n\nB偷取了钻石")
    if c_steal == 1:
        print("\n\nC偷取了钻石")
    if d_steal == 1:
        print("\n\nD偷取了钻石")
print("题目：\nA：我没有偷钻石。\nB：D就是罪犯。\nC：B是盗窃这块钻石的罪犯。\nD：B有意诬陷我。\n假定只有一个人说的是真话\n：\n")
judge()
