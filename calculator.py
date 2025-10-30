check = False 
while check == False:
    print(" welcome to a 4-function calculator")
    print("which function to excute")
    print("1. addition")                    
    print("2.subtraction")
    print("3. multiplcation") 
    print("4. divison") 
    print("5. quit ")
    option = input(" enter which functioon to excute") 
    if option.strip() == "1": 
        try:
            x = int(input("enter num 1: "))
            y = int(input(" enter number 2: ")) 
            sum = x + y 
            print(sum) 
        except ValueError: 
            print(" x and y must be numbers") 
        except TypeError: 
            print(" x and y must be integers")
        except TypeError:
                print("x and y must be integers")
        except Exception as e:
                print(e)
        finally:
                print("Thanks for using my calculator")
    elif option.strip() == "2":
            try:
                x = int(input("Enter Num 1: "))
                y = int(input("Enter Num 2: "))
                difference = x - y
                print(difference)
            except ValueError: 
                print("x and y must be numbers")
            except TypeError:
                print("x and y must be integers")
            except Exception as e:
                print(e)
            finally:
                print("Thanks for using my calculator")
    elif option.strip() == "3":
            try:
                x = int(input("Enter Num 1: "))
                y = int(input("Enter Num 2: "))
                product = x * y
                print(product)
            except ValueError: 
                print("x and y must be numbers")
            except TypeError:
                print("x and y must be integers")
            except Exception as e:
                print(e)
            finally:
                print("Thanks for using my calculator")
    elif option.strip() =="4":
            try:
                x = int(input("Enter Num 1: "))
                y = int(input("Enter Num 2: "))
                quotient = x / y
                print(quotient)
            except ValueError: 
                print("x and y must be numbers")
            except ZeroDivisionError:
                print("y must be nonzero")
            except TypeError:
                print("x and y must be integers")
            except Exception as e:
                print(e)
            finally:
                print("Thanks for using my calculator")
    elif option.strip() == "5":
            print("Goodbye")
            check = True
    else:
            print("Invalid option")
