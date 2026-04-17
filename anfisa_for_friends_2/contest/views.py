from django.shortcuts import render

from .forms import ContestForm


def proposal(request):
    form = ContestForm(request.GET or None)
    context = {'form':form}
    # if form.is_valid():
    #     title = form.cleaned_data['title']
    #     context.update({'title':title})
    return render(request, 'contest/form.html', context)


# def accepted(request):
#     return render(request, 'contest/proposal_accepted.html')