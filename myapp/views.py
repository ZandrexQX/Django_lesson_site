from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.info("Index page open")
    return render(request, 'main.html')


def about(request):
    logger.info("Index page open")
    return render(request, 'about.html')
