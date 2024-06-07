from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from .serializers import (
    AccountSerializer, NguongcanhbaoSerializer, FactlichsugiaSerializer, FactchibaoSerializer
)
from .models import Account, Nguongcanhbao, Factlichsugia, Factchibao
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
import jwt, datetime
from django.contrib.auth.hashers import check_password
import jwt

# Chuc nang Login voi authentication
class LoginView(APIView):
    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]

        user = Account.objects.filter(username=username).first()
        acc = Account.objects.get(username=user.username)
        serializerUser = AccountSerializer(acc)

        if user is None:
            raise AuthenticationFailed("User not found")
        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password")

        payload = {
            "id": user.pk,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            "iat": datetime.datetime.utcnow(),
        }

        token = jwt.encode(payload, "secret", algorithm="HS256")

        response = Response()

        response.set_cookie(key="jwt", value=token, httponly=True)
        response.data = {"jwt": token, "account": serializerUser.data}
        return response

# ACCOUNT : GET , POST, PUT, DELETE : Option


class GetUserID(APIView):
    def get(self, request):
        pass


class UserRegisterView(APIView):
    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class UpdateUserView(APIView):
    def put(self, request, id):
        try:
            account = Account.objects.get(pk=id)
            serializer = AccountSerializer(account, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Account.DoesNotExist:
            return Response(
                {"message": "account not found"}, status=status.HTTP_404_NOT_FOUND
            )


class DeleteUserView(APIView):
    def delete(self, request):
        try:
            account = Account.objects.get(pk=id)
            account.delete()
            return Response({"message": "Delete account successfully"})
        except Account.DoesNotExist:
            return Response(
                {"message": "Account not found"}, status=status.HTTP_404_NOT_FOUND
            )


# nguong canh bao : GET, POST, PUT, DELETE

class GetNguongCanhBao(APIView):
    def get(self, request):
        nguongcanhbao = Nguongcanhbao.objects.all()
        serializer = NguongcanhbaoSerializer(nguongcanhbao, many=True)
        return Response({"nguongcanhbao": serializer.data})


class GetNguongCanhBao_Detail(APIView):
    def get(self, request, matk):
        nguongcanhbao = Nguongcanhbao.objects.filter(MaTaiKhoan=matk)
        serializer = NguongcanhbaoSerializer(nguongcanhbao, many=True)
        return Response({"nguongcanhbao": serializer.data})
    
class PostNguongCanhBao(APIView):    
    def post(self, request):
        serializer = NguongcanhbaoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class UpdateNguongCanhBao(APIView):    
    def put(self, request, id):
        try:
            nguongcanhbao = Nguongcanhbao.objects.get(pk=id)
            serializer = NguongcanhbaoSerializer(nguongcanhbao, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Nguongcanhbao.DoesNotExist:
            return Response(
                {"message": "Nguongcanhbao not found"}, status=status.HTTP_404_NOT_FOUND
            )

class DeleteNguongCanhBao(APIView):    
    def delete(self, request, id):
        try:
            nguongcanhbao = Nguongcanhbao.objects.get(pk=id)
            nguongcanhbao.delete()
            return Response({"message": "Delete nguongcanhbao successfully"})
        except Nguongcanhbao.DoesNotExist:
            return Response(
                {"message": "Nguongcanhbao not found"}, status=status.HTTP_404_NOT_FOUND
            )

# fact chi bao : GET

class GetFactchibao(APIView):
    def get(self, request):
        factchibao = Factchibao.objects.all()
        serializer = FactchibaoSerializer(factchibao, many=True)
        return Response({"factchibao": serializer.data})


class GetFactchibao_detail(APIView):
    def get(self, request, mack, loaichibao, ngaygiaodich):
        factchibao_detail = Factchibao.objects.filter(
                MaChungKhoan=mack,
                TenChiBao=loaichibao,
                NgayGiaoDich=ngaygiaodich
            )
        serializer = FactchibaoSerializer(factchibao_detail, many=True)
        return Response({"giatrichibao": serializer.data})
    

class GetFactlichsugia(APIView):
    def get(self, request):
        factlichsugia = Factlichsugia.objects.all()
        serializer = FactlichsugiaSerializer(factlichsugia, many=True)
        return Response({"factlichsugia": serializer.data})
    

class GetFactlichsugia_detail(APIView):
    def get(self, request, mack, ngaygiaodich):
        factlichsugia_detail = Factlichsugia.objects.filter(
                MaChungKhoan=mack,
                NgayGiaoDich=ngaygiaodich
            ).all()
        serializer = FactlichsugiaSerializer(factlichsugia_detail, many=True)
        return Response({"factlichsugia": serializer.data})
    