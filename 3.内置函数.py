#-*-coding:utf-8-*-
# Author:Lu Wei

# USER_LIST=[]
# for i in range(0,869):
#     data={'name':'luwei%s'%(i,),'psd':'xyz%s'%(i,)}
#     USER_LIST.append(data)
#
# LIST_len=len(USER_LIST)
# PEER_LINE=10
# PAPG_NUM,a=divmod(LIST_len,PEER_LINE)
# if a>0:
#     PAPG_NUM+=1
#
# while True:
#     USER_PAPG=int(input('PAPG NUM：'))
#
#     if USER_PAPG<=0 or USER_PAPG>PAPG_NUM:
#         print('again')
#     else:
#             start_line=(USER_PAPG-1)*10
#             end_line=USER_PAPG*10
#             for i in USER_LIST[start_line:end_line]:
#                 print(i)

# a="0b1001"
# print(int(a,base=2))
#
# # print(type(int(a)))
# print(type(a))
# print(type(oct(a)))
# print(hex(a))
#
# b=0o11
# print(int(b))
#
#
#
# a=10
# print(bin(a))
# print(type(bin(a)))
# print(oct(10))
# print(hex(10))
#
# a=0o12
# print(int(a))#10
# a='0o12'
# print(int(a,base=8))


#1.将ip='192.168.1.2',转化为二进制
# ip_new_list=[]
# ip='192.168.1.2'
# ip_list=ip.split('.')
# for i in ip_list:
#     i_2=bin(int(i))
#     ip_new_list.append(i_2)
#
# ip_0b='.'.join(ip_new_list)
# print(ip_0b)

