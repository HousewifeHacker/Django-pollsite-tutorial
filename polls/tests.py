"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test import client
from polls.models import Poll, Choice
from datetime import datetime
from django.core.urlresolvers import reverse
from django.test.client import Client

class PollCountTest(TestCase):
    def test_poll_increases_count(self):
        poll = Poll(question='What is your favorite color?',
                pub_date=datetime.now())
        poll.save()

        choice1 = Choice(poll=poll, choice='Blue', votes=0)
        choice2 = Choice(poll=poll, choice='red', votes=0)

        choice1.save()
        choice2.save()
        c = Client()

        response = c.post(reverse('vote', args=(poll.id, )),
                {'choice': choice1.id,}, follow=True)
#        result_choice = Choice.objects.get(pk=choice1.id)
        result_choice = response.context['object'].choice_set.get(pk=choice1.id)
        self.assertRedirects(response, reverse('poll_results', args=(poll.id,)))
        self.assertEqual(result_choice.votes, 1)
