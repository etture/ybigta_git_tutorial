import fire

def multiply(a, n):
	answer = 0
	for i in range(n):
		answer += a
	return answer


if __name__ == '__main__':
	fire.Fire(multiply)
