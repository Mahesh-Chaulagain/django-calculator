from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def result(request):
    num1 = int(request.GET.get('num1'))
    num2 = int(request.GET.get('num2'))

    if request.GET.get('add') == "":
        ans = num1 + num2
        operation = '+'

    elif request.GET.get('subtract') == "":
        ans = num1 - num2
        operation = '-'

    elif request.GET.get('multiply') == "":
        ans = num1 * num2
        operation = '*'

    else:
        ans = num1/num2
        operation = '/'
    
    context={
        'first': num1,
        'second': num2,
        'condition': operation,
        'answer': ans,
    }

    return render(request, 'result.html', context)