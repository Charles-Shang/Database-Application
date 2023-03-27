from django.shortcuts import render

def homeView(request):
    context = {}
    context['intro'] = 'Hello World'
    func_ctrl = Functionalities()
    data_count = {
        "movie": func_ctrl.count_entries("Movie"),
        "user": func_ctrl.count_entries("User"),
        "director": func_ctrl.count_entries("Director"),
        "actor": func_ctrl.count_entries("Actor"),
        "rating": func_ctrl.count_entries("Rating"),
    }
    data_count['celebrity'] = data_count['director'] + data_count['actor']
    context['data_count'] = data_count
    
    return render(request, 'index.html', context)