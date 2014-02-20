from django.shortcuts import render
import random

nomes = ['Paulo', 'Calhau', 'Renan', 'Coutinho', 'Possati', 'Phillipi',
			'Breno', 'Ivana', 'Marcos']

def home(request):
	return render(request, 'index.html',
		{'nome': random.choice(nomes)})

def integrantes(request):
	return render(request, 'integrantes.html',
		{'nome': random.choice(nomes)})
