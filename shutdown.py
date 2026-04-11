def shutdown(positive,negative):
    """Do you want to shutdown your PC"""

    response1 = "yes"
    response2 = "no"
    if response1 == True:
        return shutdown(positive)
    else:
        return print("Aborting shutdwon")
    

    
