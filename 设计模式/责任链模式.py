class Handler(object):
    """抽象接口"""

    def __init__(self):
        pass

    def successor(self, successor):
        """下一主管"""
        self.successor = successor

    def handler(self, request):
        pass



class Student(Handler):

    def __init__(self, name):
        super(Student, self).__init__()
        self.name = name

    def handler(self, request):
        if request.task == 'worked':
            print('i am {}, worked to {}'.format(self.name, self.successor.name))
            self.successor.handler(request)


class Teacher(Handler):

    def __init__(self, name):
        super(Teacher, self).__init__()
        self.name = name

    def handler(self, request):
        if request.task == 'worked':
            print('i am {}, worked to {}'.format(self.name, self.successor.name))
            self.successor.handler(request)


class President(Handler):

    def __init__(self, name):
        super(President, self).__init__()
        self.name = name

    def handler(self, request):
        if request.task != 'worked':
            print('i am {}'.format(self.name, 'no working for'))


class Request:
    def __init__(self, task):
        self.task = task



request = Request('worked')
student = Student('stuend')
teacher = Teacher('teacher')
president = President('president')
student.successor(teacher)
teacher.successor(president)
student.handler(request)