# Модули
import random
import webbrowser
import time
itertime=0
itertime=time.time()
timer = 0

def selector():
    global timer
    print("Режим сложности:")
    print("1: Блять куда я попал")
    print("2: Я уже фурри")
    print("3: Я трап со стажем")
    print("4: Полный пиздец")
    print("0: Выход")
    choice=int(input())
    if choice == 1:
        timer = 30
        #print('1')
        torture()
    elif choice == 2:
        timer = 15
        #print('2')
        torture()
    elif choice == 3:
        timer = 5
        #print('3')
        torture()
    elif choice == 4:
        timer == 0.1
        torture()
    elif choice == 0:
        print("Выхода нет, теперь ты фурри!")
        selector()

def send_images_on_screen(index_picture):
    picture={1: 'https://i.pinimg.com/736x/8f/d4/ad/8fd4ad912881e773e7c8e2919be22361.jpg', 2: 'https://i.pinimg.com/originals/e7/24/d1/e724d1d44d56c41aaece9aa51e24f547.png', 3: 'https://i.pinimg.com/736x/c4/24/fe/c424fe1414cc0de942a01be1717b0125.jpg', 4: 'https://i.pinimg.com/736x/51/24/16/5124169ab0ddfd26854c3fd4db98f0ed.jpg', 5: 'https://i.pinimg.com/originals/33/a7/91/33a791d8ffa13df50126a864b6969dc0.jpg', 6: 'https://i.pinimg.com/originals/91/a0/02/91a002b5d8b31dc4d4305e5cd792663a.jpg', 7: 'https://i.redd.it/ahc7ibq22mb61.png', 8: 'https://i.redd.it/cy58jcex12311.jpg', 9: 'http://images6.fanpop.com/image/photos/41100000/Furry-Wallpap-furries-41145215-2000-1125.png', 10: 'https://i.pinimg.com/originals/0e/15/00/0e1500eeceeec9a04b6fe163a09f7652.jpg', 11: 'https://i.kym-cdn.com/photos/images/facebook/001/113/902/91f.jpg', 12: 'https://cdn.vox-cdn.com/thumbor/EV3IaI6bnxkvRAjXfRCdN0DXuXs=/53x246:1166x1081/2120x1413/filters:focal(53x246:1166x1081)/cdn.vox-cdn.com/uploads/chorus_image/image/44306254/4756098992_5fbae5e9a3_o.0.0.jpg', 13: 'https://get.wallhere.com/photo/furry-Anthro-falvie-1375101.jpg', 14: 'https://i.pinimg.com/originals/3e/32/97/3e3297fca0156af21c4f0f4d45c028d1.jpg', 15: 'http://getwallpapers.com/wallpaper/full/e/f/9/386925.jpg', 16: 'https://i1.wp.com/nypost.com/wp-content/uploads/sites/2/2017/04/170417-alt-furries-internet-feature.jpg?quality=90&strip=all&ssl=1', 17: 'https://i.pinimg.com/originals/d8/1b/5f/d81b5fe35e5771e5703911c324369e14.jpg', 18: 'https://i.pinimg.com/originals/47/a6/63/47a6630b73b1c5b2c9714ea64df278c1.jpg', 19: 'https://pm1.narvii.com/6909/289317b0264a4aed9b351ea8e0687010c77a66c9r1-1600-900v2_hq.jpg', 20: 'https://i.pinimg.com/originals/d8/da/0c/d8da0cbbd745c443123c4662fa5bf1e4.jpg', 21: 'https://i.pinimg.com/originals/3e/c3/87/3ec387ee6cf56f2015d56f1861ec1034.jpg', 22: 'https://i.pinimg.com/originals/66/0e/3a/660e3ac39e1fd4ae90344a6294b9fce6.png', 23: 'http://images6.fanpop.com/image/photos/40900000/Husky-furries-40996425-1269-1269.png', 24: 'https://i.pinimg.com/originals/26/c8/95/26c895b6c8df8d9b040b764fcd23345e.jpg', 25: 'https://i.pinimg.com/736x/8f/d4/ad/8fd4ad912881e773e7c8e2919be22361.jpg', 26: 'https://i.pinimg.com/originals/41/f1/e9/41f1e964dc3ff72b8f76989f3f1353dd.png', 27: 'http://getwallpapers.com/wallpaper/full/5/1/3/1021135-download-free-furry-wallpaper-1920x1080.jpg', 28: 'https://i.pinimg.com/originals/10/ad/19/10ad197f7d615b135187ea990568b27c.jpg', 29: 'https://i.imgflip.com/7f440l.gif', 30: 'https://i.imgflip.com/1oxkz4.jpg', 31: 'https://i.pinimg.com/736x/61/56/8d/61568d030ad715a42f59343c9990f02e.jpg', 32: 'https://cdn.wallpapersafari.com/65/8/YvkhJ3.png', 33: 'https://i.pinimg.com/originals/e7/24/d1/e724d1d44d56c41aaece9aa51e24f547.png', 34: 'https://www.enwallpaper.com/wp-content/uploads/wp5846275.jpg', 35: 'https://i.pinimg.com/originals/5e/5f/f6/5e5ff60e2eb291ccc72dd25ba1b95f00.jpg', 36: 'https://i.pinimg.com/originals/c9/71/12/c97112b341a53cb1ba77cce384688e13.jpg', 37: 'https://anitrendz.net/news/wp-content/uploads/2020/11/Furry.png', 38: 'https://i.pinimg.com/736x/65/ce/c0/65cec0e357976723d22453c205bf90c8.jpg', 39: 'https://i.pinimg.com/736x/58/9d/b8/589db8d6f846bc5b8399a68a08901a62--fursuit-furry-art.jpg', 40: 'https://i.pinimg.com/originals/10/b7/d9/10b7d92bf22e8b2a4e5a7e3ef0d90fe8.jpg', 41: 'https://i.pinimg.com/736x/6e/07/46/6e074640333e7439042a0cfdabfefeac--furry-wolf-furry-art.jpg', 42: 'https://i.pinimg.com/originals/1e/f6/f3/1ef6f391a09022f75b344218cb7baaa1.jpg', 43: 'http://getwallpapers.com/wallpaper/full/a/c/3/451568.jpg', 44: 'https://i.pinimg.com/originals/01/b5/67/01b56716c0573873fa57b8d5e365ea3c.png', 45: 'http://wallpapercave.com/wp/LpX7pXA.jpg', 46: 'https://s-media-cache-ak0.pinimg.com/736x/5b/46/83/5b468337e7392f805c98cc4e62668ab1.jpg', 47: 'https://i.pinimg.com/736x/d6/88/51/d68851954209b6917821bce23b2ed865.jpg', 48: 'https://i.pinimg.com/736x/12/ea/3b/12ea3b65cc2cd91873abdcc55cba035a.jpg', 49: 'https://i.pinimg.com/originals/48/a1/75/48a175f2e1ddba34b90c0e9864675f19.jpg', 50: 'https://i.pinimg.com/originals/48/a1/75/48a175f2e1ddba34b90c0e9864675f19.jpg', 51: 'http://images6.fanpop.com/image/photos/41000000/Paws-furries-41058807-831-1125.png', 52: 'https://i.pinimg.com/736x/0b/62/eb/0b62ebccb873d9d9471d42c0895ba42c--arte-furry-furry-art.jpg', 53: 'https://i.pinimg.com/originals/c0/61/05/c061050870c6bb4d68a6a62cc216d395.jpg', 54: 'https://i.pinimg.com/736x/9d/a3/50/9da35043e1968737a06b7247d4240e03.jpg', 55: 'https://i.pinimg.com/736x/bc/be/35/bcbe35536ef560c7b70bcdcf8c362dd7.jpg', 56: 'http://wallpapercave.com/wp/eE04yca.jpg', 57: 'https://i.pinimg.com/originals/a6/c4/76/a6c476d6000d6b751f661047daf22979.jpg', 58: 'https://i.pinimg.com/originals/3b/21/47/3b21476144015f13005ee7488a338e66.jpg', 59: 'http://getwallpapers.com/wallpaper/full/e/a/4/1021104-furry-wallpaper-2048x1152-iphone.jpg', 60: 'https://i.pinimg.com/originals/ff/b0/e0/ffb0e074861eca156d0ddc71546a4af7.jpg', 61: 'https://i.pinimg.com/736x/bc/33/70/bc337008c357984a065efd674edd8108.jpg', 62: 'https://lgbtqnation-assets.imgix.net/2019/02/furries.jpg?w=790&h=530&fit=crop&auto=format&auto=compress&crop=faces', 63: 'https://i.pinimg.com/originals/97/09/49/9709492b8c9d4253209b986684721c72.jpg', 64: 'https://i.pinimg.com/originals/29/e0/2b/29e02b586bd8d662a096491288d57770.png', 65: 'https://s-media-cache-ak0.pinimg.com/736x/02/1f/46/021f4674f773c1c2b7f6d7f166b95f39.jpg', 66: 'https://i.pinimg.com/736x/3b/37/c0/3b37c09babfad11c39e71c2aeb443bf5.jpg', 67: 'http://wallup.net/wp-content/uploads/2016/04/10/315935-furry-Anthros-Anthro.jpg', 68: 'https://i.pinimg.com/originals/48/d8/85/48d8850eb2db1f9d82f400ee11d771a6.jpg', 69: 'https://i.pinimg.com/originals/97/7c/a1/977ca140baa0a6f8f55efa6d4b66923d.jpg', 70: 'https://i.pinimg.com/originals/a2/d0/21/a2d021143638483fcc5ab354071104a8.jpg', 71: 'https://i.pinimg.com/originals/e2/28/43/e22843e5613509ef502872fda381bca3.jpg', 72: 'https://i.pinimg.com/originals/cc/37/42/cc3742cd4b0d035d87b0b41056053697.jpg', 73: 'https://i.pinimg.com/736x/db/da/91/dbda91ff1e01254f898aa524c33f08a2--furry-art-furries.jpg', 74: 'https://i.pinimg.com/736x/db/51/5e/db515ee68b22b13ddb948a03f455e937.jpg', 75: 'https://i.pinimg.com/736x/a8/e7/ae/a8e7aecb839979a6c7bcf74765321a38.jpg', 76: 'https://i.pinimg.com/originals/0f/e8/55/0fe85510bc3159c341dd34a07449f69c.jpg', 77: 'https://i.pinimg.com/originals/41/b3/72/41b372bba1e356f6361a14beae3f4bbb.png', 78: 'https://i.pinimg.com/originals/f5/48/a4/f548a46c05e6603cf2ffb7c0ce5b7563.jpg', 79: 'https://i.pinimg.com/originals/89/de/b8/89deb856604d8d8eeef3ff8e1bf0a265.jpg', 80: 'https://i.pinimg.com/originals/9d/d1/bd/9dd1bd4fcd74df2ef2aad3e2a8f25490.jpg', 81: 'https://i.pinimg.com/originals/20/7c/14/207c14326c9eeec21beaaed525f62a12.jpg', 82: 'https://images6.fanpop.com/image/photos/39100000/Furry-wolf-live-love-furries-39147906-1060-1506.jpg', 83: 'https://i.pinimg.com/originals/53/28/3c/53283c4fe490d80dad00a6c642cdc87a.jpg', 84: 'https://i.pinimg.com/originals/8d/a0/8e/8da08ea3c93e3f150689132afa66ebc9.png', 85: 'https://i.pinimg.com/originals/ae/dc/d3/aedcd386ec2e3e8f2d38f59ceebdf4fa.jpg', 86: 'https://i.pinimg.com/736x/48/f7/91/48f7914f2a5a214d8e2d94ffa7da34f5.jpg', 87: 'https://i.pinimg.com/736x/0f/d4/ab/0fd4abaa1ce5f6a9b0a06520d3d81191.jpg', 88: 'https://i.pinimg.com/736x/0e/64/d7/0e64d721550baec382f115659075da50--fox-furry-art-male-furry-art.jpg', 89: 'https://i.pinimg.com/736x/8f/b3/07/8fb3070b7d00cd331195a094d3f79f14.jpg', 90: 'https://i.pinimg.com/736x/51/24/16/5124169ab0ddfd26854c3fd4db98f0ed.jpg', 91: 'http://getwallpapers.com/wallpaper/full/f/d/4/1021276-furry-wallpaper-1920x1080-for-4k.jpg', 92: 'https://i.pinimg.com/736x/ba/a4/09/baa409c62eb2a8f722be236f814da547.jpg', 93: 'https://i.pinimg.com/originals/2c/9d/ec/2c9dec49a76ded9b901900c404378b6e.jpg', 94: 'https://i.pinimg.com/originals/b0/13/aa/b013aa1c671f9fb54d7590f7f11a48a8.png', 95: 'https://i.pinimg.com/originals/5b/31/62/5b31626d75fa8a019797435f88658e5a.jpg', 96: 'https://i.pinimg.com/originals/bf/8c/5e/bf8c5ec89342278380a4b625b6c28d3f.jpg', 97: 'https://i.pinimg.com/736x/67/18/64/6718644f56ade3e40476b2eeeb432b2a.jpg', 98: 'https://i.pinimg.com/736x/bf/82/2b/bf822b69de515597e4359ca0b3c59997.jpg', 99: 'https://i.pinimg.com/736x/4d/f1/6f/4df16fc852d101127b31e04afa19f599.jpg', 100: 'https://i.pinimg.com/originals/33/a7/91/33a791d8ffa13df50126a864b6969dc0.jpg'}
    print("Индекс:" + str(index_picture))
    webbrowser.open_new(picture.get(index_picture))

def torture():
    counter=0
    while(counter<60):
        send_images_on_screen(random.randint(1,100))
        time.sleep(timer)
        counter+=timer
    print("Теперь вы трансфурмированны, ищите свой хвост!")





print("|------------------------------------------------|")
print("|               Фурринатор 3000                  |")
print("|                                                |")
print("|     Превращает комп в фурри за ваши деньги!    |")
print("|------------------------------------------------|")
print("(Запустя эту программу, вы согласились стать фурри и присылать в чат всё что появится на экране в течении минуты)")
selector()




