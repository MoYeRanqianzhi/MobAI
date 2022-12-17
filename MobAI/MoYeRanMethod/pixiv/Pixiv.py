import json

import requests


class PV:
    def __init__(
            self,
            r18: int = 0,
            size: str = 'thumb'
    ):
        """
        Parameters:

            r18(int):
                0 or 1
            size(Str):
                size must be str and in ['original','regular','small','thumb','mini']
        """

        try:
            self.r18 = r18
            self.size = size
            self.num = 1
            self.uid = None
            self.keyword = ''
            self.tag = []
            # self.proxy = 'i.pixiv.re'
            self.proxy = None
            self.dateAfter = None
            self.dateBefore = None
            # self.dsc = False
            self.dsc = None
            self.post_data = {}
            self.response = ''
            self.response_json = ''
            self.author = ''
            self.title = ''
        except Exception as e:
            raise e

    def clean(self):
        self.num = 1
        self.uid = None
        self.keyword = ''
        self.tag = []
        # self.proxy = 'i.pixiv.re'
        self.proxy = None
        self.dateAfter = None
        self.dateBefore = None
        # self.dsc = False
        self.dsc = None
        self.post_data = {}
        self.response = ''
        self.response_json = ''
        self.author = ''
        self.title = ''

    def get(
            self,
            tag=None
    ):
        try:
            if tag is not None and tag != '':
                self.tag_process(tag)
                self.post_data = {
                    'r18': self.r18,
                    'tag': self.tag,
                    'size': self.size
                }
            else:
                self.post_data = {
                    'r18': self.r18,
                    'size': self.size
                }
                print(self.post_data)
            self.response = requests.post(url='https://api.lolicon.app/setu/v2', json=self.post_data)
            self.response_json = json.loads(self.response.text)
            print(self.response_json)
            if self.response_json['error'] == '':
                return {
                    'title': self.response_json['data'][0]['title'],
                    'author': self.response_json['data'][0]['author'],
                    'url': self.response_json['data'][0]['urls'][self.size]
                }
        except:
            return False

    def tag_process(
            self,
            tag: str
    ):
        for i in tag.split('和'):
            self.tag.append(i.split('或'))


if __name__ == '__main__':
    m = PV(0, 'small')
    print(m.get('萝莉或小学生和白丝'))
