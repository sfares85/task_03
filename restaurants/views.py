from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
		"my_list":[
            {
                'restaurant_name':'Hardees',
                'food_type':'traditional.',
            },
            {
                'restaurant_name':'KFC',
                'food_type':'gourmet',
            },
            {
                'restaurant_name':'dandoosh',
                'food_type':'comfort food',
            },
        ]
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    "my_object":{
                        'restaurant_name':'dandoosh',
                'food_type':'comfort food',
                    },
    }
    return render(request, 'detail.html', context)
