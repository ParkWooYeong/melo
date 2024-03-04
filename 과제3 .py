# ----- 코드 정의 ------
class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def display(self):
        print(f'name: {self.name}')
        print(f'Username: {self.username}')

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

members = []
members0 = Member('Pikachu', 'Pikachu1', 'Pikachu123' )
members1 = Member('Pororo', 'Pororo1', 'Pororo321' )
members2 = Member('Doge', 'Doge1', 'Doge231' )

print('members:')
for member in members:
    member.display()


posts = []

for member in members:
    for i in range(3):
        posts_tittle = f'{member.name}{i+1}'
        posts_content = f'{member.content}{i+1}'
        post = Post(posts_tittle, posts_content, member.username)
        posts.append(post)

특정_유저 = 'Help'


print("특정 유저 게시글")
for member in members:
    print(f'{member.name}')
    for post in posts:
        if post.author == 특정_유저:
            members.append(members0)
            print(post.title)

특정_단어 = 'Wellcome'

print('특정 단어 게시글 제목')
for post in posts:
    if 특정_단어.lower() in post.title.lower():
        print(f'post.title')
