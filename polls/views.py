from django.shortcuts import render_to_response , get_object_or_404, render, redirect
from polls.models import Poll, Choice
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from polls.forms import PollForm
from django.forms.models import inlineformset_factory

def create_poll(request, template='polls/create.html'):
    ChoiceFormSet = inlineformset_factory(Poll, Choice, extra=3)
    # If initial load of the page
    if not request.POST:
        form = PollForm()
        p = Poll()
        formset = ChoiceFormSet(instance=p)
    else:
        form = PollForm(request.POST)
        p = Poll()
        formset = ChoiceFormSet(request.POST, instance=p)

        if form.is_valid():
            p = form.save()
            formset.instance = p
            if formset.is_valid():
                formset.save()

            return redirect('poll_detail', p.id)

    return render(request, template, {'form': form, 'formset': formset})
    
def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
#redisplays poll voting form
        return render_to_response('polls/detail.html', {
            'poll' : p,
            'error_message' : "You didn't select a choice",
        }, context_instance=RequestContext(request))
    else:
        selected_choice.votes+=1
        selected_choice.save()

        return HttpResponseRedirect(reverse('poll_results', args=(p.id,)))
