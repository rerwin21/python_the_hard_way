# Most of the uses of inheritance can be simplified or replaced with composition, and multiple # inheritance should be avoided at all costs

# implicit inheritance: what happens when you define a function in the parent, but not in 
# child?

class Parent(object):
    
    def implicit(self, string_arg):
        print "PARENT implicit(%s)" % string_arg

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit("Go to bed!")
son.implicit("Why doe?")


