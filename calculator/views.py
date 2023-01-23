from django.shortcuts import render


def check_sign_and_perform_action(sign, num_1, num_2):
	"""Check sign and perform action."""

	if sign == '+':
		answer = num_1 + num_2
	elif sign == '-':
		answer = num_1 - num_2
	elif sign == '/':
		answer = num_1 / num_2
	elif sign == '*':
		answer = num_1 * num_2

	return answer


def calculate(request):
	"""Performing calculations."""

	# Create an empty value for "context".
	sign = None
	num_1 = None
	num_2 = None
	context = {}

	# Checking for user input.
	if request.GET.get("num_1") and request.GET.get("num_2"):
		num_1 = request.GET.get("num_1")
		num_2 = request.GET.get("num_2")
		sign = request.GET.get("sign")

		# Сheck if the user has entered numbers.
		try:
			num_1 = int(num_1)
			num_2 = int(num_2)

			# After checking, we save the data, perform actions on it and pass it to the template.the template.

			answer = check_sign_and_perform_action(sign, num_1, num_2)

		except:
			answer = "Вы ввели не цифры."
	else:
		answer = "Вы забыли ввести значения."

	context = {'answer': answer}

	return render(request, 'calculator/calculate.html', context)