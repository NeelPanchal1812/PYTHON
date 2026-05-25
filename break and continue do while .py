#break statement enables a programme to skip over a part of the code j loop ma hoy ene break kri de 6
for i in range(12):
     if(i==10):
        break
     print("5 *",i+1,"=",5*(i+1))
  
     
print("loop ne chodi didhu")

#continue ma iteration ne chodi deshe

for i in range(12):
     if(i==10):
        print("skip iteration")
        continue
     print("5 *",i,"=",5*(i))



# DO WHILE LOOP
     i=0
while True:
    print(i)
    i=i+1
    if(i%100 == 0):
        break