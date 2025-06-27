import cfg

def check_agreement_status():
    print(cfg.const.agreement_text)
    try:
        user_agreement = input("Вы согласны с условиями? (да/нет): ")
        if user_agreement.lower() in cfg.const.ANSW_YES_LIST:
            return True
        elif user_agreement.lower() in cfg.const.ANSW_NO_LIST:
            return False
        else:
            raise ValueError
    except ValueError:
        print("Некорректный ввод. Пожалуйста, ответьте 'да' или 'нет'.")
        return check_agreement_status()
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return False
