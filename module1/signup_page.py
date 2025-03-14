x = 5
#print("hello")
def print_lyrics():
    print("i am a jack")
    print("i sleep all night and work all day")

#print("yo")
#print_lyrics()
#x = x + 2 
#print(x)    

#def greet():
#    return "Hello"
#print(greet(),"Glenn")
#print(greet(), "Sally")


#while True:
    #line = input(">")
    #if line == "done":
    #    break
    #print(line)
#print("done")    

#zork = 0 
#print("before", zork)
#for thing in [9,41,12,3,74,15] :
#    zork = zork + thing
#    print(zork, thing)
#print("After", zork)    
  

fhand = open("syntax.text") 
count = 0 
for line in fhand :
    count = count + 1 
    print("line count:", count)