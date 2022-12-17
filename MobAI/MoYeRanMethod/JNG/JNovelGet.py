import requests
from lxml import etree
import urllib.parse
import time
import os

class MoYeRanError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

    __module__ = 'builtins'


class JN:

    def __init__(
            self,
            word: str = None
    ):
        """
        Parameters:

            word(str):
                关键词，如'全球高考' or '木苏里的全球高考' or '木苏里的《全球高考》'
        """
        self.word = word
        self.words = []
        self.found = {
            'names': [

            ],
            'authors': [

            ],
            'urls': [

            ]
        }
        self.error = '未知错误'
        self.message = ''
        self.url = ''
        self.info = {
            'name': '',
            'author': '',
            'introduction': '',
        }
        self.response = None
        self.tree = None
        self.if_title_sorted = None
        self.name = ''
        self.path = ''


    def clean(self):
        self.words = []
        self.found = {
            'names': [

            ],
            'authors': [

            ],
            'urls': [

            ]
        }
        self.error = '未知错误'
        self.message = ''
        self.url = ''
        self.info = {
            'name': '',
            'author': '',
            'introduction': '',
        }
        self.response = None
        self.tree = None
        self.if_title_sorted = None
        self.name = ''
        self.path = ''


    def convert_message(self):
        for i in range(len(self.found['urls'])):
            self.message = self.message + f"\n{i + 1} {self.found['names'][i]}-{self.found['authors'][i]}"
        self.message = self.message + f"\n----共{len(self.found['urls'])}项搜索结果----"
        return self.message


    def check(self):
        try:
            if self.words[-1]:
                return True
            else:
                self.error = '输入的格式错误'
                return False
        except:
            self.error = '未知错误'
            return False

    def process(self):
        self.word = self.word.replace('《', '').replace('》', '')
        self.words = self.word.split('的')

    def search(self):
        try:
            self.process()
            page = 0
            con = True
            while con:
                if page >= 100:
                    break
                page = page + 1
                res = etree.HTML(
                    requests.get(
                        f"http://www.jjwxc.net/search.php?kw={urllib.parse.quote(self.words[-1].encode('gbk'))}&t=1&p={page}&ord=novelscore"
                    ).content.decode(
                        'GB18030', 'ignore'
                    ).encode(
                        'utf-8', 'ignore'
                    ).decode(
                        'utf-8'
                    )
                )

                for i in range(2, 27):
                    if res.xpath(f"//*[@id='search_result']//div[{i}]/h3/a//text()"):
                        self.found['names'].append(
                            "".join(res.xpath(
                                f"//*[@id='search_result']//div[{i}]/h3/a//text()"
                            )
                            ).replace(
                                " ", ""
                            ).replace(
                                "\n", ""
                            ).replace(
                                "\r", ""
                            )
                        )
                        self.found['authors'].append(
                            "".join(
                                res.xpath(
                                    f"//*[@id='search_result']//div[{i}]/div[2]/a/span/text()"
                                )
                            ).replace(
                                " ", ""
                            ).replace(
                                "\n", ""
                            ).replace(
                                "\r", ""
                            )
                        )
                        self.found['urls'].append(
                            "".join(
                                res.xpath(
                                    f"//*[@id='search_result']//div[{i}]/h3/a/@href")).replace(
                                " ", ""
                            ).replace(
                                "\n", ""
                            ).replace(
                                "\r", ""
                            )
                        )
                    else:
                        con = False
            if len(self.found['names']) == len(self.found['authors']) == len(self.found['urls']):
                if len(self.words) == 2:
                    found_temp = {
                        'names': [

                        ],
                        'authors': [

                        ],
                        'urls': [

                        ]
                    }
                    for i in range(len(self.found['names'])):
                        if self.words[0] in self.found['authors'][i]:
                            found_temp['names'].append(self.found['names'][i])
                            found_temp['authors'].append(self.found['authors'][i])
                            found_temp['urls'].append(self.found['urls'][i])
                    self.found = found_temp
                    return True
                elif len(self.words) >= 3:
                    self.error = '搜索格式错误'
                    return False
                else:
                    return True
            else:
                self.error = '服务器在搜索过程中出错'
                return False
        except:
            self.error = '未知错误'
            return False

    def url_index(
            self,
            index: int
    ):
        """
        parameters:

            index(int):
                index must be a int in self.found
        """
        try:
            if index in range(1,len(self.found['urls'])+1):
                self.url = self.found['urls'][index-1]
                return True
            else:
                self.error = '输入的序号错误'
                return False
        except:
            self.error = '未知错误'
            return False

    def get_info(self):
        """get info of name, author and introduction"""

        self.info.update(
            {
                'name': self.tree.xpath(
                    "//*[@id='oneboolt']/tbody/tr[1]/td/div/span/h1/span/text()"
                )[0]
            }
        )
        self.info.update(
            {
                'author': self.tree.xpath(
                    "//*[@id='oneboolt']/tbody/tr[1]/td/div/h2/a/span/text()"
                )[0]
            }
        )
        self.info.update(
            {
                'introduction': self.upper_format(
                    self.tree.xpath(
                        "//div[@id='novelintro']/text()"
                    )
                )
            }
        )

    def get_chapter_urls(self):
        """获取所有为被锁和非VIP章节的url"""
        self.chapter_urls = self.tree.xpath(
            "//*[@id='oneboolt']/tbody/tr/td[2]/span/div[1]/a/@href"
        )

    def prepare(self):
        """prepare for download"""
        try:
            self.response = requests.get(self.url)
            self.response.encoding = 'gb18030'
            self.tree = etree.HTML(self.response.text)
        except:
            self.error = '下载准备错误'
            return False
        else:
            return True

    def save(
            self,
            path: str = None
    ):
        """下载并存储小说"""
        if path is None:
            path = f'./MoYeRanTemp/MobAI/Download/InfiniteTool/JN/JNovelGet/'
        path = path + f"{time.time()}/{self.info['name']}-{self.info['author']}"
        if not os.path.exists(path):
            os.makedirs(path)
        self.name = f"{self.info['name']}-{self.info['author']}.txt"
        self.path = path + f"/{self.name}"
        try:
            self.get_chapter_urls()
            self.if_title()
            book = open(self.path, 'w', encoding='utf-8')

            info = f"书名：{self.info['name']}\n作者：{self.info['author']}\n介绍：\n{self.info['introduction']}\n\n"
            book.write(info)
            if self.if_title_sorted:
                for url in self.chapter_urls:
                    output = self.download(url)
                    text = (output['title'] + '\n\n' + output['content'] + '\n\n' + output['words'])
                    text += '\n\n\n'
                    book.write(text)
            else:
                i = 1
                for url in self.chapter_urls:
                    output = self.download(url)
                    text = ('第' + str(i) + '章 ' + output['title'] + '\n\n' + output['content'] + '\n\n' + output['words'])
                    text += '\n\n\n'
                    i += 1
                    book.write(text)
        except:
            self.error = '未知错误'
            return False
        else:
            return True

    def if_title(self):
        """判断标题是否是第xxx章的形式"""

        url = self.chapter_urls[0]
        test = self.download(url)
        if ('第' in test['title'] and '章' in test['title']) or ('第' in test['title'] and '篇' in test['title']):
            self.if_title_sorted = 1
        else:
            self.if_title_sorted = 0

    def download(self, url):
        """获取一章的标题，内容，作者有话要说"""
        output = {
            'title': '',
            'content': '',
            'words': '',
        }
        chapter = requests.get(url)
        chapter.encoding = 'gb18030'
        chapter_element = etree.HTML(chapter.text)
        title = self.lower_format(
            chapter_element.xpath(
                "//*[@id='oneboolt']/tr[2]/td[1]/div/div[2]/h2/text()"
            )[0]
        )
        output['title'] = title
        content = chapter_element.xpath("//*[@id='oneboolt']/tr[2]/td[1]/div/text()")
        content = self.upper_format(content)
        output['content'] = content

        words = chapter_element.xpath(
            "//*[@id='oneboolt']/tr[2]/td[1]/div/div[@class='readsmall']/text()"
        )
        words = self.upper_format(words)
        output['words'] = words

        return output

    @staticmethod
    def upper_format(unformated_contents):
        """将数组中的字符串格式化，并返回字符串。返回的字符串有段首缩进"""
        formated_contents = ''
        for unformated_content in unformated_contents:
            text = unformated_content.strip()
            if text != '':
                formated_contents = formated_contents + '\u3000\u3000' + text + '\n'
        return formated_contents

    @staticmethod
    def lower_format(unformated_content):
        """将传入字符串格式化，返回无段首缩进的字符串"""
        return unformated_content.strip()


if __name__ == '__main__':
    a=JN('全球高考')
    print(a.search())
    print(a.error)
    print(a.found)
    print(a.convert_message())
    print(a.found['urls'][0])
    a.url_index(1)
    a.prepare()
    a.get_info()
    print(a.info['introduction'])
    a.get_chapter_urls()
    a.save()
