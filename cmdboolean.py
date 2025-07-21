"""arg using parse
default values
Boolean chesk"""
import argparse
p=argparse.ArgumentParser(description= "add 2 numbers")
p.add_argument('--x',type=int,required=True,help="first number")
p.add_argument('--y',type=int,required=True,help="second number")
p.add_argument('--opt',type=str,required=True, choices=['add','sub','mul','div'],help="operation")
args=p.parse_args()
if args.opt=='add':
	result=args.x+args.y
elif args.opt=='sub':
	result=args.x-args.y
elif  args.opt=='mul':
	result=args.x*args.y
elif  args.opt=='div':
	result=args.x/args.y
print("result is ",result)