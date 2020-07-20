from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index2(request):
    # return HttpResponse("Home")
    
    return render(request,'index2.html')

def home(request):
    return HttpResponse("Home")

# code for remove punctuation else convert string to uppercase
def analyze(request):
    
    # get the text from index2.html
    djtext=request.POST.get('text','default')
    print(djtext)

    # check checkbox value
    removepunc=request.POST.get('removepunc','off')
    capitalized=request.POST.get('fullycapitalized','off')
    newlineremove=request.POST.get('newlineremover','off')
    # extraspaceremove=request.POST.get('extraspaceremover','off')
    charactercount=request.POST.get('charcount','off')

    # check which checkbox is on
    if removepunc=="on":
        analyzed=""
        punctuations=''';()-[]{};;'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        p={'purpose':'Remove punctuation','analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',p)

    if capitalized=='on':
        analyzed=''
        for char in djtext:
            analyzed=analyzed+char.upper()
        p={'purpose':'Uppercase','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',p)
        
    if newlineremove=='on':
        analyzed=''
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed=analyzed+char
        p={'purpose':'Remove new line','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',p)
    # if extraspaceremove=='on':
    #     analyzed=''
    #     for index,char in enumerate(djtext):
    #         if not(djtext[index]==" " and djtext[index+1]==" "):
    #             analyzed=analyzed+char
                
            
                
    #     p={'purpose':'Remove new line','analyzed_text':analyzed}
    #     djtext=analyzed
        # return render(request,'analyze.html',p)
    
    if charactercount=='on':
        count=0
        analyzed=''
        for char in djtext:
            analyzed=analyzed+char
            if analyzed!=" ":
                count=len(analyzed)
        p={'purpose':'Remove new line','analyzed_text':analyzed,'count':count}
        
    if(removepunc != "on" and newlineremove!="on" and charactercount!='on' and capitalized!='on'):
        return HttpResponse('Please select any operation and try again')


    
        # else:
        #     return HttpResponse("ERROR")
    return render(request,'analyze.html',p)
    

    


