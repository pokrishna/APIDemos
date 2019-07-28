from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.generic import View
from myapp.mixins import JsonResponseMixin
import io
import json
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from myapp.models import Employee
from myapp.serializers import EmployeeSerializer,NameSerializer,EmployeeModelSerailizer
from django.core.serializers import serialize
from myapp.mixins import SerializeMixin,HttpresponseMixin
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from myapp.utils import is_json
from myapp.forms import EmployeeForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import generics

# Hai Small update and github
# Hai
# Hai
# Hai

#updated from Git Examples

class TestAPIView2(APIView):
    def get(self,request,format=None):
        qs=Employee.objects.all()
        serializer=EmployeeModelSerailizer(qs,many=True)
        return Response(serializer.data)

class EmployeeListAPIView(generics.ListAPIView):
    #queryset=Employee.objects.all()
    serializer_class=EmployeeModelSerailizer
    def get_queryset(self):
        qs=Employee.objects.all()
        name=self.request.GET.get('ename')
        if name is not None:
            qs=qs.filter(ename__icontains=name)
        return qs

class EmployeeCreateAPIView(generics.CreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeModelSerailizer
    










class TestApiView(APIView):
    def get(self,request,format=None):
        colors=['red','blue','green','yellow','indigo']
        return Response({'msg':'welcome to colorful year','color':colors})
    def post(self,request):
        serializer=NameSerializer(data=request.data)
        if serializer.is_valid():
            name=serializer.data.get('name')
            msg='Hello {} wish you happy new year !!!'.format(name)
            return Response({'msg':msg})
        return Response(serializer.errors,status=400)

    def put(self,request,pk=None):
        return Response({'msg':"Response from put method"})
    def patch(self,request,pk=None):
        return Response({'msg':"Response from patch"})
    def delete(self,request,pk=None):
        return Response({'msg':"Response from delete method"})

class TestViewSet(viewsets.ViewSet):
    def list(self,request):
        colors=['Red','Green','Yellow','Orange']
        return Response({'msg':'Which you colorful life in 2019','color':colors})

    def create(self,request):
        serializer=NameSerializer(data=request.data)
        if serializer.is_valid():
            name=serializer.data.get('name')
            msg='Hello {} your life will be settled in 2019'.format(name)
            return Response({'msg':msg})
        return Response(serializer.errors,status=400)

    def retrieve(self,request,pk=None):
        return Response({'msg':'Response from retrieve method'})

    def update(self,request,pk=None):
        return Response({'msg':'Response from update'})

    def partial_update(self,request,pk=None):
        return Response({'msg':'Response from partial update'})

    def destroy(self,request,pk=None):
        return Response({'msg':'Response from destroy method'})




@method_decorator(csrf_exempt,name='dispatch')
class EmpCBV3(SerializeMixin,HttpresponseMixin,View):
    def get_object_by_id(self,id):
        try:
            obj=Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            obj=None
        return obj

    def get(self,request,*args,**kwargs):
        data=request.body
        if not is_json(data):
            return self.render_to_http_response(json.dumps({'msg':'Please provide json_data'}),status=400)
        pdata=json.loads(request.body)
        id=pdata.get('id',None)
        if id is not None:
            emp=self.get_object_by_id(id)
            if emp is None:
                return self.render_to_http_response(json.dumps({'msg':"Object does not exits"}))
            json_data=self.serialize([emp,])
            return self.render_to_http_response(json_data)
        qs=Employee.objects.all()
        json_data=self.serialize(qs)
        return self.render_to_http_response(json_data)

    def post(self,request,*args,**kwargs):
        data=request.body
        if not is_json(data):
            return self.render_to_http_response(json.dumps({'msg':'please send valid json'}),status=400)
        pdata=json.loads(request.body)
        form=EmployeeForm(pdata)
        if form.is_valid():
            form.save(commit=True)
            return self.render_to_http_response(json.dumps({'msg':'employee save successfully'}),status=200)
        if form.error:
            json_data=json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)

    def put(self,request,*args,**kwargs):
        data=request.body
        if not is_json(data):
            return self.render_to_http_response(json.dumps({'msg':'please send valid json'}),status=400)
        pdata=json.loads(request.body)
        id=pdata.get('id',None)
        if id is None:
            return self.render_to_http_response(json.dumps({'msg':'please send me id '}),status=400)
        emp=self.get_object_by_id(id)
        if emp is None:
            return self.render_to_http_response(json.dumps({'msg':'Object Does not DoesNotExistq1'}),status=400)
        original_data={
        'eno':emp.eno,
        'ename':emp.ename,
        'esal':emp.esal,
        'passw':emp.passw,
        'rpass':emp.rpass
        }
        original_data.update(pdata)
        form=EmployeeForm(original_data,instance=emp)
        if form.is_valid():
            form.save(commit=True)
            return self.render_to_http_response(json.dumps({'msg':"Record updated successfully"}))
        if form.errors:
            json_data=json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)

    def delete(self,request,*args,**kwargs):
        data=request.body
        if not is_json(data):
            return self.render_to_http_response(json.dumps({'msg':'pls send me valid data'}),status=400)
        data=json.loads(request.body)
        id=data.get('id',None)
        if id is None:
            return self.render_to_http_response(json.dumps({'msg':'pls send me id'}),status=400)
        obj=self.get_object_by_id(id)
        if obj is None:
            json_data=json.dumps({'msg':'object does not exits'})
            return self.render_to_http_response(json_data,status=400)
        status,deleted_item=obj.delete()
        if status==1:
            json_data=json.dumps({'msg':'Record Deleted successfully'})
            return self.render_to_http_response(json_data)
        json_data=json.dumps({'msg':'unable to belete the record'})
        return self.render_to_http_response(json_data,status=500)


# @method_decorator(csrf_exempt,name='dispatch')
# class EmpCBV(HttpresponseMixin,SerializeMixin,View):
#     def get_object_by_id(self,id):
#         try:
#             emp=Employee.objects.get(id=id)
#         except Employee.DoesNotExist:
#             emp=None
#         return emp
#     def get(self,request,*args,**kwargs):
#         data=request.body
#         if not is_json(data):
#             return self.render_to_http_response(json.dumps({'msg':'please send a valid Json data only'}),status=400)
#         data=json.loads(request.body)
#         id=data.get('id',None)
#         if id is not None:
#             obj=self.get_object_by_id(id)
#             if obj is None:
#                 return self.render_to_http_response(json.dumps({'msg':'No matching record found for specific id'}),status=404)
#             json_data=self.serialize([obj,])
#             return self.render_to_http_response(json_data)
#         qs=Employee.objects.all()
#         json_data=self.serialize(qs)
#         return self.render_to_http_response(json_data)
#
#     def post(self,request,*args,**kwargs):
#         json_data=request.body
#         if not is_json(json_data):
#             return self.render_to_http_response(json.dumps({'msg':'Please send me valid Json data only '}),status=400)
#         data=json.loads(request.body)
#         form=EmployeeForm(data)
#         if form.is_valid():
#             obj=form.save(commit=True)
#             return self.render_to_http_response(json.dumps({'msg':'resource created successfully'}))
#         if form.errors:
#             json_data=json.dumps(form.errors)
#             return self.render_to_http_response(json_data,status=400)
#
#     def put(self,request,*args,**kwargs):
#         data=request.body
#         if not is_json(data):
#             return self.render_to_http_response(json.dumps({'msg':'Please Send me the Json_data'}),status=400)
#         data=json.loads(request.body)
#         id=data.get('id',None)
#         if id is None:
#             return self.render_to_http_response(json.dumps({'msg':'ID is mandatary'}),status=400)
#         obj=self.get_object_by_id(id)
#         if obj is None:
#             json_data=json.dumps({'msg':'Object is does not exist'})
#             return self.render_to_http_response(json_data,status=404)
#         new_data=data
#         old_data={'eno':obj.eno,'ename':obj.ename,'esal':obj.esal,'passw':obj.passw,'rpass':obj.rpass}
#         old_data.update(new_data)
#         form=EmployeeForm(old_data,instance=obj)
#         if form.is_valid():
#             form.save(commit=True)
#             json_data=json.dumps({'msg':'Updated successfully'})
#             return self.render_to_http_response(json_data,status=201)
#         if form.errors:
#             json_data=json.dumps(form.error)
#             return self.render_to_http_response(json_data,status=400)
#
#     def delete(self,request,*args,**kwargs):
#         data=request.body
#         if not is_json(data):
#             json_data=json.dumps({'msg':'Not a valid Json Data'})
#             return self.render_to_http_response(json_data,status=400)
#         data=json.loads(request.body)
#         id=data.get('id',None)
#         if id is None:
#             json_data=json.dumps({'msg':'Require Id for delete'})
#             return self.render_to_http_response(json_data,status=400)
#         obj=self.get_object_by_id(id)
#         if obj is None:
#             json_data=json.dumps({'msg':'Object Not found'})
#             return self.render_to_http_response(json_data,status=404)
#         status,deleted_item=obj.delete()
#         if status==1:
#             json_data=json.dumps({'msg':'resource Deleted'})
#             return self.render_to_http_response(json_data,status=201)
#         json_data=json.dumps({'msg':'resouce unable to delete try again'})
#         return self.render_to_http_response(json_data,status=500)
#
#
#

# Emp={'eno':101,'ename':'Krishna'}
#
# def rhttp(request):
#     resp="<h1> The Emp No :{}<br> The Emp Name :{}".format(Emp['eno'],Emp['ename'])
#     return HttpResponse(resp)
#
# def rjson(request):
#     return JsonResponse(Emp)

class EmployeeCBV(View):
    def get(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pdata=JSONParser().parse(stream)
        print(pdata)
        id=pdata.get('id',None)
        if id is not None:
            emp=Employee.objects.get(id=id)
            serialize=EmployeeSerializer(emp)
            json_data=JSONRenderer().render(serialize.data)
            return HttpResponse(json_data,content_type='application/json')
        qs=Employee.objects.all()
        serialize=EmployeeSerializer(qs,many=True)
        json_data=JSONRenderer().render(serialize.data)
        return HttpResponse(json_data,content_type='application/json')
    def post(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pdata=JSONParser().parse(stream)
        serializer=EmployeeSerializer(data=pdata)
        if serializer.is_valid():
            serializer.save()
            msg={"msg":"resource created successfully"}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type="application/json")
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

    def put(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        data=JSONParser().parse(stream)
        id=data.get('id')
        emp=Employee.objects.get(id=id)
        serializer=EmployeeSerializer(emp,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            msg={'msg':'resource updataed successfully'}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.error)
        return HttpResponse(json_data,content_type='application/json')
