import json

import requests


class MoYeRanQQBindGet:
    def __init__(
            self,
            qq=None
    ):
        qq = str(qq)
        self.ret = '错误'
        if qq is not None:
            if qq.isdigit():
                self.qq = qq
                self.get()
            else:
                self.ret = '输入非数字'
        else:
            self.ret = '无输入'

    def get(self):
        try:
            data = json.loads(requests.get(f'https://zy.xywlapi.cc/qqapi?qq={self.qq}').text)
            if data['message'] == '查询成功':
                self.ret = f"查询成功！{data['qq']}手机号绑定为{data['phone']}，地区为{data['phonediqu']}。"
            elif data['message'] == '输入参数类型错误':
                self.ret = '输入不规范'
            else:
                self.ret = '查询失败'
        except:
            self.ret = '查询异常'


if __name__ == "__main__":
    import termcolor

    print(termcolor.colored(MoYeRanQQBindGet(3228993382).ret, 'red', None, ['bold']))
