my_library=[]

my_wish=[]

my_library.append(input("Enter the name of a book you win "))

anther_book_win=input("Enter the name of anther book you win(or press(Enter)to skip)\n")

if anther_book_win:

    my_library.append(anther_book_win)
    print("your library is")
    print(my_library)    
   
else:
    print("you library"+  my_library)    

my_wish.append(input("Enter the name of a book you wish to have in futuer:\n"))

anther_wish=input("Enter the name of anther book you wish to have in futuer:(or press(Enter)to skip)\n")
if anther_wish:
    my_wish.append(anther_wish
                   )
    print("your wishlist")
    print( my_wish)

else:
    
    print("your wishlist")
    print( my_wish)

        
wish_done=input("Enter the name of book form your wishlist that you have :(or press(Enter)to skip)\n"
                )
if wish_done:
    my_wish.remove(wish_done
                   )

    my_library.append(wish_done)

    print("updated library")

    print( my_library
          )
    print("updated wishlist")
    print(my_wish
              )
else:

    print("updated library")

    print( my_library
              )
    print("updated wishlist")
    
    print(my_wish
                  )
donate_book=input("Enter a name of book from your library you wish to donate:(or press(Enter)to skip)\n")

if donate_book in my_library:

    my_library.remove(donate_book)

    print("final library after dontions")

    print( my_library)

else:


    print("your library is"
          
          )

    
    print(my_library
          )
