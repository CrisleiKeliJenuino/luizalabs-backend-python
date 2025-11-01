linguagens = ["python", "js", "C", "java", "csharp"]
linguagens.sort() # Ordena a lista em ordem alfabética ['C', 'csharp', 'java', 'js', 'python']

linguagens = ["python", "js", "C", "java", "csharp"]
linguagens.sort(reverse=True) # Ordena a lista em ordem alfabética reversa ['python', 'js', 'java', 'csharp', 'C']  

linguagens = ["python", "js", "C", "java", "csharp"]
linguagens.sort(key=lambda x: len(x)) # Ordena a lista pelo tamanho das strings ['C', 'js', 'java', 'python', 'csharp']

linguagens = ["python", "js", "C", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True) # Ordena a lista pelo tamanho das strings em ordem reversa ['csharp', '