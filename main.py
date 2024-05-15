# Main part
def main(): 
  
  argv=sys.argv
  if len(argv) != 2:
    print("Usage: python", argv[0], "initial_time")
    sys.exit(1)
    
  print("Begin DataBase start at", argv[1])
  
  datazero = DataBase(initialTime = int(argv[1]), user="Nare", password="Nare", host="localhost", database="datazero2")
  datazero.run()
  datazero.closeDataZeroApp()
  
  print("End DataBase started at", argv[1])
  
  sys.exit(0)
  
if __name__ == "__main__":
  print("Starting")
  main()
