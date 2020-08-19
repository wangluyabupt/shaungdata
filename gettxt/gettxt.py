import os


def load_data():
    # after goalnd process \n
    with open((os.path.join('simple_list.txt')), 'r') as f:
        data = f.read()
    strlist = data.split('\n')

    for item in strlist[1:]:

        try:
            context = item.split(' #\n')
            # print("each context:",context[0],type(context[0]))
            context = context[0].split(' ')
            # print(context)
            deal_each_str(context)

        except:
            pass


def deal_each_str(context):
    zero_count=0
    f_zero = open('zero.txt', 'a+')
    f_except_zero = open('except_zero.txt', 'a+')
    if context[8 + 5] == "#":
        if context[8] == "0":
            str1 = ' '.join(context)+'\n'
            # print(str1)
            f_zero.write(str(str1))
        else:
            # print(str(context))
            str1 = ' '.join(context) + '\n'
            f_except_zero.write(str1)
    else:
        if context[8 + 5] != "#" and context[8 + 5 + 5] != "#":  # 3
            if context[8] == "0":
                zero_count = zero_count + 1
                context = context[:8] + context[13:]
                if context[8] == "0":
                    zero_count = zero_count + 1
                    context = context[:8] + context[13:]
                    if context[8] == "0":
                        zero_count = zero_count + 1
                        context = context[:8] + context[13:]
                else:
                    if context[13] == "0":
                        zero_count = zero_count + 1
                        context = context[:13] + context[18:]
                    if context[13] == "0":
                        zero_count = zero_count + 1
                        context = context[:13] + context[18:]
            elif context[13]=="0":
                zero_count = zero_count + 1
                context = context[:13] + context[18:]
                if context[13] == "0":
                    zero_count = zero_count + 1
                    context = context[:13] + context[18:]
            elif context[18]=="0":
                zero_count = zero_count + 1
                context = context[:18] + context[23:]

            if zero_count==3:
                str1 = ' '.join(context) + '\n'
                # print(str1)
                f_zero.write(str(str1))
            elif zero_count==2:
                context[7]="1"
                # print(str(context))
                str1 = ' '.join(context) + '\n'
                f_except_zero.write(str1)
            elif zero_count==1:
                context[7]="2"
                # print(str(context))
                str1 = ' '.join(context) + '\n'
                f_except_zero.write(str1)
            elif zero_count==0:
                # print(str(context))
                str1 = ' '.join(context) + '\n'
                f_except_zero.write(str1)


        else:
            if context[8+5] != "#" and  context[8+5+5] == "#" : #2
                one = context[8]
                two = context[8+5]
                if one=="0"  and two=="0":
                    str1 = ' '.join(context) + '\n'
                    # print(str1)
                    f_zero.write(str(str1))
                elif one == "0" and two != "0":
                    context[7] = "1"
                    context =context[:8]+context[13:]
                    # print(str(context))
                    str1 = ' '.join(context) + '\n'
                    f_except_zero.write(str1)
                elif one != "0" and two == "0":
                    context[7] = "1"
                    context =context[:13]+context[18:]
                    # print(str(context))
                    str1 = ' '.join(context) + '\n'
                    f_except_zero.write(str1)
                else:
                    # print(str(context))
                    str1 = ' '.join(context) + '\n'
                    f_except_zero.write(str1)


    f_zero.close()
    f_except_zero.close()



if __name__ == "__main__":
    load_data()
    #输出copy
    #4、5量级
    #输出'str'list


