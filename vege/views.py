from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url='/login/')
def addRecipes(req):
    if req.method == "POST":
        data= req.POST

        name = data.get('name')
        description= data.get('description')
        image = req.FILES.get('image')
        user = req.user

        Recipe.objects.create(
            name= name,
            description= description,
            image= image,
            user = user
        )
        return redirect('/add/')
    getRecipes = Recipe.objects.filter(user=req.user)
   # getRecipes = Recipe.objects.all()

    if(req.GET.get('search')):
        req.GET.get('search')
        getRecipes = getRecipes.filter(name__icontains= req.GET.get('search')) #__icontains = django keyword that searches if the certain key word exists within that or not 

    context = {'recipes':getRecipes}

    return render(req,'recipes.html',context)


def recipeDetail(req, recipe_id):
    # Retrieve the recipe with the given ID or return a 404 error if not found
    recipe = get_object_or_404(Recipe, id=recipe_id)
    context = {'recipe': recipe}
    return render(req, 'recipeDetail.html', context)

@login_required(login_url='/login/')
def updateRecipe(req,id):
    getRecipe = Recipe.objects.get(id=id) 
    context = {'recipe':getRecipe}
    if req.method == "POST":
        data= req.POST

        name = data.get('name')
        description= data.get('description')
        image = req.FILES.get('image')

        getRecipe.name= name
        getRecipe.description= description
        if(image):
            getRecipe.image = image
        
        getRecipe.save()
        return redirect('/add/')
    return render(req,'updateRecipe.html',context)

@login_required(login_url='/login/')
def deleteRecipes(req,id):
    getRecipe = Recipe.objects.get(id = id )
    getRecipe.delete()
    return redirect('/add/')

def registerPage(req):
     
    if req.method == "POST":
        firstName = req.POST.get('firstName')
        lastName = req.POST.get('lastName')
        username = req.POST.get('username')
        password = req.POST.get('password')

        user = User.objects.filter(username = username)
        if user.exists():
            messages.info(req, 'Username already exists')
            return redirect('/register/')

        user = User.objects.create(
            first_name = firstName,
            last_name = lastName,
            username = username,
        )
        user.set_password(password)
        messages.info(req, 'Account created successfully')

        user.save()
        return redirect('/register/')

    return render(req, 'register.html')


def loginPage(req):
    if req.method == "POST":
        username = req.POST.get('username')
        password = req.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(req,'Invalid username')
            return redirect('/login/')
        user = authenticate(username = username , password = password)

        if user is None:
            messages.error(req,'Invalid Password')
            return redirect('/login/') 
        else:
            login(req,user)
            return redirect('/add/')
    return render(req, 'login.html')

def logoutPage(req):
    logout(req)
    return redirect('/login/')

def shareRecipe(req, recipe_id):
    
        # Retrieve the recipe object
    getRecipe = Recipe.objects.filter(id=recipe_id).first()
    
        # Toggle the is_shared status
    getRecipe.is_shared = not getRecipe.is_shared
    getRecipe.save()
    
    # Redirect back to the list of recipes
    return redirect('/add/')

def sharedRecipes(req):
    sharedRecipes = Recipe.objects.filter(is_shared=True)
    return render(req, 'sharedRecipes.html', {'sharedRecipes': sharedRecipes})