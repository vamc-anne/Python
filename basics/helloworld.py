if 5 > 4:
    print("helloworld!")
else:
    print("no Hello :(")

my_array = ["vamsi", "sai", "rama", "krishna"]
if "vamsi" in my_array:
    print("vamsi listed in array!")


for name in my_array:
    print("my name is {0}").format(name)

start = 10
end = 20
inc = 2

for index in range(start, end, inc):
    print("my index is {0}".format(index))
