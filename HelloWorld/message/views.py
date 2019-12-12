from django.shortcuts import render
from .models import UserMessage

def getform(resquest):
    # all_messages = UserMessage.objects.all()
    # for message in all_messages:
    #     print(message.name)

    if resquest.method == 'POST':
        print(resquest)
        name = resquest.POST.get('name', '')
        message = resquest.POST.get('message', '')
        address = resquest.POST.get('address', '')
        email = resquest.POST.get('email', '')
        user_message = UserMessage()
        user_message.name = name
        user_message.message = message
        user_message.address = address
        user_message.email = email
        user_message.object_id = "helloworld"
        user_message.save()

    return render(resquest, 'message_form.html')

