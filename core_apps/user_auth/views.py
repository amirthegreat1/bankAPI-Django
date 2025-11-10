# TEST LOGGING
# from django.shortcuts import render
# from django.http import HttpResponse
# from django.views import View
# from loguru import logger
# from django.http import JsonResponse
# # Create your views here.
# class TestLogging(View):
#     def get(self, request):
#         logger.info("this is a debug message")
#         logger.error("this is an error message")
#         logger.warning("this is a warning message")
#         logger.critical("this is a critical message")
#         logger.debug("this is a debug message")
#         return JsonResponse({"message": "we are testing logging"})