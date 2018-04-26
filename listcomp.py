def minPassword(password):
    lower = [x for x in password if x.islower()]
    upper = [x for x in password if x.isupper()]
    nums = [x for x in password if x.isdigit()]
    return len(lower) > 0 and len(upper) > 0 and len(nums) > 0

def strength(password):
    lower = [x for x in password if x.islower()]
    upper = [x for x in password if x.isupper()]
    nums = [x for x in password if x.isdigit()]
    syms = [x for x in password if not x.isalnum()]

    #additions
    char_score = len(password) * 4
    lower_score = 0
    if len(lower) > 0:
        lower_score = (len(password) - len(lower)) * 2
    upper_score = 0
    if len(upper) > 0:
        upper_score = (len(password) - len(upper)) * 2
    num_score = len(nums) * 4
    sym_score = len(syms) * 6

    criteria = 0
    if len(lower) > 0:
        criteria += 1
    if len(upper) > 0:
        criteria += 1
    if len(nums) > 0:
        criteria += 1
    if len(syms) > 0:
        criteria += 1
    if len(password) >= 8:
        criteria += 1
    requirement_score = 0
    if criteria >= 4:
        requirement_score = criteria * 2

    #deductions
    lettersonly_score = 0
    if (len(lower) > 0 or len(upper) > 0) and len(nums) == 0 and len(syms) == 0:
        lettersonly_score = len(password)
    numbersonly_score = 0
    if len(lower) == 0 and len(upper) == 0 and len(nums) > 0 and len(syms) == 0:
        numbersonly_score = len(password)

    print "---"
    print password
    #print "char_score: " + str(char_score)
    #print "lower_score: " + str(lower_score)
    #print "upper_score: " + str(upper_score)
    #print "num_score: " + str(num_score)
    #print "sym_score: " + str(sym_score)
    #print "requirement_score: " + str(requirement_score)
    #print "lettersonly_score: -" + str(lettersonly_score)
    #print "numbersonly_score: -" + str(numbersonly_score)
    total_score = char_score + lower_score + upper_score + num_score + sym_score + requirement_score - lettersonly_score - numbersonly_score
    #print "*****TOTAL SCORE: " + str(total_score) + "*****"
    if total_score / 10 > 10:
        return "=====SCALED SCORE: 10====="
    else:
        return "=====SCALED SCORE: " + str(total_score / 10) + "====="
        

print minPassword("aA2") #True
print minPassword("aAA2") #True
print minPassword("a2") #False
print minPassword("A2") #False
print minPassword("aA") #False
print minPassword("aaaaaa2") #False
print minPassword("AAAAAA2") #False
print minPassword("aaaAAA22") #True

print strength("test")
print strength("Test")
print strength("password")
print strength("password2")
print strength("hunter2")
print strength("Pass.Word2")
