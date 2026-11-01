# p IMPLIES (q OR r). note: parentheses first

con_and = [ [True , True , True ],
            [True , False, False],
            [False, True , False],
            [False, False, False]
          ] 

con_or = [ [True , True , True ],
           [True , False, True ],
           [False, True , True ],
           [False, False, False]
         ]

#                p      q      r
three_var = [ [True , True , True ],
              [True , False, True ],
              [True , True , False],
              [True , False, False],
              [False, True , True ],
              [False, False, True ],
              [False, True , False],
              [False, False, False]
            ] 

def formula_two():
    for row in three_var:
        #analyze (q or r) first
        if row[0] and row[1] == False:
            row.append(False)
        else:
            row.append(True)

        #analyze p implies next
        if row [2] == True and row[3] == False:
            row.append(False)
        else:
            row.append(True)

        print(row)

formula_two()