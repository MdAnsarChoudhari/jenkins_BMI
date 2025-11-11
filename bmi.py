import sys

if len(sys.argv)==3:
    script_name=sys.argv[0]
    weight=sys.argv[1]
    height=sys.argv[2]

else:
    script_name=sys.argv[0]
    weight=60
    height=5.7



bmi=weight/(height*height)

print("Script Name : ",script_name)
print("BMI ",bmi)