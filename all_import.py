from django.shortcuts import render ,redirect
from rest_framework import serializers
from django.http import  JsonResponse,HttpResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from django.db import IntegrityError
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta  ,date
from django.core.paginator import Paginator
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

import datetime
import json

from src.models import *