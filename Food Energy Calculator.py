import math
print ("Food Energy Calculator\n")

# This is code created to calculated total energy used to raise 
# temperature of water from room temperature to boiling.


# This part takes inputs for specific heat and returrns the value to J/kg.

def Joules(original):
   if type(original) == float:
      new = original*80
      print str(new) + " J/kg"
      return new
   else:
      print ("You enter a value! :/ ")
      return -1 # This means that code did not work.

# This part takes inputs for density and returns the value to kg.

def Mass(original1):
   if type(original1) == float:
      new1 = (original1*0.0002365)
      print str(new1) + " kg is your mass."
      return new1
   else:
      print ("You enter a value! :/ ")
      return -1 # This means that code did not work.


# This part takes the outputs for Mass() and Joules() to return a value in J.  
  
def main():
   original = float(raw_input ("Please enter specific capacity (J/kg*K)for item.\t"))
   original1 = float(raw_input ("Please enter density (kg/m^3) for item.\t"))
   mass = Mass(original)
   joules = Joules(original1)  
   print str((mass * joules)/1000) + " J is you energy!"

main()
      

