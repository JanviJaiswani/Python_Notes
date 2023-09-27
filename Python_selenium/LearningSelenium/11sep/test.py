def func(num):
    res={}
    for i in num:
        if i not in res:
            res[i]=1
        else:
            res[i]+=1
    print(res)
    op=[]
    for u,v in res.items():
        if v%2==0:
            op.append(u)
    return op

num = [1,3,0,4,9,8,3,6,4]
print(func(num))

def compress_string(input_str):
    
    compressed = []
    current_char = input_str[0]
    char_count = 0

    for char in input_str:
        if char == current_char:
            char_count += 1
        else:
            compressed.append(current_char)
            if char_count > 1:
                compressed.append(str(char_count))
            current_char = char
            char_count = 1

    compressed.append(current_char)
    if char_count > 1:
        compressed.append(str(char_count))

    return ''.join(compressed)

input_str = "aaaaaaccrrrrr"
compressed_str = compress_string(input_str)
print(compressed_str)  # Output: "a6c2r5"
