from tkinter import *
from CheckIDC import *

class IDCheckGUI:
    def __init__(self):
        self.frame=Tk()
        self.frame.title('身份证信息校验')
        self.frame.geometry('700x465+200+200')
        self.frame['bg']='lightblue'
        # 图片
        self.image=PhotoImage(file='6L9PO.png')
        self.Label_image=Label(self.frame,image=self.image)
        self.Label_image.place(x=10,y=10)
        # 校验表单
        self.label=Label(self.frame,text='请输入身份证号码：',font=('微软雅黑',14,'bold'),bg='navy',fg='lightblue')
        self.label.place(x=320,y=20)

        self.Entry_is_input=Entry(self.frame,width=21,font=('微软雅黑',14,'bold'))
        self.Entry_is_input.place(x=320,y=60)

        self.Button_exits=Button(self.frame,command=self.get_info,text='校验',width=8,font=('微软雅黑',11,'bold'),fg='blue')
        self.Button_exits.place(x=600,y=60)
        # 显示表单
        self.label=Label(self.frame,text='是否有效：',font=('微软雅黑',16,'bold'),bg='lightblue',fg='blue')
        self.label.place(x=320,y=140)

        self.varEntry1=StringVar()
        self.Entry1=Entry(self.frame,width=8,state=DISABLED,font=('微软雅黑',14,'bold'),textvariable=self.varEntry1)
        self.Entry1.place(x=430,y=140)

        self.label=Label(self.frame,text='性别：',font=('微软雅黑',16,'bold'),bg='lightblue',fg='blue')
        self.label.place(x=362,y=200)

        self.varEntry2=StringVar()
        self.Entry2=Entry(self.frame,width=8,state=DISABLED,font=('微软雅黑',14,'bold'),textvariable=self.varEntry2)
        self.Entry2.place(x=430,y=200)

        self.label=Label(self.frame,text='出生日期：',font=('微软雅黑',16,'bold'),bg='lightblue',fg='blue')
        self.label.place(x=320,y=260)

        self.varEntry3=StringVar()
        self.Entry3=Entry(self.frame,width=18,state=DISABLED,font=('微软雅黑',14,'bold'),textvariable=self.varEntry3)
        self.Entry3.place(x=430,y=260)

        self.label=Label(self.frame,text='所在地：',font=('微软雅黑',16,'bold'),bg='lightblue',fg='blue')
        self.label.place(x=342,y=320)

        self.varEntry4=StringVar()
        self.Entry4=Entry(self.frame,width=18,state=DISABLED,font=('微软雅黑',14,'bold'),textvariable=self.varEntry4)
        self.Entry4.place(x=430,y=320)

        self.Button_close=Button(self.frame,text='关闭',width=8,font=('微软雅黑',12,'bold'),fg='blue',command=self.close)
        self.Button_close.place(x=560,y=400)

        self.show()
    def show(self):
        self.frame.mainloop()
    #关闭
    def close(self):
        self.frame.destroy()

    # 校验按钮事件
    def get_info(self):
        # 获取身份证号码
        self.id_number=self.Entry_is_input.get()
        checkidc=CheckIDC(str(self.id_number))
        result_lists=checkidc.results()

        # 设置到数据
        if result_lists[0]==False or result_lists[1]==False or result_lists[3]==False:
            self.varEntry1.set('无效')
            self.varEntry2.set('')
            self.varEntry3.set('')
            self.varEntry4.set('')
        else:
            self.varEntry1.set(result_lists[3])
            self.varEntry2.set(result_lists[1])
            self.varEntry3.set(result_lists[0])
            self.varEntry4.set(result_lists[2])


IDCheckGUI()