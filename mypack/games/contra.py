#contra.py


def play():
    print("正在玩contra")

print("contra模块被加载")


def gameover():
    #from mypack.menu import show_menu 绝对调用
    #相对调用目录
    from ..menu import show_menu
    show_menu()


    #相对调用tanks游戏play
    #from mypack.games.tanks import play
    #from .tanks import play
    from ..games.tanks import play
    #from ...mypack.games.tanks import play #超出路径了
    
    play()