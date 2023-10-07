from flask import Flask

app = Flask (__name__)

@app.route ('/', methods = ['GET','POST','PUT',]) #GET,POST,PUT,Delete

def hello () :
    
    return 'Hello, Flask !'

@app.route('/pricing')
def pricing ():
    return "1000"

@app.route ('/identifyPoly')

def pollycheck () :
    num = int(input ('enter a number'))
    temp = num
    rev = 0

    #234 -- 432
    #343 -- 343

    while (temp > 0 ) :
    
        rem = temp%10
        rev = rev*10+rem
        temp = temp//10
        #print("temp%10=",rem)
        #print("rev*10+rem",rev)
        #print("temp//10",temp)
    
    if num == rev :
        print (num, " is a polyndrome")

        return str(num)+" is a polyndrome *"

    else :
        print (num," is not! a polyndrome *")

        return str(num)+" is a 'not!' polyndrome !!"

'''
@app.route('/student',methods=['GET','POST'])
def name():
    name = request.args.get('name')
    age = 0
    for i in student:
        if name == i['name']:
            age = i['age']
    return str(age)
    
'''
pass

'''
@app.route('/identifyUserCred',methods=['GET','POST','])
'''

if __name__ == '__main__' :
    app.run ()
