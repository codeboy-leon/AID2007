import pymysql
from student_controller import Controller
class View:
    def __init__(self,controller):
        self.db = pymysql.connect(
            host='176.140.2.117',
            port=3306,user='root',
            passwd='123456',
            db='stu',
            charset='utf8')
        self.cur = self.db.cursor()
        self.__controller = controller()
    def main(self):
        self.condition = True
        while self.condition:
            self.__menu()
            self.condition = self.__input()
    def __menu(self):
        print('''
            ╔———————学生信息管理系统————————╗
            │                                              │
            │   =============== 功能菜单 ===============   │
            │                                              │
            │   1 录入学生信息                             │
            │   2 查找学生信息                             │
            │   3 删除学生信息                             │
            │   4 修改学生信息                             │
            │   5 排序                                     │
            │   6 统计学生总人数                           │
            │   7 显示所有学生信息                         │
            │   0 退出系统                                 │
            │  ==========================================  │
            │  说明：通过数字键选择菜单          │
            ╚———————————————————————╝
            ''')
    def __input(self):
        choose = input('请输入你的选择：')
        if choose == '1':
            self.__insert_student()
            return True
        elif choose == '2':
            self.data = self.__select_student()
            self.__controller.print_info(self.data)
            return True
        elif choose =='3':
            self.__delete_student()
            return True
        elif choose == '4':
            self.__modify_student()
            return True
        elif choose== '5':
            self.__sorted_()
            return True
        elif choose == '6':
            self.__count_student()
            return True
        elif choose == '7':
            self.__show_students()
            return True
        elif choose == '0':
            return self.__exit()
    def __show_students(self):
        self.cur.execute('select * from cls;')
        self.data = self.cur.fetchall()
        self.__controller.show_students(self.data)
    def __insert_student(self):
        pass
    def __select_student(self):
        print('''
             ╔———————选择菜单————————╗
            │   1 按照学生ID查找     　│
            │   2 按照学生姓名查找     | 
            |   0 返回主菜单          |  
            │  说明：通过数字键选择菜单 │
            ╚———————————————————————╝
            ''')
        while True:
            self.choose = input('请输入你的选择：')

            if self.choose == '1':
                while True:
                    self.id = input('请输入学生ID:')
                    self.cur.execute('select * from cls where id=%s',[self.id])
                    if not self.cur.fetchall():
                        print('没有该学生信息,请从新输入：')
                        continue
                    return self.cur.fetchall()
            elif self.choose == '2':
                while True:
                    self.name = input('请输入学生姓名：')
                    self.cur.execute('select * from cls where name=%s',[self.name])
                    if not self.cur.fetchall():
                        print('没有该学生信息,请重新输入')
                        continue
                    return self.cur.fetchall()
            elif self.choose == '0':
                break
            else:
                print('输入有误,请重新输入：')
    def __delete_student(self):
        print('''
             ╔———————选择菜单————————╗
            │   1 按照学生ID删除     　│
            │   2 按照学生姓名删除     | 
            |   0 返回主菜单          |  
            │  说明：通过数字键选择菜单 │
            ╚———————————————————————╝
            ''')
        while True:
            self.choose = input('请输入你的选择：')

            if self.choose == '1':
                while True:
                    self.id = input('请输入学生ID:')
                    self.cur.execute('select * from cls where id=%s',[self])
                    self.stu = self.cur.fetchall()
                    self.__controller.print_info(self.stu)
                    self.confirm = input('是否删除y/n：')
                    if self.confirm=='y':
                        self.cur.execute('delere from cls where id=%s',[self.id])
                        self.db.commit()
                    else:
                        break
                    if not self.cur.fetchall():
                        print('没有该学生信息,请从新输入：')
                        continue
                    return self.cur.fetchall()
            elif self.choose == '2':
                while True:
                    self.name = input('请输入学生姓名：')
                    self.cur.execute('delete from cls where name=(%s)',[self.name])
                    if not self.cur.fetchall():
                        print('没有该学生信息,请重新输入')
                        continue
                    return self.cur.fetchall()
            elif self.choose == '0':
                break
            else:
                print('输入有误,请重新输入：')
    def __modify_student(self):
        pass
    def __update_student(self):
        pass
    def __sorted_(self):
        pass
    def __count_student(self):
        pass
    def __exit(self):
        self.cur.close()
        self.db.close()
        return False
if __name__ == '__main__':
    view = View(Controller)
    view.main()
