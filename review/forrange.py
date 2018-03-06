
for every_letter in 'Hello world':
    print(every_letter)


for num in range(1,11):
    # print('$[num] + 1 = {num+1}')
    # print('{} + 1 = {}'.format(num,num+1))
    print(str(num) + ' + 1 =',num+1)

songslist = ['Holy Diver','Thunderstruck','Rebel Rebel']
for song in songslist:
    if song == 'Holy Diver':
        print(song,'- Dio')
    elif song == 'Thunderstruck':
        print(song,'- AC/DC')
    elif song == 'Rebel Rebel':
        print(song,'- David Bowie')

for i in range(1,10):
    for j in range(1,10):
        print('{} X {} = {}'.format(i,j,i*j))