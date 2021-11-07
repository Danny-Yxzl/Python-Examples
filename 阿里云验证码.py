#coding=utf-8
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
client = AcsClient('LTAI4GKDNA17S9eFTiDvdPVp', 'd91aThRARoGjXs9iULgMnIQjFLVhAQ', 'cn-hangzhou')

def sending(phonenumber,name):
    templateparam='{"name":"'+name+'"}'
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('dysmsapi.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https') # https | http
    request.set_version('2017-05-25')
    request.set_action_name('SendSms')
    request.add_query_param('RegionId', "cn-hangzhou")
    request.add_query_param('PhoneNumbers', int(phonenumber))
    request.add_query_param('SignName', "异想之旅")
    request.add_query_param('TemplateCode', "SMS_207970004")
    request.add_query_param('TemplateParam', templateparam)
    response = client.do_action(request)
    print(str(response,encoding='utf-8'),end='')

f=open("D:/Desktop/md.txt",'r',encoding='utf-8')
text=f.read()
f.close()
text=text.split('\n')
for i in range(len(text)):
    text[i]=text[i].split('\t')
print(text)

for i in range(1,len(text)):
    sending(int(text[i][1]), text[i][0])
    print("成功发送第%d条短信给%s，手机号码为%d"%(i,text[i][0],int(text[i][1])))