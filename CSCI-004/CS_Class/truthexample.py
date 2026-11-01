con_and = [ [True , True , True ],
            [True , False, False],
            [False, True , False],
            [False, False, False]
            ] 

con_implies = [ [True , True , True ],
                [True , False, False],
                [False, True , True ],
                [False, False, True ]
           ]

three_var = [ [True , True , True ],
              [True , False, True ],
              [True , True , False],
              [True , False, False],
              [False, True , True ],
              [False, False, True ],
              [False, True , False],
              [False, False, False]
            ]

def formula_1_example():
     for i in three_var:
          if i[0] == True and i[1] == True:
               i.append(True)
          else: 
               i.append(False)
          if (i[3] == False) or (i[2] == True and i[3] == True):
               i.append(True)
          else: i.append(False)

          print(i)
formula_1_example()


