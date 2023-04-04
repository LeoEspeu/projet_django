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

validate_password('passoire')
validate_password('motdepasse')
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

result = Message.objects.get_or_create(body='texte')
print(result)

result = msg6.delete()
print(result)

pprint(vars(msg6))

result = Message.objects.filter(pk=5).delete()
print(result)

len(Message.objects.all())

Message.objects.count()

if Message.objects.filter(sender=foo):
    print('Au moins un msg envoyé par foo.')

superuser = User.objects.get(pk=1)
Message.objects.filter(sender=foo).exists() and 'ok'
Message.objects.filter(sender=superuser).exists() and 'ok'

msg = Message.objects.get(pk=1)
msg.subject = 'sujet4'
msg.save()

Message.objects.filter(pk=1).update(subject='sujet4-2')

msgs = [Message(
    subject='Annonce',
    sender=superuser,
    body='Demain, le site sera fermé pour maintenance.',
    recipient=user
) for user in User.objects.all()]

Message.objects.bulk_create(msgs)

result = Message.objects.in_bulk([7,8,9])
pprint(result)