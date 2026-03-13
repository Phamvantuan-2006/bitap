import itertools

ops = ['+','-','*','/']

for o in itertools.product(ops, repeat=5):

    exp = f"((((1{o[0]}2){o[1]}3){o[2]}4){o[3]}5){o[4]}6"
    
    try:
        if eval(exp) == 36:
            print(exp,"= 36")
    except:
        pass
