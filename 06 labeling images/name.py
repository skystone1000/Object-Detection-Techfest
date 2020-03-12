import os 
  
# Function to rename multiple files 
def main(): 
    i = 134
      
    for filename in os.listdir("nopuppies"): 
        dst = str(i) + ".jpg"
        src = 'nopuppies/'+ filename 
        dst ='nopuppies/'+ dst 
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
        i += 1
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main()