from flask import Flask

app= Flask ( __name__)

@app.route("/")

def home():
      return "hello"

@app.route("/about")

def about():
   return "this is about page"




@app.route("/add")


def add():
    a=15
    b=20
    c=a+b
    return str(c)

@app.route("/sub")

def sub():
    a=20
    b=10
    c=a-b
    return str(c)

@app.route("/mul")

def mul():
    a=10
    b=5
    c=a*b
    return str(c)

@app.route("/div")

def div():
    a=50
    b=5
    c=a/b
    return str(c)

@app.route("/user/<username>")


def user(username):
    return (f"my name is {username}")

@app.route("/person_list")
def person():
    user_name="nisha"
    age=24
    list1=[user_name,age]
    return list1

@app.route("/student_list")
def student():
    student_list=student_list= [{"Name":"Sivapackia","Age":22 ,"Roll_NO": 101, "Marks":[90,75,80,98,65]},
                    {"Name":"Siva","Age":21 ,"Roll_NO": 102, "Marks":[90,75,80,78,99]},
                    {"Name":"Vilobin","Age":21 ,"Roll_NO": 103, "Marks":[94,75,80,88,35]},
                    {"Name":"Mahadevi","Age":27 ,"Roll_NO": 104, "Marks":[70,85,80,98,35]},          
                    {"Name":"Nisha","Age":23 ,"Roll_NO": 105, "Marks":[90,75,85,98,35]},
                    {"Name":"Vaisali","Age":27 ,"Roll_NO": 106, "Marks":[80,98,35,90,75]},
                    {"Name":"Vijay","Age":22 ,"Roll_NO": 107, "Marks":[90,80,98,35,75]},
                    {"Name":"Mohamed Ismail","Age":22 ,"Roll_NO": 108, "Marks":[75,80,90,98,35]},
                    ]
    student=list()
    for i in student_list:
        if i['Age']>25:
            student.append(i)
    
    return student




if __name__ == "__main__":
  app.run(debug=True)
