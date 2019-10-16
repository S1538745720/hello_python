import datetime,time
import tkinter.messagebox as messbox

class CheckIDC:
    def __init__(self,id_number):
        self.id_number=id_number
        # 切片身份号码
        self.area=id_number[:6]
        self.birthday=id_number[6:14]
        self.gender=id_number[14:17]
        self.exits=id_number[17:]

        self.lists=[]
        self.lists.append(self.check_birthday(self.birthday))
        self.lists.append(self.check_gender())
        self.lists.append(self.check_area())
        self.lists.append(self.check_number())

    def results(self):
        return self.lists

    def check_gender(self):
        if int(self.gender)%2==0:
            return '女'
        else:
            return '男'
    #获取时间
    def check_birthday(self,birthday):
        try:
            old_date=datetime.datetime(1970,1,2)
            old_time=time.mktime(old_date.timetuple())
            now_time=time.time()

            year=birthday[:4]
            month=birthday[4:6]
            day=birthday[6:]
            ymd=datetime.datetime(int(year),int(month),int(day))

            yearmd=time.mktime(ymd.timetuple())

            if old_time<yearmd and yearmd<now_time:
                return ymd.strftime("%Y-%m-%d")
            else:
                return False
        except:
            messbox.showinfo('消息',"您输入的日期不对，请重新输入")

    # 验证归属地
    def check_area(self):
        # 获取到所有的归属地
        f=open(file='身份证归属地.txt',mode='r',encoding='utf-8')
        all_area=f.readlines()
        res_area=''
        for item in all_area:
            if self.area==item[:6]:
                res_area=item[6:-1]
        if res_area=='':
            return False
        else:
            return res_area

    # 获取验证
    def get_check_number(self):
        number=self.id_number[:17]
        # 系数
        xi_list=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
        check_number= ['1','0','X','9','8','7','6','5','4','3','2']
        # 验证
        of_num=0
        for index in range(len(number)):
            of_num+=int(number[index])*int(xi_list[index])

        yu_num=of_num%11
        return check_number[yu_num]

    # 校验码验证
    def check_number(self):
        if self.get_check_number()==self.exits:
            return '有效'
        else:
            return False







