import os
import time

import requests


class GV:
    def __init__(
            self,
            mode: int = 0
    ):
        self.mode = mode
        self.url = 'https://v.api.aa1.cn/api/api-dy-girl/index.php?aa1=ajdu987hrjfw'
        self.name = ''
        self.path = ''

    def makepath(self):
        if not os.path.exists('./MoYeRanTemp/MobAI/Download/InfiniteTool/GV/GirlVideoGet'):
            os.makedirs('./MoYeRanTemp/MobAI/Download/InfiniteTool/GV/GirlVideoGet')
        self.name = f'temp-{time.time()}.mp4'
        if self.mode == 0:
            self.path = f'./MoYeRanTemp/MobAI/Download/InfiniteTool/GV/GirlVideoGet/{self.name}'
        if self.mode == 1:
            self.path = f'./go-cqhttp/data/videos/{self.name}'

    def get(self):
        try:
            response = requests.get(url=self.url).content
            self.makepath()
            with open(file=self.path, mode='wb') as f:
                f.write(response)
        except:
            return False
        else:
            return True

    def delete(self):
        os.remove(path=self.path)
        if self.mode == 1:
            if os.path.exists(self.path + '.jpg'):
                os.remove(self.path + '.jpg')


if __name__ == '__main__':
    m = GV()
    m.get()
    print(m.path, m.name)
    time.sleep(30)
    m.delete()
