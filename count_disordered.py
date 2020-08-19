import os


def load_data():
    count1 = 0
    coutn2 = 0
    count0 = 0
    # after goalnd process \n
    with open((os.path.join('disordered_except_zeoro_list.txt')), 'r') as f:
        data = f.read()
    strlist = data.split('\n')

    for item in strlist[1:]:

        try:
            context = item.split(' #\n')
            context = context[0].split(' ')
            # print(context)
            if context[7] == "5":
                print("有个5", context)
            if context[13] == "#":
                if context[8] == "1":
                    count1 += 1
                elif context[8] == "2":
                    coutn2 += 1
                elif context[8] == "0":
                    count0 += 1
            elif context[18] == "#":
                if context[8] == "1":
                    count1 += 1
                elif context[8] == "2":
                    coutn2 += 1
                elif context[8] == "0":
                    count0 += 1
                if context[13] == "1":
                    count1 += 1
                elif context[13] == "2":
                    coutn2 += 1
                elif context[13] == "0":
                    count0 += 1
            elif context[23] == "#":
                if context[8] == "1":
                    count1 += 1
                elif context[8] == "2":
                    coutn2 += 1
                elif context[8] == "0":
                    count0 += 1
                if context[13] == "1":
                    count1 += 1
                elif context[13] == "2":
                    coutn2 += 1
                elif context[13] == "0":
                    count0 += 1
                if context[18] == "1":
                    count1 += 1
                elif context[18] == "2":
                    coutn2 += 1
                elif context[18] == "0":
                    count0 += 1
            elif context[28] == "#":
                if context[8] == "1":
                    count1 += 1
                elif context[8] == "2":
                    coutn2 += 1
                elif context[8] == "0":
                    count0 += 1
                if context[13] == "1":
                    count1 += 1
                elif context[13] == "2":
                    coutn2 += 1
                elif context[13] == "0":
                    count0 += 1
                if context[18] == "1":
                    count1 += 1
                elif context[18] == "2":
                    coutn2 += 1
                elif context[18] == "0":
                    count0 += 1
                if context[23] == "1":
                    count1 += 1
                elif context[23] == "2":
                    coutn2 += 1
                elif context[23] == "0":
                    count0 += 1

        except:
            pass
    print("count0:", count0, '\n', "count1:", count1, '\n', "count2:", coutn2, '\n')


if __name__ == "__main__":
    load_data()

#1、
# 按规则对0号病例进行筛选后，共得到4192张图 pwd:/mnt/data_space_1/shuang/voc/resultJPEGImages/all；
# 训练集测试集分别为同路径下testdata（1258张），traindata（2934张);其中1、2号病例类型分布算法一致
# 对上述处理结果后的病例数进行统计，数目为
# count0: 10
# count1: 3463
# count2: 1900
# total: 5373
# 其中0号占比约0.186%；1号占比约64.45；2号占比约35.36。
#2、
# 乱序处理后的对照txt文本位于pwd:/home/wly/shuang/disordered_except_zero_list.txt文本中
