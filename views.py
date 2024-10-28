import random



context = {"lucky_number" : lucky_number}

def miniProject(request):
    lucky_number = random.randint(0,99)
    context = {"lucky_number" : lucky_number}
    return render(request, "miniProject/project.html",context)
