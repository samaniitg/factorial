from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import factorial


class FindFactorial(APIView):
    """ API to find factorial of input number """

    def get(self, request):
        """ API method to find factorial of input number """
        response = {}
        try:
            input_number = request.GET.get('input_number', None)
            if input_number:
                response["answer"]=factorial(int(input_number))
                return Response(response, status=status.HTTP_200_OK)
            else:
                response['message'] = "Provide input_number"
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            response = {}
            response['message'] = str(e)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)