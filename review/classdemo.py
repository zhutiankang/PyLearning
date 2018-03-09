ln_path = 'last_name.txt'
fn_path = 'first_name.txt'
fn = []
ln1 = []  # 单字名
ln2 = []  # 双字名

with open(fn_path, 'r', encoding='utf-8') as f:
    for line in f.readlines():
        fn.append(line.split('\n')[0])

with open(ln_path, 'r', encoding='utf-8') as f:
    for line in f.readlines():
        if len(line.split('\n')[0]) == 1:
            ln1.append(line.split('\n')[0])
        else:
            ln2.append(line.split('\n')[0])

# 元组比列表更节省内存
fn = tuple(fn)
ln1 = tuple(ln1)
ln2 = tuple(ln2)
print(fn)
print(ln1)
print('=' * 50)
print(ln2)
'''
import random
class FakeUser:
    def fake_name(self,one_word=False,two_words=False):
        if one_word:
            full_name = random.choice(fn) + random.choice(ln1)
        elif two_words:
            full_name = random.choice(fn) + random.choice(ln2)
        else:
            full_name = random.choice(fn) + random.choice(ln1+ln2)
        print(full_name)

    def fake_gender(self):
        gender = random.choice(['男','女','其他'])
        print(gender)

class SnsUser(FakeUser):
    def get_followers(self,few=True,a_lot=False):
        if few:
            followers = random.randrange(1,50)
        elif a_lot:
            followers = random.randrange(200,10000)
        print(followers)

user_a = FakeUser()
user_b = SnsUser()
user_a.fake_name()
user_a.fake_gender()
user_b.get_followers(few=True)
'''
# 使用生成器 yield，在任意一种循环中使用yield返回结果，就可以得到类似于生成函数range的效果
# yield会把每次循环得出的结果存到generator生成器中，最后循环结束，可迭代取出
import random


class FakeUser:
    def fake_name(self, amount=1, one_word=False, two_words=False):
        n = 0
        while n <= amount:
            if one_word:
                full_name = random.choice(fn) + random.choice(ln1)
            elif two_words:
                full_name = random.choice(fn) + random.choice(ln2)
            else:
                full_name = random.choice(fn) + random.choice(ln1 + ln2)
            # print(full_name)
            yield full_name
            n += 1

    def fake_gender(self, amount=1):
        n = 0
        while n <= amount:
            gender = random.choice(['男', '女', '其他'])
            # print(gender)
            yield gender
            n += 1


class SnsUser(FakeUser):
    def get_followers(self, amount=1,few=True, a_lot=False):
        n = 0
        while n <= amount:
            if few:
                followers = random.randrange(1, 50)
            elif a_lot:
                followers = random.randrange(200, 10000);
            # print(followers)
            yield followers
            n += 1

user_a = FakeUser()
user_b = SnsUser()
print(type(user_a.fake_name(3)))
for name in user_a.fake_name(3):
    print(name)

for gender in user_a.fake_gender(3):
    print(gender)

for follower in user_b.get_followers(3):
    print(follower)
