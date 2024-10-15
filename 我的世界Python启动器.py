import subprocess
import sys
# 下面的路径增加或减少都行把路径改了
python_1_8_path = r"C:\Users\mcyan\Desktop\启动 kk.bat"
python_1_18_2_path = r"D:\桌面\Python我的世界启动器\Python1.18.2.bat"
python_1_12_2_path = r"D:\桌面\Python我的世界启动器\Python1.12.2.bat"
python_1_20_2_path = r"D:\桌面\Python我的世界启动器\Python1.20.2.bat"
minecraft_versions_path = r"D:\桌面\游戏\.minecraft\versions"
# 这里是自定义变量自己改，像是1.20.6就改成
# def open_python_1_20_6():
# subprocess.run([python_1_20_2_path])
def open_python_1_8():
    subprocess.run([python_1_8_path])

def open_python_1_18_2():
    subprocess.run([python_1_18_2_path])

def open_python_1_12_2():
    subprocess.run([python_1_12_2_path])

def open_python_1_20_2():
    subprocess.run([python_1_20_2_path])

def open_minecraft_versions():
    subprocess.run(["explorer", minecraft_versions_path])  # 使用 explorer 打开文件夹
#选项可减少可增加
def main(看来出了点问题=None):
    print("请选择要打开的版本:")
    print("1. Python 1.8")
    print("2. Python 1.18.2")
    print("3. python 1.12.2")
    print("4. python 1.20.2")
    print("quit.离开")
    print("6. 打开 Minecraft 版本文件夹")

    while True:
        choice = input("输入选项的数字编号: ")
# 判断并执行可减少可增加
        if choice == '1':
            open_python_1_8()
            break
        elif choice == '2':
            open_python_1_18_2()
            break
        elif choice == '3':
            open_python_1_12_2()
            break
        elif choice == '4':
            open_python_1_20_2()
            break
        elif choice == '6':
            open_minecraft_versions()
            break
        elif choice == '114514':
            sentence = "好臭啊,呃呃呃呃呃啊啊啊啊啊啊啊啊啊啊啊啊！"
            while True:
                for char in sentence:
                    print(char, end='')  # 使用 end='' 避免在每个字符后换行
                print()  # 打印完一遍句子后换行
                break
        elif choice == 'PCL':
            print("那是我的兄弟o(〃＾▽＾〃)o")
            break
        elif choice == 'HMCL' :
            print("那是我的堂哥\( ° ▽ ° )/ ")
            break
        elif choice == 'hmcl' :
            print("那是我的堂哥\( ° ▽ ° )/ ")
            break
        elif choice == 'pcl':
            print("那是我的兄弟o(〃＾▽＾〃)o")
            break
        elif choice == 'quit':
            # 正常退出，退出代码为0
            sys.exit(-114514)

        else:
            print("无效的选项，请输入 '1' , '2' , '3' , '4' , '5' .")

if __name__ == "__main__":
    main()
