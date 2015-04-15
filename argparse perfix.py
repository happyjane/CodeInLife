import argparse

 

parser = argparse.ArgumentParser(

    description='Changethe option prefix characters',

    prefix_chars='-+/',

    )

 

parser.add_argument('-a', action="store_false",

                   default=None,

                   help='Turn A off',

                    )

parser.add_argument('+a', action="store_true",

                   default=None,

                   help='Turn A on',

                    )

parser.add_argument('//noarg', '++noarg',#可以用两个调用方法

                   action="store_true",

                    default=False)

 

print parser.parse_args()
