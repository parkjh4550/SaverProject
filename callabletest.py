SIMPLE = 0
INNER = 1

mode = INNER

##############################
##### Simple Callable Test####
#############################
if mode == SIMPLE:
    print('SIMPLE mode------------')

    print('----------1. varaible test')
    sample = 1
    print('sample = 1')
    print(callable(sample))
    print('--------------------')

    print('-------------2. function test')
    def funcSample(number):
        print('func_in : sample')
        print('func_in : ', number)

    print('2 - 1. Sample1')
    # there is no return in function 'funcSample', so sample = None
    sample1 = funcSample(10)
    print('sample2 = funcSample : when sample1 is result of funcSample')
    print('callable(sample1) : ', callable(sample1))  # None can't be callable -> False
    print()

    print('2 - 2. Sample2')
    sample2 = funcSample  # sample2 is a same function with funcSample
    print('sample2 = funcSample : when sample2 is a Function name funcSample')
    print('sample2(10) : ',sample2(10))  # there is no return in funcSample, so None
    print('callable(sample2) : ', callable(sample2))  # function can be callabe, so True


    print('--------------3. object test')
    class Sample:
        def funcPrint(self):
            print('Sample1 function called')
    class Sample2:
        def funcPrint(self):
            print('Sample2 function called')
        def __call__(self):
            print('callable')

    print('3 - 1. Class Callable Test')
    print('Class callable : ', callable(Sample), '\n')

    print('3 - 2. Instance Callable Test')
    sample_class = Sample()
    print('Instance callable : ', callable(sample_class), '\n')

    print('3 - 3. Instance Callable Test (with __call__ function)')
    sample_class2 = Sample2()
    print('Instance callable : ', callable(sample_class2), '\n')


###########################################
#####Class inner function Callabe Test#####
###########################################
elif mode == INNER:
    print('INNER mode-------------')

    class SampleClass:
        def __init__(self, input_number):
            self.data = input_number
            self.increase_data = True
            self.has_callable = callable(getattr(self, 'increase_data', None))

        def increase_data(self):
            print('old data : ', self.data)
            increased = self.data + 1
            print('updated data : ', increased)
            return increased

        def update(self):
            self.data = self.increase_data()

        def callable_test(self):
            return self.has_callable


    sample_class = SampleClass(3)
    print(sample_class.callable_test())
