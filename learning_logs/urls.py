from django.urls import path
from . import views
app_name = 'learning_logs'# namespace for learning_logs app
# Define the URL patterns for learning_logs app
urlpatterns = [
    path('',views.index,name="index"), #3 arguments: route ='' it means the home page of the app, view function = views.index (it specifies the view function to handle requests to this URL), name="index" (it assigns a name to this URL pattern for easy reference in templates and other parts of the app)
    path('topics/',views.topics, name="topics"),
    #page for a single topic, <int:topic_id> captures an integer from the URL and passes it as an argument named topic_id to the views.topic function. This allows the view to retrieve and display the specific topic based on the provided topic_id.
    path('topic/<int:topic_id>/',views.topic, name='topic'),
    #page for adding new topic.
    path("new_topic/", views.new_topic, name = 'new_topic'),
    #Page for adding a new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    path('delete_entry/<int:entry_id>/', views.delete_entry, name='delete_entry'),
    path('delete_topic/<int:topic_id>/', views.delete_topic, name='delete_topic'),

]