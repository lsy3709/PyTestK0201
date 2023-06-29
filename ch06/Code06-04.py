with open("C:/CookAnalysis/CSV/singer1.csv", "r") as inFp :
    with open("C:/CookAnalysis/CSV/new_singer1_0628.csv", "w") as outFp:
        header = inFp.readline()
        header = header.strip()
        header_list = header.split(',')
        header_str = ','.join(map(str, header_list))
        outFp.write(header_str + '\n')
        #헤더를 제외한 2번째행 부터 데이터
        for inStr in inFp:
            inStr = inStr.strip()
            row_list = inStr.split(',')
            # -1 , 해당 리스트의 마지막 요소.
            row_list[-1] = row_list[-1].replace('.', '/')
            height_str = "{0:.2f}".format(int(row_list[-2]))
            row_list[-2] = height_str
            row_str = ','.join(map(str, row_list))
            outFp.write(row_str + '\n')

print('Save. OK~')