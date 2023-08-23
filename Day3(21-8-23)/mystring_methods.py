ex ="This is learning!!"
ex1 ="you should practice!"
ex2="Tanvi1234"
ex3 ="Janvi\nJaipur"

print("String is::" , ex + "\n")
print("len:: " ,len(ex))    #Give length
print("lower:: ",ex.lower()) #covert every letter into small letter
print("upper:: ",ex.upper()) #covert every letter into capital
print("title:: ",ex.title()) # camelcase
print("strip:: " ,ex.strip()) # remove white space from begining
print("split:: " ,ex.split()) # separate with ,
print("find:: " ,ex.find("is")) # return index of first occurence
print("index:: " ,ex.index("is")) # return index of first occurence
print("rstrip:: " ,ex.rstrip("!")) # remove trailling character
print("replace:: " ,ex.replace("learning","process")) # swap with given word
print("capitalize:: " ,ex1.capitalize()) # first letter capital
print("center:: " ,ex1.center(40))  # move towords center

# print(len(ex1))
# print(len(ex1.center(40)))

print("count:: " ,ex.count("!")) #no of given string present
print("endswith:: " ,ex.endswith("!!")) # check end of the string
print("enswith:: " ,ex.endswith("ing" ,13,16)) #slicing &  check end of string
print("isalnum:: " ,ex2.isalnum()) #cehck for A-Z,a-z,0-9
print("isalpha:: " ,ex.isalpha()) #check for A-Z,a-z
print("isprintable:: ", ex3.isprintable()) #false for escape character
print("swapcase:: " ,ex.swapcase()) #change the case
print("startswith:: ", ex.startswith("This"))

ex = "Janvi is learner"

ex1 = ex.split(" ")

print("_".join(ex1))



