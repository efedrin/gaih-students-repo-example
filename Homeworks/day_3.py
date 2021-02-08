username = "user"
password = "1234"

log_id = input("Please enter your username: ")
log_pass = input("Please enter your password: ")

if log_id != username and log_pass == password:
  print("Invalid username, try again!")
elif log_id == username and log_pass != password:
  print("Invalid password, try again!")
elif log_id != username and log_pass != password:
  print("Invalid username and password, try again!")
else:
  print("Login successful")
