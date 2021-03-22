import myCmd
import sys
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Schedule")
if __name__ == '__main__':
    try:
        if sys.argv[1] == 'all':
            myCmd.MyPrompt().do_show('')
    except:
        pass
    #myCmd.MyPrompt().do_show('')
    myCmd.MyPrompt().cmdloop()