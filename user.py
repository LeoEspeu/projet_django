import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from mysite.messenger.models import Message


from pprint import pprint
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

foo = User.objects.create_user('foo2','','passoire')
foo.first_name = 'John'
foo.last_name = 'Doe'
foo.save()

#validate_password('passoire')
#validate_password('motdepasse')
pprint(vars(foo))

bar = User.objects.create_user('bar',password='passoire',first_name='Alan',last_name='Smithee')

msg = Message()
msg.sender = foo
msg.recipient = bar
msg.save()
pprint(vars(msg))

msg3 = Message(sender=foo,recipient=bar,subject='sujet',body='texte')
msg3.save()


msg4 = Message.objects.create(sender=foo,recipient=bar,subject='sujet',body='texte')
pprint(vars(msg4))
msg4.body = 'texte révisé'
msg4.save()
pprint(vars(msg4))

msg5 = Message(sender=foo,recipient=bar,id=5)
msg5.save()

msg6 = Message(sender=foo, recipient=bar)
msg6.save()

msg4.body = 'texte révisé'
msg4.save(update_fields=['body'])

msg = Message.objects.get(pk=3)
print(msg)

msg = Message.objects.filter(sender=foo)[0]
print(msg)