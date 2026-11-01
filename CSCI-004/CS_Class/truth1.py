# (P AND Q) IF AND ONLY IF r

con_and = [ [True , True , True ],
            [True , False, False],
            [False, True , False],
            [False, False, False]
          ] 

con_biconditional = [ [True , True , True ],
                      [True , False, False],
                      [False, True , False],
                      [False, False, True ]
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

def prop_formula(): 
    for row in three_var:
        #analyze (p AND q) first
        if row[0] == True and row[1] == True:
            row.append(True)
        else:
            row.append(False)

        #analyze biconditonal with respect to row[3] or column 4 (previous outputs) next
        if row[3] == row[2]:
            row.append(True)
        else:
            row.append(False)

        print(row)

prop_formula()
            