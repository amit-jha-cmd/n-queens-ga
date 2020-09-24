from tabulate import tabulate
def print_table(history):
    print(tabulate(history, 
                   colalign=("center", 
                             "center",
                             "center",
                             "center",
                             "center"),
                   tablefmt="fancy_grid",
                   headers=["Epoch", 
                            "Best Solution",
                            "Score",
                            "Worst Solution", 
                            "Score"]
                   )
          )