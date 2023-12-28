from django.shortcuts import render,redirect
from .forms import registrationform,postform
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth import login,logout,authenticate
from .models import post
from django.contrib.auth.models import User,Group

def base(request):
    return render(request,'base.html')


@login_required(login_url='login')
def home(request):
    Post=post.objects.all()

    if request.method == 'POST':
        post_id=request.POST.get('post-id')# for creating the post
        user_id=request.POST.get('user-id')# for banning the certain user

        if post_id:
            post1=post.objects.filter(id=post_id).first()

            if post1 and (post1.author == request.user or request.user.has_perm('base.delete_post')): # to check wheather the user has the permission to delete the post
                post1.delete() 

        elif user_id:
            user=User.objects.filter(id=user_id).first()#get the user from the main User

            if user and request.user.is_staff:
                try:
                    group=Group.objects.get(name='default')#get the group called default
                    group.user_set.remove(user)#remove the user from the group
                except:
                    pass
                try:
                    group=Group.objects.get(name='mod')
                    group.user_set.remove(user)
                except:
                    pass
    return render(request,'base/home.html',{'Post':Post})


@login_required(login_url='login')
@permission_required('base.add_post',login_url='login',raise_exception=True) # to chect wheather the user is logged in or not
def createpost(request):
    if request.method == "POST":
        form= postform(request.POST)
        if form.is_valid():
            post=form.save(commit=False)# we have to add auther so commit = false 
            post.author=request.user # to save the author to the form
            post.save()
            return redirect('home')
    else:
        form=postform()
    return render(request,'base/create-post.html',{'form':form})



def signup(request):
    if request.method=='POST':
        form=registrationform(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('/home')
    else:
        form=registrationform()

    return render(request,'base/signup.html',{'form':form})

def profile(request):
    Post=post.objects.all()

    if request.method == 'POST':
        post_id=request.POST.get('post-id')
        post1=post.objects.filter(id=post_id).first()
        post1.delete()

    return render(request,'base/profile.html',{'Post':Post})