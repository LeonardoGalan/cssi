x = int(raw_input("enter number"))
y = int(raw_input("enter number"))
s = int(x+y)
print(x+y=s)

'''
ALL ANSWERS BELOW ARE ANSWERS TO question 1(a)

print("(0)+(1)=(2)".format(x,y,x+y))
print("%s+%s=%s"%(x,y,x+y))
print(str(x)"+"+str(y)+"="+str(x+y))
print x,"+",y,"=",x+y
---------------------
print "%s-%s=%s"%(x,y,x-y)
print x,"*",y,"=",x*y

if not y==0:
    print "%s/%s=%s"%(x,y,x/y)
if y!=0:
    print"{0}%{1}={2}".format(x,y,x%y)
for i in range(1,101,1):
    print(i)
------------------------------
2) THIS QUESTION IS A POSSIBLE QUESTION INTERVIEWERS WILL ASK YOU TO WRITE WHEN LOOKING FOR A JOB
for i in range(1,101,1):
    if i%3==0 and i%5==0:
        print('fizzbuzz')
    elif i%3==0:
        print('fizz')
    elif i%5==0:
        print('buzz')
    else:print(i)

'''

def GreetAgent(first_name,last_name):
    print "%s. %s %s" %(last_name,first_name,last_name)

def createAgentGreeting(first_name,last_name):
    return "%s. %s %s" %(last_name,first_name,last_name)

print "Calling GreetAgent() function with arguments JaMes, BoNd"
GreetAgent("JaMes","BoNd")

print "calling createAgentGreeting() function with arguments JaMes,BoNd"
g = createAgentGreeting("JaMes","BoNd")
print g.uppper()

story = ''' jack and jill went
up a {0}'''.format('hill')

print story.format('hill')

noun = raw_input("enter a noun: ")

print (story.format(noun))
