from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Topic,Entry
from .forms import topicForm,  EntryForm
# Create your views here.
def index(request): #request is an HttpRequest object that contains metadata about the request
    """The home page for Learning Log"""
    #this page for learning log
    return render(request, "learning_logs/index.html") #render() function combines a given template with a given context dictionary and returns an HttpResponse object with that rendered text

@login_required #this decorator is used to restrict access to a view to only authenticated users. not logged in user will be redirected to the login page. you can specify the login URL in your settings.py file using the LOGIN_URL setting. if not specified, it defaults to '/accounts/login/'.
def topics(request):
    '''show all topics'''
    topics = Topic.objects.filter(owner=request.user).order_by('date_added') #filter the owner of the topic to the current user, so that each user can only see their own topics. order_by('date_added') is used to sort the topics by the date they were added, with the oldest topics appearing first.
    context = {'topics' : topics}
    return render(request, 'learning_logs/topics.html',context)

@login_required
def topic(request,topic_id):
    topic = Topic.objects.get(id=topic_id)
    #make sure the topic belong to the current user
    if topic.owner != request.user: #if the owner of the topic is not the current user, this page should not be accessible, and we raise an Http404 error to indicate that the page was not found. This is a security measure to prevent unauthorized access to topics that do not belong to the user.
        raise Http404
    # entries = Entry.objects.filter(topic=topic).order_by('-date_added')    
    entries = topic.entry_set.order_by('-date_added') #entry_set is a related manager that allows you to access the related Entry objects associated with a specific Topic instance. It is automatically created by Django when you define a ForeignKey relationship between two models. In this case, it allows you to retrieve all Entry objects that are related to a particular Topic instance.
    context = {'topic':topic, 'entries':entries}
    return render(request, 'learning_logs/topic.html',context)

@login_required #
def new_topic(request):
    '''add new topic'''
    if request.method != 'POST':
        form = topicForm()
    else:
        #data submitad; process data.
        form = topicForm(data= request.POST)
        if form.is_valid():
            new_topic =form.save(commit=False) 
            new_topic.owner = request.user #the error of NOT NULL constraint failed: learning_logs_topic.owner_id fix
            new_topic.save()
            return redirect('learning_logs:topics')
    #display a blank or invalid form
    context = {'form':form}
    return render(request,'learning_logs/new_topic.html',context)

@login_required
def new_entry(request,topic_id):
    '''add a new entry for a particular topic'''
    topic = Topic.objects.get(id = topic_id)

    if request.method != "POST":
        form = EntryForm()
    else:
        # post a submitted; create a blank data
        form = EntryForm(data= request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect("learning_logs:topic", topic_id=topic_id)
    #display a blank or invalid form
    context = {'topic':topic, 'form':form}
    return render(request, "learning_logs/new_entry.html",context)

@login_required
def delete_entry(request,entry_id):
    '''delete an existing entry'''
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    #make sure the topic belong to the current user
    if topic.owner != request.user:
        raise Http404
    if request.method != "POST":
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry,data=request.POST)
        entry.delete()
        return redirect('learning_logs:topic',topic_id=topic.id)
    context = {'entry':entry, 'topic':topic, 'form':form}
    return render(request,'learning_logs/delete_entry.html',context)

@login_required
def delete_topic(request,topic_id):
    '''delete an existing topic'''
    topic = Topic.objects.get(id=topic_id)
    #make sure the topic belong to the current user
    if topic.owner != request.user:
        raise Http404
    if request.method != "POST":
        form = topicForm(instance=topic)
    else:
        form = topicForm(instance=topic,data=request.POST)
        topic.delete()
        return redirect('learning_logs:topics')
    context = {'topic':topic, 'form':form}
    return render(request,'learning_logs/delete_topic.html',context)

@login_required
def edit_entry(request,entry_id):
    '''edit an existing entry'''
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    #make sure the topic belong to the current user
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        #initial request; pre-fill form with the current entry
        form = EntryForm(instance=entry)
        #tell django to create a form pre-filled with information from the existing entry object.
    else:
        #POST data submitted; process data
        form = EntryForm(instance=entry,data=request.POST) #tell django to create a form pre-filled with information from the existing entry object and update it with the data submitted in the POST request.
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic',topic_id=topic.id)
    context = {'entry':entry, 'topic':topic, 'form':form}
    return render(request,'learning_logs/edit_entry.html',context)
