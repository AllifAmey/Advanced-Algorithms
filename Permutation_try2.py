#Permutationtry2.

""" DESCRIPTION:

Where I got the algorithm from: https://www.freecodecamp.org/challenges/no-repeats-please

This algorithm:
1. You give me your input in the form of a string.
2. I will treat every individual character of the string as being unique.
3. I will then find the most amount of "unique" combinations I can make with the string.
4. If any of the "unique" combinations are found to contain consecutive letters, they will be removed.
5. I will then return the "unique" combinations.
"""

#Factorise.

def factorial(number):
    empty_number = 1
    for number in list(range(0, number+1)):
        if number == 0:
            continue
        empty_number *= number
    
    return empty_number

dogmire = list(range(10, 0, -1))

def PermutationAlgorithm(User_input):

    User_Length = list(range(0, len(User_input)))
    
    """Rules:
         1. Treat every string literal as unique in the user's input.
         1. No repetition of user's indexes.
         2.  Unique combinations of user indexes are only permissible. 
    """

    """ We will base the permutations on the the indexes
          hence why I have created a list with the maximum length of the user's string in mind.
          I will use the user's indexes to forumulate a way to create all possible unique combinations relative to the length of the user's input.
          with no repetition of the user's indexes in the same combination as it would break the rule I have set.
    """
    
    #Algorithm for creating unique combinations.
    #_______________________________

    List_ofUniques = []
    Perm_iteration = list(range(len(User_input), 0, -1))
    user_index1 = User_Length[:]
    user_index = []
    #turning user_index into what it should be.

    for number in user_index1:
        user_index.append(str(number))
    
    
    
    for iteration in Perm_iteration:
        if iteration == len(User_Length):
            """
            Here: Establish length of column. Section size.
            Formula to act upon to determine colomun length.
            Forumla to act upon to determine the section size. Factorized length/Length.
            Dividing Column_length/Section_size gives me the amount of sections I will have in that column.
            Use this to iterate with as Section_amount*section_size will give you length anyway.
            """
            Column_length = int(factorial(len(User_Length)))
            Section_size = int(factorial(len(User_Length))/len(User_Length))
            
            Section_amount = int(Column_length/Section_size)
            user_index_check = 0

            for Section_loop in list(range(0, Section_amount)):
                
                for section in list(range(0, Section_size)):
                    Str_number = user_index[user_index_check]
                    
                    List_ofUniques.append(Str_number)
                user_index_check += 1
            #Error_check
            List_check = []
            for numbahh in user_index:
                List_check.append(List_ofUniques.count(str(numbahh)))
            List_checkadd = 0
            for number in List_check:
                List_checkadd += number
            #thoroughly tested and works.
                
        elif iteration <= len(User_Length)-1:
            """
            Now that we have correctly implimented the initial number of indexes.
            We can use that to find the next set of indexes, the set after the next set and so forth.
            To this:
            1. Find the length of the list containing the number of indexes.
            2. 
            """
            List_start = 0
            ListIndex = int(List_check[0]/iteration)
            New_ListLength = int(List_checkadd/ListIndex)
            List_new = []
            for element in list(range(0, New_ListLength)):
                List_new.append(int(ListIndex))
            New_check = []
            #works. Leave alone.

            """
            Using Prev_section I know at what point the cycle of implimenting
            and checking the list will stop and end.
            What i don't know is how to impliment the thing,
            """
            Section_size = int(List_check[0]/ListIndex)
            Prev_section = int(List_checkadd/List_check[0])
            for iteration in list(range(0, Prev_section)):
                
                #Check on what to delete.
                Iterated_list = user_index[:]
                for number in List_ofUniques[List_start]:
                    if number in Iterated_list:
                        del Iterated_list[Iterated_list.index(number)]
                
                for section_sizee in list(range(0, Section_size )):
                    for section_length in list(range(0,ListIndex)):
                        List_ofUniques[List_start] += Iterated_list[section_sizee]
                        List_start += 1
            #done.
            #Future proof it.

            List_check[0] = ListIndex
            
        elif iteration <= 2 and iteration != 0:
            if iteration == 2:
                
                List_start = 0
                Section_amount = int(len(List_ofUniques)/2)
                Section_size = 2

                for section in list(range(0, Section_amount)):
                    Manipul_index=  List_ofUniques[List_start]
                    Iterated_list = user_index[:]

                    for element in Manipul_index:
                        if element in Iterated_list:
                            del Iterated_list[Iterated_list.index(element)]
                   
                    for character in list(range(0, Section_size)):
                        List_ofUniques[List_start] += Iterated_list[character]
                        List_start += 1
            else:
                List_start = 0
                Section_amount = int(len(List_ofUniques)/2)
                Uniques_copy = List_ofUniques[:]
                
                for element in Uniques_copy:

                    Iterated_list = user_index[:]
                    
                    for string_literal in element:
                        if string_literal in Iterated_list:
                            del Iterated_list[Iterated_list.index(string_literal)]
                            
                    List_ofUniques[List_start] += Iterated_list[0]
                    
                    List_start += 1
                    
        elif iteration == 0:
            continue
    #_______________________________
    #Algorithm to rid the list of unique combinations of any element that contains a string which has consecutive letters within.

    #Going through and converting.

    List_start = 0

    #User_input has been unchanged and is a string not a list.
    List_ofUniques_copy = List_ofUniques
    for element in List_ofUniques_copy:
        New_element = ""

        for character in List_ofUniques[List_start]:
            New_element += User_input[int(character)]
        List_ofUniques[List_start] = New_element
        List_start += 1

    #check and impliment.

    List_ofUniques_copy1 = List_ofUniques[:]
    
    for element in List_ofUniques_copy1:
        Element_copy = element
        
        For_start = 0
        for character in Element_copy:
            if For_start == 0:
                For_start += 1
                continue
            else:
                Character_current = Element_copy[For_start]
                Character_prev = Element_copy[For_start-1]
                if Character_prev == Character_current:
                    del List_ofUniques[List_ofUniques.index(element)]
                    break

                For_start += 1
                
        

    return len(List_ofUniques)

"""
The error that plagued my mind for hours was simply the incorrect usage of a COMPARISION OPERATOR.

I USED == len(User_length)-1 instead of  <= len(User_length)-1
"""


print(PermutationAlgorithm("abfdefa"))







