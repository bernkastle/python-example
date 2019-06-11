import subprocess


def run_with_subprocess():
    """
    使用python建立新的线程，并运行bash脚本
    :return:
    """
    bash = 'ps -ef'
    result = subprocess.run(bash, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE,
                            shell=True)

    # 如果result.returncode不是0，则表示脚本运行出错
    if result.returncode is not 0:
        print(f"表执行失败！")
        print(result.stderr.decode('utf-8'))  # 打印错误信息需要解码
    else:
        print(f"执行完成")
        print(result.stdout)
