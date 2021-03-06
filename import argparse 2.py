import argparse

 

parser = argparse.ArgumentParser()

 

parser.add_argument('-s', action='store', #python自带的action

                   dest='simple_value',#下面调用时所用的参数名称

                    help='Storea simple value')#调用-h时的介绍

 

parser.add_argument('-c', action='store_const',#注意与-s的不同

                   dest='constant_value',

                   const='value-to-store',#要保存的常数

                   help='Store a constant value')

 

parser.add_argument('-t', action='store_true',

                   default=False,#直接-t即将boolean_swich改为true

                   dest='boolean_switch',

                   help='Set a switch to true')

parser.add_argument('-f', action='store_false',

                   default=False,#默认值为faulse

                   dest='boolean_switch',

                   help='Set a switch to false')

 

parser.add_argument('-a', action='append',#可以连续添加多个值，相当于一个集合

                   dest='collection',

                   default=[],

                   help='Add repeated values to a list')

 

parser.add_argument('-A', action='append_const',

                   dest='const_collection',

                   const='value-1-to-append',

                   default=[],

                   help='Add different values to list')

parser.add_argument('-B', action='append_const',

                    dest='const_collection',

                   const='value-2-to-append',

                   help='Add different values to list')

 

parser.add_argument('--version', action='version',

                   version='%(prog)s 1.0')##会用%(prog)s用于调出保存的文件名

 

results = parser.parse_args()

print 'simple_value    = %r' % results.simple_value

print 'constant_value  = %r' % results.constant_value

print 'boolean_switch  = %r' % results.boolean_switch

print 'collection      = %r' % results.collection

print 'const_collection = %r' % results.const_collection
