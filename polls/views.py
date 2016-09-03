from django.shortcuts import render
from .models import Question, Choice
from django.template import loader
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect	
from django.urls import reverse



def index(request):
	question_list=Question.objects.order_by('-pub_date')[:5]
	template=loader.get_template('polls/index.html')
	context={
	'question_list': question_list,
	}
	return HttpResponse(template.render(context, request))
    

def detail(request,question_id):
	question=get_object_or_404(Question,pk=question_id)
	try:
		select_question=question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html',{'question':question, 'error_message': "You didn;t select "})
	else:
		select_question.vote+=1
		select_question.save()
		return(reverse('polls/results',args=(question.id,)))


def result(request, question_id):
	return HttpResponse("You are seeing the result page")

def vote(requst, question_id):
	return HttpResponse("You are voting on the question %s" % question_id)