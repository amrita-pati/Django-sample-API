from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import  Persons, User
# Create your views here.
def home(request):
    # return HttpResponse('Hello, World!')
    return render(request,'index.html')

@api_view(['POST'])
def addUser(request):
    try:
        passward= request.data.get('user_passward')
        user_name = request.data.get('user_name')
        user_age = request.data.get('user_age')
        user_salary = request.data.get('user_salary')
        user_department = request.data.get('user_department')
        
        newUser = User(name=user_name,age=user_age,salary=user_salary,department=user_department,passward=passward)
        newUser.save()
        return Response({"status":"Success","message":"User added Successfully"})
    except Exception as e:
        return Response({"status":"Fail","message":f"Error:{e}"})

@api_view(['POST'])
def updateUsers(request):
    try:
        id= request.data.get("id")
        newName= request.data.get('newName')
        newAge= request.data.get('newAge')
        newsalary= request.data.get('newsalary')
        newdepartment= request.data.get('newdepartment')
        userInfo= User.objects.get(id=id)
        userInfo.name= newName
        userInfo.age= newAge
        userInfo.salary= newsalary
        userInfo.department= newdepartment
        userInfo.save()

        return Response({"status":"Success","message":"Users updated Successfully"})
    except Exception as e:
        return Response({"status":"Fail","message":f"Error:{e}"})


@api_view(['POST'])
def updateselectedUsers(request):
    try:
        id= request.data.get("id")
        userInfo = User.objects.filter(id=id).first()
        if userInfo!=None:
            newsalary= request.data.get('newsalary')

            userInfo.salary=newsalary
            userInfo.save()
            return Response({"status":"Success","message":"Users updated Successfully"})
        else:
            return Response({"user not exist with given id"})
    except Exception as e:
        return Response({"status":"Fail","message":f"Error:{e}"})


@api_view(['POST'])
def updateAge(request):
    try:
        id= request.data.get("id")
        userInfo = User.objects.filter(id=id).first()
        if userInfo!=None:
            newAge= request.data.get('newAge')

            userInfo.age=newAge
            userInfo.save()
            return Response({"status":"Success","message":"Users updated Successfully"})
        else:
            return Response({"user not exist with given id"})
    except Exception as e:
        return Response({"status":"Fail","message":f"Error:{e}"})

@api_view(['POST'])
def updatePassward(request):
    try:
        id= request.data.get("id")
        userInfo = User.objects.filter(id=id).first()
        if userInfo!=None:
            newPassward= request.data.get('newPassward')

            userInfo.passward=newPassward
            userInfo.save()
            return Response({"status":"Success","message":"Users updated Successfully"})
        else:
            return Response({"user not exist with given id"})
    except Exception as e:
        return Response({"status":"Fail","message":f"Error:{e}"})





@api_view(['GET'])
def getAllUsers(request):
    try:
        userInfo= User.objects.all()
        userdict={}
        userlist=[]
        for eachuser in userInfo:
            userdict['name']=eachuser.name
            userdict['age']=eachuser.age
            userdict['salary']=eachuser.salary
            userdict['department']=eachuser.department
            userlist.append(userdict.copy())

        return Response(userlist)
    except Exception as e:
        return Response({"status":f"Error:{e}"})

@api_view(['GET'])
def getSelectedUsers(request):
    try:
        userInfo= User.objects.filter(salary__gte=20000).order_by('-salary').all()
        userdict={}
        userlist=[]
        if userInfo==[]: 
            for eachuser in userInfo:
                userdict['name']=eachuser.name
                userdict['age']=eachuser.age
                userdict['salary']=eachuser.salary
                userdict['department']=eachuser.department
                userlist.append(userdict.copy())

        return Response(userlist)
    except Exception as e:
        return Response({"status":f"Error:{e}"})



@api_view(['DELETE'])
def deleteUsers(request):
    try:
        id= request.data.get("id")
        userInfo= User.objects.get(id=id)
        userInfo.delete()

        # User.objects.filter(id=id).delete()

        return Response({"status":"Success","message":"Successfully Deleted"})
    except Exception as e:
        return Response({"status":"Fail","message":f"Error : {e}"})

@api_view(['POST'])
def addPersons(request):
    try:
        person_name = request.data.get('person_name')
        person_age = request.data.get('person_age')
        person_contactno = request.data.get('person_contactno')
        person_status = request.data.get('person_status')
        joining_date = request.data.get('joining_date')

        
        newPerson = Persons(person_name=person_name,person_age=person_age,person_contactno=person_contactno,person_status=person_status,joining_date=joining_date)
        newPerson.save()
        return Response({"status":"Success","message":"Person added Successfully"})
    except Exception as e:
        return Response({"status":"Fail","message":f"Error:{e}"})




# LOGIN API----------------------------------

@api_view(['POST'])
def login(request):
    try:
        name= request.data.get("name")
        passward= request.data.get("passward")
        userCheck = User.objects.filter(name=name).first()
        if name == '' or name == None or passward == '' or passward == None:
            return Response({"status":"Success","message":" nme nd passward can not be null"})
            
        if userCheck!=None:
            userInfo = User.objects.filter(name=name,passward=passward).first()
            if userInfo!=None:

                return Response({"status":"Success","message":"login Successfully"})
            else:
                return Response({"status":"failed","message":"invalid credential"})
        else:

            return Response({"status":"Success","message":"User not exist"})
        
        
    except Exception as e:
        return Response({"status":"Fail","message":f"Error:{e}"})


