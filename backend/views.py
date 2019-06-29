from django.shortcuts import render

from django.shortcuts import HttpResponse
from django.http import HttpResponse
import  json
from django.http import JsonResponse
# Create your views here.


# def test(request):
#     response = {}
#     response['msg'] = 'success'
#     # return JsonResponse(response)
#
#     resp = {'ok':12}
#     return HttpResponse(json.dump(resp),content_type="application/json")


def testapi(request):
	print(request)
	print(request.method)
	if request.method == "GET":
		print(request.GET.get('aa'))
		resp = {'errorcode': 100, 'type': 'Get', 'data': {'main': request.GET.get('aa')}}
		return HttpResponse(json.dumps(resp), content_type="application/json")
	else:
		print(request.POST)
		print(request.body)
		str1=str(request.body, encoding = "utf-8")
		data=eval(str1)
		print(data)
		print(data['aa'])
		print(type(request.body))
		resp = {'errorcode': 100, 'type': 'Post', 'data': {'main': data['aa']}}
		return HttpResponse(json.dumps(resp), content_type="application/json")

