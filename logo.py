import os
import uuid
import json
import hashlib
import secrets
import subprocess
import time
from colorama import *
logo = "                                                                                                                                                               \n                                                                                                                                                               \n                                                                                                                                                               \n                                                                                                                                                               \n                                                                                                                                                               \n                                                                                                                                                               \n                                                                                                                                                               \n                                                                                                                                                               \n                                                                                                                                                               \n                                                                                                                                                               \n                                       .;;++++++;;       ;+++x++Xx;+;::                                                                                        \n                                     ...:;;;;xxx;;+X+;::+X+xXx;+;;;+xxXXXx+;;+;+xXXXxXXx+XXX:.                                                                 \n                                      :::::.:++++X+xxxXX$xXx+++Xx++XXxxx+++xX$X$X$XXXXX+:::+X+++;::::.                                                         \n                                     .::::;:::;;xx+++;++;x$x+$Xx$XX$XxXxxX++++xX$XX$XXXXXxxx;+xxxX;;:XX::+:::.                                                 \n                                   .;;:::;+;+;::.:x+x+;;+;;;:;+X$$$x++Xx+X++xXX$$&$XX$XXX$XXxx+x;+++;;$XXX+:;:;+:.                                             \n                           ...:.:::.:;; ..::;+++++;;++++xxxXX$X++XxXXX++++++x+++++xxXxxXXXXXX$$XXXx+;xXX$$xx++:::;+++;;:.                                      \n                        ::.   .::: .:.:...;;;;::+X$$XXXx++XX$$$$$XXXxxX++;;;:;;;+:;:+++;;;;;+++xXX$$$+::;;+XX+++x+;:;+x+++x;:.                                 \n                       ..:;: ...  ::. ;;;:.::+xxXX$Xx+;::+X$$$$$$$$$X$XX$X+;;::+++xxX$X$$X$X++;++++X$XXXX+;::;;+x+x+:::+xx+++++;.                              \n                      :::.:+;::.:..:;;:.:;;;::::;;:::.   :X$$$$$$$$$$$$$$$$X;;+;+;+Xx+XX$$$$$$XX$$+$$$$$$$$$$++;;;:+++:.;+xx+++++++:                           \n                     .;;.:.:.::: .;:..;;+++;;:::.. .    .+X$$$$&&$&$$$$&$&$$$$$$$&$&$$$X$$$$$$$$$$$&X$&$$$$$$$$$$x;+;;x;.:+++xx++x+++;                         \n                       :::..:+::;;:.:;++++++::.:        .::;+x+xx+;;:;;+xXX$$$$$$$$$$$$$$$$$$$&&&&&&X&&&&$$$$$$$XXXX+;;+;+;;++xxxx+++++;:                      \n                       :;..:;::++: :;+++;;;::;x+x+.     .::   .;;;+X$X++XXXxX$&$$$$&&&&&&&&&&$$$$&&&$$&XX&$$$$$$$$XXX$X;;;+::++xXXxx+++++;:                    \n                       .+:::;:;+:..:;::;..:;+;;::... ...:::...:;;;++xX$X$X$$$$&&$$$$$$&&&&&&&&&&&&&$$&&$&$$$$$$&&$$$XXX$+:;:;+;;+xxXxxx++++;.                  \n                        .:..;:;::  ::..:  .::::::::.::::.....::;+XXxxxx++x+;;;++xxxX$$&$$$&&&&&&&&&&X&&&&&$$$$$$&$$$$$$$X;+;++:++xxxxxxx+;;++;;.               \n                        .;:.;;::   .....::::::;;:;;;;;;::::::+++;::::..::;:.::::::::;+xX$$$&&&&&&&&&$&&&&$&&$&&$$&&&&$$$$:+;:;;++++xxxXx+;+++++:              \n                           .;:++;:  ....:..::;;;;+;++;;:::...:;;;:..;+Xx+;:::.      ...:;++X$$$&$&&&&&&&&&&&&$&&&&&&&&&$$$X++++;;;+xx+++x+++++++;              \n                             ;;;::    .::.::::;:;;;;;:;:;::...::;:.:                       :;$$$$&$&&&&&&&&&&&&&&&&&$&&&$$$;;;+::;;xx+++xx+++++++              \n                            ..:++;    .:;:::;:::;:;x++++;::::.;x+: ..                        x$$&&&&$&&&&&&&&&&&&&&&$&$$&$$$++;;:;:+xx+++x+++++++.             \n                            .  .;;;    :;;:::::;:::::::;;++;;::;+:...:.             .:;;;;:..X$$&&&&&&&&$$&&&&&&&&$$$&$$$$$$$:;+;;;+xxx++xx++xx++              \n                           .:    ::...   :::;::;;::::::;;;;;+++XX+:. .    ::::;;;;+x+XX$X+;;XX$X$&&&&&&&&$$&$&$$$$$$$$$X&$$$X+::;;;;++xx++++++++;.             \n                           ...  .: .:..    .::::::::;;;:::::;+x+x+;X+: :XXxxxXXx++++Xx$x++XX$XX$$&$$&&&&&&&&&&$$$$$$$$$$$$$X+;;:::;+x++xx++++++;;;.            \n                            ::.  .:..::..     .:;:;;:::::;;;;++;;;;:;: .;xXXXx++;;+X$+++;+++xxX$$$$$&$&&&&&&&&$$$$$$$$$Xxx+;:+:+x+;;x++xx++++x++;+;            \n                            :.....  ....: ..... .:::;;;;::::;+;:::::.. . .:+xXX++;;:;+X$XXXXXX$X$$$$&&&&&&&&&$$$$XXXxXx++;;;;;.::;;;+++++++++++++++;.          \n                            :;::...    . .:..:.:.   .::::::;::;;::::... ..  .;+x+;x++++xXX&$&$$$$&&&$$&$$&$$XXXXXx+;;:;;;++::;.+;X;++x+++xx+++x++++++:         \n                             ;;:..:       ...  ...... ..:;;;;;;;;::;;::::.. .. .:;+;;;;+xX$$$$$$$$$$XXXXXXxx++;;;::++x+;::+::.::;;;++x+++++++++;+xx;+x:        \n                             :+::.:            . ..  ::..  .::;;;;;;+;;;:::::....  :;;+X+++++;;++++;+;:;;;;:::;;x+++;;:::;:;;:.+;;;+xxx+x++Xxx;++x+++x+.       \n                             :+:: ..             .. .     :::..:::;;;;;+;:;;::::::....+XX+:::;;;::;:::.:  .::.;;+:.;++:+:+:::. .;+;+xxxxx++xx+++x++++++:       \n                          ::.:+:....                           .  . .::::;;;;;:;;+;;:::+$+:::::.. .... ....::..:.+:;;+;:+;;;...+++;++XXx+++x+x++xx++++++.      \n                         :::..;:...:.                   .   ..  . . .  .       ......  ;X+.  .. ..... .:..::::;+;;;;+::;;;:..  .;;+;+x+xx++Xx+++xx++x+++;      \n                         .::::::.:::.                    .  .. . . .    . ....  ..::. ..$;       ..:.::::.:::;;;;;;;;:;:;::... :++;++xx+X++xx+++xx;;+++++:     \n                       ... .:;;:.::::                     .    ..  ....   . ..  .. ....++X:.......:...:;;;+:++;;:+;;:+;:;::: ..:::;++xXxxx++x+++xx+;;+;x++.    \n                  ::..      ..::::.::                    .:   .. :..:.   ..... :... ..:&++X...: ;;.+:;;:;::;;+;+;+++;+++;;:.....;++;;+xXXxx+++++xxx+:;;x++:    \n                :::...    ...:+;.;:::                     ...   . .    ..  .. ..:...:..:;$++;:x:+:+;;;+;::+;;;;:;+;;;+;+:::....:;;+;;xXXxxXx+++++x++:;++++:   \n             .:...;;:::....  ::::  ..                  .......  ..   :...: .. ..:..::+;++:.X+;++x++;;x+;x:;x;X:+;;;:+::+;:;::.:.;;+;+;+XXXXXxX++++++++;;++x;   \n          .: ..    .:;;:::..  ....::               .  .   . .  ... ... .... :. ..::::;;;:;x++;x:;::+:;;;;:;:;;:+:+:+;+;:;:+:..:..::;+;+++xx+xx+++++++++x;;++:  \n       ..::.       ..;;::...:::..:.:.         .    .:..:.  . .. .. .. .....::::;::;:;;:;++;+:X::;:;;;+:x;:;:+;;;:;;+;X;;;:::.:. .+++;+;+XxxxXX+;;;++;++++++++. \n   .::....     ...:::::.::::;::..    .         .  .  ... ....  :..:...:+;:;;;;x;;;+;;:;:;;;:+++;++++x+x;+;;+;;;;;+;;:;::;:;:.:.. .:;++;xx+Xxxx+;+x+++++++++++;.\n.::::....: ...:..   ......         .. .:... .. ..  ...:.::.... .:.::;:::;:::;+;;;;:;::;;:++;;;+++x:;;+;+:+;+;;+;;;;x:+::..:..  ...;+++++++XXxxx+:;++;+++++++++:\n:::::::::;:;;:::.::;;.        .   ... ...      . ...:..::;:;+:;.:;::.:;:;::;:;;;.X::+;:::+.+.::.;:+:x.:+.$:+.:x:+;:.::..::   ..  . ;;x+;+xxXXxxx+;;;;.;+;+++++;\nxx++++++++++++xxxx+++++;;::;::::.. .. .:. ....:;::;:;;:;;;;;::;;;.+;:+:;+:+;;;::+::+:x;;:+:;+::;:;:;;+::;:;:+;+:+:x:;::::. . .... :++;+++xXXXXxx+:;:::::+++++++\n;;+x++X+X+xXXXXx+X+++++;++++++:;:::;:::+;:+;:+:;+;;;::;+.x;:;;+++++;;x;+::X;;;:x.;:+;.+::+:::;;x;;+;;;;++;;X:;+:X::;.;:::.::......  ;+++;+XXxXX+++::::::;;+++xx\n                                                                                                                                                               \n                  .                .                                         :xXx:                                      ;x;.                                   \n               +&&&$.           +.                             $&&&.      x&&.   :&&+                                  x&&&&.                                  \n                &&&&+          +;                              $&&&     ;&&&.     .&&&:                                 x&$;                                   \n                .&&&&.        ;+                               $&&&    ;&&&;     . x&&&.                                                                       \n                 +&&&$      . x                                $&&&   .&&&&        .&&&$                                                                       \n                  $&&&;      x:        ;$$$$+.          x&&$;. $&&&   +&&&&        .&&&&;  .   .  ;$&&;.   ;$&&x.     .   .     . .  .                         \n                  .&&&&.    ;+      x&&x    $&&x     x&&x  . ;;$&&&   X&&&&         &&&&x   $&&&+;   $&&x:;   x&&$     .&&&x    ;&&&x       .x.                \n                   +&&&X   .x     .&&&$     :&&&$ ..&&&$      .&&&&   X&&&$         &&&&x   $&&&:    x&&&;    ;&&&;    .&&&x     ;&&&X     .x.                 \n                    $&&&:  +.     x&&&+     .&&&&. x&&&x       &&&&   x&&&&         &&&&+   $&&&     x&&&;    ;&&&;    .&&&x      x&&&x    +:                  \n                    .&&&& ;;     .$&&&;            x&&&+       &&&&   .&&&&        .&&&&.   $&&&     x&&&:    ;&&&;    .&&&x       x&&&+  ;;                   \n                     ;&&&X;       x&&&x            x&&&+       &&&&    +&&&.       ;&&&;    $&&&     x&&&:    ;&&&;    .&&&x        x&&&+:x                    \n                      $&&&.       .&&&$        .x  .&&&$      :&&&&     x&&$       $&&+     $&&&     x&&&:    ;&&&;    .&&&x         X&&&X.                    \n                      .&&;          x&&x      ;;     x&&x.   :;$&&&      :&&x     $&$.      $&&&     x&&&:    ;&&&;    .&&&x          $&&:                     \n                       ;x             .;xxxx;.         .+X$x:  .;::..      .:xxxx;:       ...;;: .  ..;:;..  ..;::..  ..::;..         .&+                      \n                                                                                                                                      :+                       \n                                                                                                                                     .x                        \n                                                                                                                                .$&&&X.                        \n                                                                                                                                 x&&&:                         \n                                                                                                                                     .                         \n_______________________________________________________________________________________________________________________________________________________________\n \n "


init(autoreset=True)

DB = "users.json"
SOFT = "main.py"

try:
    with open(DB, "r") as f:
        users_db = json.load(f)
except FileNotFoundError:
    users_db = {}

sessions = {} 

def save():
    with open(DB, "w") as f:
        json.dump(users_db, f, indent=4)

def hash(value, salt=None):
    if salt is None:
        salt = secrets.token_hex(16)
    hash_obj = hashlib.sha256((salt + value).encode())
    return salt, hash_obj.hexdigest()

def vrfy(stored_hash, stored_salt, value_attempt):
    _, attempt_hash = hash(value_attempt, stored_salt)
    return attempt_hash == stored_hash

def genK(username):
    key = str(uuid.uuid4())
    salt, hashed_key = hash(key)
    users_db[username]['key_hash'] = hashed_key
    users_db[username]['key_salt'] = salt
    sessions[key] = username
    save()
    return key

def checkK(input_key):
    if input_key in sessions:
        return sessions[input_key]

    for username, user in users_db.items():
        key_hash = user.get('key_hash')
        key_salt = user.get('key_salt')
        if key_hash and vrfy(key_hash, key_salt, input_key):
            sessions[input_key] = username
            return username
    return None

def reg():
    username = input("Введите новый логин: ")
    if username in users_db:
        print(Fore.RED + "Такой логин уже существует!")
        return None
    password = input("Введите пароль: ")
    salt, hashed = hash(password)
    users_db[username] = {
        "password_hash": hashed,
        "password_salt": salt,
        "data": "Данные пользователя",
        "key_hash": "",
        "key_salt": ""
    }
    save()
    print(Fore.GREEN + f"Пользователь {username} успешно зарегистрирован")
    return username

def launch(username):
    os.system('clear')

    print(Fore.GREEN + f"{username}")
  
    
    if os.path.exists(SOFT):
        try:
            subprocess.run(['python3', SOFT], check=True)
        except subprocess.CalledProcessError as e:
            print(Fore.RED + f"\nОшибка при запуске {SOFT}: {e}")
        except FileNotFoundError:
            print(Fore.RED + f"\nPython не найден")

def menu():
    Style.RESET_ALL
    os.system('cls')
    print(Fore.WHITE + '1 - Зарегистрироваться')
    print('2 - Сгенерировать ключ')
    print('3 - Войти по ключу')
    print('4 - Выход')

def main():
    os.system('cls')
    print(logo)

    for i in range(3):
        print(Fore.RED + 'Нажмите ENTER для продолжения...')

    enter = input(Fore.RED + 'Нажмите ENTER для продолжения...')
    
    while True:
        menu()
        choice = input(Fore.YELLOW + '\nВыберите действие (1-4): ').strip()

        if choice == '1':
            os.system('cls')
            username = reg()

        elif choice == '2':
            os.system('cls')
            username = input('\nЛогин: ')
            password = input('Пароль: ')

            user = users_db.get(username)
            if not user or not vrfy(user['password_hash'], user['password_salt'], password):
                print(Fore.RED + '\nНеверный логин или пароль')
                input(Fore.RED + "\nНажмите ENTER для возврата в меню...")
                continue

            key = genK(username)
            print(Fore.GREEN + 'ВАШ КЛЮЧ:', Fore.WHITE + key)
            print(Fore.RED + '\nВАЖНО: Сохраните этот ключ! Он больше не будет показан.')
            input("\nНажмите ENTER для возврата в меню...")

        elif choice == '3':
            os.system('cls')
            input_key = input('\nВведите ключ авторизации: ')
            username = checkK(input_key)
            if username:
                print(Fore.CYAN + '\nПользователь:', Fore.WHITE + username)
                time.sleep(1)
                launch(username)
            else:
                print(Fore.RED + '\nНеверный ключ')
                input("\nНажмите ENTER для возврата в меню...")

        elif choice == '4':
            os.system('cls')
            print(Fore.YELLOW + "\nВыход из программы...")
            break

        else:
            print(Fore.RED + '\nНеверный выбор. Пожалуйста, выберите от 1 до 4.')
            input(Fore.RED + "Нажмите ENTER для продолжения...")

if __name__ == "__main__":
    main()
