import requests
import wikipedia
from pyrogram import filters, Client
from pyrogram.errors import BadRequest
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(filters.command("wiki"))
async def wiki(client, message):
    args = message.text.split(None, 1)
    if len(args) == 1:
        await message.reply_text("Enter keywords")
        return
    kueri = re.split(pattern="wiki", string=args[1])
    wikipedia.set_lang("en")
    try:
        pertama = await message.reply_text("Processing!")
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Read More", url=wikipedia.page(kueri).url
                    )
                ]
            ]
        )
        await pertama.edit_text(
                text=wikipedia.summary(kueri, sentences=10),
                reply_markup=keyboard,
        )
    except wikipedia.PageError as e:
        await message.reply_text(f"⚠ Error: {e}")
    except BadRequest as et:
        await message.reply_text(f"⚠ Error: {et}")
    except wikipedia.exceptions.DisambiguationError as eet:
        await message.reply_text(
            f"⚠ Error\n There are too many query! Express it more!\nPossible query result:\n{eet}"
        )
