linguagens = ["python", "js", "C", "java", "csharp"]

sorted(linguagens, key=lambda x: len(x)) # ["c", "js", "C", "java", "python", "csharp"]

sorted(linguagens, key=lambda x: len(x), reverse=True) # ["python", "csharp", "java", "js", "C", "c"]

print(sorted(linguagens))