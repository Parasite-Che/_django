from django.shortcuts import render

posts = [
	{
    	'author': 'Администратор',
    	'title': 'Это первый пост',
    	'content': 'Содержание первого поста.',
    	'date_posted': '12 мая, 2022'
	},
	{
    	'author': 'Пользователь',
    	'title': 'Это второй пост',
    	'content': 'Подробное содержание второго поста.',
    	'date_posted': '13 мая, 2022'
	}
]
 
def base(request):
	return render(request ,'polls/base.html' ,{
        'foo': 'bar',
    })

def home(request):
	return render(request ,'polls/home.html' ,{
        'foo': 'bar',
    })

def about(request):
	return render(request ,'polls/about.html' ,{
        'foo': 'bar',
    })

# Create your views here.
