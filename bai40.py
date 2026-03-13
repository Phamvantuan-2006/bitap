for dung in range(21):      # trâu đứng
    for nam in range(34):   # trâu nằm
        
        gia = 100 - dung - nam
        
        if 5*dung + 3*nam + gia/3 == 100:
            print((dung,nam,gia))
