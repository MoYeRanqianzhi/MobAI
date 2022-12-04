import base64
import os
import time
import threading
import requests
from ttkbootstrap import *
from ttkbootstrap.dialogs import *

url = 'http://127.0.0.1:5701'


def save(key):
    post_data = {'post_type': 'local',
                 'local_type': 'operation',
                 'operation': 'save',
                 'time': int(time.time()),
                 'self_id': 2171956482}
    requests.post(url=url, json=post_data)


def power_off():
    post_data = {'post_type': 'local',
                 'local_type': 'operation',
                 'operation': 'power off',
                 'time': int(time.time()),
                 'self_id': 2171956482}
    requests.post(url=url, json=post_data)



if not os.path.exists('./appData/Temp/MoYeRanSoft/SoftWareTemp/myr/save/resource/save.myr'):
    if not os.path.exists('./appData/Temp/MoYeRanSoft/SoftWareTemp/myr/save/resource'):
        os.makedirs('./appData/Temp/MoYeRanSoft/SoftWareTemp/myr/save/resource')
    with open('./appData/Temp/MoYeRanSoft/SoftWareTemp/myr/save/resource/save.myr', 'wb') as f:
        f.write(base64.b64decode(
            b'iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAAAXNSR0IArs4c6QAAAARzQklUCAgICHwIZIgAAAKYSURBVHic7ZmxTsMwEIYvkSJEpb5BJUaQeAMGdp6iT9C1I+IJkEBsPAIbAywMXRhZEIJ26MDIQIcOVIKCGUqIU/vsc4P4JbhfipTYd/Z3fxwnhcwQGfrHytEAaKkBaAC01AA0AFpqABoALTUADYCWGoAGQEsNQAOgpQagAdBSA9AAaKkBaAC01AA0AFpqABoALb8Bt7dExriHVPf3bu7zc3Pacqzr63Bcryfmz5x/jMQKzbI4ZEizGVGr5bZPp0Ttdnj84ZBoczPMIrlRVl59BUiSQzGS/PV1N86YRfFERK+vfO7WFt93cSFfpVYcvwfM5wunfEdk0G+dnsZXzLKKIi2eiGg0Itrbc9sF3PVHwC4iBXy5eKlJdlyeE72/L85brcWjEhujzG8w/8+/BeZzWdzVVf3646M6f3nx59gFlCvl/LweIy3+5uar3d4nl9Xp+PZSE8yRxm5shPtj+dL5j47cGCuubsDTUzA4CjWd8nF3d6sVWB7jcdU3mfAGHB76a2DGJmeiovAnvb2lQ6euFFu9nmyeFK2tOXO6BpTHwYF/kN8ywI55fKzazs6q9u1tWeEBLt4ADur4uOrb35dNJIW6vPTHhPJ8KopwTdbhfglKdtCmrx9pbJbF55AyMMq/B/FBrjhoTaFxU3ObcDBjyz6Fufbd3fr1w0N1fnLSrPhlSb8QJxO+b2fHvdnsc9TtGjMYxJ/fJmq6Z8QYuI3cGpOSC+n3VzMgpTBJTNOb4GyC0uW6yk9QOyd14+R+PqcyMHPmtcbQJjOb8f1crq/dvg7NV/ZJig8xlOr3vTGy1+Aflv5NEA2AlhqABkBLDUADoKUGoAHQUgPQAGipAWgAtNQANABaagAaAC01AA2AlhqABkDr3xvwCXcT9gghog+2AAAAAElFTkSuQmCC'))
root = Window()
root.title('MoYeRanGUI')
root.geometry('400x225')
root.resizable(False, False)
root.overrideredirect(1)
root.wm_attributes('-topmost', 1)
style = Style()
style.theme_use('darkly')

var_x = IntVar()
var_y = IntVar()
# region 菜单
menubar = Menu(root
               )
File_menu = Menu(menubar)
Edit_menu = Menu(menubar)
Check_menu = Menu(menubar)
Order_menu = Menu(menubar)
Auto_menu = Menu(menubar)
Help_menu = Menu(menubar)
#region 文件

# region 账户
class AccountOperate:
    def main():
        account_window = Toplevel(title='文件(F)>账户(A)'
                                  )
        account_window.geometry('500x300'
                                )
        account_window.resizable(False
                                 ,
                                 False
                                 )
        account_window.iconbitmap()
        label_zhi_zun = Label(account_window
                              ,
                              text='至尊特供版无需登录以及许可证'
                              )
        label_zhi_zun.pack()


File_menu.add_command(label='账户(A)'
                      ,
                      command=AccountOperate.main
                      )
# endregion

# region 设置
Setting_submenu = Menu(File_menu)
# region 个性化
Personalise_submenu = Menu(Setting_submenu)
# region 主题
Theme_submenu = Menu(Personalise_submenu)


# region主题变换操作
def be_cosmo():
    style.theme_use('cosmo')


def be_flatly():
    style.theme_use('flatly')


def be_litera():
    style.theme_use('litera')


def be_minty():
    style.theme_use('minty')


def be_lumen():
    style.theme_use('lumen')


def be_sandstone():
    style.theme_use('sandstone')


def be_yeti():
    style.theme_use('yeti')


def be_pulse():
    style.theme_use('pulse')


def be_united():
    style.theme_use('united')


def be_morph():
    style.theme_use('morph')


def be_journal():
    style.theme_use('journal')


def be_darkly():
    style.theme_use('darkly')


def be_superhero():
    style.theme_use('superhero')


def be_solar():
    style.theme_use('solar')


def be_cyborg():
    style.theme_use('cyborg')


def be_vapor():
    style.theme_use('vapor')


def be_simplex():
    style.theme_use('simplex')


def be_cerculean():
    style.theme_use('cerculean')


# endregion
Theme_submenu.add_command(label='cosmo'
                          ,
                          command=be_cosmo
                          )

Theme_submenu.add_command(label='flatly'
                          ,
                          command=be_flatly
                          )

Theme_submenu.add_command(label='litera'
                          ,
                          command=be_litera
                          )

Theme_submenu.add_command(label='minty'
                          ,
                          command=be_minty
                          )

Theme_submenu.add_command(label='lumen'
                          ,
                          command=be_lumen
                          )

Theme_submenu.add_command(label='sandstone'
                          ,
                          command=be_sandstone
                          )

Theme_submenu.add_command(label='yeti'
                          ,
                          command=be_yeti
                          )

Theme_submenu.add_command(label='pulse'
                          ,
                          command=be_pulse
                          )

Theme_submenu.add_command(label='united'
                          ,
                          command=be_united
                          )

Theme_submenu.add_command(label='morph'
                          ,
                          command=be_morph
                          )

Theme_submenu.add_command(label='journal'
                          ,
                          command=be_journal
                          )

Theme_submenu.add_command(label='darkly'
                          ,
                          command=be_darkly
                          )

Theme_submenu.add_command(label='superhero'
                          ,
                          command=be_superhero
                          )

Theme_submenu.add_command(label='solar'
                          ,
                          command=be_solar
                          )

Theme_submenu.add_command(label='cyborg'
                          ,
                          command=be_cyborg
                          )

Theme_submenu.add_command(label='vapor'
                          ,
                          command=be_vapor
                          )

Theme_submenu.add_command(label='simplex'
                          ,
                          command=be_simplex
                          )

Theme_submenu.add_command(label='cerculean'
                          ,
                          command=be_cerculean
                          )

# endregion
Personalise_submenu.add_cascade(label='主题(T)'
                                ,
                                menu=Theme_submenu
                                )

# endregion
Setting_submenu.add_cascade(label='个性化(P)'
                            ,
                            menu=Personalise_submenu
                            )
# endregion
File_menu.add_cascade(label='设置(S)'
                      ,
                      menu=Setting_submenu
                      )

File_menu.add_command(label='EXIT'
                      ,
                      command=exit
                      )

con = 0

def move_gui():
    global con
    con = 1
    def move_loop():
        while True:
            if con == 1:
                print(1)
                root.geometry(f'400x225+{int(var_x.get())}+{int(var_y.get())}')
                time.sleep(0.01)

            if con == -1:
                print(0)
                break
    threading.Thread(target=move_loop,daemon=True).start()

    toplevel_move = Toplevel(title='文件(F)>MOVE GUI'
                             ,
                             size=(int(root.winfo_screenwidth()/5),int(root.winfo_screenheight()/5))
                             ,
                             position=(500,500))
    scale_toplevel_move_x = Scale(toplevel_move
                                  ,
                                  from_=0
                                  ,
                                  to=root.winfo_screenwidth()-400
                                  ,
                                  variable=var_x
                                  ,
                                  orient=HORIZONTAL
                                  ,
                                  bootstyle=WARNING
                                  ,
                                  length=root.winfo_screenwidth()/6
                                  )

    scale_toplevel_move_x.place(relx=0.1,rely=0.05)

    scale_toplevel_move_y = Scale(toplevel_move
                                  ,
                                  from_=0
                                  ,
                                  to=root.winfo_screenheight()-225
                                  ,
                                  variable=var_y
                                  ,
                                  orient=VERTICAL
                                  ,
                                  bootstyle=SUCCESS
                                  ,
                                  length=root.winfo_screenheight()/6
                                  )
    scale_toplevel_move_y.place(relx=0.05,rely=0.1)

    entry_show_x = Entry(toplevel_move
                         ,
                         text=var_x
                         )
    entry_show_x.place(relx=0.3,rely=0.3)

    entry_show_y = Entry(toplevel_move
                         ,
                         text=var_y
                         )
    entry_show_y.place(relx=0.3,rely=0.5)


    def toplevel_move_exit():
        global con
        con = -1
        toplevel_move.destroy()
    toplevel_move.protocol("WM_DELETE_WINDOW", toplevel_move_exit)


File_menu.add_command(label='MOVE'
                      ,
                      command=move_gui
                      )

#endregion
menubar.add_cascade(label='文件(F)'
                    ,
                    menu=File_menu
                    )
menubar.add_cascade(label='编辑(E)'
                    ,
                    menu=Edit_menu
                    )
menubar.add_cascade(label='检查(C)'
                    ,
                    menu=Check_menu
                    )
menubar.add_cascade(label='命令(O)'
                    ,
                    menu=Order_menu
                    )
menubar.add_cascade(label='自动(A)'
                    ,
                    menu=Auto_menu
                    )
menubar.add_cascade(label='帮助(H)'
                    ,
                    menu=Help_menu
                    )
root.config(menu=menubar)
#endregion


image_save = ImageTk.PhotoImage(file='./appData/Temp/MoYeRanSoft/SoftWareTemp/myr/save/resource/save.myr')
label_save = Label(root, image=image_save)
label_save.pack()

label_save.bind('<Button-1>', save)

button_power_off = Button(root, text='关机', command=power_off)
button_power_off.pack()

root.mainloop()
