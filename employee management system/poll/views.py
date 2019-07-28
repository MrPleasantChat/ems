from django.shortcuts import render

# Create your views here.


def index(request):
    Context = {}
    Context['title'] = 'polls'
    # context = Context({'title':'polls'})

    return render(request, 'polls/index.html', Context)


# context = Context({"my_name": "Adrian"})
# t.render(Context({"person": p}))
