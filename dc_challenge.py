full_name = "Michael Gaynor"
age = 30
my_array = []
my_array.append(full_name)
my_array.append(age)

print (my_array)

def say_hello():
  print ("Hello!")
say_hello()

split_name = full_name.split()
print split_name

def say_name():
  print ("Hello, " + split_name[0])

say_name()

def my_age(year_born):
  print 2017 - year_born

my_age(1987)

def sum_odd_numbers():
  the_sum = 0
  for i in range(1,5001,2):
    the_sum += i
  return the_sum


print (sum_odd_numbers())

# break example
i = 0
while 1: #this will run forever...
  i +=1
  print i
  if (i == 10):
    break
print ("We broke out of the loop!")














