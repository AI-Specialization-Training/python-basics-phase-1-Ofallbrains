# ============================================================================
# TODO: Data Type Conversion 

#Create a function called data_type_conversion. 
# It takes two parameters, the value and the name of the data type requested, one of float, str, or int. 
# Return the converted value.
#Error handling: The function might be called with a bad parameter. 
# For example, the caller might try to convert the string "nonsense" to a float. 
# Catch the error that occurs in this case. If this error occurs, 
# return the string You can't convert {value} into a {type}., so again you use a formatted string.

# ============================================================================

def data_type_conversion(value, type):
    try:
        if type == "float":
            return float(value)
        if type == 'str':
            return str(value)
        if type == 'int':
            return int(value)
    except:
        return  f"You can't convert {value} into a {type}"
print(data_type_conversion("nonsense", "float"))