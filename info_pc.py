import time, os, sys, socket, requests
import platform, re, uuid


# THIS CODE JUST FOR FUN !! 
try:
    from colorama import Fore
except:
    print('[#] you most install this package [pip install colorama]')
    time.sleep(3)
    sys.exit()

try:
    import psutil
except:
    print('[#] you most install this package [pip install psutil]')
    time.sleep(3)
    sys.exit()

try:
    from tqdm import tqdm
except:
    print('[#] you most install this package [pip install tqdm]')
    time.sleep(3)
    sys.exit()

try:
    from subprocess import check_output
except:
    print('[#] you most install this package [pip install subprocess]')
    time.sleep(3)
    sys.exit()
try:
    import requests
except:
    print('[#] you most install this package [pip install requests]')
    time.sleep(3)
    sys.exit()


# >> clear or cls
def cl():
    name = platform.uname()
    if name[0] == 'Windows':
        os.system('cls')
    else:
        os.system('clear')




# >> banner
def banner_windows():
    print(Fore.CYAN + """""""""
                                                                                                                                              ``..--:/+osyhh-
                                                                                                                                   ..--:/+osyhddmmNNMMMMMMMMM-
                                                                                                                   ``..--:/+osyyy .NNNMMMMMMMMMMMMMMMMMMMMMMM-
                                                                                                            `+osyhhdmmNMMMMMMMMMd`.MMMMMMMMMMMMMMMMMMMMMMMMMM-
                                                                                                            -MMMMMMMMMMMMMMMMMMMd`.MMMMMMMMMMMMMMMMMMMMMMMMMM-
                                                                                                            -MMMMMMMMMMMMMMMMMMMd`.MMMMMMMMMMMMMMMMMMMMMMMMMM-
                                                                                                            -MMMMMMMMMMMMMMMMMMMd`.MMMMMMMMMMMMMMMMMMMMMMMMMM-
                                                                                                            -MMMMMMMMMMMMMMMMMMMd`.MMMMMMMMMMMMMMMMMMMMMMMMMM-
                                                                                                            -MMMMMMMMMMMMMMMMMMMd`.MMMMMMMMMMMMMMMMMMMMMMMMMM-
                                                                                                            -MMMMMMMMMMMMMMMMMMMd`.MMMMMMMMMMMMMMMMMMMMMMMMMM-
                                                                                                            -MMMMMMMMMMMMMMMMMMMd`.MMMMMMMMMMMMMMMMMMMMMMMMMM-
                                                                                                            -NNNNNNNNNNNNNNNNNNNd .NNNNNNNNNNNNNNNNNNNNNNNNNN-
                                                                                                            ````````````````````  ``````````````````````````
                                                                                                            -NNNNNNNNNNNNNNNNNNNd .NNNNNNNNNNNNNNNNNNNNNNNNNN-
                                                                                                            -MMMMMMMMMMMMMMMMMMMd`.MMMMMMMMMMMMMMMMMMMMMMMMMM-
                                                                                                            -MMMMMMMMMMMMMMMMMMMd`.MMMMMMMMMMMMMMMMMMMMMMMMMM-
                                                                                                            -MMMMMMMMMMMMMMMMMMMd`.MMMMMMMMMMMMMMMMMMMMMMMMMM-
                                                                                                            -MMMMMMMMMMMMMMMMMMMd`.MMMMMMMMMMMMMMMMMMMMMMMMMM-
                                                                                                            -MMMMMMMMMMMMMMMMMMMd`.MMMMMMMMMMMMMMMMMMMMMMMMMM-
                                                                                                            -MMMMMMMMMMMMMMMMMMMd`.MMMMMMMMMMMMMMMMMMMMMMMMMM-
                                                                                                            -MMMMMMMMMMMMMMMMMMMd`.MMMMMMMMMMMMMMMMMMMMMMMMMM-
                                                                                                            `+osyhhdmmNMMMMMMMMMd`.MMMMMMMMMMMMMMMMMMMMMMMMMM-
                                                                                                                  ```..--:/+osyhy .NNNMMMMMMMMMMMMMMMMMMMMMMM-
                                                                                                                                   ..--:/+osyhddmmNNMMMMMMMMM-
                                                                                                                                               ``..--:/+osyhh-""")


# >> banner linux
def banner_linux():
    print(Fore.RED + '''''''''                                                                                
                                                                                                    
             `..........````                                                                                
              `````...---:://++ooooooooo+//:-.``                                                            
                                 `````.-:/+osyhhdhso/:-`                                                    
                                              ``.-/+sydmdy+:`                                               
                                            ```````....-/ohN/                                               
                     ``..-:::///++ooossssyyyyyyyyyyhhhhhhd:m-                                               
         `....---::////::---......```````````````````.-://:+/                                               
        `.```````                          `.-:/osyyyyyyyyy:s.                                              
                                    `.:/+ossoo+/-...````    .h/`              `.`                           
                               .://oo+/-..`                  :mmy+:-----.`    `.:/:-`                       
                          .-:/+:-.``                         `oMMMMNNNNNmmdyo:-```.-+/:`                    
                     `.-::-.`                              -smNNdyo/::::+oyhdmNmdh/-/.:o+-                  
                   `--``                                 .yNMd+-`           `.-/oyddNd++hyy:                
                                                        :mMm+`                    `.:+ydNmyy+`              
                                                       -NMm-                           `-mMMMd:             
                                                       hMM:                              :hmMMN:            
                                                       NMN                                 .-odms:-`        
                                                       NMN                                    `-sms-        
                                                       yMM/                                      .          
                                                       .mMN:                                                
                                                        -dMNo.                                              
                                                         `omMms:.                                           
                                                           .+dNMmhs+///:::::---...``                        
                                                             `-/shmmmmmmmmmmmmmmmmddhyo+:-.`                
                                                                  ``..........--:+ohdNNhhhhys+:.`           
                                                                                    `.:oys/--:oss+-`        
                                                                                         .+s+.  `-/o+-`     
                                                                                            -oo.    ./+-    
                                                                                              -o/`     :+.  
                                                                                                :o.     `/- 
                                                                                                 `o-      -.
                                                                                                   +-      .
                                                                                                    +.      
                                                                                                     +      
                                                                                                     `:     
                                                                                                      -    
                                                                                                   ''''''''''')


# system information
def systeminfo():
    ke = []
    val = []

    info = {}
    info['platform'] = platform.system()
    info['platform-release'] = platform.release()
    info['platform-version'] = platform.version()
    info['architecture'] = platform.machine()
    info['mac-address'] = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
    info['processor'] = platform.processor()
    info['ram'] = str(round(psutil.virtual_memory().total / (1024.0 ** 3))) + " GB"

    for num in info.keys():
        ke.append(num)

    for va in info.values():
        val.append(va)

    print(Fore.GREEN + ke[0] + ':' + val[0])
    print('')
    print(Fore.GREEN + ke[1] + ':' + val[1])
    print('')
    print(Fore.GREEN + ke[2] + ':' + val[2])
    print('')
    print(Fore.GREEN + ke[3] + ':' + val[3])
    print('')
    print(Fore.GREEN + ke[4] + ':' + val[4])
    print('')
    print(Fore.GREEN + ke[5] + ':' + val[5])
    print('')
    print(Fore.GREEN + ke[6] + ':' + val[6])
    print('')

    # >> inputs
    while True:
        answer = input(
            Fore.RED + " ┌─[" + Fore.LIGHTGREEN_EX + "INFROMATIOM" + Fore.BLUE + "~" + Fore.WHITE + "@HOME" + Fore.RED + "/" + Fore.CYAN + "System" + Fore.RED + "/" + Fore.CYAN + "info_pc" + Fore.RED + """]
 └── """ + Fore.WHITE + " ").lower()
        if answer[0] == 'b' or answer[0] == 'B':
            welcome()
        elif answer[0] == 'E' or answer[0] == 'e':
            sys.exit()
        else:
            answer = input(
                Fore.RED + " ┌─[" + Fore.LIGHTGREEN_EX + "INFROMATIOM" + Fore.BLUE + "~" + Fore.WHITE + "@HOME" + Fore.RED + "/" + Fore.CYAN + "System" + Fore.RED + "/" + Fore.CYAN + "info_pc" + Fore.RED + """]
 └── """ + Fore.WHITE + " ").lower()


# ======================================
def loading(name):
    for _ in tqdm(range(100), desc=f'{name}....', ascii=False, ncols=75, colour='green'):
        time.sleep(0.01)
    print(Fore.RED + '\t [' + Fore.GREEN + '^' + Fore.RED + '] ' + Fore.WHITE + f'{name} is successfully  !!')


# ======================================
def show_profies():
    cl()

    name = platform.uname()
    if name[0] == 'Windows':
        wlan = check_output('netsh wlan show profiles', shell=True).decode()
        loading('Finding')
        cl()
        print(Fore.CYAN + '''''''''
                                                                    ██╗███╗   ██╗████████╗███████╗██████╗ ███╗   ██╗████████╗
                                                                    ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗████╗  ██║╚══██╔══╝
                                                                    ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝██╔██╗ ██║   ██║   
                                                                    ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗██║╚██╗██║   ██║   
                                                                    ██║██║ ╚████║   ██║   ███████╗██║  ██║██║ ╚████║   ██║   
                                                                    ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝                                                
        ''''''''')

        print(Fore.GREEN + wlan)
        print('')
        print('')

        print(Fore.YELLOW + '[01]', Fore.CYAN + ' Find the password of wifi')
        print('****************')
        print(Fore.YELLOW + '[02]', Fore.CYAN + ' Back to menu')
        print('****************')
        print(Fore.YELLOW + '[03]', Fore.CYAN + ' Exit')
        a = str(input(' └──['))

        while True:
            if a == '1':
                print('')

                name_password = input(
                    Fore.RED + " ┌─[" + Fore.LIGHTGREEN_EX + "What is your name of device ?" + Fore.RED + """
 └── """ + Fore.WHITE + " ").lower()

                wifi = check_output(f'netsh wlan show profiles {name_password} key=clear', shell=True).split()
                password = wifi[104]
                cl()
                print(Fore.GREEN + '[' + Fore.RED + '~' + Fore.GREEN + '] ' + Fore.WHITE + 'Find Password.........')
                time.sleep(0.8)
                print(Fore.GREEN + '[' + Fore.RED + '~' + Fore.GREEN + '] ' + Fore.WHITE + 'Get Password.........')
                time.sleep(0.8)
                cl()
                print(Fore.RED + '''''''''
    
                                                                      _____            ____       _____   ____ 
                                                                     |\    \   _____  |    | ____|\    \ |    |
                                                                     | |    | /    /| |    ||    | \    \|    |
                                                                     \/     / |    || |    ||    |______/|    |
                                                                     /     /_  \   \/ |    ||    |----'\ |    |
                                                                    |     // \  \   \ |    ||    |_____/ |    |
                                                                    |    |/   \ |    ||    ||    |       |    |
                                                                    |\ ___/\   \|   /||____||____|       |____|
                                                                    | |   | \______/ ||    ||    |       |    |
                                                                     \|___|/\ |    | ||____||____|       |____|
                                                                        \(   \|____|/   \(    )/           \(  
                                                                         '      )/       '    '             '  
                                                                                '                              
                ''''''''')
                print('')
                print(Fore.GREEN + f'└──[£ {name_password}/', Fore.YELLOW + 'Security settings/',
                      Fore.CYAN + 'Key Content/', Fore.RED + f'{password}')
                print('')

                an = str(input(Fore.RED + '[' + Fore.WHITE + '01' + Fore.RED + '] ' + Fore.CYAN +
                               'Back to Menu :'))
                while True:
                    if an == '1':
                        welcome()
                    else:
                        an = str(input(Fore.RED + '[' + Fore.WHITE + '01' + Fore.RED + '] ' + Fore.CYAN +
                                       'Back to Menu :'))

            elif a == '2':
                welcome()
            elif a == '3':
                sys.exit()
            else:
                a = str(input())
    else:
        cl()
        print(Fore.RED + '[' + Fore.GREEN + '!' + Fore.RED + '] ' + Fore.CYAN + 'This items just for window !! ')
        an = str(input(Fore.RED + '[' + Fore.WHITE + '0' + Fore.RED + '] ' + Fore.YELLOW + 'Back : '))
        if an == '0':
            welcome()
        else:
            show_profies()

def get_ip():
    cl()
    hostname = socket.gethostname()
    ip_local = socket.gethostbyname(hostname)
    https = requests.get('https://api.ipify.org/').text
    print(Fore.GREEN + '[!] pay attention you should connect to internet [!]')
    print('')
    print(Fore.RED + '[' + Fore.WHITE + '01' + Fore.RED + '] ' + Fore.YELLOW + 'ip_local')
    print(Fore.RED + '[' + Fore.WHITE + '02' + Fore.RED + '] ' + Fore.YELLOW + 'ip_public')
    print(Fore.RED + '[' + Fore.WHITE + '03' + Fore.RED + '] ' + Fore.CYAN + 'Back')
    print('')

    ans = input(
        Fore.RED + " ┌─[" + Fore.LIGHTGREEN_EX + "INFROMATIOM" + Fore.BLUE + "~" + Fore.WHITE + "@HOME" + Fore.RED + "/" + Fore.CYAN + "System" + Fore.RED + "/" + Fore.CYAN + "Ip_info" + Fore.RED + """] 
 └── """ + Fore.WHITE + " ").lower()

    if ans == '1':
        cl()
        loading('Connecting')
        print('')
        print(Fore.GREEN + '[*]', Fore.WHITE + f'your ip_local : {ip_local}')
        print('')

        while True:
            print(Fore.YELLOW + 'Back to menu' + Fore.RED + '[' + Fore.WHITE + '0' + Fore.RED + ']')
            print(Fore.YELLOW + 'Back ' + Fore.RED + '[' + Fore.WHITE + '00' + Fore.RED + ']')
            print('')
            answer = input(
                Fore.RED + " ┌─[" + Fore.LIGHTGREEN_EX + "INFROMATIOM" + Fore.BLUE + "~" + Fore.WHITE + "@HOME" + Fore.RED + "/" + Fore.CYAN + "System" + Fore.RED + "/" + Fore.CYAN + "Ip_info" + Fore.RED + """] 
 └── """ + Fore.WHITE + " ").lower()
            if answer == '0':
                welcome()
            elif answer == '00':
                get_ip()
            elif answer == '000':
                sys.exit()
            else:
                print(Fore.YELLOW + 'Back to menu' + Fore.RED + '[' + Fore.WHITE + '0' + Fore.RED + ']')
                print(Fore.YELLOW + 'Back ' + Fore.RED + '[' + Fore.WHITE + '00' + Fore.RED + ']')
                answer = input(
                    Fore.RED + " ┌─[" + Fore.LIGHTGREEN_EX + "INFROMATIOM" + Fore.BLUE + "~" + Fore.WHITE + "@HOME" + Fore.RED + "/" + Fore.CYAN + "System" + Fore.RED + "/" + Fore.CYAN + "Ip_info" + Fore.RED + """] 
                └── """ + Fore.WHITE + " ").lower()
    if ans == '2':
        cl()
        loading('Connecting')
        print('')
        print(Fore.GREEN + '[*]', Fore.WHITE + f'your ip_public : {https}')
        print('')

        while True:
            print(Fore.YELLOW + 'Back to menu' + Fore.RED + '[' + Fore.WHITE + '0' + Fore.RED + ']')
            print(Fore.YELLOW + 'Back ' + Fore.RED + '[' + Fore.WHITE + '00' + Fore.RED + ']')
            print('')
            answer = input(
                Fore.RED + " ┌─[" + Fore.LIGHTGREEN_EX + "INFROMATIOM" + Fore.BLUE + "~" + Fore.WHITE + "@HOME" + Fore.RED + "/" + Fore.CYAN + "System" + Fore.RED + "/" + Fore.CYAN + "Ip_info" + Fore.RED + """] 
 └── """ + Fore.WHITE + " ").lower()
            if answer == '0':
                welcome()
            elif answer == '00':
                get_ip()
            elif answer == '000':
                sys.exit()
            else:
                print(Fore.YELLOW + 'Back to menu' + Fore.RED + '[' + Fore.WHITE + '0' + Fore.RED + ']')
                print(Fore.YELLOW + 'Back ' + Fore.RED + '[' + Fore.WHITE + '00' + Fore.RED + ']')
                answer = input(
                    Fore.RED + " ┌─[" + Fore.LIGHTGREEN_EX + "INFROMATIOM" + Fore.BLUE + "~" + Fore.WHITE + "@HOME" + Fore.RED + "/" + Fore.CYAN + "System" + Fore.RED + "/" + Fore.CYAN + "Ip_info" + Fore.RED + """] 
                └── """ + Fore.WHITE + " ").lower()



    elif ans == '3':
        welcome()

    else:
        get_ip()


def about():
    cl()
    print(Fore.GREEN + '''''''''

                                   ...             .....     .        ...          
                               .x888888hx    :   .d88888Neu. 'L    xH88"`~ .x8X    
                              d88888888888hxx    F""""*8888888F  :8888   .f"8888Hf 
                             8" ... `"*8888%`   *      `"*88*"  :8888>  X8L  ^""`  
                            !  "   ` .xnxx.      -....    ue=:. X8888  X888h       
                            X X   .H8888888%:           :88N  ` 88888  !88888.     
                            X 'hn8888888*"   >          9888L   88888   %88888     
                            X: `*88888%`     !   uzu.   `8888L  88888 '> `8888>    
                            '8h.. ``     ..x8> ,""888i   ?8888  `8888L %  ?888   ! 
                             `88888888888888f  4  9888L   %888>  `8888  `-*""   /  
                              '%8888888888*"   '  '8888   '88%     "888.      :"   
                                 ^"****""`          "*8Nu.z*"        `""***~"`  
                                    
                                 system             information          command                                                
                                                                                                

    ''''''''')
    print(Fore.GREEN + '[^]', Fore.WHITE + 'Create :  AMIRZIYA')
    print('')
    print(Fore.GREEN + '[^]', Fore.WHITE + 'About: you can use the tool for get some information about your device')
    print('')
    print(Fore.GREEN + '[^]', Fore.WHITE + 'Version: 2.1.0')
    print('')
    answer = str(input(Fore.RED + '[' + Fore.WHITE + '0' + Fore.RED + '] ' +Fore.YELLOW + 'Back : '))

    if answer == '00':
        welcome()
    else:
        welcome()


# ==============information===============
def info_pc():
    plat = platform.uname()
    if plat[0] == "Windows":
        os.system("cls")
        information = check_output('systeminfo.exe', shell=True).decode()

        print(Fore.GREEN + '[!]', Fore.WHITE + 'Find information.........')
        time.sleep(0.8)
        print(Fore.GREEN + '[!]', Fore.WHITE + 'Get information.........')
        time.sleep(0.8)
        print(Fore.GREEN + '[!]', Fore.WHITE + 'Print information.........')
        cl()
        banner_windows()
        print(Fore.LIGHTGREEN_EX + information)
        print('')
        while True:
            answer = input(
                Fore.RED + " ┌─[" + Fore.LIGHTGREEN_EX + "INFROMATIOM" + Fore.BLUE + "~" + Fore.WHITE + "@HOME" + Fore.RED + "/" + Fore.CYAN + "System" + Fore.RED + "/" + Fore.CYAN + "info_pc" + Fore.RED + """]
 └── """ + Fore.WHITE + " ").lower()
            if answer[0] == 'b' or answer[0] == 'B':
                welcome()
            elif answer[0] == 'E' or answer[0] == 'e':
                sys.exit()
            else:
                answer = input(
                    Fore.RED + " ┌─[" + Fore.LIGHTGREEN_EX + "INFROMATIOM" + Fore.BLUE + "~" + Fore.WHITE + "@HOME" + Fore.RED + "/" + Fore.CYAN + "System" + Fore.RED + "/" + Fore.CYAN + "info_pc" + Fore.RED + """]
 └── """ + Fore.WHITE + " ").lower()
    else:
        cl()
        print(Fore.GREEN + '[!]', Fore.WHITE + 'Find information.........')
        time.sleep(0.8)
        print(Fore.GREEN + '[!]', Fore.WHITE + 'Get information.........')
        time.sleep(0.8)
        print(Fore.GREEN + '[!]', Fore.WHITE + 'Print information.........')
        cl()
        banner_linux()
        systeminfo()


def welcome():
    cl()
    print(Fore.GREEN + '''''''''
                                    

                                   ...             .....     .        ...          
                               .x888888hx    :   .d88888Neu. 'L    xH88"`~ .x8X    
                              d88888888888hxx    F""""*8888888F  :8888   .f"8888Hf 
                             8" ... `"*8888%`   *      `"*88*"  :8888>  X8L  ^""`  
                            !  "   ` .xnxx.      -....    ue=:. X8888  X888h       
                            X X   .H8888888%:           :88N  ` 88888  !88888.     
                            X 'hn8888888*"   >          9888L   88888   %88888     
                            X: `*88888%`     !   uzu.   `8888L  88888 '> `8888>    
                            '8h.. ``     ..x8> ,""888i   ?8888  `8888L %  ?888   ! 
                             `88888888888888f  4  9888L   %888>  `8888  `-*""   /  
                              '%8888888888*"   '  '8888   '88%     "888.      :"   
                                 ^"****""`          "*8Nu.z*"        `""***~"`  
                                                                                   
                                                                                   
                                                   

''''''''')
    print('')
    print(Fore.RED + '[' + Fore.WHITE + '01' + Fore.RED + '] ' + Fore.YELLOW + 'information about your pc')
    time.sleep(0.1)
    print('****************')
    print(Fore.RED + '[' + Fore.WHITE + '02' + Fore.RED + '] ' + Fore.YELLOW + 'Find ip')
    time.sleep(0.1)
    print('****************')
    print(Fore.RED + '[' + Fore.WHITE + '03' + Fore.RED + '] ' + Fore.YELLOW + 'Information of Internet')
    time.sleep(0.1)
    print('****************')
    print(Fore.RED + '[' + Fore.WHITE + '04' + Fore.RED + '] ' + Fore.YELLOW + 'About us')
    time.sleep(0.1)
    print('****************')
    print(Fore.RED + '[' + Fore.WHITE + '05' + Fore.RED + '] ' + Fore.CYAN + 'Exit')
    print(Fore.CYAN + '****************')
    print('')
    answer = input(
        Fore.RED + " ┌─[" + Fore.LIGHTGREEN_EX + "INFROMATIOM" + Fore.BLUE + "~" + Fore.WHITE + "@HOME" + Fore.RED + "/" + Fore.CYAN + "System" + Fore.RED + """]
 └── """ + Fore.WHITE + " ").lower()

    if answer == '1':
        info_pc()
    elif answer == '2':
        get_ip()
    elif answer == '3':
        show_profies()
    elif answer == '4':
        about()
    elif answer == '5':
        sys.exit()
    else:
        welcome()


welcome()
