a = int(input())
for i in range(1, a+1):
  string = str(input())
  reverse = ''
  stack =[]
  for j in range(0, len(string)):
    if string[j] == ' ':
      while(stack):
        alphabet = stack.pop()
        reverse = reverse + alphabet
      reverse = reverse + ' '
      stack = []
    else:
      stack.append(string[j])
  if stack:
     while(stack):
        alphabet = stack.pop()
        reverse = reverse + alphabet
  print(reverse)