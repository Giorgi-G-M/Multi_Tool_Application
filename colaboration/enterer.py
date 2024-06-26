from calculator import main_calculator, numbers
from to_do import main_to_do
from money import main_currency
from weather import weather_main,inputer
from register import *
from settings import *
from contact import *

def main():
      user_id = register_main()
      printer()
      choice = enter_program()
      orderer(choice,user_id[1])


def printer():
      print(f"1. TO DO\n"            
            f"2. Calculator\n"        
            f"3. Currency exchange\n"
            f"4. Weather forecast\n" 
            f"5. Contact information\n"      
            f"6. Settings")

def enter_program():
      choice = input("Now choose from 1 to 6 which one you want to use. or just click 'ENTER' edn program will end: ")
      return choice

def orderer(choice,id):
      if len(choice) == 1:
            if choice.isdigit():
                  if choice == "1":
                        print("You are in 'TO DO' application")
                        while True:
                              main_to_do()
                              another_try = input("If you want to create new to_do app enter yes/y, if not anything else. ").lower()
                              if another_try == "yes" or another_try =="y":
                                    pass
                              else:
                                    print("the proggram is over")
                                    break
                        printer()
                        choice = enter_program()
                        orderer(choice,id)

                  elif choice == "2":
                        print("You are in 'Calculator' application")
                        while True:
                              main_calculator(numbers())
                              again = input("If you want another calculations enter YES/Y, if not enter enything else: ")
                              if again.lower() == "y" or again.lower() == "yes":
                                    pass
                              else:
                                    print("The calculator proggram is over.")
                                    break
                        printer()
                        choice = enter_program()
                        orderer(choice,id)

                  elif choice == "3":
                        print("You are in currency 'Currency exchange' application")
                        while True:
                              main_currency()
                              another_try = input("You want to try again? YES/NO ").lower()
                              if another_try == "yes":
                                    pass
                              else:
                                    print("the proggram is over")
                                    break
                        printer()
                        choice = enter_program()
                        orderer(choice,id)

                  elif choice == "4":
                        print("You are in 'Weather forecast' application")
                        while True:
                              weather_main(inputer())
                              another_try = input("If you want to try another citi enter YES/Y, if not enter enything else. ").lower()
                              if another_try == "yes" or another_try =="y":
                                    pass
                              else:
                                    print("the proggram is over")
                                    break

                        printer()
                        choice = enter_program()
                        orderer(choice,id)

                  elif not choice:
                        print("End proggram.")
                  elif choice == "5":
                        print("You are in 'contact' application")
                        while True:
                              contact_main(id)
                              another_try = input("If you want to use this proggram again enter YES/Y, if not enter enything else.").lower()
                              if another_try == "yes" or another_try =="y":
                                    pass
                              else:
                                    print("the proggram is over")
                                    break
                        printer()
                        choice = enter_program()
                        orderer(choice,id)
                  elif choice == "6":
                        print("You are in 'settings' application")
                        while True:
                              settings_main(id)
                              another_try = input("If you want to use again the Settings proggram enter YES/Y, if not enter enything else.").lower()

                              if another_try == "yes" or another_try =="y":
                                    pass
                              else:
                                    print("the proggram is over")
                                    break
                        printer()
                        choice = enter_program()
                        orderer(choice,id)

                  else:
                        print("Something went wrong in your input.")

if __name__ == "__main__":
      main()