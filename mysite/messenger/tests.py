from django.test import TestCase

# Create your tests here.
class MessengerTestCase(TestCase):
    fixtures = ['tests/users.json','tests/messages.xml']