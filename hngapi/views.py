import numbers

from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.


user = {
    "slackUsername": "Oluwatobiloba777",
    "backend": True,
    "age": 26,
    "bio": "I'm a backend developer"
}



@api_view(['GET'])
def hngUser(request):
    if request.method == 'GET':
        return Response(user)


@api_view(['POST'])
def calculate(request):
    data = request.data
    operation_type = str(data['operation_type'])
    try:
        firstNumber = data['x']
    except KeyError:
        firstNumber = ''
    try:
        secondNumber = data['y']
    except KeyError:
        secondNumber = ''
    message = ''

    # addittion
    if operation_type.strip().lower() == 'addition':
        if firstNumber and secondNumber:
            result = firstNumber + secondNumber
        else:
            try:
                firstNumber = int(numbers[0])
                secondNumber = int(numbers[1])
                operation_type = 'addition'
                result = firstNumber + secondNumber
            except IndexError:
                message = 'provide 2 valid numbers'

    # subtraction
    elif operation_type.strip().lower() == 'subtraction':
        if firstNumber and secondNumber:
            result = firstNumber - secondNumber
        else:
            try:
                firstNumber = int(numbers[0])
                secondNumber = int(numbers[1])
                operation_type = 'subtraction'
                result = firstNumber - secondNumber
            except IndexError:
                message = 'provide 2 valid numbers'

    # multiplication

    elif operation_type.strip().lower() == 'multiplication':
        if firstNumber and secondNumber:
            result = firstNumber * secondNumber
        else:
            try:
                firstNumber = int(numbers[0])
                secondNumber = int(numbers[1])
                operation_type = 'multiplication'
                result = firstNumber * secondNumber
            except IndexError:
                message = 'provide 2 valid numbers'

    if message:
        answer = {
            "slackUsername": "Oluwatobiloba777",
            "message": "Error" + message
        }
    else:
        answer = {
            "slackUsername": "Oluwatobiloba777",
            "result": result,
            "operation_type": operation_type
        }

    return Response(answer)
