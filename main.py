import os
import random
import shutil


def renamePhoto():
    originDir = 'data/origin/test/test'
    nm=1
    filelist=os.listdir(originDir)
    for files in filelist:
        Olddir=os.path.join(originDir,files)
        filename=os.path.splitext(files)[0]
        print("filename:",filename)
        filetype=os.path.splitext(files)[1]
        Newdir=os.path.join(originDir,str(nm)+filetype)
        os.rename(Olddir,Newdir)
        nm+=1



def ReadFileDatas():
    FileNamelist = []
    file = open('except_zeoro_list.txt', 'r+')
    for line in file:
        line = line.strip('\n')  # 删除每一行的\n
        FileNamelist.append(line)
    # print('len ( FileNamelist ) = ', len(FileNamelist))
    file.close()
    return FileNamelist


def WriteDatasToFile(listInfo):
    file_handle = open('disordered_except_zeoro_list.txt', mode='a')
    disorderedIndex = []
    for idx in range(len(listInfo)):
        str = listInfo[idx]
        print("str:", str)
        findNumber = str.find(" ")
        disorderedIndex.append(str[0:findNumber])
        # 查找最后一个 “_”的位置
        ndex = str.rfind('_')
        # print('ndex = ',ndex)
        # 截取字符串
        str_houZhui = str[(ndex + 1):]
        # print('str_houZhui = ',str_houZhui)
        str_Result = str + '\n'  # + str_houZhui+'\n'
        # print("str_Result:",str_Result)
        file_handle.write(str_Result)
    file_handle.close()
    return disorderedIndex


def DisOrderPhoto(disorderedIndex):
    # disorderedIndex = map(int, disorderedIndex)
    path_img = 'data/origin/test/test'
    des_img = 'data/operate/all'

    ls = os.listdir(path_img)
    lenl = len(ls)
    print("lenl:", lenl)

    for index in disorderedIndex:
        print("index:", index)
        shutil.copy(path_img + '/' + index + ".png", des_img + '/' + index + ".png")  # " vs ' !


def TestAndTrain(disorderedIndex):
    allfiles = os.listdir('data/operate/all')  # （图片文件夹）
    num_all = len(allfiles)
    print("num_train: " + str(num_all))
    index_list = list(range(num_all))
    print("index_list: ", index_list)  # [0, 1, 2, 3,
    num = 0
    trainDir = 'data/operate/traindata'  # （将图片文件夹中的7份放在这个文件夹下）
    testDir = 'data/operate/testdata'  # （将图片文件夹中的3份放在这个文件夹下）

    i = 1;
    for index in disorderedIndex:
        if i < num_all * 0.7:
            shutil.copy('data/operate/all' + '/' + index + ".png", trainDir + '/' + index + ".png")
        else:
            shutil.copy('data/operate/all' + '/' + index + ".png", testDir + '/' + index + ".png")
        i = i + 1


if __name__ == "__main__":
    #go处理txt：

    #linux复制文件

    # 对图像文件重命名
    renamePhoto()
    listFileInfo = ReadFileDatas()
    # 打乱列表中的顺序
    random.shuffle(listFileInfo)
    disorderedIndex = WriteDatasToFile(listFileInfo)
    print("disorderedIndex:", disorderedIndex)

    # # # 获取对应乱序下的photo
    # disorderedIndex = ['2', '30', '25', '5', '23', '22', '6', '29', '3', '4', '26', '1', '24', '27', '7', '28']
    DisOrderPhoto(disorderedIndex)

    ##对乱序photo进行3、7分
    TestAndTrain(disorderedIndex)
