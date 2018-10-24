
def print_help():
    help=("Hi there!\n" 
          "So I can help you properly, please use the following commands:\n"
          "```"
          "For more information use\n"
          "     -> !help\n"
          "To add a new assignment, test or exam:\n"
          "     ->!hmwk -- [assignment name/course code/test/exam] -- [descriptop] --[Due date] \n"
          "```")
    return help

def print_assignment(message):
    l = message.split('--')
    if(len(l)==4):
        hmwk = l[1]
        description = l[2]
        due_date = l[3]

        save_all = f"```{hmwk} : \n" \
                   f"{description} \n" \
                   f" due at: {due_date}```"
        return save_all
    else:
        return "Incorrect input. Try !help for more info"