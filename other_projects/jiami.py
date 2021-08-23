# _*_ coding: UTF-8 _*_
# @Time : 2021/6/25 16:52
# @Author : caoyujie
# @Site : 
# @File : jiemi.py
# @Software : PyCharm

from hashlib import sha1
import hashlib
def get_md5(str1):
    get_object=hashlib.md5()
    get_object.update(str1.encode("utf-8"))
    get_md5_result=get_object.hexdigest()
    # get_md5_result=get_md5_result.upper()
    return get_md5_result


if __name__ == '__main__':
    print(get_md5('admin'))



# def jia_mi(str):
#     sh = sha1()
#     sh.update(str.encode())
#     return sh.hexdigest()
#
# if __name__ == "__main__":
#     pwd = jia_mi("admin")
#     print(pwd)

