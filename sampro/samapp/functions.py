def upload(f):
    with open('samapp/static/upload/'+f.name,'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)