from hammett.core import Bot
from hammett.core.constants import DEFAULT_STATE

from screens import MainMenuScreen, PaymentScreen, MenuVersionsScreen


def main():
    name = 'GeminiTgBot'
    app = Bot(
        name,
        entry_point=MainMenuScreen,
        states={
            DEFAULT_STATE: {MainMenuScreen, PaymentScreen, MenuVersionsScreen},
        },
    )
    app.run()


if __name__ == '__main__':
    main()