item_cart=0
# Example 1 Method to FAIL ///////////////////////////////////////////////////////////////////////////////////////////
# if item_cart !=2:
#     raise Exception("Number of products don't match")
# Example 2 Method to FAIL //////////////////////////////////////////////////////////////////////////////////////////
# assert (item_cart==2)
# Example 3 Method to PASS /////////////////////////////////////////////////////////////////////////////////////////
# we can have a custom message(with simple except), or we can use Exception, and we will see the specific reason
try:
    fh = open("non-existing-file.txt")
except Exception as e:
    print(e)
#     this part is always executed (one purpose is to clear something for ex)
finally:
    print("cleaning up resources")
