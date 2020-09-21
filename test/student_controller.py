class Controller():

    def show_students(self,data):
        print('''
        -------------
        |所有学生信息：|
        -------------
        ''')
        self.print_info(data)

    def print_info(self,data):
        for item in data:
            title=['学生ID:','学生姓名:','年龄:','性别:','分数:']
            count = 0
            for i in item:
                print(title[count],i,end=' ')
                count+=1
            print('')