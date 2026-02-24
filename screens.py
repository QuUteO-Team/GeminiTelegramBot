from hammett.core import Screen, Button
from hammett.core.constants import SourceTypes
from hammett.core.mixins import StartMixin

MAIN_MENU_SCREEN_DESCRIPTION = (
    "🤖 Welcome to Gemini Bot!\n\n"
    "✨ Your personal AI assistant powered by Google Gemini\n\n"
    "📌 Main Menu\n"
    "• Choose a Gemini version to start chatting\n"
    "• Buy tokens for premium features\n"
    "• Check your stats and settings\n\n"
    "👇 Select an option below:"
)

PAYMENT_SCREEN_DESCRIPTION = (
    "💰 Token Store\n\n"
    "💎 Token Packages:\n"
    "• 100 tokens - $4.99\n"
    "• 500 tokens - $19.99\n"
    "• 1000 tokens - $34.99\n\n"
    "🎁 Bonus: First purchase gets +50 free tokens!\n\n"
    "⬇️ Choose a package:"
)

MENU_VERSIONS_SCREEN_DESCRIPTION = (
    "🚀 Gemini Versions\n\n"
    "🆓 Gemini Lite - FREE\n"
    "• Basic chat assistance\n"
    "• Text generation\n"
    "• 10 messages per day\n\n"
    "👇 Select a version:"
)

class MenuVersionsScreen(Screen):
    description = MENU_VERSIONS_SCREEN_DESCRIPTION

    async def add_default_keyboard(self, update, context):
        return [
            [
                Button(
                    'Back to main manu',
                    MainMenuScreen,
                    source_type=SourceTypes.MOVE_SOURCE_TYPE
                )
            ]
        ]


class PaymentScreen(Screen):
    description = PAYMENT_SCREEN_DESCRIPTION

    async def add_default_keyboard(self, update, context):
        return [
            [
                Button(
                    'Back to main manu',
                    MainMenuScreen,
                    source_type=SourceTypes.MOVE_SOURCE_TYPE
                )
            ]
        ]


def request_dynamic_keyboard():
    keyboard = [
        [
            Button(
                'Payment',
                PaymentScreen,
                source_type=SourceTypes.MOVE_SOURCE_TYPE
            ),
            Button(
                'MenuWithGeminiVersions',
                MenuVersionsScreen,
                source_type=SourceTypes.MOVE_SOURCE_TYPE
            )
        ]
    ]
    return keyboard

class MainMenuScreen(StartMixin, Screen):
    description = MAIN_MENU_SCREEN_DESCRIPTION

    async def add_default_keyboard(self, update, context):
        keyboard = request_dynamic_keyboard()

        return keyboard