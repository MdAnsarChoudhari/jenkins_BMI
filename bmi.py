import sys

if len(sys.argv)==3:
    script_name=sys.argv[0]
    weight=sys.argv[1]
    height=sys.argv[2]

else:
    script_name=sys.argv[0]
    weight=60
    height=6



bmi=weight/(height*height)

print("Script Name : ",script_name)
print("Weight",weight)
print("Height",height)
print("BMI ",bmi)