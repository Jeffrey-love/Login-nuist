def create_data():
    phone = input('账号:')
    password = input('密码:')
    option = 0
    while option != '1' and option != '2' and option != '3':
        option = input('运营商[1.移动,2.电信,3.联通]:')
    if option == '1':
        oper = '中国移动'
    elif option == '2':
        oper = '中国电信'
    else:
        oper = '中国联通'
    data = '[data]\nphone =' + phone + '\npassword =' + password + '\noperator =' + oper
    try:
        with open('data.conf', 'w+') as f:
            f.write(data)
            print('文件data.conf创建成功......')
    except Exception as e:
        print(e)


def create_vbs():
    # 获取当前文件的路径，包括文件名
    filepath = __file__
    filepath = filepath[:-8]
    disk = filepath[0]
    shell = 'Set Shell=CreateObject("Shell.Application")\nShell.ShellExecute "cmd.exe","/k ' \
            + disk + ':&&cd ' + filepath + '&&python nuist-auto-login.py&&timeout /T 2&&exit","' \
            + filepath + '", "runas", 1'
    try:
        with open('auto-login.vbs', 'w+') as f:
            f.write(shell)
            print('文件auto-login.vbs创建成功')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    create_data()
    create_vbs()
