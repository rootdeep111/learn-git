class Student1(object):
    def score_init(self,score):
        self.score = score

    def print_score(self,name):
        self.name = name
        print('%s: %s' % (self.name, self.score))
bart = Student1()
bart.score_init(99)
bart.print_score('bart')

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(std):
        print('%s: %s' % (std.name, std.score))
lisa = Student('Lisa Simpson', 87)
lili = Student('lili Simpson', 87)
lisa.print_score()
lili.print_score()
#和静态语言不同的是，实例可以随时绑定变量
lisa.age = 25
print(lisa.age)
#print(lili.age)