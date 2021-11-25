def Trijstūris():
  a= int(input("ievadi trijstūra pamata garumu"))
  h= int(input("ievadi trijstūra augstumu"))
  S= (a*h)/2
  print("trijastūra laukums ir", S)
def trapece():
  a= int(input("ievadi vienas trapeces pamata garumu"))
  b= int(input("ievadi otras trapeces pamata garumu"))
  h= int(input("ievadi trapeces augstumu"))
  S= (a+b)*h/2
  print("trapeces laukums ir", S)
def palalelograms():
  a= int(input("ievadi palalelograma pamata garumu"))
  h= int(input("ievadi augstumu kurš novilkts pret pamatu "))
  S= a*h
  print("palalelograma laukums ir", S)
print("Lai aprēķināu laukumu nepieciešamai tev figūrai lūdzu nospied burtu kurš tai atbilst")
print("T - ja figūra kaurai vēlies aprēķināt laukumu ir trijstūris")
print("Tr - ja figūra kaurai vēlies aprēķināt laukumu ir trapece")
print("P - ja figūra kaurai vēlies aprēķināt laukumu ir paralelograms")
print("Ta - ja figūra kaurai vēlies aprēķināt laukumu ir taisnstūris")
print("K - ja figūra kaurai vēlies aprēķināt laukumu ir kvadrāts")
print("R - ja figūra kaurai vēlies aprēķināt laukumu ir riņķis")
print("ievadi savu burtu:")
x = input()
if x == "T" :
  Trijstūris()
elif x =="Tr" :
  trapece()
elif x =="P" :
  palalelograms()
  


