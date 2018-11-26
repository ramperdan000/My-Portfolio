running = True
while running == True:

	print("Please open your terminal to full screen.")
	print("""
 	   ____                                  ____  _         _                   _____                                   _    _                   __ ____                                   _    _                
	  / ___| __ _   ___  ___   __ _  _ __   / ___|(_) _ __  | |__    ___  _ __  | ____| _ __    ___  _ __  _   _  _ __  | |_ (_)  ___   _ __     / /|  _ \   ___   ___  _ __  _   _  _ __  | |_ (_)  ___   _ __   
	 | |    / _` | / _ \/ __| / _` || '__| | |    | || '_ \ | '_ \  / _ \| '__| |  _|  | '_ \  / __|| '__|| | | || '_ \ | __|| | / _ \ | '_ \   / / | | | | / _ \ / __|| '__|| | | || '_ \ | __|| | / _ \ | '_ \  
	 | |___| (_| ||  __/\__ \| (_| || |    | |___ | || |_) || | | ||  __/| |    | |___ | | | || (__ | |   | |_| || |_) || |_ | || (_) || | | | / /  | |_| ||  __/| (__ | |   | |_| || |_) || |_ | || (_) || | | | 
	  \____|\__,_| \___||___/ \__,_||_|     \____||_|| .__/ |_| |_| \___||_|    |_____||_| |_| \___||_|    \__, || .__/  \__||_| \___/ |_| |_|/_/   |____/  \___| \___||_|    \__, || .__/  \__||_| \___/ |_| |_| 
                                                         |_|                                                   |___/ |_|                                                          |___/ |_|                   """)        
                                                                                                                                                                                   
	print("\033[1m Welcome to the Caesar Cipher Encryption/Decryption Machine! \033[0m")
	input("Press Enter to Continue")

	encrypting = True
	while encrypting == True:

		clear_text = input("Please enter your message. ")
		shift = int(input("Enter a shift value. The range is 1-26. "))
		print("")
		input("Press enter to continue.")
		print("|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")

	
		cipher_text = ""
	
		for c in clear_text:
		
			if c.isalpha():
				print(c)
				current = ord(c)
		
				if current > 96:
					current = ord(c) - 96
					current += shift
					current = current % 26
					current = chr(current + 96)
					cipher_text += current
					print(cipher_text)
					
				else:
					current = ord(c) - 64
					current += shift
					current = current % 26
					current = chr(current + 64)
					cipher_text += current
					print(cipher_text)

			else:
				cipher_text += c

		Go_Forwards = input("Would you like to decrypt the message? Type 'Yes' or 'No'. ")
		Go_Forwards = Go_Forwards.lower()

		if Go_Forwards == "yes":
			encrypting = False
		
		elif Go_Forwards == "no":
			print("Taking you back to the start of the program.")
			input("Press enter to continue.")
		
		else:
			print("I'm sorry, I didn't understand that. We are taking you back to the start of the program.")
			input("Press enter to continue.")


	decrypting = True
	while decrypting == True:
			
		decoded_text = ""

		for c in cipher_text:
			
			if c.isalpha():
				print(c)
				current = ord(c)
				
				if current > 96:
					current = ord(c) - 97
					current = current - shift
					current = current % 26
					current = chr(current + 97)
					decoded_text += current
					print(decoded_text)

				else:
					current = ord(c) - 65
					current = current - shift
					current = current % 26
					current = chr(current + 65)
					decoded_text += current
					print(decoded_text)
			else:
				decoded_text += c
		
		print(decoded_text)
		input("Press enter to continue.")
		
		Go_Backwards = input("Would you like to go back to the start or exit the program? Press enter to exit or type 'Yes' to re-run the program. ")
		Go_Backwards = Go_Backwards.lower()
		
		if Go_Backwards == "yes":
			encrypting = False
			decrypting = False
			input("Press enter to return to the start.")

		else:
			running = False
			encrypting = False
			decrypting = False
			input("Press enter to exit.")



			


	

	
