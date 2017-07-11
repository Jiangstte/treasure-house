#coding= utf-8
from sys import exit
from random import randint

class Scene(object):

    def enter(self):
         print "this scene is not yet configured.subclass it andimplement enter()."
         exit(1)

class Floor(object):
   
    def __init__(self,loucenshu):
        self.loucengshu = loucengshu

    def play(self):
        muqian = self.diantinei()

class Death(Scene):
    quips = [
           "you died.you kinda suck at this.",
           "your mom would be proud...if she were smarter.",
           "such a luser.",
           "I have a small puppy that's better at this."
]

    def enter(self):
        print Death.quips[randint(0,len(self.quips)-1)]
        exit(1)       

class diantinei(Scene):

    def enter(self):
        print "现在，你被困到电梯里面了。"
        print "电梯面板上只有6个楼层可以选择。"
        print "请在1-6楼之间随便选择一个："

        action = raw_input(">")

class yiceng(Floor):
     
    def enter(self):
        
        action = raw_input(">")

        if action == "1":
            print "现在你来到了一楼。"
            print "在你眼前的是一片布满了钉子的地面。"
            print "不过眼尖的你看到了一个角落有两块不起眼的木板。"
            print "那就要看你怎么选择咯？"
            print "1.直接走过去，相信自己adidas名牌鞋的鞋底质量。"
            print "2.宝宝的鞋还是很珍贵的，拿来木板铺在钉子上，然后走过去。"
            print "3.哇，本宝宝对钉子有着天然的恐惧感，还是会电梯吧。"

            action = raw_input(">")

            if action == "1":
                print "adidas的鞋底果然不是盖的。"
                print "刚走了两步鞋底就穿了，你被带毒的钉子扎死了。"
                return 'death'

            elif action == "2":
                print "可以得嘛，，小伙子还是很聪明的就喜欢你这样的。"
                print "可惜你太重了，把木板压断了。。。。。"
                print "一路走好，，来生再见。"
                return 'death'

            else:
                print "嘿，就喜欢你这样啥都怕的人。"
                print "你走进了电梯。。。"
                print "发现四周突然出现了茫茫多钉子，，，"
                print "可爱的你被吓死咯。。。"
                return 'death'

class erceng(Floor):
   
    def enter(self):

	print "你是自己一个人来的吗？"
	print "1.是"
	print "2.不是。"

	action = raw_input(">")

	if action == "1":

            print "你怎么可以这么聪明来到二楼。。真棒，，你距离逃生只有一步之遥，你信吗？"
            print "这是真的，我不骗你。看到脚底的按钮了，，按下他，你就可以逃生了"
            print "再见咯！！！"
            print "算了，再给你个选择，万一你不想离开呢。。。"
            print "1.当然踩下按钮逃生了。。。我又不傻。"
            print "2.算了，我还想玩一玩。我要回去继续选择。"

            action = raw_input(">")
 
            if action == "1":
                print "哎，，你踩下了按钮，，然后远方的门开了。你走了过去。"
                print "啊，你发现门又关了，什么鬼。"
                print "你又走到了按钮上，发现门又开了。。"
                print "是的，你发现你被套路了。。。你自己一个人出不去。"
                return 'erceng'
 
            elif action == "2":
                print "是的，就喜欢你这么有个性的人。。来吧，继续奋斗。"
	        print "给你一个么么哒。"
                return 'diantinei'

            else:
                print "小伙子，你不按套路出牌啊。。"
	        return 'death'
	else:
            print "你怎么可以这么聪明来到二楼。。真棒，，你距离逃生只有一步之遥，你信吗？"
            print "这是真的，我不骗你。看到脚底的按钮了，，按下他，你就可以逃生了"
            print "再见咯！！！"
            print "算了，再给你个选择，万一你不想离开呢。。。"
            print "1.当然踩下按钮逃生了。。。我又不傻。"
            print "2.算了，我还想玩一玩。我要回去继续选择。"

            action = raw_input(">")

            if action == "1":
                print "好吧，你让美女踩在了按钮上，然后大门开了"
                print "你走过了大门，发现了一个木头箱子。"
                print "你搬起来这个木头箱子，将他放在按钮上，带着美女走了过了"
                print "发现原来木头箱子上有个滑梯，你俩上拉手上了滑梯，，成功逃生"
                exit(1)

            elif action == "2":
                print "是的，就喜欢你这么有个性的人。。来吧，继续奋斗。"
                print "给你一个么么哒。"
                return 'diantinei'

            else:
                print "小伙子，你不按套路出牌啊。。"
                return 'death'



class sanceng(Floor):

    def enter(self):

	print "你空着手来的吗?"
	print "1.是."
	print "2.不是。"

	action = raw_input(">")

        if action == "1":
	    print "你看看，映入眼帘的是一片汪洋的游泳池。。。哈哈"
 	    print "哇，你看那是什么。。嗯，金光闪闪的钥匙内。。"
	    print "嗯嗯，是的，又到了选择的时候了；"
	    print "1.我是游泳健将，这个问题对于我来说就是小case，跳下去，游过去。"
	    print "2.嗯，我才不要下去呢，我要继续回去探险去，啦啦啦，气死你。"

            action = raw_input(">")

	    if action == "1":
	        print "你一往无前的跳了下去。向钥匙冲过去。"
	        print "a哎呦喂，你不小心抽筋了，这怎么办呀。。"
	        print "你果断的不知道干什么，然后淹死了。。。"
	        return 'death'

            elif action == "2":
                print "是的，就喜欢你这么有个性的人。。来吧，继续奋斗。"
                print "给你一个么么哒。"
                return 'diantinei'

	else:
            print "你看看，映入眼帘的是一片汪洋的游泳池。。。哈哈"
            print "哇，你看那是什么。。嗯，金光闪闪的钥匙内。。"
            print "嗯嗯，是的，又到了选择的时候了；"
            print "1.我这回可是有皮划艇的，看我游过去。"
            print "2.嗯，我才不要下去呢，我要继续回去探险去，啦啦啦，气死你。"

        action = raw_input(">")

        if action == "1":
            print "你划着皮划艇，到了游泳池的中间。"
            print "然后拿到了金光闪闪的钥匙。"
            print "你有划着皮划艇回到了岸边，然后进了电梯"
            return 'diantinei'

        elif action == "2":
            print "是的，就喜欢你这么有个性的人。。来吧，继续奋斗。"
            print "给你一个么么哒。"
            return 'diantinei'




class siceng(Floor):

    def enter(self):

	print "欢迎来到第四层。你的运气非常的好呀！！！"
	print "这里又一只饥饿的熊看到了你。。"
	print "你本来想跑的，但是自己这么厉害，怎能轻易放弃，于是，于是，"
	print "你挂了。。。"
	return 'death'

class wuceng(Floor):

    def enter(self):

	print "你是空着手来的吗？"
	print "1.是."
	print "2.不是."

	action = raw_input(">")

	if action == "1":

  	    print "这里就是最重要的地方，这里呢，有着你想想不到的东西。"
	    print "在你的不远处，有一只小笼子，算了，大笼子。"
	    print "里面管着一位美女。。"
	    print "你又要做出抉择了:"
	    print "1.你觉得自己的牙很硬，于是动嘴咬了锁。"
	    print "2.你总觉得哪里不对，又走进了楼梯。"
 	    print "3.当然是找钥匙了啊。"

	    action = raw_input(">")

	    if action == "1":
	        print "哎呦喂，你的牙口真好。"
	        print "好吧，那就让你咬断吧，你厉害。"
	        print "你拉着美女的手就要跑。"
	        print "美女'啪'给了你一巴掌。。"
	        print "然后你被扇死了，，哈哈。。"
	        return 'death'

	    elif action == "2":
                print "是的，就喜欢你这么有个性的人。。来吧，继续奋斗。"
                print "给你一个么么哒。"
                return 'diantinei'

	    else:
	        print "那你慢慢找吧，程序猿哥哥要回家吃饭了。。"
	        print "你找了一天，两天，三天，程序猿哥哥没有拯救你，你饿死了。。"
	        return 'death'
	
	else:
            print "这里就是最重要的地方，这里呢，有着你想想不到的东西。"
            print "在你的不远处，有一只小笼子，算了，大笼子。"
            print "里面管着一位美女。。"
            print "你又要做出抉择了:"
            print "1.你觉得自己的牙很硬，于是动嘴咬了锁。"
            print "2.你总觉得哪里不对，又走进了楼梯。"
            print "3.我已经拿到钥匙了。"

            action = raw_input(">")

            if action == "1":
                print "哎呦喂，你的牙口真好。"
                print "好吧，那就让你咬断吧，你厉害。"
                print "你拉着美女的手就要跑。"
                print "美女'啪'给了你一巴掌。。"
                print "然后你被扇死了，，哈哈。。"
                return 'death'

            elif action == "2":
                print "是的，就喜欢你这么有个性的人。。来吧，继续奋斗。"
                print "给你一个么么哒。"
                return 'diantinei'

            else:
                print "你拿着钥匙去把锁打开，成功的营救出了美女"
                print "美女被你的聪明所折服，牵着你的手走进了电梯"
                return 'diantinei'




class liceng(Floor):

    def enter(self):

        print "这里是最轻松的一关，随随便便就过了。"
	print "在这里呢，你需要回答三个问题，看我心情怎么样，来判断答案的对错。"
	print "第一题:"

    def diyiti(self):

	print "你觉得谁长的最帅；"
	print "1,我自己！"
	print "2,还是我自己！"
	print "3.程序员欧巴！"
	print "4.其他！"

	action = raw_input(">")

	if action == "1":
	    print "就喜欢你这自信的样子。过关！"
	    return 'dierti'

        elif action == "2":
            print "就喜欢你这自信的样子。过关！"
            return 'dierti'

	elif action == "3":
	    print "马屁精，，不过我喜欢。。去吧！"
	    return 'dierti'

	else:
	    print "拜拜！"
	    return 'death'

    def dierti(self):

	print "天上有多少颗星星呢？"

	action = int(raw_input(">"))

	if action < "50000":
	    print "喂，老哥。。有点少吧。。。"
	    return 'action'

	else:
	    print "嗯嗯，差不都，那就过关吧。"
	    return 'disanti'

    def disanti(self):

	print "这个游戏好玩吗?"
	print "1.好玩。"
	print "2.不好玩。"

	action = raw_input(">")

	if action == "1":
	    print "嗯嗯，我都觉得不好玩。不成。"
	    return 'death'

	else:
	    print "说实话才对嘛，过关！！！"
	    print "奖励一个皮划艇。。啦啦啦！"
	    return 'loutinei'

class Laolong(object):

    scenes = {
        'diantinei':diantinei(),
        'death':Death(),
        'erceng':erceng(),
        'dierti':dierti(),
        'disanti':desanti(),
    }

    def __init__(self,start_scene):
        self.start_scene = start_scene

    def next_scene(self,scene_name):
        val = laolong.scenes.get(scene_name)
        return val

    def opening_scene(Self):
        return self.next_scene(self.start_scene)

a_louceng = Laolong
a_game = Floor(a_loucen)
a_game.play()
