# Python-Telegram-Bot - Other

**Pages:** 100

---

## BackgroundFillSolid¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.backgroundfillsolid.html

**Contents:**
- BackgroundFillSolid¶

Added in version 21.2.

Bases: telegram.BackgroundFill

The background is filled using the selected color.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their color is equal.

telegram.BackgroundTypeFill.fill

telegram.BackgroundTypePattern.fill

Added in version 21.2.

color (int) – The color of the background fill in the RGB24 format.

Type of the background fill. Always SOLID.

The color of the background fill in the RGB24 format.

---

## ChatMember¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.chatmember.html

**Contents:**
- ChatMember¶

Bases: telegram.TelegramObject

Base class for Telegram ChatMember Objects. Currently, the following 6 types of chat members are supported:

telegram.ChatMemberOwner

telegram.ChatMemberAdministrator

telegram.ChatMemberMember

telegram.ChatMemberRestricted

telegram.ChatMemberLeft

telegram.ChatMemberBanned

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their user and status are equal.

telegram.ChatMemberUpdated.new_chat_member

telegram.ChatMemberUpdated.old_chat_member

telegram.Bot.get_chat_administrators()

telegram.Bot.get_chat_member()

Changed in version 20.0:

As of Bot API 5.3, ChatMember is nothing but the base class for the subclasses listed above and is no longer returned directly by get_chat(). Therefore, most of the arguments and attributes were removed and you should no longer use ChatMember directly.

The constant ChatMember.CREATOR was replaced by OWNER

The constant ChatMember.KICKED was replaced by BANNED

user (telegram.User) – Information about the user.

status (str) – The member’s status in the chat. Can be ADMINISTRATOR, OWNER, BANNED, LEFT, MEMBER or RESTRICTED.

Information about the user.

The member’s status in the chat. Can be ADMINISTRATOR, OWNER, BANNED, LEFT, MEMBER or RESTRICTED.

telegram.constants.ChatMemberStatus.ADMINISTRATOR

telegram.constants.ChatMemberStatus.BANNED

telegram.constants.ChatMemberStatus.LEFT

telegram.constants.ChatMemberStatus.MEMBER

telegram.constants.ChatMemberStatus.OWNER

telegram.constants.ChatMemberStatus.RESTRICTED

See telegram.TelegramObject.de_json().

---

## ChatMemberLeft¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.chatmemberleft.html

**Contents:**
- ChatMemberLeft¶

Bases: telegram.ChatMember

Represents a chat member that isn’t currently a member of the chat, but may join it themselves.

telegram.ChatMemberUpdated.new_chat_member

telegram.ChatMemberUpdated.old_chat_member

telegram.Bot.get_chat_administrators()

telegram.Bot.get_chat_member()

Added in version 13.7.

user (telegram.User) – Information about the user.

The member’s status in the chat, always 'left'.

Information about the user.

---

## ForumTopic¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.forumtopic.html

**Contents:**
- ForumTopic¶

Bases: telegram.TelegramObject

This object represents a forum topic.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their message_thread_id, name and icon_color are equal.

telegram.Bot.create_forum_topic()

Added in version 20.0.

message_thread_id (int) – Unique identifier of the forum topic

name (str) – Name of the topic

icon_color (int) – Color of the topic icon in RGB format

icon_custom_emoji_id (str, optional) – Unique identifier of the custom emoji shown as the topic icon.

Unique identifier of the forum topic

Color of the topic icon in RGB format

Optional. Unique identifier of the custom emoji shown as the topic icon.

---

## Giveaway¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.giveaway.html

**Contents:**
- Giveaway¶

Bases: telegram.TelegramObject

This object represents a message about a scheduled giveaway.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their chats, winners_selection_date and winner_count are equal.

telegram.ExternalReplyInfo.giveaway

telegram.Message.giveaway

Added in version 20.8.

chats (tuple[telegram.Chat]) – The list of chats which the user must join to participate in the giveaway.

winners_selection_date (datetime.datetime) – The date when the giveaway winner will be selected. The default timezone of the bot is used for localization, which is UTC unless telegram.ext.Defaults.tzinfo is used.

winner_count (int) – The number of users which are supposed to be selected as winners of the giveaway.

only_new_members (True, optional) – If True, only users who join the chats after the giveaway started should be eligible to win.

has_public_winners (True, optional) – True, if the list of giveaway winners will be visible to everyone

prize_description (str, optional) – Description of additional giveaway prize

country_codes (Sequence[str]) – A list of two-letter ISO 3166-1 alpha-2 country codes indicating the countries from which eligible users for the giveaway must come. If empty, then all users can participate in the giveaway. Users with a phone number that was bought on Fragment can always participate in giveaways.

prize_star_count (int, optional) – The number of Telegram Stars to be split between giveaway winners; for Telegram Star giveaways only. Added in version 21.6.

The number of Telegram Stars to be split between giveaway winners; for Telegram Star giveaways only.

Added in version 21.6.

premium_subscription_month_count (int, optional) – The number of months the Telegram Premium subscription won from the giveaway will be active for; for Telegram Premium giveaways only.

The list of chats which the user must join to participate in the giveaway.

Sequence[telegram.Chat]

The date when the giveaway winner will be selected. The default timezone of the bot is used for localization, which is UTC unless telegram.ext.Defaults.tzinfo is used.

The number of users which are supposed to be selected as winners of the giveaway.

Optional. If True, only users who join the chats after the giveaway started should be eligible to win.

Optional. True, if the list of giveaway winners will be visible to everyone

Optional. Description of additional giveaway prize

Optional. A tuple of two-letter ISO 3166-1 alpha-2 country codes indicating the countries from which eligible users for the giveaway must come. If empty, then all users can participate in the giveaway. Users with a phone number that was bought on Fragment can always participate in giveaways.

Optional. The number of Telegram Stars to be split between giveaway winners; for Telegram Star giveaways only.

Added in version 21.6.

Optional. The number of months the Telegram Premium subscription won from the giveaway will be active for; for Telegram Premium giveaways only.

See telegram.TelegramObject.de_json().

---

## InlineKeyboardButton¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.inlinekeyboardbutton.html

**Contents:**
- InlineKeyboardButton¶

Bases: telegram.TelegramObject

This object represents one button of an inline keyboard.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their text, url, login_url, callback_data, switch_inline_query, switch_inline_query_current_chat, callback_game, web_app and pay are equal.

Exactly one of the optional fields must be used to specify type of the button.

Mind that callback_game is not working as expected. Putting a game short name in it might, but is not guaranteed to work.

If your bot allows for arbitrary callback data, in keyboards returned in a response from telegram, callback_data may be an instance of telegram.ext.InvalidCallbackData. This will be the case, if the data associated with the button was already deleted.

Added in version 13.6.

Since Bot API 5.5, it’s now allowed to mention users by their ID in inline keyboards. This will only work in Telegram versions released after December 7, 2021. Older clients will display unsupported message.

If your bot allows your arbitrary callback data, buttons whose callback data is a non-hashable object will become unhashable. Trying to evaluate hash(button) will result in a TypeError.

Changed in version 13.6.

After Bot API 6.1, only HTTPS links will be allowed in login_url.

telegram.InlineKeyboardMarkup

telegram.InlineKeyboardMarkup.inline_keyboard

Changed in version 20.0: web_app is considered as well when comparing objects of this type in terms of equality.

text (str) – Label text on the button.

url (str, optional) – HTTP or tg:// url to be opened when the button is pressed. Links tg://user?id=<user_id> can be used to mention a user by their ID without using a username, if this is allowed by their privacy settings. Changed in version 13.9: You can now mention a user using tg://user?id=<user_id>.

HTTP or tg:// url to be opened when the button is pressed. Links tg://user?id=<user_id> can be used to mention a user by their ID without using a username, if this is allowed by their privacy settings.

Changed in version 13.9: You can now mention a user using tg://user?id=<user_id>.

login_url (telegram.LoginUrl, optional) – An HTTPS URL used to automatically authorize the user. Can be used as a replacement for the Telegram Login Widget. Caution Only HTTPS links are allowed after Bot API 6.1.

An HTTPS URL used to automatically authorize the user. Can be used as a replacement for the Telegram Login Widget.

Only HTTPS links are allowed after Bot API 6.1.

callback_data (str | object, optional) – Data to be sent in a callback query to the bot when the button is pressed, UTF-8 1- 64 bytes. If the bot instance allows arbitrary callback data, anything can be passed. Tip The value entered here will be available in telegram.CallbackQuery.data. See also Arbitrary callback_data

Data to be sent in a callback query to the bot when the button is pressed, UTF-8 1- 64 bytes. If the bot instance allows arbitrary callback data, anything can be passed.

The value entered here will be available in telegram.CallbackQuery.data.

Arbitrary callback_data

web_app (telegram.WebAppInfo, optional) – Description of the Web App that will be launched when the user presses the button. The Web App will be able to send an arbitrary message on behalf of the user using the method answer_web_app_query(). Available only in private chats between a user and the bot. Not supported for messages sent on behalf of a Telegram Business account. Added in version 20.0.

Description of the Web App that will be launched when the user presses the button. The Web App will be able to send an arbitrary message on behalf of the user using the method answer_web_app_query(). Available only in private chats between a user and the bot. Not supported for messages sent on behalf of a Telegram Business account.

Added in version 20.0.

switch_inline_query (str, optional) – If set, pressing the button will prompt the user to select one of their chats, open that chat and insert the bot’s username and the specified inline query in the input field. May be empty, in which case just the bot’s username will be inserted. Not supported for messages sent on behalf of a Telegram Business account. Tip This is similar to the parameter switch_inline_query_chosen_chat, but gives no control over which chats can be selected.

If set, pressing the button will prompt the user to select one of their chats, open that chat and insert the bot’s username and the specified inline query in the input field. May be empty, in which case just the bot’s username will be inserted. Not supported for messages sent on behalf of a Telegram Business account.

This is similar to the parameter switch_inline_query_chosen_chat, but gives no control over which chats can be selected.

switch_inline_query_current_chat (str, optional) – If set, pressing the button will insert the bot’s username and the specified inline query in the current chat’s input field. May be empty, in which case only the bot’s username will be inserted. This offers a quick way for the user to open your bot in inline mode in the same chat - good for selecting something from multiple options. Not supported in channels and for messages sent on behalf of a Telegram Business account.

If set, pressing the button will insert the bot’s username and the specified inline query in the current chat’s input field. May be empty, in which case only the bot’s username will be inserted.

This offers a quick way for the user to open your bot in inline mode in the same chat - good for selecting something from multiple options. Not supported in channels and for messages sent on behalf of a Telegram Business account.

copy_text (telegram.CopyTextButton, optional) – Description of the button that copies the specified text to the clipboard. Added in version 21.7.

Description of the button that copies the specified text to the clipboard.

Added in version 21.7.

callback_game (telegram.CallbackGame, optional) – Description of the game that will be launched when the user presses the button Note This type of button must always be the first button in the first row.

Description of the game that will be launched when the user presses the button

This type of button must always be the first button in the first row.

pay (bool, optional) – Specify True, to send a Pay button. Substrings “⭐️” and “XTR” in the buttons’s text will be replaced with a Telegram Star icon. Note This type of button must always be the first button in the first row and can only be used in invoice messages.

Specify True, to send a Pay button. Substrings “⭐️” and “XTR” in the buttons’s text will be replaced with a Telegram Star icon.

This type of button must always be the first button in the first row and can only be used in invoice messages.

switch_inline_query_chosen_chat (telegram.SwitchInlineQueryChosenChat, optional) – If set, pressing the button will prompt the user to select one of their chats of the specified type, open that chat and insert the bot’s username and the specified inline query in the input field. Not supported for messages sent on behalf of a Telegram Business account. Added in version 20.3. Tip This is similar to switch_inline_query, but gives more control on which chats can be selected. Caution The PTB team has discovered that this field works correctly only if your Telegram client is released after April 20th 2023.

If set, pressing the button will prompt the user to select one of their chats of the specified type, open that chat and insert the bot’s username and the specified inline query in the input field. Not supported for messages sent on behalf of a Telegram Business account.

Added in version 20.3.

This is similar to switch_inline_query, but gives more control on which chats can be selected.

The PTB team has discovered that this field works correctly only if your Telegram client is released after April 20th 2023.

Label text on the button.

Optional. HTTP or tg:// url to be opened when the button is pressed. Links tg://user?id=<user_id> can be used to mention a user by their ID without using a username, if this is allowed by their privacy settings.

Changed in version 13.9: You can now mention a user using tg://user?id=<user_id>.

Optional. An HTTPS URL used to automatically authorize the user. Can be used as a replacement for the Telegram Login Widget.

Only HTTPS links are allowed after Bot API 6.1.

Optional. Data to be sent in a callback query to the bot when the button is pressed, UTF-8 1- 64 bytes.

Optional. Description of the Web App that will be launched when the user presses the button. The Web App will be able to send an arbitrary message on behalf of the user using the method answer_web_app_query(). Available only in private chats between a user and the bot. Not supported for messages sent on behalf of a Telegram Business account.

Added in version 20.0.

Optional. If set, pressing the button will prompt the user to select one of their chats, open that chat and insert the bot’s username and the specified inline query in the input field. May be empty, in which case just the bot’s username will be inserted. Not supported for messages sent on behalf of a Telegram Business account.

This is similar to the parameter switch_inline_query_chosen_chat, but gives no control over which chats can be selected.

Optional. If set, pressing the button will insert the bot’s username and the specified inline query in the current chat’s input field. May be empty, in which case only the bot’s username will be inserted.

This offers a quick way for the user to open your bot in inline mode in the same chat - good for selecting something from multiple options. Not supported in channels and for messages sent on behalf of a Telegram Business account.

Optional. Description of the button that copies the specified text to the clipboard.

Added in version 21.7.

telegram.CopyTextButton

Optional. Description of the game that will be launched when the user presses the button.

This type of button must always be the first button in the first row.

telegram.CallbackGame

Optional. Specify True, to send a Pay button. Substrings “⭐️” and “XTR” in the buttons’s text will be replaced with a Telegram Star icon.

This type of button must always be the first button in the first row and can only be used in invoice messages.

Optional. If set, pressing the button will prompt the user to select one of their chats of the specified type, open that chat and insert the bot’s username and the specified inline query in the input field. Not supported for messages sent on behalf of a Telegram Business account.

Added in version 20.3.

This is similar to switch_inline_query, but gives more control on which chats can be selected.

The PTB team has discovered that this field works correctly only if your Telegram client is released after April 20th 2023.

telegram.SwitchInlineQueryChosenChat

telegram.constants.InlineKeyboardButtonLimit.MAX_CALLBACK_DATA

Added in version 20.0.

telegram.constants.InlineKeyboardButtonLimit.MIN_CALLBACK_DATA

Added in version 20.0.

See telegram.TelegramObject.de_json().

Sets callback_data to the passed object. Intended to be used by telegram.ext.CallbackDataCache.

Added in version 13.6.

callback_data (object) – The new callback data.

---

## InaccessibleMessage¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.inaccessiblemessage.html

**Contents:**
- InaccessibleMessage¶

Bases: telegram.MaybeInaccessibleMessage

This object represents an inaccessible message.

These are messages that are e.g. deleted.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their message_id and chat are equal

telegram.CallbackQuery.message

telegram.Message.pinned_message

Added in version 20.8.

message_id (int) – Unique message identifier.

chat (telegram.Chat) – Chat the message belongs to.

Unique message identifier.

Always datetime.datetime(1970, 1, 1, 0, 0, tzinfo=datetime.timezone.utc). The field can be used to differentiate regular and inaccessible messages.

Chat the message belongs to.

---

## BusinessOpeningHoursInterval¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.businessopeninghoursinterval.html

**Contents:**
- BusinessOpeningHoursInterval¶

Bases: telegram.TelegramObject

This object describes an interval of time during which a business is open.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their opening_minute and closing_minute are equal.

telegram.BusinessOpeningHours.opening_hours

Added in version 21.1.

A day has (24 * 60 =) 1440 minutes, a week has (7 * 1440 =) 10080 minutes. Starting the minute’s sequence from Monday, example values of opening_minute, closing_minute will map to the following day times:

opening_minute = 480 8 * 60

closing_minute = 1230 20 * 60 + 30

opening_minute = 1440 24 * 60

closing_minute = 2879 2 * 24 * 60 - 1

opening_minute = 8640 6 * 24 * 60

closing_minute = 10078 7 * 24 * 60 - 2

opening_minute (int) – The minute’s sequence number in a week, starting on Monday, marking the start of the time interval during which the business is open; 0 - 7 * 24 * 60.

closing_minute (int) – The minute’s sequence number in a week, starting on Monday, marking the end of the time interval during which the business is open; 0 - 8 * 24 * 60

The minute’s sequence number in a week, starting on Monday, marking the start of the time interval during which the business is open; 0 - 7 * 24 * 60.

The minute’s sequence number in a week, starting on Monday, marking the end of the time interval during which the business is open; 0 - 8 * 24 * 60

Convenience attribute. A tuple parsed from closing_minute. It contains the weekday, hour and minute in the same ranges as datetime.datetime.weekday, datetime.datetime.hour and datetime.datetime.minute

Convenience attribute. A tuple parsed from opening_minute. It contains the weekday, hour and minute in the same ranges as datetime.datetime.weekday, datetime.datetime.hour and datetime.datetime.minute

---

## BackgroundTypePattern¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.backgroundtypepattern.html

**Contents:**
- BackgroundTypePattern¶

Added in version 21.2.

Bases: telegram.BackgroundType

The background is a .PNG or .TGV (gzipped subset of SVG with MIME type "application/x-tgwallpattern") pattern to be combined with the background fill chosen by the user.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their document and fill and intensity are equal.

telegram.ChatBackground.type

Added in version 21.2.

document (telegram.Document) – Document with the pattern.

fill (telegram.BackgroundFill) – The background fill that is combined with the pattern.

intensity (int) – Intensity of the pattern when it is shown above the filled background; 0-100.

is_inverted (int, optional) – True, if the background fill must be applied only to the pattern itself. All other pixels are black in this case. For dark themes only.

is_moving (bool, optional) – True, if the background moves slightly when the device is tilted.

Type of the background. Always PATTERN.

Document with the pattern.

The background fill that is combined with the pattern.

telegram.BackgroundFill

Intensity of the pattern when it is shown above the filled background; 0-100.

Optional. True, if the background fill must be applied only to the pattern itself. All other pixels are black in this case. For dark themes only.

Optional. True, if the background moves slightly when the device is tilted.

---

## InlineKeyboardMarkup¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.inlinekeyboardmarkup.html

**Contents:**
- InlineKeyboardMarkup¶

Bases: telegram.TelegramObject

This object represents an inline keyboard that appears right next to the message it belongs to.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their size of inline_keyboard and all the buttons are equal.

An inline keyboard on a message¶

Another kind of keyboard would be the telegram.ReplyKeyboardMarkup.

telegram.Bot.copy_message()

telegram.Bot.edit_message_caption()

telegram.Bot.edit_message_checklist()

telegram.Bot.edit_message_live_location()

telegram.Bot.edit_message_media()

telegram.Bot.edit_message_reply_markup()

telegram.Bot.edit_message_text()

telegram.Bot.send_animation()

telegram.Bot.send_audio()

telegram.Bot.send_checklist()

telegram.Bot.send_contact()

telegram.Bot.send_dice()

telegram.Bot.send_document()

telegram.Bot.send_game()

telegram.Bot.send_invoice()

telegram.Bot.send_location()

telegram.Bot.send_message()

telegram.Bot.send_paid_media()

telegram.Bot.send_photo()

telegram.Bot.send_poll()

telegram.Bot.send_sticker()

telegram.Bot.send_venue()

telegram.Bot.send_video_note()

telegram.Bot.send_video()

telegram.Bot.send_voice()

telegram.Bot.stop_message_live_location()

telegram.Bot.stop_poll()

telegram.InlineQueryResultArticle.reply_markup

telegram.InlineQueryResultAudio.reply_markup

telegram.InlineQueryResultCachedAudio.reply_markup

telegram.InlineQueryResultCachedDocument.reply_markup

telegram.InlineQueryResultCachedGif.reply_markup

telegram.InlineQueryResultCachedMpeg4Gif.reply_markup

telegram.InlineQueryResultCachedPhoto.reply_markup

telegram.InlineQueryResultCachedSticker.reply_markup

telegram.InlineQueryResultCachedVideo.reply_markup

telegram.InlineQueryResultCachedVoice.reply_markup

telegram.InlineQueryResultContact.reply_markup

telegram.InlineQueryResultDocument.reply_markup

telegram.InlineQueryResultGame.reply_markup

telegram.InlineQueryResultGif.reply_markup

telegram.InlineQueryResultLocation.reply_markup

telegram.InlineQueryResultMpeg4Gif.reply_markup

telegram.InlineQueryResultPhoto.reply_markup

telegram.InlineQueryResultVenue.reply_markup

telegram.InlineQueryResultVideo.reply_markup

telegram.InlineQueryResultVoice.reply_markup

telegram.Message.reply_markup

inline_keyboard (Sequence[Sequence[telegram.InlineKeyboardButton]]) – Sequence of button rows, each represented by a sequence of InlineKeyboardButton objects. Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list. The input is converted to a tuple.

Sequence of button rows, each represented by a sequence of InlineKeyboardButton objects.

Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list. The input is converted to a tuple.

Tuple of button rows, each represented by a tuple of InlineKeyboardButton objects.

Changed in version 20.0: This attribute is now an immutable tuple.

tuple[tuple[telegram.InlineKeyboardButton]]

See telegram.TelegramObject.de_json().

Return an InlineKeyboardMarkup from a single InlineKeyboardButton

button (telegram.InlineKeyboardButton) – The button to use in the markup

Return an InlineKeyboardMarkup from a single column of InlineKeyboardButtons

button_column (Sequence[telegram.InlineKeyboardButton]) – The button to use in the markup Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list.

The button to use in the markup

Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list.

Return an InlineKeyboardMarkup from a single row of InlineKeyboardButtons

button_row (Sequence[telegram.InlineKeyboardButton]) – The button to use in the markup Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list.

The button to use in the markup

Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list.

---

## Dice¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.dice.html

**Contents:**
- Dice¶

Bases: telegram.TelegramObject

This object represents an animated emoji with a random value for currently supported base emoji. (The singular form of “dice” is “die”. However, PTB mimics the Telegram API, which uses the term “dice”.)

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their value and emoji are equal.

If emoji is '🎯', a value of 6 currently represents a bullseye, while a value of 1 indicates that the dartboard was missed. However, this behaviour is undocumented and might be changed by Telegram.

If emoji is '🏀', a value of 4 or 5 currently score a basket, while a value of 1 to 3 indicates that the basket was missed. However, this behaviour is undocumented and might be changed by Telegram.

If emoji is '⚽', a value of 4 to 5 currently scores a goal, while a value of 1 to 3 indicates that the goal was missed. However, this behaviour is undocumented and might be changed by Telegram.

If emoji is '🎳', a value of 6 knocks all the pins, while a value of 1 means all the pins were missed. However, this behaviour is undocumented and might be changed by Telegram.

If emoji is '🎰', each value corresponds to a unique combination of symbols, which can be found in our wiki. However, this behaviour is undocumented and might be changed by Telegram.

telegram.ExternalReplyInfo.dice

telegram.Message.dice

telegram.Message.effective_attachment

value (int) – Value of the dice. 1-6 for '🎲', '🎯' and '🎳' base emoji, 1-5 for '🏀' and '⚽' base emoji, 1-64 for '🎰' base emoji.

emoji (str) – Emoji on which the dice throw animation is based.

Value of the dice. 1-6 for '🎲', '🎯' and '🎳' base emoji, 1-5 for '🏀' and '⚽' base emoji, 1-64 for '🎰' base emoji.

Emoji on which the dice throw animation is based.

A list of all available dice emoji.

telegram.constants.DiceEmoji.BASKETBALL

telegram.constants.DiceEmoji.BOWLING

Added in version 13.4.

telegram.constants.DiceEmoji.DARTS

telegram.constants.DiceEmoji.DICE

telegram.constants.DiceEmoji.FOOTBALL

telegram.constants.DiceLimit.MAX_VALUE_BASKETBALL

Added in version 20.0.

telegram.constants.DiceLimit.MAX_VALUE_BOWLING

Added in version 20.0.

telegram.constants.DiceLimit.MAX_VALUE_DARTS

Added in version 20.0.

telegram.constants.DiceLimit.MAX_VALUE_DICE

Added in version 20.0.

telegram.constants.DiceLimit.MAX_VALUE_FOOTBALL

Added in version 20.0.

telegram.constants.DiceLimit.MAX_VALUE_SLOT_MACHINE

Added in version 20.0.

telegram.constants.DiceLimit.MIN_VALUE

Added in version 20.0.

telegram.constants.DiceEmoji.SLOT_MACHINE

---

## File¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.file.html

**Contents:**
- File¶

Bases: telegram.TelegramObject

This object represents a file ready to be downloaded. The file can be e.g. downloaded with download_to_drive. It is guaranteed that the link will be valid for at least 1 hour. When the link expires, a new one can be requested by calling telegram.Bot.get_file().

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their file_unique_id is equal.

telegram.Sticker.premium_animation

telegram.Bot.get_file()

telegram.Bot.upload_sticker_file()

Changed in version 20.0: download was split into download_to_drive() and download_to_memory().

Maximum file size to download is 20 MB.

If you obtain an instance of this class from telegram.PassportFile.get_file, then it will automatically be decrypted as it downloads when you call e.g. download_to_drive().

file_id (str) – Identifier for this file, which can be used to download or reuse the file.

file_unique_id (str) – Unique identifier for this file, which is supposed to be the same over time and for different bots. Can’t be used to download or reuse the file.

file_size (int, optional) – File size in bytes, if known.

file_path (str, optional) – File path. Use e.g. download_to_drive() to get the file.

Identifier for this file, which can be used to download or reuse the file.

Unique identifier for this file, which is supposed to be the same over time and for different bots. Can’t be used to download or reuse the file.

Optional. File size in bytes, if known.

Optional. File path. Use e.g. download_to_drive() to get the file.

Download this file and return it as a bytearray.

Changed in version 21.7: Raises RuntimeError if file_path is not set. Note that files without a file_path could never be downloaded, as this attribute is mandatory for that operation.

buf (bytearray, optional) – Extend the given bytearray with the downloaded data.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE. Added in version 20.0.

Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

Added in version 20.0.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE. Added in version 20.0.

Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

Added in version 20.0.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE. Added in version 20.0.

Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

Added in version 20.0.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE. Added in version 20.0.

Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

Added in version 20.0.

The same object as buf if it was specified. Otherwise a newly allocated bytearray.

RuntimeError – If file_path is not set.

Download this file. By default, the file is saved in the current working directory with file_path as file name. If custom_path is supplied as a str or pathlib.Path, it will be saved to that path.

If custom_path isn’t provided and file_path is the path of a local file (which is the case when a Bot API Server is running in local mode), this method will just return the path.

The only exception to this are encrypted files (e.g. a passport file). For these, a file with the prefix decrypted_ will be created in the same directory as the original file in order to decrypt the file without changing the existing one in-place.

Working with Files and Media

Changed in version 20.0:

custom_path parameter now also accepts pathlib.Path as argument.

Returns pathlib.Path object in cases where previously a str was returned.

This method was previously called download. It was split into download_to_drive() and download_to_memory().

Changed in version 21.7: Raises RuntimeError if file_path is not set. Note that files without a file_path could never be downloaded, as this attribute is mandatory for that operation.

custom_path (pathlib.Path | str , optional) – The path where the file will be saved to. If not specified, will be saved in the current working directory with file_path as file name or the file_id if file_path is not set.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

Returns the Path object the file was downloaded to.

RuntimeError – If file_path is not set.

Download this file into memory. out needs to be supplied with a io.BufferedIOBase, the file contents will be saved to that object using the out.write method.

Working with Files and Media

If you want to immediately read the data from out after calling this method, you should call out.seek(0) first. See also io.IOBase.seek().

Added in version 20.0.

Changed in version 21.7: Raises RuntimeError if file_path is not set. Note that files without a file_path could never be downloaded, as this attribute is mandatory for that operation.

out (io.BufferedIOBase) – A file-like object. Must be opened for writing in binary mode.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

RuntimeError – If file_path is not set.

Sets the passport credentials for the file.

credentials (telegram.FileCredentials) – The credentials.

---

## Audio¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.audio.html

**Contents:**
- Audio¶

Bases: telegram.TelegramObject

This object represents an audio file to be treated as music by the Telegram clients.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their file_unique_id is equal.

telegram.Bot.get_file()

telegram.Bot.send_audio()

telegram.ExternalReplyInfo.audio

telegram.InputMediaAudio.media

telegram.Message.audio

telegram.Message.effective_attachment

Changed in version 20.5: Removed the deprecated argument and attribute thumb.

file_id (str) – Identifier for this file, which can be used to download or reuse the file.

file_unique_id (str) – Unique identifier for this file, which is supposed to be the same over time and for different bots. Can’t be used to download or reuse the file.

duration (int | datetime.timedelta) – Duration of the audio in seconds as defined by the sender. Changed in version v22.2: datetime.timedelta objects are accepted in addition to plain int values.

Duration of the audio in seconds as defined by the sender.

Changed in version v22.2: datetime.timedelta objects are accepted in addition to plain int values.

performer (str, optional) – Performer of the audio as defined by the sender or by audio tags.

title (str, optional) – Title of the audio as defined by the sender or by audio tags.

file_name (str, optional) – Original filename as defined by the sender.

mime_type (str, optional) – MIME type of the file as defined by the sender.

file_size (int, optional) – File size in bytes.

thumbnail (telegram.PhotoSize, optional) – Thumbnail of the album cover to which the music file belongs. Added in version 20.2.

Thumbnail of the album cover to which the music file belongs.

Added in version 20.2.

Identifier for this file, which can be used to download or reuse the file.

Unique identifier for this file, which is supposed to be the same over time and for different bots. Can’t be used to download or reuse the file.

Duration of the audio in seconds as defined by the sender.

Deprecated since version v22.2: In a future major version this attribute will be of type datetime.timedelta. You can opt-in early by setting PTB_TIMEDELTA=true or PTB_TIMEDELTA=1 as an environment variable.

int | datetime.timedelta

Optional. Performer of the audio as defined by the sender or by audio tags.

Optional. Title of the audio as defined by the sender or by audio tags.

Optional. Original filename as defined by the sender.

Optional. MIME type of the file as defined by the sender.

Optional. File size in bytes.

Optional. Thumbnail of the album cover to which the music file belongs.

Added in version 20.2.

See telegram.TelegramObject.de_json().

Convenience wrapper over telegram.Bot.get_file()

For the documentation of the arguments, please see telegram.Bot.get_file().

telegram.error.TelegramError –

---

## GiveawayWinners¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.giveawaywinners.html

**Contents:**
- GiveawayWinners¶

Bases: telegram.TelegramObject

This object represents a message about the completion of a giveaway with public winners.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their chat, giveaway_message_id, winners_selection_date, winner_count and winners are equal.

telegram.ExternalReplyInfo.giveaway_winners

telegram.Message.giveaway_winners

Added in version 20.8.

chat (telegram.Chat) – The chat that created the giveaway

giveaway_message_id (int) – Identifier of the message with the giveaway in the chat

winners_selection_date (datetime.datetime) – Point in time when winners of the giveaway were selected. The default timezone of the bot is used for localization, which is UTC unless telegram.ext.Defaults.tzinfo is used.

winner_count (int) – Total number of winners in the giveaway

winners (Sequence[telegram.User]) – List of up to 100 winners of the giveaway

prize_star_count (int, optional) – The number of Telegram Stars to be split between giveaway winners; for Telegram Star giveaways only. Added in version 21.6.

The number of Telegram Stars to be split between giveaway winners; for Telegram Star giveaways only.

Added in version 21.6.

additional_chat_count (int, optional) – The number of other chats the user had to join in order to be eligible for the giveaway

premium_subscription_month_count (int, optional) – The number of months the Telegram Premium subscription won from the giveaway will be active for

unclaimed_prize_count (int, optional) – Number of undistributed prizes

only_new_members (True, optional) – True, if only users who had joined the chats after the giveaway started were eligible to win

was_refunded (True, optional) – True, if the giveaway was canceled because the payment for it was refunded

prize_description (str, optional) – Description of additional giveaway prize

The chat that created the giveaway

Identifier of the message with the giveaway in the chat

Point in time when winners of the giveaway were selected. The default timezone of the bot is used for localization, which is UTC unless telegram.ext.Defaults.tzinfo is used.

Total number of winners in the giveaway

tuple of up to 100 winners of the giveaway

Optional. The number of other chats the user had to join in order to be eligible for the giveaway

Optional. The number of Telegram Stars to be split between giveaway winners; for Telegram Star giveaways only.

Added in version 21.6.

Optional. The number of months the Telegram Premium subscription won from the giveaway will be active for

Optional. Number of undistributed prizes

Optional. True, if only users who had joined the chats after the giveaway started were eligible to win

Optional. True, if the giveaway was canceled because the payment for it was refunded

Optional. Description of additional giveaway prize

See telegram.TelegramObject.de_json().

---

## BotCommandScopeChat¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.botcommandscopechat.html

**Contents:**
- BotCommandScopeChat¶

Bases: telegram.BotCommandScope

Represents the scope of bot commands, covering a specific chat.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their type and chat_id are equal.

telegram.Bot.delete_my_commands()

telegram.Bot.get_my_commands()

telegram.Bot.set_my_commands()

Added in version 13.7.

chat_id (str | int) – Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername).

Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername).

---

## ChatMemberAdministrator¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.chatmemberadministrator.html

**Contents:**
- ChatMemberAdministrator¶

Bases: telegram.ChatMember

Represents a chat member that has some additional privileges.

telegram.ChatMemberUpdated.new_chat_member

telegram.ChatMemberUpdated.old_chat_member

telegram.Bot.get_chat_administrators()

telegram.Bot.get_chat_member()

Added in version 13.7.

Changed in version 20.0:

Argument and attribute can_manage_voice_chats were renamed to can_manage_video_chats and can_manage_video_chats in accordance to Bot API 6.0.

The argument can_manage_topics was added, which changes the position of the optional argument custom_title.

Changed in version 21.1: As of this version, can_post_stories, can_edit_stories, and can_delete_stories is now required. Thus, the order of arguments had to be changed.

user (telegram.User) – Information about the user.

can_be_edited (bool) – True, if the bot is allowed to edit administrator privileges of that user.

is_anonymous (bool) – True, if the user’s presence in the chat is hidden.

can_manage_chat (bool) – True, if the administrator can access the chat event log, get boost list, see hidden supergroup and channel members, report spam messages and ignore slow mode. Implied by any other administrator privilege.

can_delete_messages (bool) – True, if the administrator can delete messages of other users.

can_manage_video_chats (bool) – True, if the administrator can manage video chats. Added in version 20.0.

True, if the administrator can manage video chats.

Added in version 20.0.

can_restrict_members (bool) – True, if the administrator can restrict, ban or unban chat members.

can_promote_members (bool) – True, if the administrator can add new administrators with a subset of his own privileges or demote administrators that he has promoted, directly or indirectly (promoted by administrators that were appointed by the user).

can_change_info (bool) – True, if the user can change the chat title, photo and other settings.

can_invite_users (bool) – True, if the user can invite new users to the chat.

can_post_messages (bool, optional) – True, if the administrator can post messages in the channel, or access channel statistics; for channels only.

can_edit_messages (bool, optional) – True, if the administrator can edit messages of other users and can pin messages; for channels only.

can_pin_messages (bool, optional) – True, if the user is allowed to pin messages; for groups and supergroups only.

can_post_stories (bool) – True, if the administrator can post stories to the chat. Added in version 20.6. Changed in version 21.0: As of this version, this argument is now required. In accordance with our stability policy, the signature will be kept as optional for now, though they are mandatory and an error will be raised if you don’t pass it.

True, if the administrator can post stories to the chat.

Added in version 20.6.

Changed in version 21.0: As of this version, this argument is now required. In accordance with our stability policy, the signature will be kept as optional for now, though they are mandatory and an error will be raised if you don’t pass it.

can_edit_stories (bool) – True, if the administrator can edit stories posted by other users, post stories to the chat page, pin chat stories, and access the chat’s story archive Added in version 20.6. Changed in version 21.0: As of this version, this argument is now required. In accordance with our stability policy, the signature will be kept as optional for now, though they are mandatory and an error will be raised if you don’t pass it.

True, if the administrator can edit stories posted by other users, post stories to the chat page, pin chat stories, and access the chat’s story archive

Added in version 20.6.

Changed in version 21.0: As of this version, this argument is now required. In accordance with our stability policy, the signature will be kept as optional for now, though they are mandatory and an error will be raised if you don’t pass it.

can_delete_stories (bool) – True, if the administrator can delete stories posted by other users. Added in version 20.6. Changed in version 21.0: As of this version, this argument is now required. In accordance with our stability policy, the signature will be kept as optional for now, though they are mandatory and an error will be raised if you don’t pass it.

True, if the administrator can delete stories posted by other users.

Added in version 20.6.

Changed in version 21.0: As of this version, this argument is now required. In accordance with our stability policy, the signature will be kept as optional for now, though they are mandatory and an error will be raised if you don’t pass it.

can_manage_topics (bool, optional) – True, if the user is allowed to create, rename, close, and reopen forum topics; for supergroups only. Added in version 20.0.

True, if the user is allowed to create, rename, close, and reopen forum topics; for supergroups only.

Added in version 20.0.

custom_title (str, optional) – Custom title for this user.

can_manage_direct_messages (bool, optional) – True, if the administrator can manage direct messages of the channel and decline suggested posts; for channels only. Added in version 22.4.

True, if the administrator can manage direct messages of the channel and decline suggested posts; for channels only.

Added in version 22.4.

The member’s status in the chat, always 'administrator'.

Information about the user.

True, if the bot is allowed to edit administrator privileges of that user.

True, if the user’s presence in the chat is hidden.

True, if the administrator can access the chat event log, get boost list, see hidden supergroup and channel members, report spam messages and ignore slow mode. Implied by any other administrator privilege.

True, if the administrator can delete messages of other users.

True, if the administrator can manage video chats.

Added in version 20.0.

True, if the administrator can restrict, ban or unban chat members, or access supergroup statistics.

True, if the administrator can add new administrators with a subset of their own privileges or demote administrators that they have promoted, directly or indirectly (promoted by administrators that were appointed by the user).

True, if the user can change the chat title, photo and other settings.

True, if the user can invite new users to the chat.

Optional. True, if the administrator can post messages in the channel or access channel statistics; for channels only.

Optional. True, if the administrator can edit messages of other users and can pin messages; for channels only.

Optional. True, if the user is allowed to pin messages; for groups and supergroups only.

True, if the administrator can post stories to the chat.

Added in version 20.6.

Changed in version 21.0: As of this version, this argument is now required. In accordance with our stability policy, the signature will be kept as optional for now, though they are mandatory and an error will be raised if you don’t pass it.

True, if the administrator can edit stories posted by other users, post stories to the chat page, pin chat stories, and access the chat’s story archive

Added in version 20.6.

Changed in version 21.0: As of this version, this argument is now required. In accordance with our stability policy, the signature will be kept as optional for now, though they are mandatory and an error will be raised if you don’t pass it.

True, if the administrator can delete stories posted by other users.

Added in version 20.6.

Changed in version 21.0: As of this version, this argument is now required. In accordance with our stability policy, the signature will be kept as optional for now, though they are mandatory and an error will be raised if you don’t pass it.

Optional. True, if the user is allowed to create, rename, close, and reopen forum topics; for supergroups only

Added in version 20.0.

Optional. Custom title for this user.

True, if the administrator can manage direct messages of the channel and decline suggested posts; for channels only.

Added in version 22.4.

---

## ChatBoostRemoved¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.chatboostremoved.html

**Contents:**
- ChatBoostRemoved¶

Added in version 20.8.

Bases: telegram.TelegramObject

This object represents a boost removed from a chat.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their chat, boost_id, remove_date, and source are equal.

telegram.Update.removed_chat_boost

chat (telegram.Chat) – Chat which was boosted.

boost_id (str) – Unique identifier of the boost.

remove_date (datetime.datetime) – Point in time when the boost was removed.

source (telegram.ChatBoostSource) – Source of the removed boost.

Chat which was boosted.

Unique identifier of the boost.

Point in time when the boost was removed. The default timezone of the bot is used for localization, which is UTC unless telegram.ext.Defaults.tzinfo is used.

Source of the removed boost.

telegram.ChatBoostSource

See telegram.TelegramObject.de_json().

---

## Checklist¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.checklist.html

**Contents:**
- Checklist¶

Bases: telegram.TelegramObject

Describes a checklist.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if all their tasks are equal.

telegram.ExternalReplyInfo.checklist

telegram.Message.checklist

Added in version 22.3.

title (str) – Title of the checklist.

title_entities (Sequence[telegram.MessageEntity], optional) – Special entities that appear in the checklist title.

tasks (Sequence[telegram.ChecklistTask]) – List of tasks in the checklist.

others_can_add_tasks (bool, optional) – True if users other than the creator of the list can add tasks to the list

others_can_mark_tasks_as_done (bool, optional) – True if users other than the creator of the list can mark tasks as done or not done

Title of the checklist.

Optional. Special entities that appear in the checklist title.

Tuple[telegram.MessageEntity]

List of tasks in the checklist.

Tuple[telegram.ChecklistTask]

Optional. True if users other than the creator of the list can add tasks to the list

Optional. True if users other than the creator of the list can mark tasks as done or not done

See telegram.TelegramObject.de_json().

Returns a dict that maps telegram.MessageEntity to str. It contains entities from this checklist’s title filtered by their type attribute as the key, and the text that each entity belongs to as the value of the dict.

This method should always be used instead of the title_entities attribute, since it calculates the correct substring from the message text based on UTF-16 codepoints. See parse_entity for more info.

types (list[str], optional) – List of MessageEntity types as strings. If the type attribute of an entity is contained in this list, it will be returned. Defaults to telegram.MessageEntity.ALL_TYPES.

A dictionary of entities mapped to the text that belongs to them, calculated based on UTF-16 codepoints.

dict[telegram.MessageEntity, str]

Returns the text in title from a given telegram.MessageEntity of title_entities.

This method is present because Telegram calculates the offset and length in UTF-16 codepoint pairs, which some versions of Python don’t handle automatically. (That is, you can’t just slice title with the offset and length.)

entity (telegram.MessageEntity) – The entity to extract the text from. It must be an entity that belongs to title_entities.

The text of the given entity.

---

## BusinessLocation¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.businesslocation.html

**Contents:**
- BusinessLocation¶

Bases: telegram.TelegramObject

This object contains information about the location of a Telegram Business account.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their address is equal.

telegram.ChatFullInfo.business_location

Added in version 21.1.

address (str) – Address of the business.

location (telegram.Location, optional) – Location of the business.

Address of the business.

Optional. Location of the business.

See telegram.TelegramObject.de_json().

---

## ChatShared¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.chatshared.html

**Contents:**
- ChatShared¶

Bases: telegram.TelegramObject

This object contains information about the chat whose identifier was shared with the bot using a telegram.KeyboardButtonRequestChat button.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their request_id and chat_id are equal.

telegram.Message.chat_shared

Added in version 20.1.

request_id (int) – Identifier of the request.

chat_id (int) – Identifier of the shared user. This number may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.

title (str, optional) – Title of the chat, if the title was requested by the bot. Added in version 21.1.

Title of the chat, if the title was requested by the bot.

Added in version 21.1.

username (str, optional) – Username of the chat, if the username was requested by the bot and available. Added in version 21.1.

Username of the chat, if the username was requested by the bot and available.

Added in version 21.1.

photo (Sequence[telegram.PhotoSize], optional) – Available sizes of the chat photo, if the photo was requested by the bot Added in version 21.1.

Available sizes of the chat photo, if the photo was requested by the bot

Added in version 21.1.

Identifier of the request.

Identifier of the shared user. This number may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.

Optional. Title of the chat, if the title was requested by the bot.

Added in version 21.1.

Optional. Username of the chat, if the username was requested by the bot and available.

Added in version 21.1.

Optional. Available sizes of the chat photo, if the photo was requested by the bot

Added in version 21.1.

tuple[telegram.PhotoSize]

See telegram.TelegramObject.de_json().

Convenience property. If username is available, returns a t.me link of the chat.

Added in version 22.4.

---

## ChatMemberBanned¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.chatmemberbanned.html

**Contents:**
- ChatMemberBanned¶

Bases: telegram.ChatMember

Represents a chat member that was banned in the chat and can’t return to the chat or view chat messages.

telegram.ChatMemberUpdated.new_chat_member

telegram.ChatMemberUpdated.old_chat_member

telegram.Bot.get_chat_administrators()

telegram.Bot.get_chat_member()

Added in version 13.7.

user (telegram.User) – Information about the user.

until_date (datetime.datetime) – Date when restrictions will be lifted for this user. Changed in version 20.3: The default timezone of the bot is used for localization, which is UTC unless telegram.ext.Defaults.tzinfo is used.

Date when restrictions will be lifted for this user.

Changed in version 20.3: The default timezone of the bot is used for localization, which is UTC unless telegram.ext.Defaults.tzinfo is used.

The member’s status in the chat, always 'kicked'.

Information about the user.

Date when restrictions will be lifted for this user.

Changed in version 20.3: The default timezone of the bot is used for localization, which is UTC unless telegram.ext.Defaults.tzinfo is used.

---

## Bot¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.bot.html

**Contents:**
- Bot¶

Bases: telegram.TelegramObject, contextlib.AbstractAsyncContextManager

This object represents a Telegram Bot.

Instances of this class can be used as asyncio context managers, where

is roughly equivalent to

__aenter__() and __aexit__().

Most bot methods have the argument api_kwargs which allows passing arbitrary keywords to the Telegram API. This can be used to access new features of the API before they are incorporated into PTB. The limitations to this argument are the same as the ones described in do_api_request().

Bots should not be serialized since if you for e.g. change the bots token, then your serialized instance will not reflect that change. Trying to pickle a bot instance will raise pickle.PicklingError. Trying to deepcopy a bot instance will raise TypeError.

Your First Bot, Builder Pattern

telegram.ext.ApplicationBuilder.bot()

telegram.ext.Application.bot

telegram.ext.CallbackContext.bot

telegram.ext.Updater.bot

Added in version 13.2: Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their bot is equal.

Changed in version 20.0:

Removed the deprecated methods kick_chat_member, kickChatMember, get_chat_members_count and getChatMembersCount.

Removed the deprecated property commands.

Removed the deprecated defaults parameter. If you want to use telegram.ext.Defaults, please use the subclass telegram.ext.ExtBot instead.

Attempting to pickle a bot instance will now raise pickle.PicklingError.

Attempting to deepcopy a bot instance will now raise TypeError.

The following are now keyword-only arguments in Bot methods: location, filename, venue, contact, {read, write, connect, pool}_timeout, api_kwargs. Use a named argument for those, and notice that some positional arguments changed position as a result.

For uploading files, file paths are now always accepted. If local_mode is False, the file contents will be read in binary mode and uploaded. Otherwise, the file path will be passed in the file URI scheme.

Changed in version 20.5: Removed deprecated methods set_sticker_set_thumb and setStickerSetThumb. Use set_sticker_set_thumbnail() and setStickerSetThumbnail() instead.

token (str) – Bot’s unique authentication token.

base_url (str | Callable[[str], str], optional) – Telegram Bot API service URL. If the string contains {token}, it will be replaced with the bot’s token. If a callable is passed, it will be called with the bot’s token as the only argument and must return the base URL. Otherwise, the token will be appended to the string. Defaults to "https://api.telegram.org/bot". Tip Customizing the base URL can be used to run a bot against Local Bot API Server or using Telegrams test environment. Example:"https://api.telegram.org/bot{token}/test" Changed in version 21.11: Supports callable input and string formatting.

Telegram Bot API service URL. If the string contains {token}, it will be replaced with the bot’s token. If a callable is passed, it will be called with the bot’s token as the only argument and must return the base URL. Otherwise, the token will be appended to the string. Defaults to "https://api.telegram.org/bot".

Customizing the base URL can be used to run a bot against Local Bot API Server or using Telegrams test environment.

"https://api.telegram.org/bot{token}/test"

Changed in version 21.11: Supports callable input and string formatting.

base_file_url (str, optional) – Telegram Bot API file URL. If the string contains {token}, it will be replaced with the bot’s token. If a callable is passed, it will be called with the bot’s token as the only argument and must return the base URL. Otherwise, the token will be appended to the string. Defaults to "https://api.telegram.org/bot". Tip Customizing the base URL can be used to run a bot against Local Bot API Server or using Telegrams test environment. Example:"https://api.telegram.org/file/bot{token}/test" Changed in version 21.11: Supports callable input and string formatting.

Telegram Bot API file URL. If the string contains {token}, it will be replaced with the bot’s token. If a callable is passed, it will be called with the bot’s token as the only argument and must return the base URL. Otherwise, the token will be appended to the string. Defaults to "https://api.telegram.org/bot".

Customizing the base URL can be used to run a bot against Local Bot API Server or using Telegrams test environment.

"https://api.telegram.org/file/bot{token}/test"

Changed in version 21.11: Supports callable input and string formatting.

request (telegram.request.BaseRequest, optional) – Pre initialized telegram.request.BaseRequest instances. Will be used for all bot methods except for get_updates(). If not passed, an instance of telegram.request.HTTPXRequest will be used.

get_updates_request (telegram.request.BaseRequest, optional) – Pre initialized telegram.request.BaseRequest instances. Will be used exclusively for get_updates(). If not passed, an instance of telegram.request.HTTPXRequest will be used.

private_key (bytes, optional) – Private key for decryption of telegram passport data.

private_key_password (bytes, optional) – Password for above private key.

local_mode (bool, optional) – Set to True, if the base_url is the URI of a Local Bot API Server that runs with the --local flag. Currently, the only effect of this is that files are uploaded using their local path in the file URI scheme. Defaults to False. Added in version 20.0..

Set to True, if the base_url is the URI of a Local Bot API Server that runs with the --local flag. Currently, the only effect of this is that files are uploaded using their local path in the file URI scheme. Defaults to False.

Added in version 20.0..

Since this class has a large number of methods and attributes, below you can find a quick overview.

Used for sending animations

Used for sending audio files

Used for sending chat actions

Used for sending contacts

Used for sending dice messages

Used for sending documents

Used for sending a game

Used for sending a gift

Used for sending an invoice

Used for sending location

Used for sending media grouped together

Used for sending text messages

Used for sending paid media to channels

Used for sending photos

Used for sending polls

Used for sending stickers

Used for sending venue locations.

Used for sending videos

Used for sending video notes

Used for sending voice messages

Used for copying the contents of an arbitrary message

Used for copying the contents of an multiple arbitrary messages

Used for forwarding messages

Used for forwarding multiple messages at once

answer_callback_query()

Used for answering the callback query

answer_inline_query()

Used for answering the inline query

answer_pre_checkout_query()

Used for answering a pre checkout query

answer_shipping_query()

Used for answering a shipping query

answer_web_app_query()

Used for answering a web app query

Used for deleting messages.

Used for deleting multiple messages as once.

edit_message_caption()

Used for editing captions

Used for editing the media on messages

edit_message_live_location()

Used for editing the location in live location messages

edit_message_reply_markup()

Used for editing the reply markup on messages

Used for editing text messages

Used for stopping the running poll

set_message_reaction()

Used for setting reactions on messages

approve_chat_join_request()

Used for approving a chat join request

decline_chat_join_request()

Used for declining a chat join request

approve_suggested_post()

Used for approving a suggested post

decline_suggested_post()

Used for declining a suggested post

Used for banning a member from the chat

Used for unbanning a member from the chat

ban_chat_sender_chat()

Used for banning a channel in a channel or supergroup

unban_chat_sender_chat()

Used for unbanning a channel in a channel or supergroup

restrict_chat_member()

Used for restricting a chat member

promote_chat_member()

Used for promoting a chat member

set_chat_administrator_custom_title()

Used for assigning a custom admin title to an admin

set_chat_permissions()

Used for setting the permissions of a chat

export_chat_invite_link()

Used for creating a new primary invite link for a chat

create_chat_invite_link()

Used for creating an additional invite link for a chat

edit_chat_invite_link()

Used for editing a non-primary invite link

revoke_chat_invite_link()

Used for revoking an invite link created by the bot

Used for setting a photo to a chat

Used for deleting a chat photo

Used for setting a chat title

set_chat_description()

Used for setting the description of a chat

set_user_emoji_status()

Used for setting the users status emoji

Used for pinning a message

Used for unpinning a message

unpin_all_chat_messages()

Used for unpinning all pinned chat messages

get_user_profile_photos()

Used for obtaining user’s profile pictures

Used for getting information about a chat

get_chat_administrators()

Used for getting the list of admins in a chat

get_chat_member_count()

Used for getting the number of members in a chat

Used for getting a member of a chat

get_user_chat_boosts()

Used for getting the list of boosts added to a chat

Used for leaving a chat

Used for verifying a chat

Used for verifying a user

remove_chat_verification()

Used for removing the verification from a chat

remove_user_verification()

Used for removing the verification from a user

Used for setting the list of commands

Used for deleting the list of commands

Used for obtaining the list of commands

get_my_default_administrator_rights()

Used for obtaining the default administrator rights for the bot

set_my_default_administrator_rights()

Used for setting the default administrator rights for the bot

get_chat_menu_button()

Used for obtaining the menu button of a private chat or the default menu button

set_chat_menu_button()

Used for setting the menu button of a private chat or the default menu button

Used for setting the description of the bot

Used for obtaining the description of the bot

set_my_short_description()

Used for setting the short description of the bot

get_my_short_description()

Used for obtaining the short description of the bot

Used for setting the name of the bot

Used for obtaining the name of the bot

Used for adding a sticker to a set

delete_sticker_from_set()

Used for deleting a sticker from a set

create_new_sticker_set()

Used for creating a new sticker set

Used for deleting a sticker set made by a bot

set_chat_sticker_set()

Used for setting a sticker set of a chat

delete_chat_sticker_set()

Used for deleting the set sticker set of a chat

replace_sticker_in_set()

Used for replacing a sticker in a set

set_sticker_position_in_set()

Used for moving a sticker’s position in the set

set_sticker_set_title()

Used for setting the title of a sticker set

set_sticker_emoji_list()

Used for setting the emoji list of a sticker

set_sticker_keywords()

Used for setting the keywords of a sticker

set_sticker_mask_position()

Used for setting the mask position of a mask sticker

set_sticker_set_thumbnail()

Used for setting the thumbnail of a sticker set

set_custom_emoji_sticker_set_thumbnail()

Used for setting the thumbnail of a custom emoji sticker set

Used for getting a sticker set

upload_sticker_file()

Used for uploading a sticker file

get_custom_emoji_stickers()

Used for getting custom emoji files based on their IDs

get_game_high_scores()

Used for getting the game high scores

Used for setting the game score

Used for getting updates using long polling

Used for getting current webhook status

Used for setting a webhook to receive updates

Used for removing webhook integration

Used for closing a forum topic

close_general_forum_topic()

Used for closing the general forum topic

Used to create a topic

Used for deleting a forum topic

edit_general_forum_topic()

Used to edit the general topic

get_forum_topic_icon_stickers()

Used to get custom emojis to use as topic icons

hide_general_forum_topic()

Used to hide the general topic

unhide_general_forum_topic()

Used to unhide the general topic

Used to reopen a topic

reopen_general_forum_topic()

Used to reopen the general topic

unpin_all_forum_topic_messages()

Used to unpin all messages in a forum topic

unpin_all_general_forum_topic_messages()

Used to unpin all messages in the general forum topic

create_invoice_link()

Used to generate an HTTP link for an invoice

edit_user_star_subscription()

Used for editing a user’s star subscription

get_my_star_balance()

Used for obtaining the bot’s Telegram Stars balance

get_star_transactions()

Used for obtaining the bot’s Telegram Stars transactions

refund_star_payment()

Used for refunding a payment in Telegram Stars

gift_premium_subscription()

Used for gifting Telegram Premium to another user.

get_business_connection()

Used for getting information about the business account.

get_business_account_gifts()

Used for getting gifts owned by the business account.

get_business_account_star_balance()

Used for getting the amount of Stars owned by the business account.

read_business_message()

Used for marking a message as read.

Used for deleting business stories posted by the bot.

delete_business_messages()

Used for deleting business messages.

remove_business_account_profile_photo()

Used for removing the business accounts profile photo

set_business_account_name()

Used for setting the business account name.

set_business_account_username()

Used for setting the business account username.

set_business_account_bio()

Used for setting the business account bio.

set_business_account_gift_settings()

Used for setting the business account gift settings.

set_business_account_profile_photo()

Used for setting the business accounts profile photo

Used for posting a story on behalf of business account.

Used for editing business stories posted by the bot.

convert_gift_to_stars()

Used for converting owned reqular gifts to stars.

Used for upgrading owned regular gifts to unique ones.

Used for transferring owned unique gifts to another user.

transfer_business_account_stars()

Used for transfering Stars from the business account balance to the bot’s balance.

Used for sending a checklist on behalf of the business account.

edit_message_checklist()

Used for editing a checklist on behalf of the business account.

Used for closing server instance when switching to another local server

Used for logging out from cloud Bot API server

Used for getting basic info about a file

get_available_gifts()

Used for getting information about gifts available for sending

Used for getting basic information about the bot

save_prepared_inline_message()

Used for storing a message to be sent by a user of a Mini App

Telegram Bot API file URL

Telegram Bot API service URL

The user instance of the bot as returned by get_me()

Whether the bot can join groups

can_read_all_group_messages

Whether the bot can read all incoming group messages

The user id of the bot

The username of the bot, with leading @

The first name of the bot

The last name of the bot

Whether the bot is running in local mode

The username of the bot, without leading @

The t.me link of the bot

Deserialized private key for decryption of telegram passport data

supports_inline_queries

Whether the bot supports inline queries

Bot’s unique authentication token

Asynchronous context manager which initializes the Bot.

The initialized Bot instance.

Exception – If an exception is raised during initialization, shutdown() is called in this case.

Asynchronous context manager which shuts down the Bot.

Customizes how copy.deepcopy() processes objects of this type. Bots can not be deepcopied and this method will always raise an exception.

Added in version 20.0.

Defines equality condition for the telegram.Bot object. Two objects of this class are considered to be equal if their attributes bot are equal.

True if both attributes bot are equal. False otherwise.

See telegram.TelegramObject.__hash__()

Customizes how copy.deepcopy() processes objects of this type. Bots can not be pickled and this method will always raise an exception.

Added in version 20.0.

pickle.PicklingError –

Give a string representation of the bot in the form Bot[token=...].

As this class doesn’t implement object.__str__(), the default implementation will be used, which is equivalent to __repr__().

Alias for add_sticker_to_set()

Use this method to add a new sticker to a set created by the bot. The format of the added sticker must match the format of the other stickers in the set. Emoji sticker sets can have up to 200 stickers. Other sticker sets can have up to 120 stickers.

Changed in version 20.2: Since Bot API 6.6, the parameter sticker replace the parameters png_sticker, tgs_sticker, webm_sticker, emojis, and mask_position.

Changed in version 20.5: Removed deprecated parameters png_sticker, tgs_sticker, webm_sticker, emojis, and mask_position.

user_id (int) – User identifier of created sticker set owner.

name (str) – Sticker set name.

sticker (telegram.InputSticker) – An object with information about the added sticker. If exactly the same sticker had already been added to the set, then the set isn’t changed. Added in version 20.2.

An object with information about the added sticker. If exactly the same sticker had already been added to the set, then the set isn’t changed.

Added in version 20.2.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. By default, 20 seconds are used as write timeout. Changed in version 22.0: The default value changed to DEFAULT_NONE.

Value to pass to telegram.request.BaseRequest.post.write_timeout. By default, 20 seconds are used as write timeout.

Changed in version 22.0: The default value changed to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Alias for answer_callback_query()

Alias for answer_inline_query()

Alias for answer_pre_checkout_query()

Alias for answer_shipping_query()

Alias for answer_web_app_query()

Use this method to send answers to callback queries sent from inline keyboards. The answer will be displayed to the user as a notification at the top of the chat screen or as an alert. Alternatively, the user can be redirected to the specified Game URL. For this option to work, you must first create a game for your bot via @BotFather and accept the terms. Otherwise, you may use links like t.me/your_bot?start=XXXX that open your bot with a parameter.

telegram.CallbackQuery.answer()

callback_query_id (str) – Unique identifier for the query to be answered.

text (str, optional) – Text of the notification. If not specified, nothing will be shown to the user, 0-200 characters.

show_alert (bool, optional) – If True, an alert will be shown by the client instead of a notification at the top of the chat screen. Defaults to False.

url (str, optional) – URL that will be opened by the user’s client. If you have created a Game and accepted the conditions via @BotFather, specify the URL that opens your game - note that this will only work if the query comes from a callback game button. Otherwise, you may use links like t.me/your_bot?start=XXXX that open your bot with a parameter.

URL that will be opened by the user’s client. If you have created a Game and accepted the conditions via @BotFather, specify the URL that opens your game - note that this will only work if the query comes from a callback game button. Otherwise, you may use links like t.me/your_bot?start=XXXX that open your bot with a parameter.

cache_time (int | datetime.timedelta, optional) – The maximum amount of time in seconds that the result of the callback query may be cached client-side. Defaults to 0. Changed in version 21.11: datetime.timedelta objects are accepted in addition to plain int values.

The maximum amount of time in seconds that the result of the callback query may be cached client-side. Defaults to 0.

Changed in version 21.11: datetime.timedelta objects are accepted in addition to plain int values.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

bool On success, True is returned.

telegram.error.TelegramError –

Use this method to send answers to an inline query. No more than 50 results per query are allowed.

In most use cases current_offset should not be passed manually. Instead of calling this method directly, use the shortcut telegram.InlineQuery.answer() with telegram.InlineQuery.answer.auto_pagination set to True, which will take care of passing the correct value.

Working with Files and Media

telegram.InlineQuery.answer()

Changed in version 20.5: Removed deprecated arguments switch_pm_text and switch_pm_parameter.

inline_query_id (str) – Unique identifier for the answered query.

results (list[telegram.InlineQueryResult] | Callable) – A list of results for the inline query. In case current_offset is passed, results may also be a callable that accepts the current page index starting from 0. It must return either a list of telegram.InlineQueryResult instances or None if there are no more results.

cache_time (int | datetime.timedelta, optional) – The maximum amount of time in seconds that the result of the inline query may be cached on the server. Defaults to 300. Changed in version 21.11: datetime.timedelta objects are accepted in addition to plain int values.

The maximum amount of time in seconds that the result of the inline query may be cached on the server. Defaults to 300.

Changed in version 21.11: datetime.timedelta objects are accepted in addition to plain int values.

is_personal (bool, optional) – Pass True, if results may be cached on the server side only for the user that sent the query. By default, results may be returned to any user who sends the same query.

next_offset (str, optional) – Pass the offset that a client should send in the next query with the same text to receive more results. Pass an empty string if there are no more results or if you don’t support pagination. Offset length can’t exceed 64 bytes.

button (telegram.InlineQueryResultsButton, optional) – A button to be shown above the inline query results. Added in version 20.3.

A button to be shown above the inline query results.

Added in version 20.3.

current_offset (str, optional) – The telegram.InlineQuery.offset of the inline query to answer. If passed, PTB will automatically take care of the pagination for you, i.e. pass the correct next_offset and truncate the results list/get the results from the callable you passed.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Once the user has confirmed their payment and shipping details, the Bot API sends the final confirmation in the form of an telegram.Update with the field telegram.Update.pre_checkout_query. Use this method to respond to such pre-checkout queries.

The Bot API must receive an answer within 10 seconds after the pre-checkout query was sent.

telegram.PreCheckoutQuery.answer()

pre_checkout_query_id (str) – Unique identifier for the query to be answered.

ok (bool) – Specify True if everything is alright (goods are available, etc.) and the bot is ready to proceed with the order. Use False if there are any problems.

error_message (str, optional) – Required if ok is False. Error message in human readable form that explains the reason for failure to proceed with the checkout (e.g. “Sorry, somebody just bought the last of our amazing black T-shirts while you were busy filling out your payment details. Please choose a different color or garment!”). Telegram will display this message to the user.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned

telegram.error.TelegramError –

If you sent an invoice requesting a shipping address and the parameter send_invoice.is_flexible was specified, the Bot API will send an telegram.Update with a telegram.Update.shipping_query field to the bot. Use this method to reply to shipping queries.

telegram.ShippingQuery.answer()

shipping_query_id (str) – Unique identifier for the query to be answered.

ok (bool) – Specify True if delivery to the specified address is possible and False if there are any problems (for example, if delivery to the specified address is not possible).

shipping_options (Sequence[telegram.ShippingOption]), optional) – Required if ok is True. A sequence of available shipping options. Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list.

Required if ok is True. A sequence of available shipping options.

Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list.

error_message (str, optional) – Required if ok is False. Error message in human readable form that explains why it is impossible to complete the order (e.g. “Sorry, delivery to your desired address is unavailable”). Telegram will display this message to the user.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Use this method to set the result of an interaction with a Web App and send a corresponding message on behalf of the user to the chat from which the query originated.

Added in version 20.0.

web_app_query_id (str) – Unique identifier for the query to be answered.

result (telegram.InlineQueryResult) – An object describing the message to be sent.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, a sent telegram.SentWebAppMessage is returned.

telegram.SentWebAppMessage

telegram.error.TelegramError –

Alias for approve_chat_join_request()

Alias for approve_suggested_post()

Use this method to approve a chat join request.

The bot must be an administrator in the chat for this to work and must have the telegram.ChatPermissions.can_invite_users administrator right.

telegram.Chat.approve_join_request()

telegram.ChatFullInfo.approve_join_request()

telegram.ChatJoinRequest.approve()

telegram.User.approve_join_request()

Added in version 13.8.

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername).

user_id (int) – Unique identifier of the target user.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Use this method to approve a suggested post in a direct messages chat. The bot must have the can_post_messages administrator right in the corresponding channel chat.

telegram.Chat.approve_suggested_post()

telegram.ChatFullInfo.approve_suggested_post()

telegram.Message.approve_suggested_post()

Added in version 22.4.

chat_id (int) – Unique identifier of the target direct messages chat.

message_id (int) – Identifier of a suggested post message to approve.

send_date (int | datetime.datetime, optional) – Date when the post is expected to be published; omit if the date has already been specified when the suggested post was created. If specified, then the date must be not more than 2678400 seconds (30 days) in the future. For timezone naive datetime.datetime objects, the default timezone of the bot will be used, which is UTC unless telegram.ext.Defaults.tzinfo is used.

Date when the post is expected to be published; omit if the date has already been specified when the suggested post was created. If specified, then the date must be not more than 2678400 seconds (30 days) in the future.

For timezone naive datetime.datetime objects, the default timezone of the bot will be used, which is UTC unless telegram.ext.Defaults.tzinfo is used.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Alias for ban_chat_member()

Alias for ban_chat_sender_chat()

Use this method to ban a user from a group, supergroup or a channel. In the case of supergroups and channels, the user will not be able to return to the group on their own using invite links, etc., unless unbanned first. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights.

telegram.Chat.ban_member()

telegram.ChatFullInfo.ban_member()

Added in version 13.7.

chat_id (int | str) – Unique identifier for the target group or username of the target supergroup or channel (in the format @channelusername).

user_id (int) – Unique identifier of the target user.

until_date (int | datetime.datetime, optional) – Date when the user will be unbanned, unix time. If user is banned for more than 366 days or less than 30 seconds from the current time they are considered to be banned forever. Applied for supergroups and channels only. For timezone naive datetime.datetime objects, the default timezone of the bot will be used, which is UTC unless telegram.ext.Defaults.tzinfo is used.

revoke_messages (bool, optional) – Pass True to delete all messages from the chat for the user that is being removed. If False, the user will be able to see messages in the group that were sent before the user was removed. Always True for supergroups and channels. Added in version 13.4.

Pass True to delete all messages from the chat for the user that is being removed. If False, the user will be able to see messages in the group that were sent before the user was removed. Always True for supergroups and channels.

Added in version 13.4.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Use this method to ban a channel chat in a supergroup or a channel. Until the chat is unbanned, the owner of the banned chat won’t be able to send messages on behalf of any of their channels. The bot must be an administrator in the supergroup or channel for this to work and must have the appropriate administrator rights.

telegram.Chat.ban_chat()

telegram.Chat.ban_sender_chat()

telegram.ChatFullInfo.ban_chat()

telegram.ChatFullInfo.ban_sender_chat()

Added in version 13.9.

chat_id (int | str) – Unique identifier for the target group or username of the target supergroup or channel (in the format @channelusername).

sender_chat_id (int) – Unique identifier of the target sender chat.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Telegram Bot API file URL, built from Bot.base_file_url and Bot.token.

Added in version 20.0.

Telegram Bot API service URL, built from Bot.base_url and Bot.token.

Added in version 20.0.

User instance for the bot as returned by get_me().

This value is the cached return value of get_me(). If the bots profile is changed during runtime, this value won’t reflect the changes until get_me() is called again.

Bot’s telegram.User.can_join_groups attribute. Shortcut for the corresponding attribute of bot.

Bot’s telegram.User.can_read_all_group_messages attribute. Shortcut for the corresponding attribute of bot.

Use this method to close the bot instance before moving it from one local server to another. You need to delete the webhook before calling this method to ensure that the bot isn’t launched again after server restart. The method will return error 429 in the first 10 minutes after the bot is launched.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Alias for close_forum_topic()

Alias for close_general_forum_topic()

Use this method to close an open topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have can_manage_topics administrator rights, unless it is the creator of the topic.

telegram.Chat.close_forum_topic()

telegram.ChatFullInfo.close_forum_topic()

telegram.Message.close_forum_topic()

Added in version 20.0.

chat_id (int | str) – Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername).

message_thread_id (int) – Unique identifier for the target message thread of the forum topic.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Use this method to close an open ‘General’ topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have can_manage_topics administrator rights.

telegram.Chat.close_general_forum_topic()

telegram.ChatFullInfo.close_general_forum_topic()

Added in version 20.0.

chat_id (int | str) – Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername).

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Alias for convert_gift_to_stars()

Converts a given regular gift to Telegram Stars. Requires the can_convert_gifts_to_stars business bot right.

Added in version 22.1.

business_connection_id (str) – Unique identifier of the business connection

owned_gift_id (str) – Unique identifier of the regular gift that should be converted to Telegram Stars.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Alias for copy_message()

Alias for copy_messages()

Use this method to copy messages of any kind. Service messages, paid media messages, giveaway messages, giveaway winners messages, and invoice messages can’t be copied. The method is analogous to the method forward_message(), but the copied message doesn’t have a link to the original message.

telegram.Chat.copy_message()

telegram.Chat.send_copy()

telegram.ChatFullInfo.copy_message()

telegram.ChatFullInfo.send_copy()

telegram.Message.copy()

telegram.Message.reply_copy()

telegram.User.copy_message()

telegram.User.send_copy()

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername).

from_chat_id (int | str) – Unique identifier for the chat where the original message was sent (or channel username in the format @channelusername).

message_id (int) – Message identifier in the chat specified in from_chat_id.

video_start_timestamp (int, optional) – New start timestamp for the copied video in the message Added in version 21.11.

New start timestamp for the copied video in the message

Added in version 21.11.

caption (str, optional) – New caption for media, 0-1024 characters after entities parsing. If not specified, the original caption is kept.

parse_mode (str, optional) – Mode for parsing entities in the new caption. See the constants in telegram.constants.ParseMode for the available modes.

caption_entities (Sequence[telegram.MessageEntity], optional) – Sequence of special entities that appear in the caption, which can be specified instead of parse_mode. Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list.

Sequence of special entities that appear in the caption, which can be specified instead of parse_mode.

Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list.

disable_notification (bool, optional) – Sends the message silently. Users will receive a notification with no sound.

protect_content (bool, optional) – Protects the contents of the sent message from forwarding and saving. Added in version 13.10.

Protects the contents of the sent message from forwarding and saving.

Added in version 13.10.

message_thread_id (int, optional) – Unique identifier for the target message thread (topic) of the forum; for forum supergroups only. Added in version 20.0.

Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.

Added in version 20.0.

reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply, optional) – Additional interface options. An object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.

reply_parameters (telegram.ReplyParameters, optional) – Description of the message to reply to. Added in version 20.8.

Description of the message to reply to.

Added in version 20.8.

show_caption_above_media (bool, optional) – Pass True, if the caption must be shown above the message media. Added in version 21.3.

Pass True, if the caption must be shown above the message media.

Added in version 21.3.

allow_paid_broadcast (bool, optional) – Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance. Added in version 21.7.

Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance.

Added in version 21.7.

suggested_post_parameters (telegram.SuggestedPostParameters, optional) – An object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined. Added in version 22.4.

An object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined.

Added in version 22.4.

direct_messages_topic_id (int, optional) – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat. Added in version 22.4.

Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat.

Added in version 22.4.

allow_sending_without_reply (bool, optional) – Pass True, if the message should be sent even if the specified replied-to message is not found. Mutually exclusive with reply_parameters, which this is a convenience parameter for Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument. Changed in version 21.0: This argument is now a keyword-only argument.

Pass True, if the message should be sent even if the specified replied-to message is not found. Mutually exclusive with reply_parameters, which this is a convenience parameter for

Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument.

Changed in version 21.0: This argument is now a keyword-only argument.

reply_to_message_id (int, optional) – If the message is a reply, ID of the original message. Mutually exclusive with reply_parameters, which this is a convenience parameter for Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument. Changed in version 21.0: This argument is now a keyword-only argument.

If the message is a reply, ID of the original message. Mutually exclusive with reply_parameters, which this is a convenience parameter for

Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument.

Changed in version 21.0: This argument is now a keyword-only argument.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, the telegram.MessageId of the sentmessage is returned.

telegram.error.TelegramError –

Use this method to copy messages of any kind. If some of the specified messages can’t be found or copied, they are skipped. Service messages, paid media messages, giveaway messages, giveaway winners messages, and invoice messages can’t be copied. A quiz poll can be copied only if the value of the field telegram.Poll.correct_option_id is known to the bot. The method is analogous to the method forward_messages(), but the copied messages don’t have a link to the original message. Album grouping is kept for copied messages.

telegram.Chat.copy_messages()

telegram.Chat.send_copies()

telegram.ChatFullInfo.copy_messages()

telegram.ChatFullInfo.send_copies()

telegram.User.copy_messages()

telegram.User.send_copies()

Added in version 20.8.

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername).

from_chat_id (int | str) – Unique identifier for the chat where the original message was sent (or channel username in the format @channelusername).

message_ids (Sequence[int]) – A list of 1 - 100 identifiers of messages in the chat from_chat_id to copy. The identifiers must be specified in a strictly increasing order.

disable_notification (bool, optional) – Sends the message silently. Users will receive a notification with no sound.

protect_content (bool, optional) – Protects the contents of the sent message from forwarding and saving.

message_thread_id (int, optional) – Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.

remove_caption (bool, optional) – Pass True to copy the messages without their captions.

direct_messages_topic_id (int, optional) – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat. Added in version 22.4.

Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat.

Added in version 22.4.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, a tuple of MessageId of the sent messages is returned.

tuple[telegram.MessageId]

telegram.error.TelegramError –

Alias for create_chat_invite_link()

Alias for create_chat_subscription_invite_link()

Alias for create_forum_topic()

Alias for create_invoice_link()

Alias for create_new_sticker_set()

Use this method to create an additional invite link for a chat. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights. The link can be revoked using the method revoke_chat_invite_link().

When joining public groups via an invite link, Telegram clients may display the usual “Join” button, effectively ignoring the invite link. In particular, the parameter creates_join_request has no effect in this case. However, this behavior is undocument and may be subject to change. See this GitHub thread for some discussion.

telegram.Chat.create_invite_link()

telegram.ChatFullInfo.create_invite_link()

Added in version 13.4.

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername).

expire_date (int | datetime.datetime, optional) – Date when the link will expire. Integer input will be interpreted as Unix timestamp. For timezone naive datetime.datetime objects, the default timezone of the bot will be used, which is UTC unless telegram.ext.Defaults.tzinfo is used.

member_limit (int, optional) – Maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1- 99999.

name (str, optional) – Invite link name; 0-32 characters. Added in version 13.8.

Invite link name; 0-32 characters.

Added in version 13.8.

creates_join_request (bool, optional) – True, if users joining the chat via the link need to be approved by chat administrators. If True, member_limit can’t be specified. Added in version 13.8.

True, if users joining the chat via the link need to be approved by chat administrators. If True, member_limit can’t be specified.

Added in version 13.8.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

telegram.ChatInviteLink

telegram.error.TelegramError –

Use this method to create a subscription invite link for a channel chat. The bot must have the can_invite_users administrator right. The link can be edited using the edit_chat_subscription_invite_link() or revoked using the revoke_chat_invite_link().

telegram.Chat.create_subscription_invite_link()

telegram.ChatFullInfo.create_subscription_invite_link()

Added in version 21.5.

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername).

subscription_period (int | datetime.timedelta) – The number of seconds the subscription will be active for before the next payment. Currently, it must always be 2592000 (30 days). Changed in version 21.11: datetime.timedelta objects are accepted in addition to plain int values.

The number of seconds the subscription will be active for before the next payment. Currently, it must always be 2592000 (30 days).

Changed in version 21.11: datetime.timedelta objects are accepted in addition to plain int values.

subscription_price (int) – The number of Telegram Stars a user must pay initially and after each subsequent subscription period to be a member of the chat; 1- 10000.

name (str, optional) – Invite link name; 0-32 characters.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

telegram.ChatInviteLink

telegram.error.TelegramError –

Use this method to create a topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have can_manage_topics administrator rights.

telegram.Chat.create_forum_topic()

telegram.ChatFullInfo.create_forum_topic()

Added in version 20.0.

chat_id (int | str) – Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername).

name (str) – New topic name, 1- 128 characters.

icon_color (int, optional) – Color of the topic icon in RGB format. Currently, must be one of telegram.constants.ForumIconColor.BLUE, telegram.constants.ForumIconColor.YELLOW, telegram.constants.ForumIconColor.PURPLE, telegram.constants.ForumIconColor.GREEN, telegram.constants.ForumIconColor.PINK, or telegram.constants.ForumIconColor.RED.

icon_custom_emoji_id (str, optional) – New unique identifier of the custom emoji shown as the topic icon. Use get_forum_topic_icon_stickers() to get all allowed custom emoji identifiers.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

telegram.error.TelegramError –

Use this method to create a link for an invoice.

Added in version 20.0.

business_connection_id (str, optional) – Unique identifier of the business connection on behalf of which the message will be sent. For payments in Telegram Stars only. Added in version 21.8.

Unique identifier of the business connection on behalf of which the message will be sent. For payments in Telegram Stars only.

Added in version 21.8.

title (str) – Product name. 1- 32 characters.

description (str) – Product description. 1- 255 characters.

payload (str) – Bot-defined invoice payload. 1- 128 bytes. This will not be displayed to the user, use it for your internal processes.

provider_token (str, optional) – Payments provider token, obtained via @BotFather. Pass an empty string for payments in Telegram Stars. Changed in version 21.11: Bot API 7.4 made this parameter is optional and this is now reflected in the function signature.

Payments provider token, obtained via @BotFather. Pass an empty string for payments in Telegram Stars.

Changed in version 21.11: Bot API 7.4 made this parameter is optional and this is now reflected in the function signature.

currency (str) – Three-letter ISO 4217 currency code, see more on currencies. Pass XTR for payments in Telegram Stars.

prices (Sequence[telegram.LabeledPrice) – Price breakdown, a sequence of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.). Must contain exactly one item for payments in Telegram Stars. Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list.

Price breakdown, a sequence of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.). Must contain exactly one item for payments in Telegram Stars.

Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list.

subscription_period (int | datetime.timedelta, optional) – The time the subscription will be active for before the next payment, either as number of seconds or as datetime.timedelta object. The currency must be set to “XTR” (Telegram Stars) if the parameter is used. Currently, it must always be 2592000 if specified. Any number of subscriptions can be active for a given bot at the same time, including multiple concurrent subscriptions from the same user. Subscription price must not exceed 10000 Telegram Stars. Added in version 21.8.

The time the subscription will be active for before the next payment, either as number of seconds or as datetime.timedelta object. The currency must be set to “XTR” (Telegram Stars) if the parameter is used. Currently, it must always be 2592000 if specified. Any number of subscriptions can be active for a given bot at the same time, including multiple concurrent subscriptions from the same user. Subscription price must not exceed 10000 Telegram Stars.

Added in version 21.8.

max_tip_amount (int, optional) – The maximum accepted amount for tips in the smallest units of the currency (integer, not float/double). For example, for a maximum tip of US$ 1.45 pass max_tip_amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). Defaults to 0. Not supported for payments in Telegram Stars.

suggested_tip_amounts (Sequence[int], optional) – An array of suggested amounts of tips in the smallest units of the currency (integer, not float/double). At most 4 suggested tip amounts can be specified. The suggested tip amounts must be positive, passed in a strictly increased order and must not exceed max_tip_amount. Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list.

An array of suggested amounts of tips in the smallest units of the currency (integer, not float/double). At most 4 suggested tip amounts can be specified. The suggested tip amounts must be positive, passed in a strictly increased order and must not exceed max_tip_amount.

Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list.

provider_data (str | object, optional) – Data about the invoice, which will be shared with the payment provider. A detailed description of required fields should be provided by the payment provider. When an object is passed, it will be encoded as JSON.

photo_url (str, optional) – URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service.

photo_size (int, optional) – Photo size in bytes.

photo_width (int, optional) – Photo width.

photo_height (int, optional) – Photo height.

need_name (bool, optional) – Pass True, if you require the user’s full name to complete the order. Ignored for payments in Telegram Stars.

need_phone_number (bool, optional) – Pass True, if you require the user’s phone number to complete the order. Ignored for payments in Telegram Stars.

need_email (bool, optional) – Pass True, if you require the user’s email address to complete the order. Ignored for payments in Telegram Stars.

need_shipping_address (bool, optional) – Pass True, if you require the user’s shipping address to complete the order. Ignored for payments in Telegram Stars.

send_phone_number_to_provider (bool, optional) – Pass True, if user’s phone number should be sent to provider. Ignored for payments in Telegram Stars.

send_email_to_provider (bool, optional) – Pass True, if user’s email address should be sent to provider. Ignored for payments in Telegram Stars.

is_flexible (bool, optional) – Pass True, if the final price depends on the shipping method. Ignored for payments in Telegram Stars.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, the created invoice link is returned.

Use this method to create new sticker set owned by a user. The bot will be able to edit the created sticker set thus created.

Changed in version 20.0: The parameter contains_masks has been removed. Use sticker_type instead.

Changed in version 20.2: Since Bot API 6.6, the parameters stickers and sticker_format replace the parameters png_sticker, tgs_sticker,``webm_sticker``, emojis, and mask_position.

Changed in version 20.5: Removed the deprecated parameters mentioned above and adjusted the order of the parameters.

Removed in version 21.2: Removed the deprecated parameter sticker_format.

user_id (int) – User identifier of created sticker set owner.

name (str) – Short name of sticker set, to be used in t.me/addstickers/ URLs (e.g., animals). Can contain only english letters, digits and underscores. Must begin with a letter, can’t contain consecutive underscores and must end in “_by_<bot username>”. <bot_username> is case insensitive. 1- 64 characters.

title (str) – Sticker set title, 1- 64 characters.

stickers (Sequence[telegram.InputSticker]) – A sequence of 1- 50 initial stickers to be added to the sticker set. Added in version 20.2.

A sequence of 1- 50 initial stickers to be added to the sticker set.

Added in version 20.2.

sticker_type (str, optional) – Type of stickers in the set, pass telegram.Sticker.REGULAR or telegram.Sticker.MASK, or telegram.Sticker.CUSTOM_EMOJI. By default, a regular sticker set is created Added in version 20.0.

Type of stickers in the set, pass telegram.Sticker.REGULAR or telegram.Sticker.MASK, or telegram.Sticker.CUSTOM_EMOJI. By default, a regular sticker set is created

Added in version 20.0.

needs_repainting (bool, optional) – Pass True if stickers in the sticker set must be repainted to the color of text when used in messages, the accent color if used as emoji status, white on chat photos, or another appropriate color based on context; for custom emoji sticker sets only. Added in version 20.2.

Pass True if stickers in the sticker set must be repainted to the color of text when used in messages, the accent color if used as emoji status, white on chat photos, or another appropriate color based on context; for custom emoji sticker sets only.

Added in version 20.2.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. By default, 20 seconds are used as write timeout. Changed in version 22.0: The default value changed to DEFAULT_NONE.

Value to pass to telegram.request.BaseRequest.post.write_timeout. By default, 20 seconds are used as write timeout.

Changed in version 22.0: The default value changed to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Alias for decline_chat_join_request()

Alias for decline_suggested_post()

Use this method to decline a chat join request.

The bot must be an administrator in the chat for this to work and must have the telegram.ChatPermissions.can_invite_users administrator right.

telegram.Chat.decline_join_request()

telegram.ChatFullInfo.decline_join_request()

telegram.ChatJoinRequest.decline()

telegram.User.decline_join_request()

Added in version 13.8.

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername).

user_id (int) – Unique identifier of the target user.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Use this method to decline a suggested post in a direct messages chat. The bot must have the can_manage_direct_messages administrator right in the corresponding channel chat.

telegram.Chat.decline_suggested_post()

telegram.ChatFullInfo.decline_suggested_post()

telegram.Message.decline_suggested_post()

Added in version 22.4.

chat_id (int) – Unique identifier of the target direct messages chat.

message_id (int) – Identifier of a suggested post message to decline.

comment (str, optional) – Comment for the creator of the suggested post. 0-128 characters.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Alias for delete_business_messages()

Alias for delete_chat_photo()

Alias for delete_chat_sticker_set()

Alias for delete_forum_topic()

Alias for delete_message()

Alias for delete_messages()

Alias for delete_my_commands()

Alias for delete_sticker_from_set()

Alias for delete_sticker_set()

Alias for delete_story()

Alias for delete_webhook()

Delete messages on behalf of a business account. Requires the can_delete_sent_messages business bot right to delete messages sent by the bot itself, or the can_delete_all_messages business bot right to delete any message.

telegram.Message.delete()

Added in version 22.1.

business_connection_id (int | str) – Unique identifier of the business connection on behalf of which to delete the messages

message_ids (Sequence[int]) – A list of 1- 100 identifiers of messages to delete. See delete_message() for limitations on which messages can be deleted.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Use this method to delete a chat photo. Photos can’t be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights.

telegram.Chat.delete_photo()

telegram.ChatFullInfo.delete_photo()

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername).

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Use this method to delete a group sticker set from a supergroup. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights. Use the field telegram.ChatFullInfo.can_set_sticker_set optionally returned in get_chat() requests to check if the bot can use this method.

chat_id (int | str) – Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername).

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

Use this method to delete a forum topic along with all its messages in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have can_delete_messages administrator rights.

telegram.Chat.delete_forum_topic()

telegram.ChatFullInfo.delete_forum_topic()

telegram.Message.delete_forum_topic()

Added in version 20.0.

chat_id (int | str) – Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername).

message_thread_id (int) – Unique identifier for the target message thread of the forum topic.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Use this method to delete a message, including service messages, with the following limitations:

A message can only be deleted if it was sent less than 48 hours ago.

Service messages about a supergroup, channel, or forum topic creation can’t be deleted.

A dice message in a private chat can only be deleted if it was sent more than 24 hours ago.

Bots can delete outgoing messages in private chats, groups, and supergroups.

Bots can delete incoming messages in private chats.

Bots granted can_post_messages permissions can delete outgoing messages in channels.

If the bot is an administrator of a group, it can delete any message there.

If the bot has can_delete_messages permission in a supergroup or a channel, it can delete any message there.

telegram.CallbackQuery.delete_message() (calls delete_message() indirectly, via telegram.Message.delete())

telegram.Chat.delete_message()

telegram.ChatFullInfo.delete_message()

telegram.Message.delete()

telegram.User.delete_message()

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername).

message_id (int) – Identifier of the message to delete.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Use this method to delete multiple messages simultaneously. If some of the specified messages can’t be found, they are skipped.

telegram.Chat.delete_messages()

telegram.ChatFullInfo.delete_messages()

telegram.User.delete_messages()

Added in version 20.8.

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername).

message_ids (Sequence[int]) – A list of 1- 100 identifiers of messages to delete. See delete_message() for limitations on which messages can be deleted.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Use this method to delete the list of the bot’s commands for the given scope and user language. After deletion, higher level commands will be shown to affected users.

Added in version 13.7.

get_my_commands(), set_my_commands()

scope (telegram.BotCommandScope, optional) – An object, describing scope of users for which the commands are relevant. Defaults to telegram.BotCommandScopeDefault.

language_code (str, optional) – A two-letter ISO 639-1 language code. If empty, commands will be applied to all users from the given scope, for whose language there are no dedicated commands.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Use this method to delete a sticker from a set created by the bot.

sticker (str | telegram.Sticker) – File identifier of the sticker or the sticker object. Changed in version 21.10: Accepts also telegram.Sticker instances.

File identifier of the sticker or the sticker object.

Changed in version 21.10: Accepts also telegram.Sticker instances.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Use this method to delete a sticker set that was created by the bot.

Added in version 20.2.

name (str) – Sticker set name.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Deletes a story previously posted by the bot on behalf of a managed business account. Requires the can_manage_stories business bot right.

Added in version 22.1.

business_connection_id (str) – Unique identifier of the business connection.

story_id (int) – Unique identifier of the story to delete.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Use this method to remove webhook integration if you decide to switch back to get_updates().

drop_pending_updates (bool, optional) – Pass True to drop all pending updates.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Do a request to the Telegram API.

This method is here to make it easier to use new API methods that are not yet supported by this library.

Since PTB does not know which arguments are passed to this method, some caution is necessary in terms of PTBs utility functionalities. In particular

passing objects of any class defined in the telegram module is supported

when uploading files, a telegram.InputFile must be passed as the value for the corresponding argument. Passing a file path or file-like object will not work. File paths will work only in combination with local_mode.

when uploading files, PTB can still correctly determine that a special write timeout value should be used instead of the default telegram.request.HTTPXRequest.write_timeout.

insertion of default values specified via telegram.ext.Defaults will not work (only relevant for telegram.ext.ExtBot).

The only exception is telegram.ext.Defaults.tzinfo, which will be correctly applied to datetime.datetime objects.

Added in version 20.8.

endpoint (str) – The API endpoint to use, e.g. getMe or get_me.

api_kwargs (dict, optional) – The keyword arguments to pass to the API call. If not specified, no arguments are passed.

return_type (telegram.TelegramObject, optional) – If specified, the result of the API call will be deserialized into an instance of this class or tuple of instances of this class. If not specified, the raw result of the API call will be returned.

The result of the API call. If return_type is not specified, this is a dict or bool, otherwise an instance of return_type or a tuple of return_type.

telegram.error.TelegramError –

Alias for edit_chat_invite_link()

Alias for edit_chat_subscription_invite_link()

Alias for edit_forum_topic()

Alias for edit_general_forum_topic()

Alias for edit_message_caption()

Alias for edit_message_checklist()

Alias for edit_message_live_location()

Alias for edit_message_media()

Alias for edit_message_reply_markup()

Alias for edit_message_text()

Alias for edit_story()

Alias for edit_user_star_subscription()

Use this method to edit a non-primary invite link created by the bot. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights.

Though not stated explicitly in the official docs, Telegram changes not only the optional parameters that are explicitly passed, but also replaces all other optional parameters to the default values. However, since not documented, this behaviour may change unbeknown to PTB.

telegram.Chat.edit_invite_link()

telegram.ChatFullInfo.edit_invite_link()

Added in version 13.4.

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername).

invite_link (str | telegram.ChatInviteLink) – The invite link to edit. Changed in version 20.0: Now also accepts telegram.ChatInviteLink instances.

The invite link to edit.

Changed in version 20.0: Now also accepts telegram.ChatInviteLink instances.

expire_date (int | datetime.datetime, optional) – Date when the link will expire. For timezone naive datetime.datetime objects, the default timezone of the bot will be used, which is UTC unless telegram.ext.Defaults.tzinfo is used.

member_limit (int, optional) – Maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1- 99999.

name (str, optional) – Invite link name; 0-32 characters. Added in version 13.8.

Invite link name; 0-32 characters.

Added in version 13.8.

creates_join_request (bool, optional) – True, if users joining the chat via the link need to be approved by chat administrators. If True, member_limit can’t be specified. Added in version 13.8.

True, if users joining the chat via the link need to be approved by chat administrators. If True, member_limit can’t be specified.

Added in version 13.8.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

telegram.ChatInviteLink

telegram.error.TelegramError –

Use this method to edit a subscription invite link created by the bot. The bot must have telegram.ChatPermissions.can_invite_users administrator right.

telegram.Chat.edit_subscription_invite_link()

telegram.ChatFullInfo.edit_subscription_invite_link()

Added in version 21.5.

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername).

invite_link (str | telegram.ChatInviteLink) – The invite link to edit.

name (str, optional) – Invite link name; 0-32 characters. Tip Omitting this argument removes the name of the invite link.

Invite link name; 0-32 characters.

Omitting this argument removes the name of the invite link.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

telegram.ChatInviteLink

telegram.error.TelegramError –

Use this method to edit name and icon of a topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the can_manage_topics administrator rights, unless it is the creator of the topic.

telegram.Chat.edit_forum_topic()

telegram.ChatFullInfo.edit_forum_topic()

telegram.Message.edit_forum_topic()

Added in version 20.0.

chat_id (int | str) – Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername).

message_thread_id (int) – Unique identifier for the target message thread of the forum topic.

name (str, optional) – New topic name, 1- 128 characters. If not specified or empty, the current name of the topic will be kept.

icon_custom_emoji_id (str, optional) – New unique identifier of the custom emoji shown as the topic icon. Use get_forum_topic_icon_stickers() to get all allowed custom emoji identifiers.Pass an empty string to remove the icon. If not specified, the current icon will be kept.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Use this method to edit the name of the ‘General’ topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have the can_manage_topics administrator rights.

telegram.Chat.edit_general_forum_topic()

telegram.ChatFullInfo.edit_general_forum_topic()

Added in version 20.0.

chat_id (int | str) – Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername).

name (str) – New topic name, 1- 128 characters.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Use this method to edit captions of messages.

It is currently only possible to edit messages without telegram.Message.reply_markup or with inline keyboards.

Note that business messages that were not sent by the bot and do not contain an inline keyboard can only be edited within 48 hours from the time they were sent.

telegram.CallbackQuery.edit_message_caption()

telegram.Message.edit_caption()

chat_id (int | str, optional) – Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername).

message_id (int, optional) – Required if inline_message_id is not specified. Identifier of the message to edit.

inline_message_id (str, optional) – Required if chat_id and message_id are not specified. Identifier of the inline message.

caption (str, optional) – New caption of the message, 0-1024 characters after entities parsing.

parse_mode (str, optional) – Mode for parsing entities. See telegram.constants.ParseMode and formatting options for more details.

caption_entities (Sequence[telegram.MessageEntity], optional) – Sequence of special entities that appear in the caption, which can be specified instead of parse_mode. Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list.

Sequence of special entities that appear in the caption, which can be specified instead of parse_mode.

Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list.

reply_markup (telegram.InlineKeyboardMarkup, optional) – An object for an inline keyboard.

show_caption_above_media (bool, optional) – Pass True, if the caption must be shown above the message media. Added in version 21.3.

Pass True, if the caption must be shown above the message media.

Added in version 21.3.

business_connection_id (str, optional) – Unique identifier of the business connection on behalf of which the message to be edited was sent Added in version 21.4.

Unique identifier of the business connection on behalf of which the message to be edited was sent

Added in version 21.4.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, if edited message is not an inline message, the edited message is returned, otherwise True is returned.

telegram.error.TelegramError –

Use this method to edit a checklist on behalf of a connected business account.

telegram.Message.edit_checklist()

Added in version 22.3.

business_connection_id (str) – Unique identifier of the business connection on behalf of which the message will be sent.

chat_id (int) – Unique identifier for the target chat.

message_id (int) – Unique identifier for the target message.

checklist (telegram.InputChecklist) – The new checklist.

reply_markup (telegram.InlineKeyboardMarkup, optional) – An object for the new inline keyboard for the message.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, the sent Message is returned.

telegram.error.TelegramError –

Use this method to edit live location messages sent by the bot or via the bot (for inline bots). A location can be edited until its telegram.Location.live_period expires or editing is explicitly disabled by a call to stop_message_live_location().

You can either supply a latitude and longitude or a location.

telegram.CallbackQuery.edit_message_live_location()

telegram.Message.edit_live_location()

chat_id (int | str, optional) – Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername).

message_id (int, optional) – Required if inline_message_id is not specified. Identifier of the message to edit.

inline_message_id (str, optional) – Required if chat_id and message_id are not specified. Identifier of the inline message.

latitude (float, optional) – Latitude of location.

longitude (float, optional) – Longitude of location.

horizontal_accuracy (float, optional) – The radius of uncertainty for the location, measured in meters; 0-1500.

heading (int, optional) – Direction in which the user is moving, in degrees. Must be between 1 and 360 if specified.

proximity_alert_radius (int, optional) – Maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified.

reply_markup (telegram.InlineKeyboardMarkup, optional) – An object for a new inline keyboard.

live_period (int | datetime.timedelta, optional) – New period in seconds during which the location can be updated, starting from the message send date. If 2147483647 is specified, then the location can be updated forever. Otherwise, the new value must not exceed the current live_period by more than a day, and the live location expiration date must remain within the next 90 days. If not specified, then live_period remains unchanged Added in version 21.2.. Changed in version 21.11: datetime.timedelta objects are accepted in addition to plain int values.

New period in seconds during which the location can be updated, starting from the message send date. If 2147483647 is specified, then the location can be updated forever. Otherwise, the new value must not exceed the current live_period by more than a day, and the live location expiration date must remain within the next 90 days. If not specified, then live_period remains unchanged

Added in version 21.2..

Changed in version 21.11: datetime.timedelta objects are accepted in addition to plain int values.

business_connection_id (str, optional) – Unique identifier of the business connection on behalf of which the message to be edited was sent Added in version 21.4.

Unique identifier of the business connection on behalf of which the message to be edited was sent

Added in version 21.4.

location (telegram.Location, optional) – The location to send.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, if edited message is not an inline message, the edited message is returned, otherwise True is returned.

Use this method to edit animation, audio, document, photo, or video messages, or to add media to text messages. If a message is part of a message album, then it can be edited only to an audio for audio albums, only to a document for document albums and to a photo or a video otherwise. When an inline message is edited, a new file can’t be uploaded; use a previously uploaded file via its file_id or specify a URL.

It is currently only possible to edit messages without telegram.Message.reply_markup or with inline keyboards.

Note that business messages that were not sent by the bot and do not contain an inline keyboard can only be edited within 48 hours from the time they were sent.

Working with Files and Media

telegram.CallbackQuery.edit_message_media()

telegram.Message.edit_media()

media (telegram.InputMedia) – An object for a new media content of the message.

chat_id (int | str, optional) – Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername).

message_id (int, optional) – Required if inline_message_id is not specified. Identifier of the message to edit.

inline_message_id (str, optional) – Required if chat_id and message_id are not specified. Identifier of the inline message.

reply_markup (telegram.InlineKeyboardMarkup, optional) – An object for an inline keyboard.

business_connection_id (str, optional) – Unique identifier of the business connection on behalf of which the message to be edited was sent Added in version 21.4.

Unique identifier of the business connection on behalf of which the message to be edited was sent

Added in version 21.4.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, if edited message is not an inline message, the edited Message is returned, otherwise True is returned.

telegram.error.TelegramError –

Use this method to edit only the reply markup of messages sent by the bot or via the bot (for inline bots).

It is currently only possible to edit messages without telegram.Message.reply_markup or with inline keyboards.

Note that business messages that were not sent by the bot and do not contain an inline keyboard can only be edited within 48 hours from the time they were sent.

telegram.CallbackQuery.edit_message_reply_markup()

telegram.Message.edit_reply_markup()

chat_id (int | str, optional) – Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername).

message_id (int, optional) – Required if inline_message_id is not specified. Identifier of the message to edit.

inline_message_id (str, optional) – Required if chat_id and message_id are not specified. Identifier of the inline message.

reply_markup (telegram.InlineKeyboardMarkup, optional) – An object for an inline keyboard.

business_connection_id (str, optional) – Unique identifier of the business connection on behalf of which the message to be edited was sent Added in version 21.4.

Unique identifier of the business connection on behalf of which the message to be edited was sent

Added in version 21.4.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, if edited message is not an inline message, the edited message is returned, otherwise True is returned.

telegram.error.TelegramError –

Use this method to edit text and game messages.

It is currently only possible to edit messages without telegram.Message.reply_markup or with inline keyboards.

Note that business messages that were not sent by the bot and do not contain an inline keyboard can only be edited within 48 hours from the time they were sent.

telegram.CallbackQuery.edit_message_text()

telegram.Message.edit_text()

chat_id (int | str, optional) – Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername).

message_id (int, optional) – Required if inline_message_id is not specified. Identifier of the message to edit.

inline_message_id (str, optional) – Required if chat_id and message_id are not specified. Identifier of the inline message.

text (str) – New text of the message, 1- 4096 characters after entities parsing.

parse_mode (str, optional) – Mode for parsing entities. See telegram.constants.ParseMode and formatting options for more details.

entities (Sequence[telegram.MessageEntity], optional) – Sequence of special entities that appear in message text, which can be specified instead of parse_mode. Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list.

Sequence of special entities that appear in message text, which can be specified instead of parse_mode.

Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list.

link_preview_options (LinkPreviewOptions, optional) – Link preview generation options for the message. Mutually exclusive with disable_web_page_preview. Added in version 20.8.

Link preview generation options for the message. Mutually exclusive with disable_web_page_preview.

Added in version 20.8.

reply_markup (telegram.InlineKeyboardMarkup, optional) – An object for an inline keyboard.

business_connection_id (str, optional) – Unique identifier of the business connection on behalf of which the message to be edited was sent Added in version 21.4.

Unique identifier of the business connection on behalf of which the message to be edited was sent

Added in version 21.4.

disable_web_page_preview (bool, optional) – Disables link previews for links in this message. Convenience parameter for setting link_preview_options. Mutually exclusive with link_preview_options. Changed in version 20.8: Bot API 7.0 introduced link_preview_options replacing this argument. PTB will automatically convert this argument to that one, but for advanced options, please use link_preview_options directly. Changed in version 21.0: This argument is now a keyword-only argument.

Disables link previews for links in this message. Convenience parameter for setting link_preview_options. Mutually exclusive with link_preview_options.

Changed in version 20.8: Bot API 7.0 introduced link_preview_options replacing this argument. PTB will automatically convert this argument to that one, but for advanced options, please use link_preview_options directly.

Changed in version 21.0: This argument is now a keyword-only argument.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, if edited message is not an inline message, the edited message is returned, otherwise True is returned.

ValueError – If both disable_web_page_preview and link_preview_options are passed.

telegram.error.TelegramError – For other errors.

Edits a story previously posted by the bot on behalf of a managed business account. Requires the can_manage_stories business bot right.

Added in version 22.1.

business_connection_id (str) – Unique identifier of the business connection.

story_id (int) – Unique identifier of the story to edit.

content (telegram.InputStoryContent) – Content of the story.

caption (str, optional) – Caption of the story, 0-'2048' characters after entities parsing.

parse_mode (str, optional) – Mode for parsing entities in the story caption. See the constants in telegram.constants.ParseMode for the available modes.

caption_entities (Sequence[telegram.MessageEntity], optional) – Sequence of special entities that appear in the caption, which can be specified instead of parse_mode.

areas (Sequence[telegram.StoryArea], optional) – Sequence of clickable areas to be shown on the story. Note Each type of clickable area in areas has its own maximum limit: Up to 10 of telegram.StoryAreaTypeLocation. Up to 5 of telegram.StoryAreaTypeSuggestedReaction. Up to 3 of telegram.StoryAreaTypeLink. Up to 3 of telegram.StoryAreaTypeWeather. Up to 1 of telegram.StoryAreaTypeUniqueGift.

Sequence of clickable areas to be shown on the story.

Each type of clickable area in areas has its own maximum limit:

Up to 10 of telegram.StoryAreaTypeLocation.

Up to 5 of telegram.StoryAreaTypeSuggestedReaction.

Up to 3 of telegram.StoryAreaTypeLink.

Up to 3 of telegram.StoryAreaTypeWeather.

Up to 1 of telegram.StoryAreaTypeUniqueGift.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

telegram.error.TelegramError –

Allows the bot to cancel or re-enable extension of a subscription paid in Telegram Stars.

Added in version 21.8.

user_id (int) – Identifier of the user whose subscription will be edited.

telegram_payment_charge_id (str) – Telegram payment identifier for the subscription.

is_canceled (bool) – Pass True to cancel extension of the user subscription; the subscription must be active up to the end of the current subscription period. Pass False to allow the user to re-enable a subscription that was previously canceled by the bot.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Alias for export_chat_invite_link()

Use this method to generate a new primary invite link for a chat; any previously generated link is revoked. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights.

Each administrator in a chat generates their own invite links. Bots can’t use invite links generated by other administrators. If you want your bot to work with invite links, it will need to generate its own link using export_chat_invite_link() or by calling the get_chat() method. If your bot needs to generate a new primary invite link replacing its previous one, use export_chat_invite_link() again.

telegram.Chat.export_invite_link()

telegram.ChatFullInfo.export_invite_link()

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername).

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

New invite link on success.

telegram.error.TelegramError –

Bot’s first name. Shortcut for the corresponding attribute of bot.

Alias for forward_message()

Alias for forward_messages()

Use this method to forward messages of any kind. Service messages can’t be forwarded.

Since the release of Bot API 5.5 it can be impossible to forward messages from some chats. Use the attributes telegram.Message.has_protected_content and telegram.ChatFullInfo.has_protected_content to check this.

As a workaround, it is still possible to use copy_message(). However, this behaviour is undocumented and might be changed by Telegram.

telegram.Chat.forward_from()

telegram.Chat.forward_to()

telegram.ChatFullInfo.forward_from()

telegram.ChatFullInfo.forward_to()

telegram.Message.forward()

telegram.User.forward_from()

telegram.User.forward_to()

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername).

from_chat_id (int | str) – Unique identifier for the chat where the original message was sent (or channel username in the format @channelusername).

message_id (int) – Message identifier in the chat specified in from_chat_id.

video_start_timestamp (int, optional) – New start timestamp for the forwarded video in the message Added in version 21.11.

New start timestamp for the forwarded video in the message

Added in version 21.11.

disable_notification (bool, optional) – Sends the message silently. Users will receive a notification with no sound.

protect_content (bool, optional) – Protects the contents of the sent message from forwarding and saving. Added in version 13.10.

Protects the contents of the sent message from forwarding and saving.

Added in version 13.10.

message_thread_id (int, optional) – Unique identifier for the target message thread (topic) of the forum; for forum supergroups only. Added in version 20.0.

Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.

Added in version 20.0.

suggested_post_parameters (telegram.SuggestedPostParameters, optional) – An object containing the parameters of the suggested post to send; for direct messages chats only. Added in version 22.4.

An object containing the parameters of the suggested post to send; for direct messages chats only.

Added in version 22.4.

direct_messages_topic_id (int, optional) – Identifier of the direct messages topic to which the message will be forwarded; required if the message is forwarded to a direct messages chat. Added in version 22.4.

Identifier of the direct messages topic to which the message will be forwarded; required if the message is forwarded to a direct messages chat.

Added in version 22.4.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, the sent Message is returned.

telegram.error.TelegramError –

Use this method to forward messages of any kind. If some of the specified messages can’t be found or forwarded, they are skipped. Service messages and messages with protected content can’t be forwarded. Album grouping is kept for forwarded messages.

telegram.Chat.forward_messages_from()

telegram.Chat.forward_messages_to()

telegram.ChatFullInfo.forward_messages_from()

telegram.ChatFullInfo.forward_messages_to()

telegram.User.forward_messages_from()

telegram.User.forward_messages_to()

Added in version 20.8.

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername).

from_chat_id (int | str) – Unique identifier for the chat where the original message was sent (or channel username in the format @channelusername).

message_ids (Sequence[int]) – A list of 1- 100 identifiers of messages in the chat from_chat_id to forward. The identifiers must be specified in a strictly increasing order.

disable_notification (bool, optional) – Sends the message silently. Users will receive a notification with no sound.

protect_content (bool, optional) – Protects the contents of the sent message from forwarding and saving.

message_thread_id (int, optional) – Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.

direct_messages_topic_id (int, optional) – Identifier of the direct messages topic to which the messages will be forwarded; required if the messages are forwarded to a direct messages chat. Added in version 22.4.

Identifier of the direct messages topic to which the messages will be forwarded; required if the messages are forwarded to a direct messages chat.

Added in version 22.4.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, a tuple of MessageId of sent messages is returned.

tuple[telegram.Message]

telegram.error.TelegramError –

Alias for get_available_gifts()

Alias for get_business_account_gifts()

Alias for get_business_account_star_balance()

Alias for get_business_connection()

Alias for get_chat_administrators()

Alias for get_chat_member()

Alias for get_chat_member_count()

Alias for get_chat_menu_button()

Alias for get_custom_emoji_stickers()

Alias for get_forum_topic_icon_stickers()

Alias for get_game_high_scores()

Alias for get_my_commands()

Alias for get_my_default_administrator_rights()

Alias for get_my_description()

Alias for get_my_name()

Alias for get_my_short_description()

Alias for get_my_star_balance()

Alias for get_star_transactions()

Alias for get_sticker_set()

Alias for get_updates()

Alias for get_user_chat_boosts()

Alias for get_user_profile_photos()

Alias for get_webhook_info()

Returns the list of gifts that can be sent by the bot to users and channel chats. Requires no parameters.

Added in version 21.8.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

telegram.error.TelegramError –

Returns the gifts received and owned by a managed business account. Requires the can_view_gifts_and_stars business bot right.

Added in version 22.1.

business_connection_id (str) – Unique identifier of the business connection.

exclude_unsaved (bool, optional) – Pass True to exclude gifts that aren’t saved to the account’s profile page.

exclude_saved (bool, optional) – Pass True to exclude gifts that are saved to the account’s profile page.

exclude_unlimited (bool, optional) – Pass True to exclude gifts that can be purchased an unlimited number of times.

exclude_limited (bool, optional) – Pass True to exclude gifts that can be purchased a limited number of times.

exclude_unique (bool, optional) – Pass True to exclude unique gifts.

sort_by_price (bool, optional) – Pass True to sort results by gift price instead of send date. Sorting is applied before pagination.

offset (str, optional) – Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results.

limit (int, optional) – The maximum number of gifts to be returned; 1- 100. Defaults to 100.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

telegram.error.TelegramError –

Returns the amount of Telegram Stars owned by a managed business account. Requires the can_view_gifts_and_stars business bot right.

Added in version 22.1.

business_connection_id (str) – Unique identifier of the business connection.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

telegram.error.TelegramError –

Use this method to get information about the connection of the bot with a business account.

Added in version 21.1.

business_connection_id (str) – Unique identifier of the business connection.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, the object containing the businessconnection information is returned.

connection information is returned.

telegram.BusinessConnection

telegram.error.TelegramError –

Use this method to get up to date information about the chat (current name of the user for one-on-one conversations, current username of a user, group or channel, etc.).

Changed in version 21.2: In accordance to Bot API 7.3, this method now returns a telegram.ChatFullInfo.

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername).

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

telegram.ChatFullInfo

telegram.error.TelegramError –

Use this method to get a list of administrators in a chat.

telegram.Chat.get_administrators()

telegram.ChatFullInfo.get_administrators()

Changed in version 20.0: Returns a tuple instead of a list.

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername).

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, returns a tuple of ChatMember objects that contains information about all chat administrators except other bots. If the chat is a group or a supergroup and no administrators were appointed, only the creator will be returned.

tuple[telegram.ChatMember]

telegram.error.TelegramError –

Use this method to get information about a member of a chat. The method is only guaranteed to work for other users if the bot is an administrator in the chat.

telegram.Chat.get_member()

telegram.ChatFullInfo.get_member()

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername).

user_id (int) – Unique identifier of the target user.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

telegram.error.TelegramError –

Use this method to get the number of members in a chat.

telegram.Chat.get_member_count()

telegram.ChatFullInfo.get_member_count()

Added in version 13.7.

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername).

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

Number of members in the chat.

telegram.error.TelegramError –

Use this method to get the current value of the bot’s menu button in a private chat, or the default menu button.

set_chat_menu_button(), telegram.Chat.set_menu_button(), telegram.User.set_menu_button()

telegram.Chat.get_menu_button()

telegram.ChatFullInfo.get_menu_button()

telegram.User.get_menu_button()

Added in version 20.0.

chat_id (int, optional) – Unique identifier for the target private chat. If not specified, default bot’s menu button will be returned.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, the current menu button is returned.

Use this method to get information about emoji stickers by their identifiers.

Changed in version 20.0: Returns a tuple instead of a list.

custom_emoji_ids (Sequence[str]) – Sequence of custom emoji identifiers. At most 200 custom emoji identifiers can be specified. Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list.

Sequence of custom emoji identifiers. At most 200 custom emoji identifiers can be specified.

Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

tuple[telegram.Sticker]

telegram.error.TelegramError –

Use this method to get basic info about a file and prepare it for downloading. For the moment, bots can download files of up to 20 MB in size. The file can then be e.g. downloaded with telegram.File.download_to_drive(). It is guaranteed that the link will be valid for at least 1 hour. When the link expires, a new one can be requested by calling get_file again.

This function may not preserve the original file name and MIME type. You should save the file’s MIME type and name (if available) when the File object is received.

Working with Files and Media

telegram.Animation.get_file()

telegram.Audio.get_file()

telegram.ChatPhoto.get_big_file()

telegram.ChatPhoto.get_small_file()

telegram.Document.get_file()

telegram.PhotoSize.get_file()

telegram.Sticker.get_file()

telegram.Video.get_file()

telegram.VideoNote.get_file()

telegram.Voice.get_file()

file_id (str | telegram.Animation | telegram.Audio | telegram.ChatPhoto | telegram.Document | telegram.PhotoSize | telegram.Sticker | telegram.Video | telegram.VideoNote | telegram.Voice) – Either the file identifier or an object that has a file_id attribute to get file information about.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

telegram.error.TelegramError –

Use this method to get custom emoji stickers, which can be used as a forum topic icon by any user. Requires no parameters.

Added in version 20.0.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

tuple[telegram.Sticker]

telegram.error.TelegramError –

Use this method to get data for high score tables. Will return the score of the specified user and several of their neighbors in a game.

This method will currently return scores for the target user, plus two of their closest neighbors on each side. Will also return the top three users if the user and his neighbors are not among them. Please note that this behavior is subject to change.

telegram.CallbackQuery.get_game_high_scores()

telegram.Message.get_game_high_scores()

Changed in version 20.0: Returns a tuple instead of a list.

user_id (int) – Target user id.

chat_id (int, optional) – Required if inline_message_id is not specified. Unique identifier for the target chat.

message_id (int, optional) – Required if inline_message_id is not specified. Identifier of the sent message.

inline_message_id (str, optional) – Required if chat_id and message_id are not specified. Identifier of the inline message.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

tuple[telegram.GameHighScore]

telegram.error.TelegramError –

A simple method for testing your bot’s auth token. Requires no parameters.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

A telegram.User instance representing that bot if the credentials are valid, None otherwise.

telegram.error.TelegramError –

Use this method to get the current list of the bot’s commands for the given scope and user language.

set_my_commands(), delete_my_commands()

Changed in version 20.0: Returns a tuple instead of a list.

scope (telegram.BotCommandScope, optional) – An object, describing scope of users. Defaults to telegram.BotCommandScopeDefault. Added in version 13.7.

An object, describing scope of users. Defaults to telegram.BotCommandScopeDefault.

Added in version 13.7.

language_code (str, optional) – A two-letter ISO 639-1 language code or an empty string. Added in version 13.7.

A two-letter ISO 639-1 language code or an empty string.

Added in version 13.7.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, the commands set for the bot. An empty tuple is returned if commands are not set.

tuple[telegram.BotCommand]

telegram.error.TelegramError –

Use this method to get the current default administrator rights of the bot.

set_my_default_administrator_rights()

Added in version 20.0.

for_channels (bool, optional) – Pass True to get default administrator rights of the bot in channels. Otherwise, default administrator rights of the bot for groups and supergroups will be returned.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

telegram.ChatAdministratorRights

telegram.error.TelegramError –

Use this method to get the current bot description for the given user language.

language_code (str, optional) – A two-letter ISO 639-1 language code or an empty string.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, the bot description is returned.

telegram.BotDescription

telegram.error.TelegramError –

Use this method to get the current bot name for the given user language.

language_code (str, optional) – A two-letter ISO 639-1 language code or an empty string.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, the bot name is returned.

telegram.error.TelegramError –

Use this method to get the current bot short description for the given user language.

language_code (str, optional) – A two-letter ISO 639-1 language code or an empty string.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, the bot short description isreturned.

telegram.BotShortDescription

telegram.error.TelegramError –

A method to get the current Telegram Stars balance of the bot. Requires no parameters.

Added in version 22.3.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

telegram.error.TelegramError –

Returns the bot’s Telegram Star transactions in chronological order.

Added in version 21.4.

offset (int, optional) – Number of transactions to skip in the response.

limit (int, optional) – The maximum number of transactions to be retrieved. Values between 1- 100 are accepted. Defaults to 100.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

telegram.StarTransactions

telegram.error.TelegramError –

Use this method to get a sticker set.

name (str) – Name of the sticker set.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

telegram.error.TelegramError –

Use this method to receive incoming updates using long polling.

This method will not work if an outgoing webhook is set up.

In order to avoid getting duplicate updates, recalculate offset after each server response.

To take full advantage of this library take a look at telegram.ext.Updater

telegram.ext.Application.run_polling(), telegram.ext.Updater.start_polling()

Changed in version 20.0: Returns a tuple instead of a list.

offset (int, optional) – Identifier of the first update to be returned. Must be greater by one than the highest among the identifiers of previously received updates. By default, updates starting with the earliest unconfirmed update are returned. An update is considered confirmed as soon as this method is called with an offset higher than its telegram.Update.update_id. The negative offset can be specified to retrieve updates starting from -offset update from the end of the updates queue. All previous updates will be forgotten.

limit (int, optional) – Limits the number of updates to be retrieved. Values between 1- 100 are accepted. Defaults to 100.

timeout (int | datetime.timedelta, optional) – Timeout in seconds for long polling. Defaults to 0, i.e. usual short polling. Should be positive, short polling should be used for testing purposes only. Changed in version v22.2: datetime.timedelta objects are accepted in addition to plain int values.

Timeout in seconds for long polling. Defaults to 0, i.e. usual short polling. Should be positive, short polling should be used for testing purposes only.

Changed in version v22.2: datetime.timedelta objects are accepted in addition to plain int values.

allowed_updates (Sequence[str]), optional) – A sequence the types of updates you want your bot to receive. For example, specify [“message”, “edited_channel_post”, “callback_query”] to only receive updates of these types. See telegram.Update for a complete list of available update types. Specify an empty sequence to receive all updates except telegram.Update.chat_member, telegram.Update.message_reaction and telegram.Update.message_reaction_count (default). If not specified, the previous setting will be used. Please note that this parameter doesn’t affect updates created before the call to the get_updates, so unwanted updates may be received for a short period of time. Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list.

A sequence the types of updates you want your bot to receive. For example, specify [“message”, “edited_channel_post”, “callback_query”] to only receive updates of these types. See telegram.Update for a complete list of available update types. Specify an empty sequence to receive all updates except telegram.Update.chat_member, telegram.Update.message_reaction and telegram.Update.message_reaction_count (default). If not specified, the previous setting will be used. Please note that this parameter doesn’t affect updates created before the call to the get_updates, so unwanted updates may be received for a short period of time.

Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE. timeout will be added to this value. Changed in version 20.7: Defaults to DEFAULT_NONE instead of 2.

Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE. timeout will be added to this value.

Changed in version 20.7: Defaults to DEFAULT_NONE instead of 2.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

tuple[telegram.Update]

telegram.error.TelegramError –

Use this method to get the list of boosts added to a chat by a user. Requires administrator rights in the chat.

telegram.Chat.get_user_chat_boosts()

telegram.ChatFullInfo.get_user_chat_boosts()

telegram.User.get_chat_boosts()

Added in version 20.8.

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername).

user_id (int) – Unique identifier of the target user.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, the object containing the list of boostsis returned.

telegram.UserChatBoosts

telegram.error.TelegramError –

Use this method to get a list of profile pictures for a user.

telegram.User.get_profile_photos()

user_id (int) – Unique identifier of the target user.

offset (int, optional) – Sequential number of the first photo to be returned. By default, all photos are returned.

limit (int, optional) – Limits the number of photos to be retrieved. Values between 1- 100 are accepted. Defaults to 100.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

telegram.UserProfilePhotos

telegram.error.TelegramError –

Use this method to get current webhook status. Requires no parameters.

If the bot is using get_updates(), will return an object with the telegram.WebhookInfo.url field empty.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

Alias for gift_premium_subscription()

Gifts a Telegram Premium subscription to the given user.

telegram.User.gift_premium_subscription()

Added in version 22.1.

user_id (int) – Unique identifier of the target user who will receive a Telegram Premium subscription.

month_count (int) – Number of months the Telegram Premium subscription will be active for the user; must be one of 3, 6, or 12.

star_count (int) – Number of Telegram Stars to pay for the Telegram Premium subscription; must be 1000 for 3 months, 1500 for 6 months, and 2500 for 12 months.

text (str, optional) – Text that will be shown along with the service message about the subscription; 0-128 characters.

text_parse_mode (str, optional) – Mode for parsing entities. See telegram.constants.ParseMode and formatting options for more details. Entities other than BOLD, ITALIC, UNDERLINE, STRIKETHROUGH, SPOILER, and CUSTOM_EMOJI are ignored.

text_entities (Sequence[telegram.MessageEntity], optional) – A list of special entities that appear in the gift text. It can be specified instead of text_parse_mode. Entities other than BOLD, ITALIC, UNDERLINE, STRIKETHROUGH, SPOILER, and CUSTOM_EMOJI are ignored.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Alias for hide_general_forum_topic()

Use this method to hide the ‘General’ topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have can_manage_topics administrator rights. The topic will be automatically closed if it was open.

telegram.Chat.hide_general_forum_topic()

telegram.ChatFullInfo.hide_general_forum_topic()

Added in version 20.0.

chat_id (int | str) – Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername).

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Unique identifier for this bot. Shortcut for the corresponding attribute of bot.

Initialize resources used by this class. Currently calls get_me() to cache bot and calls telegram.request.BaseRequest.initialize() for the request objects used by this bot.

Added in version 20.0.

Optional. Bot’s last name. Shortcut for the corresponding attribute of bot.

Alias for leave_chat()

Use this method for your bot to leave a group, supergroup or channel.

telegram.Chat.leave()

telegram.ChatFullInfo.leave()

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername).

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Convenience property. Returns the t.me link of the bot.

Whether this bot is running in local mode.

Added in version 20.0.

Use this method to log out from the cloud Bot API server before launching the bot locally. You must log out the bot before running it locally, otherwise there is no guarantee that the bot will receive updates. After a successful call, you can immediately log in on a local server, but will not be able to log in back to the cloud Bot API server for 10 minutes.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Bot’s @username. Shortcut for the corresponding attribute of bot.

Alias for pin_chat_message()

Use this method to add a message to the list of pinned messages in a chat. If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have the can_pin_messages admin right in a supergroup or can_edit_messages admin right in a channel.

telegram.Chat.pin_message()

telegram.ChatFullInfo.pin_message()

telegram.Message.pin()

telegram.User.pin_message()

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername).

message_id (int) – Identifier of a message to pin.

disable_notification (bool, optional) – Pass True, if it is not necessary to send a notification to all chat members about the new pinned message. Notifications are always disabled in channels and private chats.

business_connection_id (str, optional) – Unique identifier of the business connection on behalf of which the message will be pinned. Added in version 21.5.

Unique identifier of the business connection on behalf of which the message will be pinned.

Added in version 21.5.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Alias for post_story()

Posts a story on behalf of a managed business account. Requires the can_manage_stories business bot right.

Added in version 22.1.

business_connection_id (str) – Unique identifier of the business connection.

content (telegram.InputStoryContent) – Content of the story.

active_period (int | datetime.timedelta, optional) – Period after which the story is moved to the archive, in seconds; must be one of '21600', '43200', '86400', or '172800'.

caption (str, optional) – Caption of the story, 0-'2048' characters after entities parsing.

parse_mode (str, optional) – Mode for parsing entities in the story caption. See the constants in telegram.constants.ParseMode for the available modes.

caption_entities (Sequence[telegram.MessageEntity], optional) – Sequence of special entities that appear in the caption, which can be specified instead of parse_mode.

areas (Sequence[telegram.StoryArea], optional) – Sequence of clickable areas to be shown on the story. Note Each type of clickable area in areas has its own maximum limit: Up to 10 of telegram.StoryAreaTypeLocation. Up to 5 of telegram.StoryAreaTypeSuggestedReaction. Up to 3 of telegram.StoryAreaTypeLink. Up to 3 of telegram.StoryAreaTypeWeather. Up to 1 of telegram.StoryAreaTypeUniqueGift.

Sequence of clickable areas to be shown on the story.

Each type of clickable area in areas has its own maximum limit:

Up to 10 of telegram.StoryAreaTypeLocation.

Up to 5 of telegram.StoryAreaTypeSuggestedReaction.

Up to 3 of telegram.StoryAreaTypeLink.

Up to 3 of telegram.StoryAreaTypeWeather.

Up to 1 of telegram.StoryAreaTypeUniqueGift.

post_to_chat_page (telegram.InputStoryContent, optional) – Pass True to keep the story accessible after it expires.

protect_content (bool, optional) – Pass True if the content of the story must be protected from forwarding and screenshotting

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

telegram.error.TelegramError –

Deserialized private key for decryption of telegram passport data.

Added in version 20.0.

Alias for promote_chat_member()

Use this method to promote or demote a user in a supergroup or a channel. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights. Pass False for all boolean parameters to demote a user.

telegram.Chat.promote_member()

telegram.ChatFullInfo.promote_member()

Changed in version 20.0: The argument can_manage_voice_chats was renamed to can_manage_video_chats in accordance to Bot API 6.0.

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername).

user_id (int) – Unique identifier of the target user.

is_anonymous (bool, optional) – Pass True, if the administrator’s presence in the chat is hidden.

can_manage_chat (bool, optional) – Pass True, if the administrator can access the chat event log, get boost list, see hidden supergroup and channel members, report spam messages and ignore slow mode. Implied by any other administrator privilege. Added in version 13.4.

Pass True, if the administrator can access the chat event log, get boost list, see hidden supergroup and channel members, report spam messages and ignore slow mode. Implied by any other administrator privilege.

Added in version 13.4.

can_manage_video_chats (bool, optional) – Pass True, if the administrator can manage video chats. Added in version 20.0.

Pass True, if the administrator can manage video chats.

Added in version 20.0.

can_change_info (bool, optional) – Pass True, if the administrator can change chat title, photo and other settings.

can_post_messages (bool, optional) – Pass True, if the administrator can post messages in the channel, or access channel statistics; for channels only.

can_edit_messages (bool, optional) – Pass True, if the administrator can edit messages of other users and can pin messages, for channels only.

can_delete_messages (bool, optional) – Pass True, if the administrator can delete messages of other users.

can_invite_users (bool, optional) – Pass True, if the administrator can invite new users to the chat.

can_restrict_members (bool, optional) – Pass True, if the administrator can restrict, ban or unban chat members, or access supergroup statistics.

can_pin_messages (bool, optional) – Pass True, if the administrator can pin messages, for supergroups only.

can_promote_members (bool, optional) – Pass True, if the administrator can add new administrators with a subset of their own privileges or demote administrators that they have promoted, directly or indirectly (promoted by administrators that were appointed by the user).

can_manage_topics (bool, optional) – Pass True, if the user is allowed to create, rename, close, and reopen forum topics; for supergroups only. Added in version 20.0.

Pass True, if the user is allowed to create, rename, close, and reopen forum topics; for supergroups only.

Added in version 20.0.

can_post_stories (bool, optional) – Pass True, if the administrator can post stories to the chat. Added in version 20.6.

Pass True, if the administrator can post stories to the chat.

Added in version 20.6.

can_edit_stories (bool, optional) – Pass True, if the administrator can edit stories posted by other users, post stories to the chat page, pin chat stories, and access the chat’s story archive Added in version 20.6.

Pass True, if the administrator can edit stories posted by other users, post stories to the chat page, pin chat stories, and access the chat’s story archive

Added in version 20.6.

can_delete_stories (bool, optional) – Pass True, if the administrator can delete stories posted by other users. Added in version 20.6.

Pass True, if the administrator can delete stories posted by other users.

Added in version 20.6.

can_manage_direct_messages (bool, optional) – Pass True, if the administrator can manage direct messages within the channel and decline suggested posts; for channels only Added in version 22.4.

Pass True, if the administrator can manage direct messages within the channel and decline suggested posts; for channels only

Added in version 22.4.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Alias for read_business_message()

Marks incoming message as read on behalf of a business account. Requires the can_read_messages business bot right.

telegram.Chat.read_business_message()

telegram.ChatFullInfo.read_business_message()

telegram.Message.read_business_message()

Added in version 22.1.

business_connection_id (str) – Unique identifier of the business connection on behalf of which to read the message.

chat_id (int) – Unique identifier of the chat in which the message was received. The chat must have been active in the last 86400 seconds.

message_id (int) – Unique identifier of the message to mark as read.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Alias for refund_star_payment()

Refunds a successful payment in Telegram Stars.

telegram.User.refund_star_payment()

Added in version 21.3.

user_id (int) – User identifier of the user whose payment will be refunded.

telegram_payment_charge_id (str) – Telegram payment identifier.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Alias for remove_business_account_profile_photo()

Alias for remove_chat_verification()

Alias for remove_user_verification()

Removes the current profile photo of a managed business account. Requires the can_edit_profile_photo business bot right.

Added in version 22.1.

business_connection_id (str) – Unique identifier of the business connection.

is_public (bool, optional) – Pass True to remove the public photo, which will be visible even if the main photo is hidden by the business account’s privacy settings. After the main photo is removed, the previous profile photo (if present) becomes the main photo.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Removes verification from a chat that is currently verified on behalf of the organization represented by the bot.

telegram.Chat.remove_verification()

telegram.ChatFullInfo.remove_verification()

Added in version 21.10.

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername).

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Removes verification from a user who is currently verified on behalf of the organization represented by the bot.

telegram.User.remove_verification()

Added in version 21.10.

user_id (int) – Unique identifier of the target user.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Alias for reopen_forum_topic()

Alias for reopen_general_forum_topic()

Use this method to reopen a closed topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have can_manage_topics administrator rights, unless it is the creator of the topic.

telegram.Chat.reopen_forum_topic()

telegram.ChatFullInfo.reopen_forum_topic()

telegram.Message.reopen_forum_topic()

Added in version 20.0.

chat_id (int | str) – Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername).

message_thread_id (int) – Unique identifier for the target message thread of the forum topic.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Use this method to reopen a closed ‘General’ topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have can_manage_topics administrator rights. The topic will be automatically unhidden if it was hidden.

telegram.Chat.reopen_general_forum_topic()

telegram.ChatFullInfo.reopen_general_forum_topic()

Added in version 20.0.

chat_id (int | str) – Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername).

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Alias for replace_sticker_in_set()

Use this method to replace an existing sticker in a sticker set with a new one. The method is equivalent to calling delete_sticker_from_set(), then add_sticker_to_set(), then set_sticker_position_in_set().

Added in version 21.1.

user_id (int) – User identifier of the sticker set owner.

name (str) – Sticker set name.

old_sticker (str | Sticker) – File identifier of the replaced sticker or the sticker object itself. Changed in version 21.10: Accepts also telegram.Sticker instances.

File identifier of the replaced sticker or the sticker object itself.

Changed in version 21.10: Accepts also telegram.Sticker instances.

sticker (telegram.InputSticker) – An object with information about the added sticker. If exactly the same sticker had already been added to the set, then the set remains unchanged.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

The BaseRequest object used by this bot.

Requests to the Bot API are made by the various methods of this class. This attribute should not be used manually.

Alias for restrict_chat_member()

Use this method to restrict a user in a supergroup. The bot must be an administrator in the supergroup for this to work and must have the appropriate admin rights. Pass True for all boolean parameters to lift restrictions from a user.

telegram.ChatPermissions.all_permissions()

telegram.Chat.restrict_member()

telegram.ChatFullInfo.restrict_member()

chat_id (int | str) – Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername).

user_id (int) – Unique identifier of the target user.

until_date (int | datetime.datetime, optional) – Date when restrictions will be lifted for the user, unix time. If user is restricted for more than 366 days or less than 30 seconds from the current time, they are considered to be restricted forever. For timezone naive datetime.datetime objects, the default timezone of the bot will be used, which is UTC unless telegram.ext.Defaults.tzinfo is used.

permissions (telegram.ChatPermissions) – An object for new user permissions.

use_independent_chat_permissions (bool, optional) – Pass True if chat permissions are set independently. Otherwise, the can_send_other_messages and can_add_web_page_previews permissions will imply the can_send_messages, can_send_audios, can_send_documents, can_send_photos, can_send_videos, can_send_video_notes, and can_send_voice_notes permissions; the can_send_polls permission will imply the can_send_messages permission.

Pass True if chat permissions are set independently. Otherwise, the can_send_other_messages and can_add_web_page_previews permissions will imply the can_send_messages, can_send_audios, can_send_documents, can_send_photos, can_send_videos, can_send_video_notes, and can_send_voice_notes permissions; the can_send_polls permission will imply the can_send_messages permission.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Alias for revoke_chat_invite_link()

Use this method to revoke an invite link created by the bot. If the primary link is revoked, a new link is automatically generated. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights.

telegram.Chat.revoke_invite_link()

telegram.ChatFullInfo.revoke_invite_link()

Added in version 13.4.

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername).

invite_link (str | telegram.ChatInviteLink) – The invite link to revoke. Changed in version 20.0: Now also accepts telegram.ChatInviteLink instances.

The invite link to revoke.

Changed in version 20.0: Now also accepts telegram.ChatInviteLink instances.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

telegram.ChatInviteLink

telegram.error.TelegramError –

Alias for save_prepared_inline_message()

Stores a message that can be sent by a user of a Mini App.

Added in version 21.8.

user_id (int) – Unique identifier of the target user that can use the prepared message.

result (telegram.InlineQueryResult) – The result to store.

allow_user_chats (bool, optional) – Pass True if the message can be sent to private chats with users

allow_bot_chats (bool, optional) – Pass True if the message can be sent to private chats with bots

allow_group_chats (bool, optional) – Pass True if the message can be sent to group and supergroup chats

allow_channel_chats (bool, optional) – Pass True if the message can be sent to channels

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, the prepared message is returned.

telegram.PreparedInlineMessage

telegram.error.TelegramError –

Alias for send_animation()

Alias for send_audio()

Alias for send_chat_action()

Alias for send_checklist()

Alias for send_contact()

Alias for send_dice()

Alias for send_document()

Alias for send_game()

Alias for send_gift()

Alias for send_invoice()

Alias for send_location()

Alias for send_media_group()

Alias for send_message()

Alias for send_paid_media()

Alias for send_photo()

Alias for send_poll()

Alias for send_sticker()

Alias for send_venue()

Alias for send_video()

Alias for send_video_note()

Alias for send_voice()

Use this method to send animation files (GIF or H.264/MPEG-4 AVC video without sound). Bots can currently send animation files of up to 50 MB in size, this limit may be changed in the future.

thumbnail will be ignored for small files, for which Telegram can easily generate thumbnails. However, this behaviour is undocumented and might be changed by Telegram.

Working with Files and Media

telegram.Chat.send_animation()

telegram.ChatFullInfo.send_animation()

telegram.Message.reply_animation()

telegram.User.send_animation()

Changed in version 20.5: Removed deprecated argument thumb. Use thumbnail instead.

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername).

animation (str | file object | InputFile | bytes | pathlib.Path | telegram.Animation) – Animation to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one. To upload a file, you can either pass a file object (e.g. open("filename", "rb")), the file contents as bytes or the path of the file (as string or pathlib.Path object). In the latter case, the file contents will either be read as bytes or the file path will be passed to Telegram, depending on the local_mode setting. Lastly you can pass an existing telegram.Animation object to send. Changed in version 13.2: Accept bytes as input.

Animation to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one. To upload a file, you can either pass a file object (e.g. open("filename", "rb")), the file contents as bytes or the path of the file (as string or pathlib.Path object). In the latter case, the file contents will either be read as bytes or the file path will be passed to Telegram, depending on the local_mode setting. Lastly you can pass an existing telegram.Animation object to send.

Changed in version 13.2: Accept bytes as input.

duration (int | datetime.timedelta, optional) – Duration of sent animation in seconds. Changed in version 21.11: datetime.timedelta objects are accepted in addition to plain int values.

Duration of sent animation in seconds.

Changed in version 21.11: datetime.timedelta objects are accepted in addition to plain int values.

width (int, optional) – Animation width.

height (int, optional) – Animation height.

caption (str, optional) – Animation caption (may also be used when resending animations by file_id), 0-1024 characters after entities parsing.

parse_mode (str, optional) – Mode for parsing entities. See telegram.constants.ParseMode and formatting options for more details.

caption_entities (Sequence[telegram.MessageEntity], optional) – Sequence of special entities that appear in the caption, which can be specified instead of parse_mode. Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list.

Sequence of special entities that appear in the caption, which can be specified instead of parse_mode.

Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list.

disable_notification (bool, optional) – Sends the message silently. Users will receive a notification with no sound.

protect_content (bool, optional) – Protects the contents of the sent message from forwarding and saving. Added in version 13.10.

Protects the contents of the sent message from forwarding and saving.

Added in version 13.10.

message_thread_id (int, optional) – Unique identifier for the target message thread (topic) of the forum; for forum supergroups only. Added in version 20.0.

Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.

Added in version 20.0.

reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply, optional) – Additional interface options. An object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.

has_spoiler (bool, optional) – Pass True if the animation needs to be covered with a spoiler animation. Added in version 20.0.

Pass True if the animation needs to be covered with a spoiler animation.

Added in version 20.0.

thumbnail (file object | bytes | pathlib.Path | str, optional) – Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail’s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file. To upload a file, you can either pass a file object (e.g. open("filename", "rb")), the file contents as bytes or the path of the file (as string or pathlib.Path object). In the latter case, the file contents will either be read as bytes or the file path will be passed to Telegram, depending on the local_mode setting. Added in version 20.2.

Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail’s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file. To upload a file, you can either pass a file object (e.g. open("filename", "rb")), the file contents as bytes or the path of the file (as string or pathlib.Path object). In the latter case, the file contents will either be read as bytes or the file path will be passed to Telegram, depending on the local_mode setting.

Added in version 20.2.

reply_parameters (telegram.ReplyParameters, optional) – Description of the message to reply to. Added in version 20.8.

Description of the message to reply to.

Added in version 20.8.

business_connection_id (str, optional) – Unique identifier of the business connection on behalf of which the message will be sent. Added in version 21.1.

Unique identifier of the business connection on behalf of which the message will be sent.

Added in version 21.1.

message_effect_id (str, optional) – Unique identifier of the message effect to be added to the message; for private chats only. Added in version 21.3.

Unique identifier of the message effect to be added to the message; for private chats only.

Added in version 21.3.

allow_paid_broadcast (bool, optional) – Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance. Added in version 21.7.

Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance.

Added in version 21.7.

show_caption_above_media (bool, optional) – Pass True, if the caption must be shown above the message media. Added in version 21.3.

Pass True, if the caption must be shown above the message media.

Added in version 21.3.

suggested_post_parameters (telegram.SuggestedPostParameters, optional) – An object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined. Added in version 22.4.

An object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined.

Added in version 22.4.

direct_messages_topic_id (int, optional) – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat. Added in version 22.4.

Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat.

Added in version 22.4.

allow_sending_without_reply (bool, optional) – Pass True, if the message should be sent even if the specified replied-to message is not found. Mutually exclusive with reply_parameters, which this is a convenience parameter for Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument. Changed in version 21.0: This argument is now a keyword-only argument.

Pass True, if the message should be sent even if the specified replied-to message is not found. Mutually exclusive with reply_parameters, which this is a convenience parameter for

Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument.

Changed in version 21.0: This argument is now a keyword-only argument.

reply_to_message_id (int, optional) – If the message is a reply, ID of the original message. Mutually exclusive with reply_parameters, which this is a convenience parameter for Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument. Changed in version 21.0: This argument is now a keyword-only argument.

If the message is a reply, ID of the original message. Mutually exclusive with reply_parameters, which this is a convenience parameter for

Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument.

Changed in version 21.0: This argument is now a keyword-only argument.

filename (str, optional) – Custom file name for the animation, when uploading a new file. Convenience parameter, useful e.g. when sending files generated by the tempfile module. Added in version 13.1.

Custom file name for the animation, when uploading a new file. Convenience parameter, useful e.g. when sending files generated by the tempfile module.

Added in version 13.1.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. By default, 20 seconds are used as write timeout. Changed in version 22.0: The default value changed to DEFAULT_NONE.

Value to pass to telegram.request.BaseRequest.post.write_timeout. By default, 20 seconds are used as write timeout.

Changed in version 22.0: The default value changed to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, the sent Message is returned.

telegram.error.TelegramError –

Use this method to send audio files, if you want Telegram clients to display them in the music player. Your audio must be in the .mp3 or .m4a format.

Bots can currently send audio files of up to 50 MB in size, this limit may be changed in the future.

For sending voice messages, use the send_voice() method instead.

Working with Files and Media

telegram.Chat.send_audio()

telegram.ChatFullInfo.send_audio()

telegram.Message.reply_audio()

telegram.User.send_audio()

Changed in version 20.5: Removed deprecated argument thumb. Use thumbnail instead.

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername).

audio (str | file object | InputFile | bytes | pathlib.Path | telegram.Audio) – Audio file to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one. To upload a file, you can either pass a file object (e.g. open("filename", "rb")), the file contents as bytes or the path of the file (as string or pathlib.Path object). In the latter case, the file contents will either be read as bytes or the file path will be passed to Telegram, depending on the local_mode setting. Lastly you can pass an existing telegram.Audio object to send. Changed in version 13.2: Accept bytes as input. Changed in version 20.0: File paths as input is also accepted for bots not running in local_mode.

Audio file to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one. To upload a file, you can either pass a file object (e.g. open("filename", "rb")), the file contents as bytes or the path of the file (as string or pathlib.Path object). In the latter case, the file contents will either be read as bytes or the file path will be passed to Telegram, depending on the local_mode setting. Lastly you can pass an existing telegram.Audio object to send.

Changed in version 13.2: Accept bytes as input.

Changed in version 20.0: File paths as input is also accepted for bots not running in local_mode.

caption (str, optional) – Audio caption, 0-1024 characters after entities parsing.

parse_mode (str, optional) – Mode for parsing entities. See telegram.constants.ParseMode and formatting options for more details.

caption_entities (Sequence[telegram.MessageEntity], optional) – Sequence of special entities that appear in the caption, which can be specified instead of parse_mode. Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list.

Sequence of special entities that appear in the caption, which can be specified instead of parse_mode.

Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list.

duration (int | datetime.timedelta, optional) – Duration of sent audio in seconds. Changed in version 21.11: datetime.timedelta objects are accepted in addition to plain int values.

Duration of sent audio in seconds.

Changed in version 21.11: datetime.timedelta objects are accepted in addition to plain int values.

performer (str, optional) – Performer.

title (str, optional) – Track name.

disable_notification (bool, optional) – Sends the message silently. Users will receive a notification with no sound.

protect_content (bool, optional) – Protects the contents of the sent message from forwarding and saving. Added in version 13.10.

Protects the contents of the sent message from forwarding and saving.

Added in version 13.10.

message_thread_id (int, optional) – Unique identifier for the target message thread (topic) of the forum; for forum supergroups only. Added in version 20.0.

Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.

Added in version 20.0.

reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply, optional) – Additional interface options. An object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.

thumbnail (file object | bytes | pathlib.Path | str, optional) – Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail’s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file. To upload a file, you can either pass a file object (e.g. open("filename", "rb")), the file contents as bytes or the path of the file (as string or pathlib.Path object). In the latter case, the file contents will either be read as bytes or the file path will be passed to Telegram, depending on the local_mode setting. Added in version 20.2.

Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail’s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file. To upload a file, you can either pass a file object (e.g. open("filename", "rb")), the file contents as bytes or the path of the file (as string or pathlib.Path object). In the latter case, the file contents will either be read as bytes or the file path will be passed to Telegram, depending on the local_mode setting.

Added in version 20.2.

reply_parameters (ReplyParameters, optional) – Description of the message to reply to. Added in version 20.8.

Description of the message to reply to.

Added in version 20.8.

business_connection_id (str, optional) – Unique identifier of the business connection on behalf of which the message will be sent. Added in version 21.1.

Unique identifier of the business connection on behalf of which the message will be sent.

Added in version 21.1.

message_effect_id (str, optional) – Unique identifier of the message effect to be added to the message; for private chats only. Added in version 21.3.

Unique identifier of the message effect to be added to the message; for private chats only.

Added in version 21.3.

allow_paid_broadcast (bool, optional) – Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance. Added in version 21.7.

Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance.

Added in version 21.7.

suggested_post_parameters (telegram.SuggestedPostParameters, optional) – An object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined. Added in version 22.4.

An object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined.

Added in version 22.4.

direct_messages_topic_id (int, optional) – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat. Added in version 22.4.

Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat.

Added in version 22.4.

allow_sending_without_reply (bool, optional) – Pass True, if the message should be sent even if the specified replied-to message is not found. Mutually exclusive with reply_parameters, which this is a convenience parameter for Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument. Changed in version 21.0: This argument is now a keyword-only argument.

Pass True, if the message should be sent even if the specified replied-to message is not found. Mutually exclusive with reply_parameters, which this is a convenience parameter for

Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument.

Changed in version 21.0: This argument is now a keyword-only argument.

reply_to_message_id (int, optional) – If the message is a reply, ID of the original message. Mutually exclusive with reply_parameters, which this is a convenience parameter for Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument. Changed in version 21.0: This argument is now a keyword-only argument.

If the message is a reply, ID of the original message. Mutually exclusive with reply_parameters, which this is a convenience parameter for

Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument.

Changed in version 21.0: This argument is now a keyword-only argument.

filename (str, optional) – Custom file name for the audio, when uploading a new file. Convenience parameter, useful e.g. when sending files generated by the tempfile module. Added in version 13.1.

Custom file name for the audio, when uploading a new file. Convenience parameter, useful e.g. when sending files generated by the tempfile module.

Added in version 13.1.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. By default, 20 seconds are used as write timeout. Changed in version 22.0: The default value changed to DEFAULT_NONE.

Value to pass to telegram.request.BaseRequest.post.write_timeout. By default, 20 seconds are used as write timeout.

Changed in version 22.0: The default value changed to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, the sent Message is returned.

telegram.error.TelegramError –

Use this method when you need to tell the user that something is happening on the bot’s side. The status is set for 5 seconds or less (when a message arrives from your bot, Telegram clients clear its typing status). Telegram only recommends using this method when a response from the bot will take a noticeable amount of time to arrive.

telegram.Chat.send_action()

telegram.Chat.send_chat_action()

telegram.ChatFullInfo.send_action()

telegram.ChatFullInfo.send_chat_action()

telegram.Message.reply_chat_action()

telegram.User.send_action()

telegram.User.send_chat_action()

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername).

action (str) – Type of action to broadcast. Choose one, depending on what the user is about to receive. For convenience look at the constants in telegram.constants.ChatAction.

message_thread_id (int, optional) – Unique identifier for the target message thread (topic) of the forum; for forum supergroups only. Added in version 20.0.

Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.

Added in version 20.0.

business_connection_id (str, optional) – Unique identifier of the business connection on behalf of which the message will be sent. Added in version 21.1.

Unique identifier of the business connection on behalf of which the message will be sent.

Added in version 21.1.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Use this method to send a checklist on behalf of a connected business account.

telegram.Chat.send_checklist()

telegram.ChatFullInfo.send_checklist()

telegram.Message.reply_checklist()

Added in version 22.3.

business_connection_id (str) – Unique identifier of the business connection on behalf of which the message will be sent.

chat_id (int) – Unique identifier for the target chat.

checklist (telegram.InputChecklist) – The checklist to send.

disable_notification (bool, optional) – Sends the message silently. Users will receive a notification with no sound.

protect_content (bool, optional) – Protects the contents of the sent message from forwarding and saving.

message_effect_id (str, optional) – Unique identifier of the message effect to be added to the message; for private chats only.

reply_parameters (telegram.ReplyParameters, optional) – Description of the message to reply to.

reply_markup (telegram.InlineKeyboardMarkup, optional) – An object for an inline keyboard

allow_sending_without_reply (bool, optional) – Pass True, if the message should be sent even if the specified replied-to message is not found. Mutually exclusive with reply_parameters, which this is a convenience parameter for

reply_to_message_id (int, optional) – If the message is a reply, ID of the original message. Mutually exclusive with reply_parameters, which this is a convenience parameter for

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, the sent Message is returned.

telegram.error.TelegramError –

Use this method to send phone contacts.

You can either supply contact or phone_number and first_name with optionally last_name and optionally vcard.

telegram.Chat.send_contact()

telegram.ChatFullInfo.send_contact()

telegram.Message.reply_contact()

telegram.User.send_contact()

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername).

phone_number (str, optional) – Contact’s phone number.

first_name (str, optional) – Contact’s first name.

last_name (str, optional) – Contact’s last name.

vcard (str, optional) – Additional data about the contact in the form of a vCard, 0-2048 bytes.

disable_notification (bool, optional) – Sends the message silently. Users will receive a notification with no sound.

protect_content (bool, optional) – Protects the contents of the sent message from forwarding and saving. Added in version 13.10.

Protects the contents of the sent message from forwarding and saving.

Added in version 13.10.

message_thread_id (int, optional) – Unique identifier for the target message thread (topic) of the forum; for forum supergroups only. Added in version 20.0.

Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.

Added in version 20.0.

reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply, optional) – Additional interface options. An object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.

reply_parameters (telegram.ReplyParameters, optional) – Description of the message to reply to. Added in version 20.8.

Description of the message to reply to.

Added in version 20.8.

business_connection_id (str, optional) – Unique identifier of the business connection on behalf of which the message will be sent. Added in version 21.1.

Unique identifier of the business connection on behalf of which the message will be sent.

Added in version 21.1.

message_effect_id (str, optional) – Unique identifier of the message effect to be added to the message; for private chats only. Added in version 21.3.

Unique identifier of the message effect to be added to the message; for private chats only.

Added in version 21.3.

allow_paid_broadcast (bool, optional) – Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance. Added in version 21.7.

Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance.

Added in version 21.7.

suggested_post_parameters (telegram.SuggestedPostParameters, optional) – An object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined. Added in version 22.4.

An object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined.

Added in version 22.4.

direct_messages_topic_id (int, optional) – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat. Added in version 22.4.

Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat.

Added in version 22.4.

allow_sending_without_reply (bool, optional) – Pass True, if the message should be sent even if the specified replied-to message is not found. Mutually exclusive with reply_parameters, which this is a convenience parameter for Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument. Changed in version 21.0: This argument is now a keyword-only argument.

Pass True, if the message should be sent even if the specified replied-to message is not found. Mutually exclusive with reply_parameters, which this is a convenience parameter for

Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument.

Changed in version 21.0: This argument is now a keyword-only argument.

reply_to_message_id (int, optional) – If the message is a reply, ID of the original message. Mutually exclusive with reply_parameters, which this is a convenience parameter for Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument. Changed in version 21.0: This argument is now a keyword-only argument.

If the message is a reply, ID of the original message. Mutually exclusive with reply_parameters, which this is a convenience parameter for

Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument.

Changed in version 21.0: This argument is now a keyword-only argument.

contact (telegram.Contact, optional) – The contact to send.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, the sent Message is returned.

telegram.error.TelegramError –

Use this method to send an animated emoji that will display a random value.

telegram.Chat.send_dice()

telegram.ChatFullInfo.send_dice()

telegram.Message.reply_dice()

telegram.User.send_dice()

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername).

disable_notification (bool, optional) – Sends the message silently. Users will receive a notification with no sound.

reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply, optional) – Additional interface options. An object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user

emoji (str, optional) – Emoji on which the dice throw animation is based. Currently, must be one of telegram.constants.DiceEmoji. Dice can have values 1-6 for '🎲', '🎯' and '🎳', values 1-5 for '🏀' and '⚽', and values 1- 64 for '🎰'. Defaults to '🎲'. Changed in version 13.4: Added the '🎳' emoji.

Emoji on which the dice throw animation is based. Currently, must be one of telegram.constants.DiceEmoji. Dice can have values 1-6 for '🎲', '🎯' and '🎳', values 1-5 for '🏀' and '⚽', and values 1- 64 for '🎰'. Defaults to '🎲'.

Changed in version 13.4: Added the '🎳' emoji.

protect_content (bool, optional) – Protects the contents of the sent message from forwarding and saving. Added in version 13.10.

Protects the contents of the sent message from forwarding and saving.

Added in version 13.10.

message_thread_id (int, optional) – Unique identifier for the target message thread (topic) of the forum; for forum supergroups only. Added in version 20.0.

Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.

Added in version 20.0.

reply_parameters (telegram.ReplyParameters, optional) – Description of the message to reply to. Added in version 20.8.

Description of the message to reply to.

Added in version 20.8.

business_connection_id (str, optional) – Unique identifier of the business connection on behalf of which the message will be sent. Added in version 21.1.

Unique identifier of the business connection on behalf of which the message will be sent.

Added in version 21.1.

message_effect_id (str, optional) – Unique identifier of the message effect to be added to the message; for private chats only. Added in version 21.3.

Unique identifier of the message effect to be added to the message; for private chats only.

Added in version 21.3.

allow_paid_broadcast (bool, optional) – Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance. Added in version 21.7.

Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance.

Added in version 21.7.

suggested_post_parameters (telegram.SuggestedPostParameters, optional) – An object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined. Added in version 22.4.

An object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined.

Added in version 22.4.

direct_messages_topic_id (int, optional) – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat. Added in version 22.4.

Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat.

Added in version 22.4.

allow_sending_without_reply (bool, optional) – Pass True, if the message should be sent even if the specified replied-to message is not found. Mutually exclusive with reply_parameters, which this is a convenience parameter for Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument. Changed in version 21.0: This argument is now a keyword-only argument.

Pass True, if the message should be sent even if the specified replied-to message is not found. Mutually exclusive with reply_parameters, which this is a convenience parameter for

Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument.

Changed in version 21.0: This argument is now a keyword-only argument.

reply_to_message_id (int, optional) – If the message is a reply, ID of the original message. Mutually exclusive with reply_parameters, which this is a convenience parameter for Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument. Changed in version 21.0: This argument is now a keyword-only argument.

If the message is a reply, ID of the original message. Mutually exclusive with reply_parameters, which this is a convenience parameter for

Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument.

Changed in version 21.0: This argument is now a keyword-only argument.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, the sent Message is returned.

telegram.error.TelegramError –

Use this method to send general files.

Bots can currently send files of any type of up to 50 MB in size, this limit may be changed in the future.

Working with Files and Media

telegram.Chat.send_document()

telegram.ChatFullInfo.send_document()

telegram.Message.reply_document()

telegram.User.send_document()

Changed in version 20.5: Removed deprecated argument thumb. Use thumbnail instead.

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername).

document (str | file object | InputFile | bytes | pathlib.Path | telegram.Document) – File to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one. To upload a file, you can either pass a file object (e.g. open("filename", "rb")), the file contents as bytes or the path of the file (as string or pathlib.Path object). In the latter case, the file contents will either be read as bytes or the file path will be passed to Telegram, depending on the local_mode setting. Lastly you can pass an existing telegram.Document object to send. Note Sending by URL will currently only work GIF, PDF & ZIP files. Changed in version 13.2: Accept bytes as input. Changed in version 20.0: File paths as input is also accepted for bots not running in local_mode.

File to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one. To upload a file, you can either pass a file object (e.g. open("filename", "rb")), the file contents as bytes or the path of the file (as string or pathlib.Path object). In the latter case, the file contents will either be read as bytes or the file path will be passed to Telegram, depending on the local_mode setting. Lastly you can pass an existing telegram.Document object to send.

Sending by URL will currently only work GIF, PDF & ZIP files.

Changed in version 13.2: Accept bytes as input.

Changed in version 20.0: File paths as input is also accepted for bots not running in local_mode.

caption (str, optional) – Document caption (may also be used when resending documents by file_id), 0-1024 characters after entities parsing.

disable_content_type_detection (bool, optional) – Disables automatic server-side content type detection for files uploaded using multipart/form-data.

parse_mode (str, optional) – Mode for parsing entities. See telegram.constants.ParseMode and formatting options for more details.

caption_entities (Sequence[telegram.MessageEntity], optional) – Sequence of special entities that appear in the caption, which can be specified instead of parse_mode. Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list.

Sequence of special entities that appear in the caption, which can be specified instead of parse_mode.

Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list.

disable_notification (bool, optional) – Sends the message silently. Users will receive a notification with no sound.

protect_content (bool, optional) – Protects the contents of the sent message from forwarding and saving. Added in version 13.10.

Protects the contents of the sent message from forwarding and saving.

Added in version 13.10.

message_thread_id (int, optional) – Unique identifier for the target message thread (topic) of the forum; for forum supergroups only. Added in version 20.0.

Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.

Added in version 20.0.

reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply, optional) – Additional interface options. An object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.

thumbnail (file object | bytes | pathlib.Path | str, optional) – Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail’s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file. To upload a file, you can either pass a file object (e.g. open("filename", "rb")), the file contents as bytes or the path of the file (as string or pathlib.Path object). In the latter case, the file contents will either be read as bytes or the file path will be passed to Telegram, depending on the local_mode setting. Added in version 20.2.

Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail’s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file. To upload a file, you can either pass a file object (e.g. open("filename", "rb")), the file contents as bytes or the path of the file (as string or pathlib.Path object). In the latter case, the file contents will either be read as bytes or the file path will be passed to Telegram, depending on the local_mode setting.

Added in version 20.2.

reply_parameters (telegram.ReplyParameters, optional) – Description of the message to reply to. Added in version 20.8.

Description of the message to reply to.

Added in version 20.8.

business_connection_id (str, optional) – Unique identifier of the business connection on behalf of which the message will be sent. Added in version 21.1.

Unique identifier of the business connection on behalf of which the message will be sent.

Added in version 21.1.

message_effect_id (str, optional) – Unique identifier of the message effect to be added to the message; for private chats only. Added in version 21.3.

Unique identifier of the message effect to be added to the message; for private chats only.

Added in version 21.3.

allow_paid_broadcast (bool, optional) – Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance. Added in version 21.7.

Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance.

Added in version 21.7.

suggested_post_parameters (telegram.SuggestedPostParameters, optional) – An object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined. Added in version 22.4.

An object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined.

Added in version 22.4.

direct_messages_topic_id (int, optional) – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat. Added in version 22.4.

Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat.

Added in version 22.4.

allow_sending_without_reply (bool, optional) – Pass True, if the message should be sent even if the specified replied-to message is not found. Mutually exclusive with reply_parameters, which this is a convenience parameter for Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument. Changed in version 21.0: This argument is now a keyword-only argument.

Pass True, if the message should be sent even if the specified replied-to message is not found. Mutually exclusive with reply_parameters, which this is a convenience parameter for

Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument.

Changed in version 21.0: This argument is now a keyword-only argument.

reply_to_message_id (int, optional) – If the message is a reply, ID of the original message. Mutually exclusive with reply_parameters, which this is a convenience parameter for Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument. Changed in version 21.0: This argument is now a keyword-only argument.

If the message is a reply, ID of the original message. Mutually exclusive with reply_parameters, which this is a convenience parameter for

Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument.

Changed in version 21.0: This argument is now a keyword-only argument.

filename (str, optional) – Custom file name for the document, when uploading a new file. Convenience parameter, useful e.g. when sending files generated by the tempfile module.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. By default, 20 seconds are used as write timeout. Changed in version 22.0: The default value changed to DEFAULT_NONE.

Value to pass to telegram.request.BaseRequest.post.write_timeout. By default, 20 seconds are used as write timeout.

Changed in version 22.0: The default value changed to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, the sent Message is returned.

telegram.error.TelegramError –

Use this method to send a game.

telegram.Chat.send_game()

telegram.ChatFullInfo.send_game()

telegram.Message.reply_game()

telegram.User.send_game()

chat_id (int) – Unique identifier for the target chat.

game_short_name (str) – Short name of the game, serves as the unique identifier for the game. Set up your games via @BotFather.

Short name of the game, serves as the unique identifier for the game. Set up your games via @BotFather.

disable_notification (bool, optional) – Sends the message silently. Users will receive a notification with no sound.

protect_content (bool, optional) – Protects the contents of the sent message from forwarding and saving. Added in version 13.10.

Protects the contents of the sent message from forwarding and saving.

Added in version 13.10.

message_thread_id (int, optional) – Unique identifier for the target message thread (topic) of the forum; for forum supergroups only. Added in version 20.0.

Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.

Added in version 20.0.

reply_markup (telegram.InlineKeyboardMarkup, optional) – An object for a new inline keyboard. If empty, one “Play game_title” button will be shown. If not empty, the first button must launch the game.

reply_parameters (telegram.ReplyParameters, optional) – Description of the message to reply to. Added in version 20.8.

Description of the message to reply to.

Added in version 20.8.

business_connection_id (str, optional) – Unique identifier of the business connection on behalf of which the message will be sent. Added in version 21.1.

Unique identifier of the business connection on behalf of which the message will be sent.

Added in version 21.1.

message_effect_id (str, optional) – Unique identifier of the message effect to be added to the message; for private chats only. Added in version 21.3.

Unique identifier of the message effect to be added to the message; for private chats only.

Added in version 21.3.

allow_paid_broadcast (bool, optional) – Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance. Added in version 21.7.

Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance.

Added in version 21.7.

allow_sending_without_reply (bool, optional) – Pass True, if the message should be sent even if the specified replied-to message is not found. Mutually exclusive with reply_parameters, which this is a convenience parameter for Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument. Changed in version 21.0: This argument is now a keyword-only argument.

Pass True, if the message should be sent even if the specified replied-to message is not found. Mutually exclusive with reply_parameters, which this is a convenience parameter for

Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument.

Changed in version 21.0: This argument is now a keyword-only argument.

reply_to_message_id (int, optional) – If the message is a reply, ID of the original message. Mutually exclusive with reply_parameters, which this is a convenience parameter for Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument. Changed in version 21.0: This argument is now a keyword-only argument.

If the message is a reply, ID of the original message. Mutually exclusive with reply_parameters, which this is a convenience parameter for

Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument.

Changed in version 21.0: This argument is now a keyword-only argument.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, the sent Message is returned.

telegram.error.TelegramError –

Sends a gift to the given user or channel chat. The gift can’t be converted to Telegram Stars by the receiver.

telegram.Chat.send_gift()

telegram.ChatFullInfo.send_gift()

telegram.User.send_gift()

Added in version 21.8.

Changed in version 22.1: Bot API 8.3 made user_id optional. In version 22.1, the methods signature was changed accordingly.

gift_id (str | Gift) – Identifier of the gift or a Gift object

user_id (int, optional) – Required if chat_id is not specified. Unique identifier of the target user that will receive the gift. Changed in version 21.11: Now optional.

Required if chat_id is not specified. Unique identifier of the target user that will receive the gift.

Changed in version 21.11: Now optional.

chat_id (int | str, optional) – Required if user_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername). It will receive the gift. Added in version 21.11.

Required if user_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername). It will receive the gift.

Added in version 21.11.

text (str, optional) – Text that will be shown along with the gift; 0- 128 characters

text_parse_mode (str, optional) – Mode for parsing entities. See telegram.constants.ParseMode and formatting options for more details. Entities other than BOLD, ITALIC, UNDERLINE, STRIKETHROUGH, SPOILER, and CUSTOM_EMOJI are ignored.

text_entities (Sequence[telegram.MessageEntity], optional) – A list of special entities that appear in the gift text. It can be specified instead of text_parse_mode. Entities other than BOLD, ITALIC, UNDERLINE, STRIKETHROUGH, SPOILER, and CUSTOM_EMOJI are ignored.

pay_for_upgrade (bool, optional) – Pass True to pay for the gift upgrade from the bot’s balance, thereby making the upgrade free for the receiver. Added in version 21.10.

Pass True to pay for the gift upgrade from the bot’s balance, thereby making the upgrade free for the receiver.

Added in version 21.10.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Use this method to send invoices.

As of API 5.2 start_parameter is an optional argument and therefore the order of the arguments had to be changed. Use keyword arguments to make sure that the arguments are passed correctly.

telegram.Chat.send_invoice()

telegram.ChatFullInfo.send_invoice()

telegram.Message.reply_invoice()

telegram.User.send_invoice()

Changed in version 13.5: As of Bot API 5.2, the parameter start_parameter is optional.

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername).

title (str) – Product name. 1- 32 characters.

description (str) – Product description. 1- 255 characters.

payload (str) – Bot-defined invoice payload. 1- 128 bytes. This will not be displayed to the user, use it for your internal processes.

provider_token (str, optional) – Payments provider token, obtained via @BotFather. Pass an empty string for payments in Telegram Stars. Changed in version 21.11: Bot API 7.4 made this parameter is optional and this is now reflected in the function signature.

Payments provider token, obtained via @BotFather. Pass an empty string for payments in Telegram Stars.

Changed in version 21.11: Bot API 7.4 made this parameter is optional and this is now reflected in the function signature.

currency (str) – Three-letter ISO 4217 currency code, see more on currencies. Pass XTR for payment in Telegram Stars.

Three-letter ISO 4217 currency code, see more on currencies. Pass XTR for payment in Telegram Stars.

prices (Sequence[telegram.LabeledPrice]) – Price breakdown, a sequence of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.). Must contain exactly one item for payment in Telegram Stars. Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list.

Price breakdown, a sequence of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.). Must contain exactly one item for payment in Telegram Stars.

Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list.

max_tip_amount (int, optional) – The maximum accepted amount for tips in the smallest units of the currency (integer, not float/double). For example, for a maximum tip of US$ 1.45 pass max_tip_amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). Defaults to 0. Not supported for payment in Telegram Stars. Added in version 13.5.

The maximum accepted amount for tips in the smallest units of the currency (integer, not float/double). For example, for a maximum tip of US$ 1.45 pass max_tip_amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). Defaults to 0. Not supported for payment in Telegram Stars.

Added in version 13.5.

suggested_tip_amounts (Sequence[int], optional) – An array of suggested amounts of tips in the smallest units of the currency (integer, not float/double). At most 4 suggested tip amounts can be specified. The suggested tip amounts must be positive, passed in a strictly increased order and must not exceed max_tip_amount. Added in version 13.5. Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list.

An array of suggested amounts of tips in the smallest units of the currency (integer, not float/double). At most 4 suggested tip amounts can be specified. The suggested tip amounts must be positive, passed in a strictly increased order and must not exceed max_tip_amount.

Added in version 13.5.

Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list.

start_parameter (str, optional) – Unique deep-linking parameter. If left empty, forwarded copies of the sent message will have a Pay button, allowing multiple users to pay directly from the forwarded message, using the same invoice. If non-empty, forwarded copies of the sent message will have a URL button with a deep link to the bot (instead of a Pay button), with the value used as the start parameter. Changed in version 13.5: As of Bot API 5.2, this parameter is optional.

Unique deep-linking parameter. If left empty, forwarded copies of the sent message will have a Pay button, allowing multiple users to pay directly from the forwarded message, using the same invoice. If non-empty, forwarded copies of the sent message will have a URL button with a deep link to the bot (instead of a Pay button), with the value used as the start parameter.

Changed in version 13.5: As of Bot API 5.2, this parameter is optional.

provider_data (str | object, optional) – data about the invoice, which will be shared with the payment provider. A detailed description of required fields should be provided by the payment provider. When an object is passed, it will be encoded as JSON.

photo_url (str, optional) – URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service. People like it better when they see what they are paying for.

photo_size (str, optional) – Photo size.

photo_width (int, optional) – Photo width.

photo_height (int, optional) – Photo height.

need_name (bool, optional) – Pass True, if you require the user’s full name to complete the order. Ignored for payments in Telegram Stars.

need_phone_number (bool, optional) – Pass True, if you require the user’s phone number to complete the order. Ignored for payments in Telegram Stars.

need_email (bool, optional) – Pass True, if you require the user’s email to complete the order. Ignored for payments in Telegram Stars.

need_shipping_address (bool, optional) – Pass True, if you require the user’s shipping address to complete the order. Ignored for payments in Telegram Stars.

send_phone_number_to_provider (bool, optional) – Pass True, if user’s phone number should be sent to provider. Ignored for payments in Telegram Stars.

send_email_to_provider (bool, optional) – Pass True, if user’s email address should be sent to provider. Ignored for payments in Telegram Stars.

is_flexible (bool, optional) – Pass True, if the final price depends on the shipping method. Ignored for payments in Telegram Stars.

disable_notification (bool, optional) – Sends the message silently. Users will receive a notification with no sound.

protect_content (bool, optional) – Protects the contents of the sent message from forwarding and saving. Added in version 13.10.

Protects the contents of the sent message from forwarding and saving.

Added in version 13.10.

message_thread_id (int, optional) – Unique identifier for the target message thread (topic) of the forum; for forum supergroups only. Added in version 20.0.

Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.

Added in version 20.0.

reply_markup (telegram.InlineKeyboardMarkup, optional) – An object for an inline keyboard. If empty, one ‘Pay total price’ button will be shown. If not empty, the first button must be a Pay button.

reply_parameters (telegram.ReplyParameters, optional) – Description of the message to reply to. Added in version 20.8.

Description of the message to reply to.

Added in version 20.8.

message_effect_id (str, optional) – Unique identifier of the message effect to be added to the message; for private chats only. Added in version 21.3.

Unique identifier of the message effect to be added to the message; for private chats only.

Added in version 21.3.

allow_paid_broadcast (bool, optional) – Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance. Added in version 21.7.

Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance.

Added in version 21.7.

suggested_post_parameters (telegram.SuggestedPostParameters, optional) – An object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined. Added in version 22.4.

An object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined.

Added in version 22.4.

direct_messages_topic_id (int, optional) – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat. Added in version 22.4.

Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat.

Added in version 22.4.

allow_sending_without_reply (bool, optional) – Pass True, if the message should be sent even if the specified replied-to message is not found. Mutually exclusive with reply_parameters, which this is a convenience parameter for Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument. Changed in version 21.0: This argument is now a keyword-only argument.

Pass True, if the message should be sent even if the specified replied-to message is not found. Mutually exclusive with reply_parameters, which this is a convenience parameter for

Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument.

Changed in version 21.0: This argument is now a keyword-only argument.

reply_to_message_id (int, optional) – If the message is a reply, ID of the original message. Mutually exclusive with reply_parameters, which this is a convenience parameter for Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument. Changed in version 21.0: This argument is now a keyword-only argument.

If the message is a reply, ID of the original message. Mutually exclusive with reply_parameters, which this is a convenience parameter for

Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument.

Changed in version 21.0: This argument is now a keyword-only argument.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, the sent Message is returned.

telegram.error.TelegramError –

Use this method to send point on the map.

You can either supply a latitude and longitude or a location.

telegram.Chat.send_location()

telegram.ChatFullInfo.send_location()

telegram.Message.reply_location()

telegram.User.send_location()

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername).

latitude (float, optional) – Latitude of location.

longitude (float, optional) – Longitude of location.

horizontal_accuracy (int, optional) – The radius of uncertainty for the location, measured in meters; 0-1500.

live_period (int | datetime.timedelta, optional) – Period in seconds for which the location will be updated, should be between 60 and 86400, or 2147483647 for live locations that can be edited indefinitely. Changed in version 21.11: datetime.timedelta objects are accepted in addition to plain int values.

Period in seconds for which the location will be updated, should be between 60 and 86400, or 2147483647 for live locations that can be edited indefinitely.

Changed in version 21.11: datetime.timedelta objects are accepted in addition to plain int values.

heading (int, optional) – For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified.

proximity_alert_radius (int, optional) – For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified.

disable_notification (bool, optional) – Sends the message silently. Users will receive a notification with no sound.

protect_content (bool, optional) – Protects the contents of the sent message from forwarding and saving. Added in version 13.10.

Protects the contents of the sent message from forwarding and saving.

Added in version 13.10.

message_thread_id (int, optional) – Unique identifier for the target message thread (topic) of the forum; for forum supergroups only. Added in version 20.0.

Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.

Added in version 20.0.

reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply, optional) – Additional interface options. An object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.

reply_parameters (telegram.ReplyParameters, optional) – Description of the message to reply to. Added in version 20.8.

Description of the message to reply to.

Added in version 20.8.

business_connection_id (str, optional) – Unique identifier of the business connection on behalf of which the message will be sent. Added in version 21.1.

Unique identifier of the business connection on behalf of which the message will be sent.

Added in version 21.1.

message_effect_id (str, optional) – Unique identifier of the message effect to be added to the message; for private chats only. Added in version 21.3.

Unique identifier of the message effect to be added to the message; for private chats only.

Added in version 21.3.

allow_paid_broadcast (bool, optional) – Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance. Added in version 21.7.

Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance.

Added in version 21.7.

suggested_post_parameters (telegram.SuggestedPostParameters, optional) – An object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined. Added in version 22.4.

An object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined.

Added in version 22.4.

direct_messages_topic_id (int, optional) – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat. Added in version 22.4.

Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat.

Added in version 22.4.

allow_sending_without_reply (bool, optional) – Pass True, if the message should be sent even if the specified replied-to message is not found. Mutually exclusive with reply_parameters, which this is a convenience parameter for Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument. Changed in version 21.0: This argument is now a keyword-only argument.

Pass True, if the message should be sent even if the specified replied-to message is not found. Mutually exclusive with reply_parameters, which this is a convenience parameter for

Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument.

Changed in version 21.0: This argument is now a keyword-only argument.

reply_to_message_id (int, optional) – If the message is a reply, ID of the original message. Mutually exclusive with reply_parameters, which this is a convenience parameter for Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument. Changed in version 21.0: This argument is now a keyword-only argument.

If the message is a reply, ID of the original message. Mutually exclusive with reply_parameters, which this is a convenience parameter for

Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument.

Changed in version 21.0: This argument is now a keyword-only argument.

location (telegram.Location, optional) – The location to send.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, the sent Message is returned.

telegram.error.TelegramError –

Use this method to send a group of photos, videos, documents or audios as an album. Documents and audio files can be only grouped in an album with messages of the same type.

If you supply a caption (along with either parse_mode or caption_entities), then items in media must have no captions, and vice versa.

Working with Files and Media

telegram.Chat.send_media_group()

telegram.ChatFullInfo.send_media_group()

telegram.Message.reply_media_group()

telegram.User.send_media_group()

Changed in version 20.0: Returns a tuple instead of a list.

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername).

media (Sequence[telegram.InputMediaAudio, telegram.InputMediaDocument, telegram.InputMediaPhoto, telegram.InputMediaVideo]) – An array describing messages to be sent, must include 2- 10 items. Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list.

An array describing messages to be sent, must include 2- 10 items.

Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list.

disable_notification (bool, optional) – Sends the message silently. Users will receive a notification with no sound.

protect_content (bool, optional) – Protects the contents of the sent message from forwarding and saving. Added in version 13.10.

Protects the contents of the sent message from forwarding and saving.

Added in version 13.10.

message_thread_id (int, optional) – Unique identifier for the target message thread (topic) of the forum; for forum supergroups only. Added in version 20.0.

Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.

Added in version 20.0.

reply_parameters (telegram.ReplyParameters, optional) – Description of the message to reply to. Added in version 20.8.

Description of the message to reply to.

Added in version 20.8.

business_connection_id (str, optional) – Unique identifier of the business connection on behalf of which the message will be sent. Added in version 21.1.

Unique identifier of the business connection on behalf of which the message will be sent.

Added in version 21.1.

message_effect_id (str, optional) – Unique identifier of the message effect to be added to the message; for private chats only. Added in version 21.3.

Unique identifier of the message effect to be added to the message; for private chats only.

Added in version 21.3.

allow_paid_broadcast (bool, optional) – Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance. Added in version 21.7.

Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance.

Added in version 21.7.

direct_messages_topic_id (int, optional) – Identifier of the direct messages topic to which the messages will be sent; required if the messages are sent to a direct messages chat. Added in version 22.4.

Identifier of the direct messages topic to which the messages will be sent; required if the messages are sent to a direct messages chat.

Added in version 22.4.

allow_sending_without_reply (bool, optional) – Pass True, if the message should be sent even if the specified replied-to message is not found. Mutually exclusive with reply_parameters, which this is a convenience parameter for Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument. Changed in version 21.0: This argument is now a keyword-only argument.

Pass True, if the message should be sent even if the specified replied-to message is not found. Mutually exclusive with reply_parameters, which this is a convenience parameter for

Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument.

Changed in version 21.0: This argument is now a keyword-only argument.

reply_to_message_id (int, optional) – If the message is a reply, ID of the original message. Mutually exclusive with reply_parameters, which this is a convenience parameter for Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument. Changed in version 21.0: This argument is now a keyword-only argument.

If the message is a reply, ID of the original message. Mutually exclusive with reply_parameters, which this is a convenience parameter for

Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument.

Changed in version 21.0: This argument is now a keyword-only argument.

caption (str, optional) – Caption that will be added to the first element of media, so that it will be used as caption for the whole media group. Defaults to None. Added in version 20.0.

Caption that will be added to the first element of media, so that it will be used as caption for the whole media group. Defaults to None.

Added in version 20.0.

parse_mode (str | None, optional) – Parse mode for caption. See the constants in telegram.constants.ParseMode for the available modes. Added in version 20.0.

Parse mode for caption. See the constants in telegram.constants.ParseMode for the available modes.

Added in version 20.0.

caption_entities (Sequence[telegram.MessageEntity], optional) – List of special entities for caption, which can be specified instead of parse_mode. Defaults to None. Added in version 20.0.

List of special entities for caption, which can be specified instead of parse_mode. Defaults to None.

Added in version 20.0.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. By default, 20 seconds are used as write timeout. Changed in version 22.0: The default value changed to DEFAULT_NONE.

Value to pass to telegram.request.BaseRequest.post.write_timeout. By default, 20 seconds are used as write timeout.

Changed in version 22.0: The default value changed to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

An array of the sent Messages.

tuple[telegram.Message]

telegram.error.TelegramError –

Use this method to send text messages.

telegram.Chat.send_message()

telegram.ChatFullInfo.send_message()

telegram.Message.reply_html()

telegram.Message.reply_markdown_v2()

telegram.Message.reply_markdown()

telegram.Message.reply_text()

telegram.User.send_message()

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername).

text (str) – Text of the message to be sent. Max 4096 characters after entities parsing.

parse_mode (str) – Mode for parsing entities. See telegram.constants.ParseMode and formatting options for more details.

entities (Sequence[telegram.MessageEntity], optional) – Sequence of special entities that appear in message text, which can be specified instead of parse_mode. Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list.

Sequence of special entities that appear in message text, which can be specified instead of parse_mode.

Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list.

link_preview_options (LinkPreviewOptions, optional) – Link preview generation options for the message. Mutually exclusive with disable_web_page_preview. Added in version 20.8.

Link preview generation options for the message. Mutually exclusive with disable_web_page_preview.

Added in version 20.8.

disable_notification (bool, optional) – Sends the message silently. Users will receive a notification with no sound.

protect_content (bool, optional) – Protects the contents of the sent message from forwarding and saving. Added in version 13.10.

Protects the contents of the sent message from forwarding and saving.

Added in version 13.10.

reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply, optional) – Additional interface options. An object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.

message_thread_id (int, optional) – Unique identifier for the target message thread (topic) of the forum; for forum supergroups only. Added in version 20.0.

Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.

Added in version 20.0.

reply_parameters (telegram.ReplyParameters, optional) – Description of the message to reply to. Added in version 20.8.

Description of the message to reply to.

Added in version 20.8.

business_connection_id (str, optional) – Unique identifier of the business connection on behalf of which the message will be sent. Added in version 21.1.

Unique identifier of the business connection on behalf of which the message will be sent.

Added in version 21.1.

message_effect_id (str, optional) – Unique identifier of the message effect to be added to the message; for private chats only. Added in version 21.3.

Unique identifier of the message effect to be added to the message; for private chats only.

Added in version 21.3.

allow_paid_broadcast (bool, optional) – Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance. Added in version 21.7.

Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance.

Added in version 21.7.

suggested_post_parameters (telegram.SuggestedPostParameters, optional) – An object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined. Added in version 22.4.

An object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined.

Added in version 22.4.

direct_messages_topic_id (int, optional) – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat. Added in version 22.4.

Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat.

Added in version 22.4.

allow_sending_without_reply (bool, optional) – Pass True, if the message should be sent even if the specified replied-to message is not found. Mutually exclusive with reply_parameters, which this is a convenience parameter for Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument. Changed in version 21.0: This argument is now a keyword-only argument.

Pass True, if the message should be sent even if the specified replied-to message is not found. Mutually exclusive with reply_parameters, which this is a convenience parameter for

Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument.

Changed in version 21.0: This argument is now a keyword-only argument.

reply_to_message_id (int, optional) – If the message is a reply, ID of the original message. Mutually exclusive with reply_parameters, which this is a convenience parameter for Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument. Changed in version 21.0: This argument is now a keyword-only argument.

If the message is a reply, ID of the original message. Mutually exclusive with reply_parameters, which this is a convenience parameter for

Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument.

Changed in version 21.0: This argument is now a keyword-only argument.

disable_web_page_preview (bool, optional) – Disables link previews for links in this message. Convenience parameter for setting link_preview_options. Mutually exclusive with link_preview_options. Changed in version 20.8: Bot API 7.0 introduced link_preview_options replacing this argument. PTB will automatically convert this argument to that one, but for advanced options, please use link_preview_options directly. Changed in version 21.0: This argument is now a keyword-only argument.

Disables link previews for links in this message. Convenience parameter for setting link_preview_options. Mutually exclusive with link_preview_options.

Changed in version 20.8: Bot API 7.0 introduced link_preview_options replacing this argument. PTB will automatically convert this argument to that one, but for advanced options, please use link_preview_options directly.

Changed in version 21.0: This argument is now a keyword-only argument.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, the sent message is returned.

ValueError – If both disable_web_page_preview and link_preview_options are passed.

telegram.error.TelegramError – For other errors.

Use this method to send paid media.

telegram.Chat.send_paid_media()

telegram.ChatFullInfo.send_paid_media()

telegram.Message.reply_paid_media()

Added in version 21.4.

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername). If the chat is a channel, all Telegram Star proceeds from this media will be credited to the chat’s balance. Otherwise, they will be credited to the bot’s balance.

star_count (int) – The number of Telegram Stars that must be paid to buy access to the media; 1 - 10000.

media (Sequence[telegram.InputPaidMedia]) – A list describing the media to be sent; up to 10 items.

payload (str, optional) – Bot-defined paid media payload, 0-128 bytes. This will not be displayed to the user, use it for your internal processes. Added in version 21.6.

Bot-defined paid media payload, 0-128 bytes. This will not be displayed to the user, use it for your internal processes.

Added in version 21.6.

caption (str, optional) – Caption of the media to be sent, 0-1024 characters.

parse_mode (str, optional) – Mode for parsing entities. See telegram.constants.ParseMode and formatting options for more details.

caption_entities (Sequence[telegram.MessageEntity], optional) – Sequence of special entities that appear in the caption, which can be specified instead of parse_mode.

show_caption_above_media (bool, optional) – Pass True, if the caption must be shown above the message media.

disable_notification (bool, optional) – Sends the message silently. Users will receive a notification with no sound.

protect_content (bool, optional) – Protects the contents of the sent message from forwarding and saving.

reply_parameters (telegram.ReplyParameters, optional) – Description of the message to reply to.

reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply, optional) – Additional interface options. An object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.

business_connection_id (str, optional) – Unique identifier of the business connection on behalf of which the message will be sent. Added in version 21.5.

Unique identifier of the business connection on behalf of which the message will be sent.

Added in version 21.5.

allow_paid_broadcast (bool, optional) – Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance. Added in version 21.7.

Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance.

Added in version 21.7.

suggested_post_parameters (telegram.SuggestedPostParameters, optional) – An object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined. Added in version 22.4.

An object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined.

Added in version 22.4.

direct_messages_topic_id (int, optional) – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat. Added in version 22.4.

Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat.

Added in version 22.4.

message_thread_id (int, optional) – Unique identifier for the target message thread (topic) of the forum; for forum supergroups only. Added in version 22.4.

Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.

Added in version 22.4.

allow_sending_without_reply (bool, optional) – Pass True, if the message should be sent even if the specified replied-to message is not found. Mutually exclusive with reply_parameters, which this is a convenience parameter for

reply_to_message_id (int, optional) – If the message is a reply, ID of the original message. Mutually exclusive with reply_parameters, which this is a convenience parameter for

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, the sent message is returned.

telegram.error.TelegramError –

Use this method to send photos.

Working with Files and Media

telegram.Chat.send_photo()

telegram.ChatFullInfo.send_photo()

telegram.Message.reply_photo()

telegram.User.send_photo()

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername).

photo (str | file object | InputFile | bytes | pathlib.Path | telegram.PhotoSize) – Photo to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one. To upload a file, you can either pass a file object (e.g. open("filename", "rb")), the file contents as bytes or the path of the file (as string or pathlib.Path object). In the latter case, the file contents will either be read as bytes or the file path will be passed to Telegram, depending on the local_mode setting. Lastly you can pass an existing telegram.PhotoSize object to send. Caution The photo must be at most 10MB in size. The photo’s width and height must not exceed 10000 in total. Width and height ratio must be at most 20. Changed in version 13.2: Accept bytes as input. Changed in version 20.0: File paths as input is also accepted for bots not running in local_mode.

Photo to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one. To upload a file, you can either pass a file object (e.g. open("filename", "rb")), the file contents as bytes or the path of the file (as string or pathlib.Path object). In the latter case, the file contents will either be read as bytes or the file path will be passed to Telegram, depending on the local_mode setting. Lastly you can pass an existing telegram.PhotoSize object to send.

The photo must be at most 10MB in size.

The photo’s width and height must not exceed 10000 in total.

Width and height ratio must be at most 20.

Changed in version 13.2: Accept bytes as input.

Changed in version 20.0: File paths as input is also accepted for bots not running in local_mode.

caption (str, optional) – Photo caption (may also be used when resending photos by file_id), 0-1024 characters after entities parsing.

parse_mode (str, optional) – Mode for parsing entities. See telegram.constants.ParseMode and formatting options for more details.

caption_entities (Sequence[telegram.MessageEntity], optional) – Sequence of special entities that appear in the caption, which can be specified instead of parse_mode. Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list.

Sequence of special entities that appear in the caption, which can be specified instead of parse_mode.

Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list.

disable_notification (bool, optional) – Sends the message silently. Users will receive a notification with no sound.

protect_content (bool, optional) – Protects the contents of the sent message from forwarding and saving. Added in version 13.10.

Protects the contents of the sent message from forwarding and saving.

Added in version 13.10.

message_thread_id (int, optional) – Unique identifier for the target message thread (topic) of the forum; for forum supergroups only. Added in version 20.0.

Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.

Added in version 20.0.

reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply, optional) – Additional interface options. An object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.

has_spoiler (bool, optional) – Pass True if the photo needs to be covered with a spoiler animation. Added in version 20.0.

Pass True if the photo needs to be covered with a spoiler animation.

Added in version 20.0.

reply_parameters (telegram.ReplyParameters, optional) – Description of the message to reply to. Added in version 20.8.

Description of the message to reply to.

Added in version 20.8.

business_connection_id (str, optional) – Unique identifier of the business connection on behalf of which the message will be sent. Added in version 21.1.

Unique identifier of the business connection on behalf of which the message will be sent.

Added in version 21.1.

message_effect_id (str, optional) – Unique identifier of the message effect to be added to the message; for private chats only. Added in version 21.3.

Unique identifier of the message effect to be added to the message; for private chats only.

Added in version 21.3.

allow_paid_broadcast (bool, optional) – Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance. Added in version 21.7.

Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance.

Added in version 21.7.

show_caption_above_media (bool, optional) – Pass True, if the caption must be shown above the message media. Added in version 21.3.

Pass True, if the caption must be shown above the message media.

Added in version 21.3.

suggested_post_parameters (telegram.SuggestedPostParameters, optional) – An object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined. Added in version 22.4.

An object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined.

Added in version 22.4.

direct_messages_topic_id (int, optional) – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat. Added in version 22.4.

Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat.

Added in version 22.4.

allow_sending_without_reply (bool, optional) – Pass True, if the message should be sent even if the specified replied-to message is not found. Mutually exclusive with reply_parameters, which this is a convenience parameter for Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument. Changed in version 21.0: This argument is now a keyword-only argument.

Pass True, if the message should be sent even if the specified replied-to message is not found. Mutually exclusive with reply_parameters, which this is a convenience parameter for

Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument.

Changed in version 21.0: This argument is now a keyword-only argument.

reply_to_message_id (int, optional) – If the message is a reply, ID of the original message. Mutually exclusive with reply_parameters, which this is a convenience parameter for Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument. Changed in version 21.0: This argument is now a keyword-only argument.

If the message is a reply, ID of the original message. Mutually exclusive with reply_parameters, which this is a convenience parameter for

Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument.

Changed in version 21.0: This argument is now a keyword-only argument.

filename (str, optional) – Custom file name for the photo, when uploading a new file. Convenience parameter, useful e.g. when sending files generated by the tempfile module. Added in version 13.1.

Custom file name for the photo, when uploading a new file. Convenience parameter, useful e.g. when sending files generated by the tempfile module.

Added in version 13.1.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. By default, 20 seconds are used as write timeout. Changed in version 22.0: The default value changed to DEFAULT_NONE.

Value to pass to telegram.request.BaseRequest.post.write_timeout. By default, 20 seconds are used as write timeout.

Changed in version 22.0: The default value changed to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, the sent Message is returned.

telegram.error.TelegramError –

Use this method to send a native poll.

telegram.Chat.send_poll()

telegram.ChatFullInfo.send_poll()

telegram.Message.reply_poll()

telegram.User.send_poll()

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername).

question (str) – Poll question, 1- 300 characters.

options (Sequence[str | telegram.InputPollOption]) – Sequence of 2- 12 answer options. Each option may either be a string with 1- 100 characters or an InputPollOption object. Strings are converted to InputPollOption objects automatically. Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list. Changed in version 21.2: Bot API 7.3 adds support for InputPollOption objects.

Sequence of 2- 12 answer options. Each option may either be a string with 1- 100 characters or an InputPollOption object. Strings are converted to InputPollOption objects automatically.

Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list.

Changed in version 21.2: Bot API 7.3 adds support for InputPollOption objects.

is_anonymous (bool, optional) – True, if the poll needs to be anonymous, defaults to True.

type (str, optional) – Poll type, 'quiz' or 'regular', defaults to 'regular'.

allows_multiple_answers (bool, optional) – True, if the poll allows multiple answers, ignored for polls in quiz mode, defaults to False.

correct_option_id (int, optional) – 0-based identifier of the correct answer option, required for polls in quiz mode.

explanation (str, optional) – Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters with at most 2 line feeds after entities parsing.

explanation_parse_mode (str, optional) – Mode for parsing entities in the explanation. See the constants in telegram.constants.ParseMode for the available modes.

explanation_entities (Sequence[telegram.MessageEntity], optional) – Sequence of special entities that appear in message text, which can be specified instead of explanation_parse_mode. Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list.

Sequence of special entities that appear in message text, which can be specified instead of explanation_parse_mode.

Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list.

open_period (int | datetime.timedelta, optional) – Amount of time in seconds the poll will be active after creation, 5- 600. Can’t be used together with close_date. Changed in version 21.11: datetime.timedelta objects are accepted in addition to plain int values.

Amount of time in seconds the poll will be active after creation, 5- 600. Can’t be used together with close_date.

Changed in version 21.11: datetime.timedelta objects are accepted in addition to plain int values.

close_date (int | datetime.datetime, optional) – Point in time (Unix timestamp) when the poll will be automatically closed. Must be at least 5 and no more than 600 seconds in the future. Can’t be used together with open_period. For timezone naive datetime.datetime objects, the default timezone of the bot will be used, which is UTC unless telegram.ext.Defaults.tzinfo is used.

is_closed (bool, optional) – Pass True, if the poll needs to be immediately closed. This can be useful for poll preview.

disable_notification (bool, optional) – Sends the message silently. Users will receive a notification with no sound.

protect_content (bool, optional) – Protects the contents of the sent message from forwarding and saving. Added in version 13.10.

Protects the contents of the sent message from forwarding and saving.

Added in version 13.10.

message_thread_id (int, optional) – Unique identifier for the target message thread (topic) of the forum; for forum supergroups only. Added in version 20.0.

Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.

Added in version 20.0.

reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply, optional) – Additional interface options. An object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.

reply_parameters (telegram.ReplyParameters, optional) – Description of the message to reply to. Added in version 20.8.

Description of the message to reply to.

Added in version 20.8.

business_connection_id (str, optional) – Unique identifier of the business connection on behalf of which the message will be sent. Added in version 21.1.

Unique identifier of the business connection on behalf of which the message will be sent.

Added in version 21.1.

question_parse_mode (str, optional) – Mode for parsing entities in the question. See the constants in telegram.constants.ParseMode for the available modes. Currently, only custom emoji entities are allowed. Added in version 21.2.

Mode for parsing entities in the question. See the constants in telegram.constants.ParseMode for the available modes. Currently, only custom emoji entities are allowed.

Added in version 21.2.

question_entities (Sequence[telegram.Message], optional) – Special entities that appear in the poll question. It can be specified instead of question_parse_mode. Added in version 21.2.

Special entities that appear in the poll question. It can be specified instead of question_parse_mode.

Added in version 21.2.

message_effect_id (str, optional) – Unique identifier of the message effect to be added to the message; for private chats only. Added in version 21.3.

Unique identifier of the message effect to be added to the message; for private chats only.

Added in version 21.3.

allow_paid_broadcast (bool, optional) – Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance. Added in version 21.7.

Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance.

Added in version 21.7.

allow_sending_without_reply (bool, optional) – Pass True, if the message should be sent even if the specified replied-to message is not found. Mutually exclusive with reply_parameters, which this is a convenience parameter for Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument. Changed in version 21.0: This argument is now a keyword-only argument.

Pass True, if the message should be sent even if the specified replied-to message is not found. Mutually exclusive with reply_parameters, which this is a convenience parameter for

Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument.

Changed in version 21.0: This argument is now a keyword-only argument.

reply_to_message_id (int, optional) – If the message is a reply, ID of the original message. Mutually exclusive with reply_parameters, which this is a convenience parameter for Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument. Changed in version 21.0: This argument is now a keyword-only argument.

If the message is a reply, ID of the original message. Mutually exclusive with reply_parameters, which this is a convenience parameter for

Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument.

Changed in version 21.0: This argument is now a keyword-only argument.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, the sent Message is returned.

telegram.error.TelegramError –

Use this method to send static .WEBP, animated .TGS, or video .WEBM stickers.

Working with Files and Media

telegram.Chat.send_sticker()

telegram.ChatFullInfo.send_sticker()

telegram.Message.reply_sticker()

telegram.User.send_sticker()

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername).

sticker (str | file object | InputFile | bytes | pathlib.Path | telegram.Sticker) – Sticker to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one. To upload a file, you can either pass a file object (e.g. open("filename", "rb")), the file contents as bytes or the path of the file (as string or pathlib.Path object). In the latter case, the file contents will either be read as bytes or the file path will be passed to Telegram, depending on the local_mode setting. Video stickers can only be sent by a file_id. Video and animated stickers can’t be sent via an HTTP URL. Lastly you can pass an existing telegram.Sticker object to send. Changed in version 13.2: Accept bytes as input. Changed in version 20.0: File paths as input is also accepted for bots not running in local_mode.

Sticker to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one. To upload a file, you can either pass a file object (e.g. open("filename", "rb")), the file contents as bytes or the path of the file (as string or pathlib.Path object). In the latter case, the file contents will either be read as bytes or the file path will be passed to Telegram, depending on the local_mode setting. Video stickers can only be sent by a file_id. Video and animated stickers can’t be sent via an HTTP URL.

Lastly you can pass an existing telegram.Sticker object to send.

Changed in version 13.2: Accept bytes as input.

Changed in version 20.0: File paths as input is also accepted for bots not running in local_mode.

emoji (str, optional) – Emoji associated with the sticker; only for just uploaded stickers Added in version 20.2.

Emoji associated with the sticker; only for just uploaded stickers

Added in version 20.2.

disable_notification (bool, optional) – Sends the message silently. Users will receive a notification with no sound.

protect_content (bool, optional) – Protects the contents of the sent message from forwarding and saving. Added in version 13.10.

Protects the contents of the sent message from forwarding and saving.

Added in version 13.10.

message_thread_id (int, optional) – Unique identifier for the target message thread (topic) of the forum; for forum supergroups only. Added in version 20.0.

Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.

Added in version 20.0.

reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply, optional) – Additional interface options. An object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.

reply_parameters (telegram.ReplyParameters, optional) – Description of the message to reply to. Added in version 20.8.

Description of the message to reply to.

Added in version 20.8.

business_connection_id (str, optional) – Unique identifier of the business connection on behalf of which the message will be sent. Added in version 21.1.

Unique identifier of the business connection on behalf of which the message will be sent.

Added in version 21.1.

message_effect_id (str, optional) – Unique identifier of the message effect to be added to the message; for private chats only. Added in version 21.3.

Unique identifier of the message effect to be added to the message; for private chats only.

Added in version 21.3.

allow_paid_broadcast (bool, optional) – Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance. Added in version 21.7.

Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance.

Added in version 21.7.

suggested_post_parameters (telegram.SuggestedPostParameters, optional) – An object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined. Added in version 22.4.

An object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined.

Added in version 22.4.

direct_messages_topic_id (int, optional) – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat. Added in version 22.4.

Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat.

Added in version 22.4.

allow_sending_without_reply (bool, optional) – Pass True, if the message should be sent even if the specified replied-to message is not found. Mutually exclusive with reply_parameters, which this is a convenience parameter for Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument. Changed in version 21.0: This argument is now a keyword-only argument.

Pass True, if the message should be sent even if the specified replied-to message is not found. Mutually exclusive with reply_parameters, which this is a convenience parameter for

Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument.

Changed in version 21.0: This argument is now a keyword-only argument.

reply_to_message_id (int, optional) – If the message is a reply, ID of the original message. Mutually exclusive with reply_parameters, which this is a convenience parameter for Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument. Changed in version 21.0: This argument is now a keyword-only argument.

If the message is a reply, ID of the original message. Mutually exclusive with reply_parameters, which this is a convenience parameter for

Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument.

Changed in version 21.0: This argument is now a keyword-only argument.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. By default, 20 seconds are used as write timeout. Changed in version 22.0: The default value changed to DEFAULT_NONE.

Value to pass to telegram.request.BaseRequest.post.write_timeout. By default, 20 seconds are used as write timeout.

Changed in version 22.0: The default value changed to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, the sent Message is returned.

telegram.error.TelegramError –

Use this method to send information about a venue.

You can either supply venue, or latitude, longitude, title and address and optionally foursquare_id and foursquare_type or optionally google_place_id and google_place_type.

Foursquare details and Google Place details are mutually exclusive. However, this behaviour is undocumented and might be changed by Telegram.

telegram.Chat.send_venue()

telegram.ChatFullInfo.send_venue()

telegram.Message.reply_venue()

telegram.User.send_venue()

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername).

latitude (float, optional) – Latitude of venue.

longitude (float, optional) – Longitude of venue.

title (str, optional) – Name of the venue.

address (str, optional) – Address of the venue.

foursquare_id (str, optional) – Foursquare identifier of the venue.

foursquare_type (str, optional) – Foursquare type of the venue, if known. (For example, “arts_entertainment/default”, “arts_entertainment/aquarium” or “food/icecream”.)

google_place_id (str, optional) – Google Places identifier of the venue.

google_place_type (str, optional) – Google Places type of the venue. (See supported types.)

disable_notification (bool, optional) – Sends the message silently. Users will receive a notification with no sound.

protect_content (bool, optional) – Protects the contents of the sent message from forwarding and saving. Added in version 13.10.

Protects the contents of the sent message from forwarding and saving.

Added in version 13.10.

message_thread_id (int, optional) – Unique identifier for the target message thread (topic) of the forum; for forum supergroups only. Added in version 20.0.

Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.

Added in version 20.0.

reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply, optional) – Additional interface options. An object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.

reply_parameters (telegram.ReplyParameters, optional) – Description of the message to reply to. Added in version 20.8.

Description of the message to reply to.

Added in version 20.8.

business_connection_id (str, optional) – Unique identifier of the business connection on behalf of which the message will be sent. Added in version 21.1.

Unique identifier of the business connection on behalf of which the message will be sent.

Added in version 21.1.

message_effect_id (str, optional) – Unique identifier of the message effect to be added to the message; for private chats only. Added in version 21.3.

Unique identifier of the message effect to be added to the message; for private chats only.

Added in version 21.3.

allow_paid_broadcast (bool, optional) – Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance. Added in version 21.7.

Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance.

Added in version 21.7.

suggested_post_parameters (telegram.SuggestedPostParameters, optional) – An object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined. Added in version 22.4.

An object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined.

Added in version 22.4.

direct_messages_topic_id (int, optional) – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat. Added in version 22.4.

Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat.

Added in version 22.4.

allow_sending_without_reply (bool, optional) – Pass True, if the message should be sent even if the specified replied-to message is not found. Mutually exclusive with reply_parameters, which this is a convenience parameter for Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument. Changed in version 21.0: This argument is now a keyword-only argument.

Pass True, if the message should be sent even if the specified replied-to message is not found. Mutually exclusive with reply_parameters, which this is a convenience parameter for

Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument.

Changed in version 21.0: This argument is now a keyword-only argument.

reply_to_message_id (int, optional) – If the message is a reply, ID of the original message. Mutually exclusive with reply_parameters, which this is a convenience parameter for Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument. Changed in version 21.0: This argument is now a keyword-only argument.

If the message is a reply, ID of the original message. Mutually exclusive with reply_parameters, which this is a convenience parameter for

Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument.

Changed in version 21.0: This argument is now a keyword-only argument.

venue (telegram.Venue, optional) – The venue to send.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, the sent Message is returned.

telegram.error.TelegramError –

Use this method to send video files, Telegram clients support mp4 videos (other formats may be sent as Document).

Bots can currently send video files of up to 50 MB in size, this limit may be changed in the future.

thumbnail will be ignored for small video files, for which Telegram can easily generate thumbnails. However, this behaviour is undocumented and might be changed by Telegram.

Working with Files and Media

telegram.Chat.send_video()

telegram.ChatFullInfo.send_video()

telegram.Message.reply_video()

telegram.User.send_video()

Changed in version 20.5: Removed deprecated argument thumb. Use thumbnail instead.

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername).

video (str | file object | InputFile | bytes | pathlib.Path | telegram.Video) – Video file to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one. To upload a file, you can either pass a file object (e.g. open("filename", "rb")), the file contents as bytes or the path of the file (as string or pathlib.Path object). In the latter case, the file contents will either be read as bytes or the file path will be passed to Telegram, depending on the local_mode setting. Lastly you can pass an existing telegram.Video object to send. Changed in version 13.2: Accept bytes as input. Changed in version 20.0: File paths as input is also accepted for bots not running in local_mode.

Video file to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one. To upload a file, you can either pass a file object (e.g. open("filename", "rb")), the file contents as bytes or the path of the file (as string or pathlib.Path object). In the latter case, the file contents will either be read as bytes or the file path will be passed to Telegram, depending on the local_mode setting. Lastly you can pass an existing telegram.Video object to send.

Changed in version 13.2: Accept bytes as input.

Changed in version 20.0: File paths as input is also accepted for bots not running in local_mode.

duration (int | datetime.timedelta, optional) – Duration of sent video in seconds. Changed in version 21.11: datetime.timedelta objects are accepted in addition to plain int values.

Duration of sent video in seconds.

Changed in version 21.11: datetime.timedelta objects are accepted in addition to plain int values.

width (int, optional) – Video width.

height (int, optional) – Video height.

cover (file object | bytes | pathlib.Path | str, optional) – Cover for the video in the message. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one. To upload a file, you can either pass a file object (e.g. open("filename", "rb")) or the file contents as bytes. If the bot is running in local_mode, passing the path of the file (as string or pathlib.Path object) is supported as well. Added in version 21.11.

Cover for the video in the message. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one. To upload a file, you can either pass a file object (e.g. open("filename", "rb")) or the file contents as bytes. If the bot is running in local_mode, passing the path of the file (as string or pathlib.Path object) is supported as well.

Added in version 21.11.

start_timestamp (int, optional) – Start timestamp for the video in the message. Added in version 21.11.

Start timestamp for the video in the message.

Added in version 21.11.

caption (str, optional) – Video caption (may also be used when resending videos by file_id), 0-1024 characters after entities parsing.

parse_mode (str, optional) – Mode for parsing entities. See telegram.constants.ParseMode and formatting options for more details.

caption_entities (Sequence[telegram.MessageEntity], optional) – Sequence of special entities that appear in the caption, which can be specified instead of parse_mode. Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list.

Sequence of special entities that appear in the caption, which can be specified instead of parse_mode.

Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list.

supports_streaming (bool, optional) – Pass True, if the uploaded video is suitable for streaming.

disable_notification (bool, optional) – Sends the message silently. Users will receive a notification with no sound.

protect_content (bool, optional) – Protects the contents of the sent message from forwarding and saving. Added in version 13.10.

Protects the contents of the sent message from forwarding and saving.

Added in version 13.10.

message_thread_id (int, optional) – Unique identifier for the target message thread (topic) of the forum; for forum supergroups only. Added in version 20.0.

Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.

Added in version 20.0.

reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply, optional) – Additional interface options. An object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.

has_spoiler (bool, optional) – Pass True if the video needs to be covered with a spoiler animation. Added in version 20.0.

Pass True if the video needs to be covered with a spoiler animation.

Added in version 20.0.

thumbnail (file object | bytes | pathlib.Path | str, optional) – Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail’s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file. To upload a file, you can either pass a file object (e.g. open("filename", "rb")), the file contents as bytes or the path of the file (as string or pathlib.Path object). In the latter case, the file contents will either be read as bytes or the file path will be passed to Telegram, depending on the local_mode setting. Added in version 20.2.

Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail’s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file. To upload a file, you can either pass a file object (e.g. open("filename", "rb")), the file contents as bytes or the path of the file (as string or pathlib.Path object). In the latter case, the file contents will either be read as bytes or the file path will be passed to Telegram, depending on the local_mode setting.

Added in version 20.2.

reply_parameters (telegram.ReplyParameters, optional) – Description of the message to reply to. Added in version 20.8.

Description of the message to reply to.

Added in version 20.8.

business_connection_id (str, optional) – Unique identifier of the business connection on behalf of which the message will be sent. Added in version 21.1.

Unique identifier of the business connection on behalf of which the message will be sent.

Added in version 21.1.

message_effect_id (str, optional) – Unique identifier of the message effect to be added to the message; for private chats only. Added in version 21.3.

Unique identifier of the message effect to be added to the message; for private chats only.

Added in version 21.3.

allow_paid_broadcast (bool, optional) – Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance. Added in version 21.7.

Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance.

Added in version 21.7.

show_caption_above_media (bool, optional) – Pass True, if the caption must be shown above the message media. Added in version 21.3.

Pass True, if the caption must be shown above the message media.

Added in version 21.3.

suggested_post_parameters (telegram.SuggestedPostParameters, optional) – An object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined. Added in version 22.4.

An object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined.

Added in version 22.4.

direct_messages_topic_id (int, optional) – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat. Added in version 22.4.

Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat.

Added in version 22.4.

allow_sending_without_reply (bool, optional) – Pass True, if the message should be sent even if the specified replied-to message is not found. Mutually exclusive with reply_parameters, which this is a convenience parameter for Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument. Changed in version 21.0: This argument is now a keyword-only argument.

Pass True, if the message should be sent even if the specified replied-to message is not found. Mutually exclusive with reply_parameters, which this is a convenience parameter for

Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument.

Changed in version 21.0: This argument is now a keyword-only argument.

reply_to_message_id (int, optional) – If the message is a reply, ID of the original message. Mutually exclusive with reply_parameters, which this is a convenience parameter for Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument. Changed in version 21.0: This argument is now a keyword-only argument.

If the message is a reply, ID of the original message. Mutually exclusive with reply_parameters, which this is a convenience parameter for

Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument.

Changed in version 21.0: This argument is now a keyword-only argument.

filename (str, optional) – Custom file name for the video, when uploading a new file. Convenience parameter, useful e.g. when sending files generated by the tempfile module. Added in version 13.1.

Custom file name for the video, when uploading a new file. Convenience parameter, useful e.g. when sending files generated by the tempfile module.

Added in version 13.1.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. By default, 20 seconds are used as write timeout. Changed in version 22.0: The default value changed to DEFAULT_NONE.

Value to pass to telegram.request.BaseRequest.post.write_timeout. By default, 20 seconds are used as write timeout.

Changed in version 22.0: The default value changed to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, the sent Message is returned.

telegram.error.TelegramError –

As of v.4.0, Telegram clients support rounded square mp4 videos of up to 1 minute long. Use this method to send video messages.

thumbnail will be ignored for small video files, for which Telegram can easily generate thumbnails. However, this behaviour is undocumented and might be changed by Telegram.

Working with Files and Media

telegram.Chat.send_video_note()

telegram.ChatFullInfo.send_video_note()

telegram.Message.reply_video_note()

telegram.User.send_video_note()

Changed in version 20.5: Removed deprecated argument thumb. Use thumbnail instead.

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername).

video_note (str | file object | InputFile | bytes | pathlib.Path | telegram.VideoNote) – Video note to send. Pass a file_id as String to send a video note that exists on the Telegram servers (recommended) or upload a new video using multipart/form-data. To upload a file, you can either pass a file object (e.g. open("filename", "rb")), the file contents as bytes or the path of the file (as string or pathlib.Path object). In the latter case, the file contents will either be read as bytes or the file path will be passed to Telegram, depending on the local_mode setting. Lastly you can pass an existing telegram.VideoNote object to send. Sending video notes by a URL is currently unsupported. Changed in version 13.2: Accept bytes as input. Changed in version 20.0: File paths as input is also accepted for bots not running in local_mode.

Video note to send. Pass a file_id as String to send a video note that exists on the Telegram servers (recommended) or upload a new video using multipart/form-data. To upload a file, you can either pass a file object (e.g. open("filename", "rb")), the file contents as bytes or the path of the file (as string or pathlib.Path object). In the latter case, the file contents will either be read as bytes or the file path will be passed to Telegram, depending on the local_mode setting. Lastly you can pass an existing telegram.VideoNote object to send. Sending video notes by a URL is currently unsupported.

Changed in version 13.2: Accept bytes as input.

Changed in version 20.0: File paths as input is also accepted for bots not running in local_mode.

duration (int | datetime.timedelta, optional) – Duration of sent video in seconds. Changed in version 21.11: datetime.timedelta objects are accepted in addition to plain int values.

Duration of sent video in seconds.

Changed in version 21.11: datetime.timedelta objects are accepted in addition to plain int values.

length (int, optional) – Video width and height, i.e. diameter of the video message.

disable_notification (bool, optional) – Sends the message silently. Users will receive a notification with no sound.

protect_content (bool, optional) – Protects the contents of the sent message from forwarding and saving. Added in version 13.10.

Protects the contents of the sent message from forwarding and saving.

Added in version 13.10.

message_thread_id (int, optional) – Unique identifier for the target message thread (topic) of the forum; for forum supergroups only. Added in version 20.0.

Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.

Added in version 20.0.

reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply, optional) – Additional interface options. An object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.

thumbnail (file object | bytes | pathlib.Path | str, optional) – Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail’s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file. To upload a file, you can either pass a file object (e.g. open("filename", "rb")), the file contents as bytes or the path of the file (as string or pathlib.Path object). In the latter case, the file contents will either be read as bytes or the file path will be passed to Telegram, depending on the local_mode setting. Added in version 20.2.

Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail’s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file. To upload a file, you can either pass a file object (e.g. open("filename", "rb")), the file contents as bytes or the path of the file (as string or pathlib.Path object). In the latter case, the file contents will either be read as bytes or the file path will be passed to Telegram, depending on the local_mode setting.

Added in version 20.2.

reply_parameters (telegram.ReplyParameters, optional) – Description of the message to reply to. Added in version 20.8.

Description of the message to reply to.

Added in version 20.8.

business_connection_id (str, optional) – Unique identifier of the business connection on behalf of which the message will be sent. Added in version 21.1.

Unique identifier of the business connection on behalf of which the message will be sent.

Added in version 21.1.

message_effect_id (str, optional) – Unique identifier of the message effect to be added to the message; for private chats only. Added in version 21.3.

Unique identifier of the message effect to be added to the message; for private chats only.

Added in version 21.3.

allow_paid_broadcast (bool, optional) – Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance. Added in version 21.7.

Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance.

Added in version 21.7.

suggested_post_parameters (telegram.SuggestedPostParameters, optional) – An object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined. Added in version 22.4.

An object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined.

Added in version 22.4.

direct_messages_topic_id (int, optional) – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat. Added in version 22.4.

Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat.

Added in version 22.4.

allow_sending_without_reply (bool, optional) – Pass True, if the message should be sent even if the specified replied-to message is not found. Mutually exclusive with reply_parameters, which this is a convenience parameter for Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument. Changed in version 21.0: This argument is now a keyword-only argument.

Pass True, if the message should be sent even if the specified replied-to message is not found. Mutually exclusive with reply_parameters, which this is a convenience parameter for

Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument.

Changed in version 21.0: This argument is now a keyword-only argument.

reply_to_message_id (int, optional) – If the message is a reply, ID of the original message. Mutually exclusive with reply_parameters, which this is a convenience parameter for Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument. Changed in version 21.0: This argument is now a keyword-only argument.

If the message is a reply, ID of the original message. Mutually exclusive with reply_parameters, which this is a convenience parameter for

Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument.

Changed in version 21.0: This argument is now a keyword-only argument.

filename (str, optional) – Custom file name for the video note, when uploading a new file. Convenience parameter, useful e.g. when sending files generated by the tempfile module. Added in version 13.1.

Custom file name for the video note, when uploading a new file. Convenience parameter, useful e.g. when sending files generated by the tempfile module.

Added in version 13.1.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. By default, 20 seconds are used as write timeout. Changed in version 22.0: The default value changed to DEFAULT_NONE.

Value to pass to telegram.request.BaseRequest.post.write_timeout. By default, 20 seconds are used as write timeout.

Changed in version 22.0: The default value changed to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, the sent Message is returned.

telegram.error.TelegramError –

Use this method to send audio files, if you want Telegram clients to display the file as a playable voice message. For this to work, your audio must be in an .ogg file encoded with OPUS , or in .MP3 format, or in .M4A format (other formats may be sent as Audio or Document). Bots can currently send voice messages of up to 50 MB in size, this limit may be changed in the future.

To use this method, the file must have the type audio/ogg and be no more than 1 MB in size. 1 MB- 20 MB voice notes will be sent as files.

Working with Files and Media

telegram.Chat.send_voice()

telegram.ChatFullInfo.send_voice()

telegram.Message.reply_voice()

telegram.User.send_voice()

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername).

voice (str | file object | InputFile | bytes | pathlib.Path | telegram.Voice) – Voice file to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one. To upload a file, you can either pass a file object (e.g. open("filename", "rb")), the file contents as bytes or the path of the file (as string or pathlib.Path object). In the latter case, the file contents will either be read as bytes or the file path will be passed to Telegram, depending on the local_mode setting. Lastly you can pass an existing telegram.Voice object to send. Changed in version 13.2: Accept bytes as input. Changed in version 20.0: File paths as input is also accepted for bots not running in local_mode.

Voice file to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one. To upload a file, you can either pass a file object (e.g. open("filename", "rb")), the file contents as bytes or the path of the file (as string or pathlib.Path object). In the latter case, the file contents will either be read as bytes or the file path will be passed to Telegram, depending on the local_mode setting. Lastly you can pass an existing telegram.Voice object to send.

Changed in version 13.2: Accept bytes as input.

Changed in version 20.0: File paths as input is also accepted for bots not running in local_mode.

caption (str, optional) – Voice message caption, 0-1024 characters after entities parsing.

parse_mode (str, optional) – Mode for parsing entities. See telegram.constants.ParseMode and formatting options for more details.

caption_entities (Sequence[telegram.MessageEntity], optional) – Sequence of special entities that appear in the caption, which can be specified instead of parse_mode. Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list.

Sequence of special entities that appear in the caption, which can be specified instead of parse_mode.

Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list.

duration (int | datetime.timedelta, optional) – Duration of the voice message in seconds. Changed in version 21.11: datetime.timedelta objects are accepted in addition to plain int values.

Duration of the voice message in seconds.

Changed in version 21.11: datetime.timedelta objects are accepted in addition to plain int values.

disable_notification (bool, optional) – Sends the message silently. Users will receive a notification with no sound.

protect_content (bool, optional) – Protects the contents of the sent message from forwarding and saving. Added in version 13.10.

Protects the contents of the sent message from forwarding and saving.

Added in version 13.10.

message_thread_id (int, optional) – Unique identifier for the target message thread (topic) of the forum; for forum supergroups only. Added in version 20.0.

Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.

Added in version 20.0.

reply_markup (InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply, optional) – Additional interface options. An object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.

reply_parameters (telegram.ReplyParameters, optional) – Description of the message to reply to. Added in version 20.8.

Description of the message to reply to.

Added in version 20.8.

business_connection_id (str, optional) – Unique identifier of the business connection on behalf of which the message will be sent. Added in version 21.1.

Unique identifier of the business connection on behalf of which the message will be sent.

Added in version 21.1.

message_effect_id (str, optional) – Unique identifier of the message effect to be added to the message; for private chats only. Added in version 21.3.

Unique identifier of the message effect to be added to the message; for private chats only.

Added in version 21.3.

allow_paid_broadcast (bool, optional) – Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance. Added in version 21.7.

Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot’s balance.

Added in version 21.7.

suggested_post_parameters (telegram.SuggestedPostParameters, optional) – An object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined. Added in version 22.4.

An object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined.

Added in version 22.4.

direct_messages_topic_id (int, optional) – Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat. Added in version 22.4.

Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat.

Added in version 22.4.

allow_sending_without_reply (bool, optional) – Pass True, if the message should be sent even if the specified replied-to message is not found. Mutually exclusive with reply_parameters, which this is a convenience parameter for Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument. Changed in version 21.0: This argument is now a keyword-only argument.

Pass True, if the message should be sent even if the specified replied-to message is not found. Mutually exclusive with reply_parameters, which this is a convenience parameter for

Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument.

Changed in version 21.0: This argument is now a keyword-only argument.

reply_to_message_id (int, optional) – If the message is a reply, ID of the original message. Mutually exclusive with reply_parameters, which this is a convenience parameter for Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument. Changed in version 21.0: This argument is now a keyword-only argument.

If the message is a reply, ID of the original message. Mutually exclusive with reply_parameters, which this is a convenience parameter for

Changed in version 20.8: Bot API 7.0 introduced reply_parameters replacing this argument. PTB will automatically convert this argument to that one, but you should update your code to use the new argument.

Changed in version 21.0: This argument is now a keyword-only argument.

filename (str, optional) – Custom file name for the voice, when uploading a new file. Convenience parameter, useful e.g. when sending files generated by the tempfile module. Added in version 13.1.

Custom file name for the voice, when uploading a new file. Convenience parameter, useful e.g. when sending files generated by the tempfile module.

Added in version 13.1.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. By default, 20 seconds are used as write timeout. Changed in version 22.0: The default value changed to DEFAULT_NONE.

Value to pass to telegram.request.BaseRequest.post.write_timeout. By default, 20 seconds are used as write timeout.

Changed in version 22.0: The default value changed to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, the sent Message is returned.

telegram.error.TelegramError –

Alias for set_business_account_bio()

Alias for set_business_account_gift_settings()

Alias for set_business_account_name()

Alias for set_business_account_profile_photo()

Alias for set_business_account_username()

Alias for set_chat_administrator_custom_title()

Alias for set_chat_description()

Alias for set_chat_menu_button()

Alias for set_chat_permissions()

Alias for set_chat_photo()

Alias for set_chat_sticker_set()

Alias for set_chat_title()

Alias for set_custom_emoji_sticker_set_thumbnail()

Alias for set_game_score()

Alias for set_message_reaction()

Alias for set_my_commands()

Alias for set_my_default_administrator_rights()

Alias for set_my_description()

Alias for set_my_name()

Alias for set_my_short_description()

Alias for set_passport_data_errors()

Alias for set_sticker_emoji_list()

Alias for set_sticker_keywords()

Alias for set_sticker_mask_position()

Alias for set_sticker_position_in_set()

Alias for set_sticker_set_thumbnail()

Alias for set_sticker_set_title()

Alias for set_user_emoji_status()

Alias for set_webhook()

Changes the bio of a managed business account. Requires the can_edit_bio business bot right.

Added in version 22.1.

business_connection_id (str) – Unique identifier of the business connection.

bio (str, optional) – The new value of the bio for the business account; 0-140 characters.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Changes the privacy settings pertaining to incoming gifts in a managed business account. Requires the can_change_gift_settings business bot right.

Added in version 22.1.

business_connection_id (str) – Unique identifier of the business connection

show_gift_button (bool) – Pass True, if a button for sending a gift to the user or by the business account must always be shown in the input field.

accepted_gift_types (telegram.AcceptedGiftTypes) – Types of gifts accepted by the business account.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Changes the first and last name of a managed business account. Requires the can_edit_name business bot right.

Added in version 22.1.

business_connection_id (int | str) – Unique identifier of the business connection

first_name (str) – New first name of the business account; 1- 64 characters.

last_name (str, optional) – New last name of the business account; 0-64 characters.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Changes the profile photo of a managed business account. Requires the can_edit_profile_photo business bot right.

Added in version 22.1.

business_connection_id (str) – Unique identifier of the business connection.

photo (telegram.InputProfilePhoto) – The new profile photo to set.

is_public (bool, optional) – Pass True to set the public photo, which will be visible even if the main photo is hidden by the business account’s privacy settings. An account can have only one public photo.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Changes the username of a managed business account. Requires the can_edit_username business bot right.

Added in version 22.1.

business_connection_id (str) – Unique identifier of the business connection.

username (str, optional) – New business account username; 0-32 characters.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Use this method to set a custom title for administrators promoted by the bot in a supergroup. The bot must be an administrator for this to work.

telegram.Chat.set_administrator_custom_title()

telegram.ChatFullInfo.set_administrator_custom_title()

chat_id (int | str) – Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername).

user_id (int) – Unique identifier of the target administrator.

custom_title (str) – New custom title for the administrator; 0-16 characters, emoji are not allowed.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Use this method to change the description of a group, a supergroup or a channel. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights.

telegram.Chat.set_description()

telegram.ChatFullInfo.set_description()

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername).

description (str, optional) – New chat description, 0-255 characters.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Use this method to change the bot’s menu button in a private chat, or the default menu button.

get_chat_menu_button(), telegram.Chat.get_menu_button() telegram.User.get_menu_button()

telegram.Chat.set_menu_button()

telegram.ChatFullInfo.set_menu_button()

telegram.User.set_menu_button()

Added in version 20.0.

chat_id (int, optional) – Unique identifier for the target private chat. If not specified, default bot’s menu button will be changed

menu_button (telegram.MenuButton, optional) – An object for the new bot’s menu button. Defaults to telegram.MenuButtonDefault.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

Use this method to set default chat permissions for all members. The bot must be an administrator in the group or a supergroup for this to work and must have the telegram.ChatMemberAdministrator.can_restrict_members admin rights.

telegram.Chat.set_permissions()

telegram.ChatFullInfo.set_permissions()

chat_id (int | str) – Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername).

permissions (telegram.ChatPermissions) – New default chat permissions.

use_independent_chat_permissions (bool, optional) – Pass True if chat permissions are set independently. Otherwise, the can_send_other_messages and can_add_web_page_previews permissions will imply the can_send_messages, can_send_audios, can_send_documents, can_send_photos, can_send_videos, can_send_video_notes, and can_send_voice_notes permissions; the can_send_polls permission will imply the can_send_messages permission.

Pass True if chat permissions are set independently. Otherwise, the can_send_other_messages and can_add_web_page_previews permissions will imply the can_send_messages, can_send_audios, can_send_documents, can_send_photos, can_send_videos, can_send_video_notes, and can_send_voice_notes permissions; the can_send_polls permission will imply the can_send_messages permission.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Use this method to set a new profile photo for the chat.

Photos can’t be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights.

telegram.Chat.set_photo()

telegram.ChatFullInfo.set_photo()

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername).

photo (file object | bytes | pathlib.Path) – New chat photo. To upload a file, you can either pass a file object (e.g. open("filename", "rb")), the file contents as bytes or the path of the file (as string or pathlib.Path object). In the latter case, the file contents will either be read as bytes or the file path will be passed to Telegram, depending on the local_mode setting. Changed in version 13.2: Accept bytes as input. Changed in version 20.0: File paths as input is also accepted for bots not running in local_mode.

New chat photo. To upload a file, you can either pass a file object (e.g. open("filename", "rb")), the file contents as bytes or the path of the file (as string or pathlib.Path object). In the latter case, the file contents will either be read as bytes or the file path will be passed to Telegram, depending on the local_mode setting.

Changed in version 13.2: Accept bytes as input.

Changed in version 20.0: File paths as input is also accepted for bots not running in local_mode.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. By default, 20 seconds are used as write timeout. Changed in version 22.0: The default value changed to DEFAULT_NONE.

Value to pass to telegram.request.BaseRequest.post.write_timeout. By default, 20 seconds are used as write timeout.

Changed in version 22.0: The default value changed to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Use this method to set a new group sticker set for a supergroup. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights. Use the field telegram.ChatFullInfo.can_set_sticker_set optionally returned in get_chat() requests to check if the bot can use this method.

chat_id (int | str) – Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername).

sticker_set_name (str) – Name of the sticker set to be set as the group sticker set.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

Use this method to change the title of a chat. Titles can’t be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights.

telegram.Chat.set_title()

telegram.ChatFullInfo.set_title()

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername).

title (str) – New chat title, 1- 128 characters.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Use this method to set the thumbnail of a custom emoji sticker set.

Added in version 20.2.

name (str) – Sticker set name.

custom_emoji_id (str, optional) – Custom emoji identifier of a sticker from the sticker set; pass an empty string to drop the thumbnail and use the first sticker as the thumbnail.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Use this method to set the score of the specified user in a game message.

telegram.CallbackQuery.set_game_score()

telegram.Message.set_game_score()

user_id (int) – User identifier.

score (int) – New score, must be non-negative.

force (bool, optional) – Pass True, if the high score is allowed to decrease. This can be useful when fixing mistakes or banning cheaters.

disable_edit_message (bool, optional) – Pass True, if the game message should not be automatically edited to include the current scoreboard.

chat_id (int, optional) – Required if inline_message_id is not specified. Unique identifier for the target chat.

message_id (int, optional) – Required if inline_message_id is not specified. Identifier of the sent message.

inline_message_id (str, optional) – Required if chat_id and message_id are not specified. Identifier of the inline message.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

The edited message. If the message is not an inline message , True.

telegram.error.TelegramError – If the new score is not greater than the user’s current score in the chat and force is False.

Use this method to change the chosen reactions on a message. Service messages of some types can’t be reacted to. Automatically forwarded messages from a channel to its discussion group have the same available reactions as messages in the channel. Bots can’t use paid reactions.

telegram.Chat.set_message_reaction()

telegram.ChatFullInfo.set_message_reaction()

telegram.Message.set_reaction()

Added in version 20.8.

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername).

message_id (int) – Identifier of the target message. If the message belongs to a media group, the reaction is set to the first non-deleted message in the group instead.

reaction (Sequence[telegram.ReactionType | str] | telegram.ReactionType | str, optional) – A list of reaction types to set on the message. Currently, as non-premium users, bots can set up to one reaction per message. A custom emoji reaction can be used if it is either already present on the message or explicitly allowed by chat administrators. Paid reactions can’t be used by bots. Tip Passed str values will be converted to either telegram.ReactionTypeEmoji or telegram.ReactionTypeCustomEmoji depending on whether they are listed in ReactionEmoji.

A list of reaction types to set on the message. Currently, as non-premium users, bots can set up to one reaction per message. A custom emoji reaction can be used if it is either already present on the message or explicitly allowed by chat administrators. Paid reactions can’t be used by bots.

Passed str values will be converted to either telegram.ReactionTypeEmoji or telegram.ReactionTypeCustomEmoji depending on whether they are listed in ReactionEmoji.

is_big (bool, optional) – Pass True to set the reaction with a big animation.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

bool On success, True is returned.

telegram.error.TelegramError –

Use this method to change the list of the bot’s commands. See the Telegram docs for more details about bot commands.

get_my_commands(), delete_my_commands()

commands (Sequence[BotCommand | (str, str)]) – A sequence of bot commands to be set as the list of the bot’s commands. At most 100 commands can be specified. Note If you pass in a sequence of tuple, the order of elements in each tuple must correspond to the order of positional arguments to create a BotCommand instance. Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list.

A sequence of bot commands to be set as the list of the bot’s commands. At most 100 commands can be specified.

If you pass in a sequence of tuple, the order of elements in each tuple must correspond to the order of positional arguments to create a BotCommand instance.

Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list.

scope (telegram.BotCommandScope, optional) – An object, describing scope of users for which the commands are relevant. Defaults to telegram.BotCommandScopeDefault. Added in version 13.7.

An object, describing scope of users for which the commands are relevant. Defaults to telegram.BotCommandScopeDefault.

Added in version 13.7.

language_code (str, optional) – A two-letter ISO 639-1 language code. If empty, commands will be applied to all users from the given scope, for whose language there are no dedicated commands. Added in version 13.7.

A two-letter ISO 639-1 language code. If empty, commands will be applied to all users from the given scope, for whose language there are no dedicated commands.

Added in version 13.7.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Use this method to change the default administrator rights requested by the bot when it’s added as an administrator to groups or channels. These rights will be suggested to users, but they are free to modify the list before adding the bot.

get_my_default_administrator_rights()

Added in version 20.0.

rights (telegram.ChatAdministratorRights, optional) – A telegram.ChatAdministratorRights object describing new default administrator rights. If not specified, the default administrator rights will be cleared.

for_channels (bool, optional) – Pass True to change the default administrator rights of the bot in channels. Otherwise, the default administrator rights of the bot for groups and supergroups will be changed.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

Returns True on success.

telegram.error.TelegramError –

Use this method to change the bot’s description, which is shown in the chat with the bot if the chat is empty.

Added in version 20.2.

description (str, optional) – New bot description; 0-512 characters. Pass an empty string to remove the dedicated description for the given language.

language_code (str, optional) – A two-letter ISO 639-1 language code. If empty, the description will be applied to all users for whose language there is no dedicated description.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Use this method to change the bot’s name.

Added in version 20.3.

name (str, optional) – New bot name; 0-64 characters. Pass an empty string to remove the dedicated name for the given language. Caution If language_code is not specified, a name must be specified.

New bot name; 0-64 characters. Pass an empty string to remove the dedicated name for the given language.

If language_code is not specified, a name must be specified.

language_code (str, optional) – A two-letter ISO 639-1 language code. If empty, the name will be applied to all users for whose language there is no dedicated name.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Use this method to change the bot’s short description, which is shown on the bot’s profile page and is sent together with the link when users share the bot.

Added in version 20.2.

short_description (str, optional) – New short description for the bot; 0-120 characters. Pass an empty string to remove the dedicated description for the given language.

language_code (str, optional) – A two-letter ISO 639-1 language code. If empty, the description will be applied to all users for whose language there is no dedicated description.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Informs a user that some of the Telegram Passport elements they provided contains errors. The user will not be able to re-submit their Passport to you until the errors are fixed (the contents of the field for which you returned the error must change).

Use this if the data submitted by the user doesn’t satisfy the standards your service requires for any reason. For example, if a birthday date seems invalid, a submitted document is blurry, a scan shows evidence of tampering, etc. Supply some details in the error message to make sure the user knows how to correct the issues.

user_id (int) – User identifier

errors (Sequence[PassportElementError]) – A Sequence describing the errors. Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list.

A Sequence describing the errors.

Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Use this method to change the list of emoji assigned to a regular or custom emoji sticker. The sticker must belong to a sticker set created by the bot.

Added in version 20.2.

sticker (str | Sticker) – File identifier of the sticker or the sticker object. Changed in version 21.10: Accepts also telegram.Sticker instances.

File identifier of the sticker or the sticker object.

Changed in version 21.10: Accepts also telegram.Sticker instances.

emoji_list (Sequence[str]) – A sequence of 1- 20 emoji associated with the sticker.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Use this method to change search keywords assigned to a regular or custom emoji sticker. The sticker must belong to a sticker set created by the bot.

Added in version 20.2.

sticker (str | Sticker) – File identifier of the sticker or the sticker object. Changed in version 21.10: Accepts also telegram.Sticker instances.

File identifier of the sticker or the sticker object.

Changed in version 21.10: Accepts also telegram.Sticker instances.

keywords (Sequence[str]) – A sequence of 0-20 search keywords for the sticker with total length up to 64 characters.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Use this method to change the mask position of a mask sticker. The sticker must belong to a sticker set that was created by the bot.

Added in version 20.2.

sticker (str | Sticker) – File identifier of the sticker or the sticker object. Changed in version 21.10: Accepts also telegram.Sticker instances.

File identifier of the sticker or the sticker object.

Changed in version 21.10: Accepts also telegram.Sticker instances.

mask_position (telegram.MaskPosition, optional) – A object with the position where the mask should be placed on faces. Omit the parameter to remove the mask position.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Use this method to move a sticker in a set created by the bot to a specific position.

sticker (str | Sticker) – File identifier of the sticker or the sticker object. Changed in version 21.10: Accepts also telegram.Sticker instances.

File identifier of the sticker or the sticker object.

Changed in version 21.10: Accepts also telegram.Sticker instances.

position (int) – New sticker position in the set, zero-based.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Use this method to set the thumbnail of a regular or mask sticker set. The format of the thumbnail file must match the format of the stickers in the set.

Added in version 20.2.

Changed in version 21.1: As per Bot API 7.2, the new argument format will be required, and thus the order of the arguments had to be changed.

name (str) – Sticker set name

user_id (int) – User identifier of created sticker set owner.

format (str) – Format of the added sticker, must be one of 'static' for a .WEBP or .PNG image, 'animated' for a .TGS animation, 'video' for a .WEBM video. Added in version 21.1.

Format of the added sticker, must be one of 'static' for a .WEBP or .PNG image, 'animated' for a .TGS animation, 'video' for a .WEBM video.

Added in version 21.1.

thumbnail (str | file object | InputFile | bytes | pathlib.Path, optional) – A .WEBP or .PNG image with the thumbnail, must be up to 128 kilobytes in size and have width and height of exactly 100 px, or a .TGS animation with the thumbnail up to 32 kilobytes in size; see the docs for animated sticker technical requirements, or a .WEBM video with the thumbnail up to 32 kilobytes in size; see this for video sticker technical requirements. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one. To upload a file, you can either pass a file object (e.g. open("filename", "rb")), the file contents as bytes or the path of the file (as string or pathlib.Path object). In the latter case, the file contents will either be read as bytes or the file path will be passed to Telegram, depending on the local_mode setting. Animated and video sticker set thumbnails can’t be uploaded via HTTP URL. If omitted, then the thumbnail is dropped and the first sticker is used as the thumbnail.

A .WEBP or .PNG image with the thumbnail, must be up to 128 kilobytes in size and have width and height of exactly 100 px, or a .TGS animation with the thumbnail up to 32 kilobytes in size; see the docs for animated sticker technical requirements, or a .WEBM video with the thumbnail up to 32 kilobytes in size; see this for video sticker technical requirements.

Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one. To upload a file, you can either pass a file object (e.g. open("filename", "rb")), the file contents as bytes or the path of the file (as string or pathlib.Path object). In the latter case, the file contents will either be read as bytes or the file path will be passed to Telegram, depending on the local_mode setting.

Animated and video sticker set thumbnails can’t be uploaded via HTTP URL. If omitted, then the thumbnail is dropped and the first sticker is used as the thumbnail.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Use this method to set the title of a created sticker set.

Added in version 20.2.

name (str) – Sticker set name.

title (str) – Sticker set title, 1- 64 characters.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Changes the emoji status for a given user that previously allowed the bot to manage their emoji status via the Mini App method requestEmojiStatusAccess .

Added in version 21.8.

user_id (int) – Unique identifier of the target user

emoji_status_custom_emoji_id (str, optional) – Custom emoji identifier of the emoji status to set. Pass an empty string to remove the status.

emoji_status_expiration_date (Union[int, datetime.datetime], optional) – Expiration date of the emoji status, if any, as unix timestamp or datetime.datetime object. For timezone naive datetime.datetime objects, the default timezone of the bot will be used, which is UTC unless telegram.ext.Defaults.tzinfo is used.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Use this method to specify a url and receive incoming updates via an outgoing webhook. Whenever there is an update for the bot, Telegram will send an HTTPS POST request to the specified url, containing An Update. In case of an unsuccessful request (a request with response HTTP status code <https://en.wikipedia.org/wiki/List_of_HTTP_status_codes>`_different from ``2XY`), Telegram will repeat the request and give up after a reasonable amount of attempts.

If you’d like to make sure that the Webhook was set by you, you can specify secret data in the parameter secret_token. If specified, the request will contain a header X-Telegram-Bot-Api-Secret-Token with the secret token as content.

You will not be able to receive updates using get_updates() for long as an outgoing webhook is set up.

To use a self-signed certificate, you need to upload your public key certificate using certificate parameter. Please upload as InputFile, sending a String will not work.

Ports currently supported for Webhooks: telegram.constants.SUPPORTED_WEBHOOK_PORTS.

If you’re having any trouble setting up webhooks, please check out this guide to Webhooks.

telegram.ext.Application.run_webhook(), telegram.ext.Updater.start_webhook()

url (str) – HTTPS url to send updates to. Use an empty string to remove webhook integration.

certificate (file object | bytes | pathlib.Path | str) – Upload your public key certificate so that the root certificate in use can be checked. See our self-signed guide for details. To upload a file, you can either pass a file object (e.g. open("filename", "rb")) or the file contents as bytes. If the bot is running in local_mode, passing the path of the file (as string or pathlib.Path object) is supported as well.

ip_address (str, optional) – The fixed IP address which will be used to send webhook requests instead of the IP address resolved through DNS.

max_connections (int, optional) – Maximum allowed number of simultaneous HTTPS connections to the webhook for update delivery, 1- 100. Defaults to 40. Use lower values to limit the load on your bot’s server, and higher values to increase your bot’s throughput.

allowed_updates (Sequence[str], optional) – A sequence of the types of updates you want your bot to receive. For example, specify [“message”, “edited_channel_post”, “callback_query”] to only receive updates of these types. See telegram.Update for a complete list of available update types. Specify an empty sequence to receive all updates except telegram.Update.chat_member, telegram.Update.message_reaction and telegram.Update.message_reaction_count (default). If not specified, the previous setting will be used. Please note that this parameter doesn’t affect updates created before the call to the set_webhook, so unwanted update may be received for a short period of time. Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list.

A sequence of the types of updates you want your bot to receive. For example, specify [“message”, “edited_channel_post”, “callback_query”] to only receive updates of these types. See telegram.Update for a complete list of available update types. Specify an empty sequence to receive all updates except telegram.Update.chat_member, telegram.Update.message_reaction and telegram.Update.message_reaction_count (default). If not specified, the previous setting will be used. Please note that this parameter doesn’t affect updates created before the call to the set_webhook, so unwanted update may be received for a short period of time.

Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list.

drop_pending_updates (bool, optional) – Pass True to drop all pending updates.

secret_token (str, optional) – A secret token to be sent in a header X-Telegram-Bot-Api-Secret-Token in every webhook request, 1- 256 characters. Only characters A-Z, a-z, 0-9, _ and - are allowed. The header is useful to ensure that the request comes from a webhook set by you. Added in version 20.0.

A secret token to be sent in a header X-Telegram-Bot-Api-Secret-Token in every webhook request, 1- 256 characters. Only characters A-Z, a-z, 0-9, _ and - are allowed. The header is useful to ensure that the request comes from a webhook set by you.

Added in version 20.0.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

bool On success, True is returned.

telegram.error.TelegramError –

Stop & clear resources used by this class. Currently just calls telegram.request.BaseRequest.shutdown() for the request objects used by this bot.

Added in version 20.0.

Alias for stop_message_live_location()

Alias for stop_poll()

Use this method to stop updating a live location message sent by the bot or via the bot (for inline bots) before live_period expires.

telegram.CallbackQuery.stop_message_live_location()

telegram.Message.stop_live_location()

chat_id (int | str, optional) – Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername).

message_id (int, optional) – Required if inline_message_id is not specified. Identifier of the sent message with live location to stop.

inline_message_id (str, optional) – Required if chat_id and message_id are not specified. Identifier of the inline message.

reply_markup (telegram.InlineKeyboardMarkup, optional) – An object for a new inline keyboard.

business_connection_id (str, optional) – Unique identifier of the business connection on behalf of which the message to be edited was sent Added in version 21.4.

Unique identifier of the business connection on behalf of which the message to be edited was sent

Added in version 21.4.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, if edited message is not an inline message, the edited message is returned, otherwise True is returned.

Use this method to stop a poll which was sent by the bot.

telegram.Message.stop_poll()

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername).

message_id (int) – Identifier of the original message with the poll.

reply_markup (telegram.InlineKeyboardMarkup, optional) – An object for a new message inline keyboard.

business_connection_id (str, optional) – Unique identifier of the business connection on behalf of which the message to be edited was sent Added in version 21.4.

Unique identifier of the business connection on behalf of which the message to be edited was sent

Added in version 21.4.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, the stopped Poll is returned.

telegram.error.TelegramError –

Bot’s telegram.User.supports_inline_queries attribute. Shortcut for the corresponding attribute of bot.

See telegram.TelegramObject.to_dict().

Bot’s unique authentication token.

Added in version 20.0.

Alias for transfer_business_account_stars()

Alias for transfer_gift()

Transfers Telegram Stars from the business account balance to the bot’s balance. Requires the can_transfer_stars business bot right.

Added in version 22.1.

business_connection_id (str) – Unique identifier of the business connection

star_count (int) – Number of Telegram Stars to transfer; 1-10000

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Transfers an owned unique gift to another user. Requires the can_transfer_and_upgrade_gifts business bot right. Requires can_transfer_stars business bot right if the transfer is paid.

telegram.Chat.transfer_gift()

telegram.ChatFullInfo.transfer_gift()

Added in version 22.1.

business_connection_id (str) – Unique identifier of the business connection

owned_gift_id (str) – Unique identifier of the regular gift that should be transferred.

new_owner_chat_id (int) – Unique identifier of the chat which will own the gift. The chat must be active in the last 86400 seconds.

star_count (int, optional) – The amount of Telegram Stars that will be paid for the transfer from the business account balance. If positive, then the can_transfer_stars business bot right is required.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Alias for unban_chat_member()

Alias for unban_chat_sender_chat()

Use this method to unban a previously kicked user in a supergroup or channel.

The user will not return to the group or channel automatically, but will be able to join via link, etc. The bot must be an administrator for this to work. By default, this method guarantees that after the call the user is not a member of the chat, but will be able to join it. So if the user is a member of the chat they will also be removed from the chat. If you don’t want this, use the parameter only_if_banned.

telegram.Chat.unban_member()

telegram.ChatFullInfo.unban_member()

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername).

user_id (int) – Unique identifier of the target user.

only_if_banned (bool, optional) – Do nothing if the user is not banned.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Use this method to unban a previously banned channel in a supergroup or channel. The bot must be an administrator for this to work and must have the appropriate administrator rights.

telegram.Chat.unban_chat()

telegram.Chat.unban_sender_chat()

telegram.ChatFullInfo.unban_chat()

telegram.ChatFullInfo.unban_sender_chat()

Added in version 13.9.

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername).

sender_chat_id (int) – Unique identifier of the target sender chat.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Alias for unhide_general_forum_topic()

Use this method to unhide the ‘General’ topic in a forum supergroup chat. The bot must be an administrator in the chat for this to work and must have can_manage_topics administrator rights.

telegram.Chat.unhide_general_forum_topic()

telegram.ChatFullInfo.unhide_general_forum_topic()

Added in version 20.0.

chat_id (int | str) – Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername).

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Alias for unpin_all_chat_messages()

Alias for unpin_all_forum_topic_messages()

Alias for unpin_all_general_forum_topic_messages()

Alias for unpin_chat_message()

Use this method to clear the list of pinned messages in a chat. If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have the can_pin_messages admin right in a supergroup or can_edit_messages admin right in a channel.

telegram.Chat.unpin_all_messages()

telegram.ChatFullInfo.unpin_all_messages()

telegram.User.unpin_all_messages()

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername).

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Use this method to clear the list of pinned messages in a forum topic. The bot must be an administrator in the chat for this to work and must have can_pin_messages administrator rights in the supergroup.

telegram.Chat.unpin_all_forum_topic_messages()

telegram.ChatFullInfo.unpin_all_forum_topic_messages()

telegram.Message.unpin_all_forum_topic_messages()

Added in version 20.0.

chat_id (int | str) – Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername).

message_thread_id (int) – Unique identifier for the target message thread of the forum topic.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Use this method to clear the list of pinned messages in a General forum topic. The bot must be an administrator in the chat for this to work and must have can_pin_messages administrator rights in the supergroup.

telegram.Chat.unpin_all_general_forum_topic_messages()

telegram.ChatFullInfo.unpin_all_general_forum_topic_messages()

Added in version 20.5.

chat_id (int | str) – Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername).

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Use this method to remove a message from the list of pinned messages in a chat. If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have the can_pin_messages admin right in a supergroup or can_edit_messages admin right in a channel.

telegram.Chat.unpin_message()

telegram.ChatFullInfo.unpin_message()

telegram.Message.unpin()

telegram.User.unpin_message()

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername).

message_id (int, optional) – Identifier of the message to unpin. Required if business_connection_id is specified. If not specified, the most recent pinned message (by sending date) will be unpinned.

business_connection_id (str, optional) – Unique identifier of the business connection on behalf of which the message will be unpinned. Added in version 21.5.

Unique identifier of the business connection on behalf of which the message will be unpinned.

Added in version 21.5.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Alias for upgrade_gift()

Upgrades a given regular gift to a unique gift. Requires the can_transfer_and_upgrade_gifts business bot right. Additionally requires the can_transfer_stars business bot right if the upgrade is paid.

Added in version 22.1.

business_connection_id (str) – Unique identifier of the business connection

owned_gift_id (str) – Unique identifier of the regular gift that should be upgraded to a unique one.

keep_original_details (bool, optional) – Pass True to keep the original gift text, sender and receiver in the upgraded gift

star_count (int, optional) – The amount of Telegram Stars that will be paid for the upgrade from the business account balance. If gift.prepaid_upgrade_star_count > 0, then pass 0, otherwise, the can_transfer_stars business bot right is required and telegram.Gift.upgrade_star_count must be passed.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Alias for upload_sticker_file()

Use this method to upload a file with a sticker for later use in the create_new_sticker_set() and add_sticker_to_set() methods (can be used multiple times).

Changed in version 20.5: Removed deprecated parameter png_sticker.

user_id (int) – User identifier of sticker file owner.

sticker (str | file object | InputFile | bytes | pathlib.Path) – A file with the sticker in the ".WEBP", ".PNG", ".TGS" or ".WEBM" format. See here for technical requirements . To upload a file, you can either pass a file object (e.g. open("filename", "rb")), the file contents as bytes or the path of the file (as string or pathlib.Path object). In the latter case, the file contents will either be read as bytes or the file path will be passed to Telegram, depending on the local_mode setting. Added in version 20.2.

A file with the sticker in the ".WEBP", ".PNG", ".TGS" or ".WEBM" format. See here for technical requirements . To upload a file, you can either pass a file object (e.g. open("filename", "rb")), the file contents as bytes or the path of the file (as string or pathlib.Path object). In the latter case, the file contents will either be read as bytes or the file path will be passed to Telegram, depending on the local_mode setting.

Added in version 20.2.

sticker_format (str) – Format of the sticker. Must be one of telegram.constants.StickerFormat.STATIC, telegram.constants.StickerFormat.ANIMATED, telegram.constants.StickerFormat.VIDEO. Added in version 20.2.

Format of the sticker. Must be one of telegram.constants.StickerFormat.STATIC, telegram.constants.StickerFormat.ANIMATED, telegram.constants.StickerFormat.VIDEO.

Added in version 20.2.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. By default, 20 seconds are used as write timeout. Changed in version 22.0: The default value changed to DEFAULT_NONE.

Value to pass to telegram.request.BaseRequest.post.write_timeout. By default, 20 seconds are used as write timeout.

Changed in version 22.0: The default value changed to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, the uploaded File is returned.

telegram.error.TelegramError –

Bot’s username. Shortcut for the corresponding attribute of bot.

Alias for verify_chat()

Alias for verify_user()

Verifies a chat on behalf of the organization which is represented by the bot.

telegram.Chat.verify()

telegram.ChatFullInfo.verify()

Added in version 21.10.

chat_id (int | str) – Unique identifier for the target chat or username of the target channel (in the format @channelusername).

custom_description (str, optional) – Custom description for the verification; 0- 70 characters. Must be empty if the organization isn’t allowed to provide a custom verification description.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

Verifies a user on behalf of the organization which is represented by the bot.

telegram.User.verify()

Added in version 21.10.

user_id (int) – Unique identifier of the target user.

custom_description (str, optional) – Custom description for the verification; 0- 70 characters. Must be empty if the organization isn’t allowed to provide a custom verification description.

read_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.read_timeout. Defaults to DEFAULT_NONE.

write_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.write_timeout. Defaults to DEFAULT_NONE.

connect_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.connect_timeout. Defaults to DEFAULT_NONE.

pool_timeout (float | None, optional) – Value to pass to telegram.request.BaseRequest.post.pool_timeout. Defaults to DEFAULT_NONE.

api_kwargs (dict, optional) – Arbitrary keyword arguments to be passed to the Telegram API. See do_api_request() for limitations.

On success, True is returned.

telegram.error.TelegramError –

---

## ChatBoostSource¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.chatboostsource.html

**Contents:**
- ChatBoostSource¶

Added in version 20.8.

Bases: telegram.TelegramObject

Base class for Telegram ChatBoostSource objects. It can be one of:

telegram.ChatBoostSourcePremium

telegram.ChatBoostSourceGiftCode

telegram.ChatBoostSourceGiveaway

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their source is equal.

telegram.ChatBoost.source

telegram.ChatBoostRemoved.source

Added in version 20.8.

source (str) – The source of the chat boost. Can be one of: PREMIUM, GIFT_CODE, or GIVEAWAY.

The source of the chat boost. Can be one of: PREMIUM, GIFT_CODE, or GIVEAWAY.

telegram.constants.ChatBoostSources.GIFT_CODE

telegram.constants.ChatBoostSources.GIVEAWAY

telegram.constants.ChatBoostSources.PREMIUM

See telegram.TelegramObject.de_json().

---

## ChecklistTasksAdded¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.checklisttasksadded.html

**Contents:**
- ChecklistTasksAdded¶

Bases: telegram.TelegramObject

Describes a service message about tasks added to a checklist.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their tasks are equal.

telegram.Message.checklist_tasks_added

Added in version 22.3.

checklist_message (telegram.Message, optional) – Message containing the checklist to which tasks were added. Note that the ~:class:telegram.Message object in this field will not contain the reply_to_message field even if it itself is a reply.

tasks (Sequence[telegram.ChecklistTask]) – List of tasks added to the checklist

Optional. Message containing the checklist to which tasks were added. Note that the ~:class:telegram.Message object in this field will not contain the reply_to_message field even if it itself is a reply.

List of tasks added to the checklist

Tuple[telegram.ChecklistTask]

See telegram.TelegramObject.de_json().

---

## ChatBoostSourceGiftCode¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.chatboostsourcegiftcode.html

**Contents:**
- ChatBoostSourceGiftCode¶

Added in version 20.8.

Bases: telegram.ChatBoostSource

The boost was obtained by the creation of Telegram Premium gift codes to boost a chat. Each such code boosts the chat 4 times for the duration of the corresponding Telegram Premium subscription.

telegram.ChatBoost.source

telegram.ChatBoostRemoved.source

Added in version 20.8.

user (telegram.User) – User for which the gift code was created.

The source of the chat boost. Always GIFT_CODE.

User for which the gift code was created.

---

## ChatMemberUpdated¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.chatmemberupdated.html

**Contents:**
- ChatMemberUpdated¶

Bases: telegram.TelegramObject

This object represents changes in the status of a chat member.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their chat, from_user, date, old_chat_member and new_chat_member are equal.

telegram.Update.chat_member

telegram.Update.my_chat_member

Added in version 13.4.

In Python from is a reserved word. Use from_user instead.

chat (telegram.Chat) – Chat the user belongs to.

from_user (telegram.User) – Performer of the action, which resulted in the change.

date (datetime.datetime) – Date the change was done in Unix time. Converted to datetime.datetime. Changed in version 20.3: The default timezone of the bot is used for localization, which is UTC unless telegram.ext.Defaults.tzinfo is used.

Date the change was done in Unix time. Converted to datetime.datetime.

Changed in version 20.3: The default timezone of the bot is used for localization, which is UTC unless telegram.ext.Defaults.tzinfo is used.

old_chat_member (telegram.ChatMember) – Previous information about the chat member.

new_chat_member (telegram.ChatMember) – New information about the chat member.

invite_link (telegram.ChatInviteLink, optional) – Chat invite link, which was used by the user to join the chat. For joining by invite link events only.

via_chat_folder_invite_link (bool, optional) – True, if the user joined the chat via a chat folder invite link Added in version 20.3.

True, if the user joined the chat via a chat folder invite link

Added in version 20.3.

via_join_request (bool, optional) – True, if the user joined the chat after sending a direct join request without using an invite link and being approved by an administrator Added in version 21.2.

True, if the user joined the chat after sending a direct join request without using an invite link and being approved by an administrator

Added in version 21.2.

Chat the user belongs to.

Performer of the action, which resulted in the change.

Date the change was done in Unix time. Converted to datetime.datetime.

Changed in version 20.3: The default timezone of the bot is used for localization, which is UTC unless telegram.ext.Defaults.tzinfo is used.

Previous information about the chat member.

New information about the chat member.

Optional. Chat invite link, which was used by the user to join the chat. For joining by invite link events only.

telegram.ChatInviteLink

Optional. True, if the user joined the chat via a chat folder invite link

Added in version 20.3.

Optional. True, if the user joined the chat after sending a direct join request without using an invite link and being approved by an administrator

Added in version 21.2.

See telegram.TelegramObject.de_json().

Computes the difference between old_chat_member and new_chat_member.

To determine, if the telegram.ChatMember.user attribute has changed, every attribute of the user will be checked.

Added in version 13.5.

A dictionary mapping attribute names to tuples of the form (old_value, new_value)

dict[str, tuple[object, object]]

---

## ChatBoostUpdated¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.chatboostupdated.html

**Contents:**
- ChatBoostUpdated¶

Added in version 20.8.

Bases: telegram.TelegramObject

This object represents a boost added to a chat or changed.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their chat, and boost are equal.

telegram.Update.chat_boost

Added in version 20.8.

chat (telegram.Chat) – Chat which was boosted.

boost (telegram.ChatBoost) – Information about the chat boost.

Chat which was boosted.

Information about the chat boost.

See telegram.TelegramObject.de_json().

---

## InputMediaAnimation¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.inputmediaanimation.html

**Contents:**
- InputMediaAnimation¶

Bases: telegram.InputMedia

Represents an animation file (GIF or H.264/MPEG-4 AVC video without sound) to be sent.

When using a telegram.Animation for the media attribute, it will take the width, height and duration from that animation, unless otherwise specified with the optional arguments.

Working with Files and Media

telegram.Bot.edit_message_media()

Changed in version 20.5: Removed the deprecated argument and attribute thumb.

media (str | file object | InputFile | bytes | pathlib.Path | telegram.Animation) – File to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one. To upload a file, you can either pass a file object (e.g. open("filename", "rb")) or the file contents as bytes. If the bot is running in local_mode, passing the path of the file (as string or pathlib.Path object) is supported as well. Lastly you can pass an existing telegram.Animation object to send. Changed in version 13.2: Accept bytes as input.

File to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one. To upload a file, you can either pass a file object (e.g. open("filename", "rb")) or the file contents as bytes. If the bot is running in local_mode, passing the path of the file (as string or pathlib.Path object) is supported as well. Lastly you can pass an existing telegram.Animation object to send.

Changed in version 13.2: Accept bytes as input.

filename (str, optional) – Custom file name for the animation, when uploading a new file. Convenience parameter, useful e.g. when sending files generated by the tempfile module. Added in version 13.1.

Custom file name for the animation, when uploading a new file. Convenience parameter, useful e.g. when sending files generated by the tempfile module.

Added in version 13.1.

caption (str, optional) – Caption of the animation to be sent, 0-1024 characters after entities parsing.

parse_mode (str, optional) – Mode for parsing entities. See telegram.constants.ParseMode and formatting options for more details.

caption_entities (Sequence[telegram.MessageEntity], optional) – Sequence of special entities that appear in the caption, which can be specified instead of parse_mode. Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list. The input is converted to a tuple.

Sequence of special entities that appear in the caption, which can be specified instead of parse_mode.

Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list. The input is converted to a tuple.

width (int, optional) – Animation width.

height (int, optional) – Animation height.

duration (int | datetime.timedelta, optional) – Animation duration in seconds. Changed in version v22.2: datetime.timedelta objects are accepted in addition to plain int values.

Animation duration in seconds.

Changed in version v22.2: datetime.timedelta objects are accepted in addition to plain int values.

has_spoiler (bool, optional) – Pass True, if the animation needs to be covered with a spoiler animation. Added in version 20.0.

Pass True, if the animation needs to be covered with a spoiler animation.

Added in version 20.0.

thumbnail (file object | bytes | pathlib.Path | str, optional) – Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail’s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file. To upload a file, you can either pass a file object (e.g. open("filename", "rb")) or the file contents as bytes. If the bot is running in local_mode, passing the path of the file (as string or pathlib.Path object) is supported as well. Added in version 20.2.

Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail’s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file. To upload a file, you can either pass a file object (e.g. open("filename", "rb")) or the file contents as bytes. If the bot is running in local_mode, passing the path of the file (as string or pathlib.Path object) is supported as well.

Added in version 20.2.

show_caption_above_media (bool, optional) – Pass True, if the caption must be shown above the message media. Added in version 21.3.

Pass True, if the caption must be shown above the message media.

Added in version 21.3.

str | telegram.InputFile

Optional. Caption of the animation to be sent, 0-1024 characters after entities parsing.

Optional. The parse mode to use for text formatting.

Optional. Tuple of special entities that appear in the caption, which can be specified instead of parse_mode.

Changed in version 20.0:

This attribute is now an immutable tuple.

This attribute is now always a tuple, that may be empty.

tuple[telegram.MessageEntity]

Optional. Animation width.

Optional. Animation height.

Optional. Animation duration in seconds.

Deprecated since version v22.2: In a future major version this attribute will be of type datetime.timedelta. You can opt-in early by setting PTB_TIMEDELTA=true or PTB_TIMEDELTA=1 as an environment variable.

int | datetime.timedelta

Optional. True, if the animation is covered with a spoiler animation.

Added in version 20.0.

Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail’s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file.

Added in version 20.2.

Optional. True, if the caption must be shown above the message media.

Added in version 21.3.

---

## ChatBoostAdded¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.chatboostadded.html

**Contents:**
- ChatBoostAdded¶

Bases: telegram.TelegramObject

This object represents a service message about a user boosting a chat.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their boost_count are equal.

telegram.Message.boost_added

Added in version 21.0.

boost_count (int) – Number of boosts added by the user.

Number of boosts added by the user.

---

## BotCommandScopeDefault¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.botcommandscopedefault.html

**Contents:**
- BotCommandScopeDefault¶

Bases: telegram.BotCommandScope

Represents the default scope of bot commands. Default commands are used if no commands with a narrower scope are specified for the user.

telegram.Bot.delete_my_commands()

telegram.Bot.get_my_commands()

telegram.Bot.set_my_commands()

Added in version 13.7.

Scope type 'default'.

---

## telegram package¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.html

**Contents:**
- telegram package¶
- Version Constants¶
- Classes in this package¶

A library that provides a Python interface to the Telegram Bot API

Shortcut for telegram.constants.BOT_API_VERSION.

Changed in version 20.0: This constant was previously named bot_api_version.

Shortcut for telegram.constants.BOT_API_VERSION_INFO.

Added in version 20.0.

The version of the python-telegram-bot library as string. To get detailed information about the version number, please use __version_info__ instead.

A tuple containing the five components of the version number: major, minor, micro, releaselevel, and serial. All values except releaselevel are integers. The release level is 'alpha', 'beta', 'candidate', or 'final'. The components can also be accessed by name, so __version_info__[0] is equivalent to __version_info__.major and so on.

Added in version 20.0.

---

## BackgroundTypeFill¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.backgroundtypefill.html

**Contents:**
- BackgroundTypeFill¶

Added in version 21.2.

Bases: telegram.BackgroundType

The background is automatically filled based on the selected colors.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their fill and dark_theme_dimming are equal.

telegram.ChatBackground.type

Added in version 21.2.

fill (telegram.BackgroundFill) – The background fill.

dark_theme_dimming (int) – Dimming of the background in dark themes, as a percentage; 0-100.

Type of the background. Always FILL.

telegram.BackgroundFill

Dimming of the background in dark themes, as a percentage; 0-100.

---

## Contact¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.contact.html

**Contents:**
- Contact¶

Bases: telegram.TelegramObject

This object represents a phone contact.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their phone_number is equal.

telegram.Bot.send_contact()

telegram.ExternalReplyInfo.contact

telegram.Message.contact

telegram.Message.effective_attachment

phone_number (str) – Contact’s phone number.

first_name (str) – Contact’s first name.

last_name (str, optional) – Contact’s last name.

user_id (int, optional) – Contact’s user identifier in Telegram.

vcard (str, optional) – Additional data about the contact in the form of a vCard.

Contact’s phone number.

Contact’s first name.

Optional. Contact’s last name.

Optional. Contact’s user identifier in Telegram.

Optional. Additional data about the contact in the form of a vCard.

---

## BotShortDescription¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.botshortdescription.html

**Contents:**
- BotShortDescription¶

Bases: telegram.TelegramObject

This object represents the bot’s short description.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their short_description is equal.

telegram.Bot.get_my_short_description()

Added in version 20.2.

short_description (str) – The bot’s short description.

The bot’s short description.

---

## ChatMemberMember¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.chatmembermember.html

**Contents:**
- ChatMemberMember¶

Bases: telegram.ChatMember

Represents a chat member that has no additional privileges or restrictions.

telegram.ChatMemberUpdated.new_chat_member

telegram.ChatMemberUpdated.old_chat_member

telegram.Bot.get_chat_administrators()

telegram.Bot.get_chat_member()

Added in version 13.7.

user (telegram.User) – Information about the user.

until_date (datetime.datetime, optional) – Date when the user’s subscription will expire. Added in version 21.5.

Date when the user’s subscription will expire.

Added in version 21.5.

The member’s status in the chat, always 'member'.

Information about the user.

Optional. Date when the user’s subscription will expire.

Added in version 21.5.

---

## ForumTopicEdited¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.forumtopicedited.html

**Contents:**
- ForumTopicEdited¶

Bases: telegram.TelegramObject

This object represents a service message about an edited forum topic.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their name and icon_custom_emoji_id are equal.

telegram.Message.forum_topic_edited

Added in version 20.0.

name (str, optional) – New name of the topic, if it was edited.

icon_custom_emoji_id (str, optional) – New identifier of the custom emoji shown as the topic icon, if it was edited; an empty string if the icon was removed.

Optional. New name of the topic, if it was edited.

Optional. New identifier of the custom emoji shown as the topic icon, if it was edited; an empty string if the icon was removed.

---

## BusinessIntro¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.businessintro.html

**Contents:**
- BusinessIntro¶

Bases: telegram.TelegramObject

This object contains information about the start page settings of a Telegram Business account.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their title, message and sticker are equal.

telegram.ChatFullInfo.business_intro

Added in version 21.1.

title (str, optional) – Title text of the business intro.

message (str, optional) – Message text of the business intro.

sticker (telegram.Sticker, optional) – Sticker of the business intro.

Optional. Title text of the business intro.

Optional. Message text of the business intro.

Optional. Sticker of the business intro.

See telegram.TelegramObject.de_json().

---

## Birthdate¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.birthdate.html

**Contents:**
- Birthdate¶

Bases: telegram.TelegramObject

This object describes the birthdate of a user.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their day, and month are equal.

telegram.ChatFullInfo.birthdate

Added in version 21.1.

day (int) – Day of the user’s birth; 1-31.

month (int) – Month of the user’s birth; 1-12.

year (int, optional) – Year of the user’s birth.

Day of the user’s birth; 1-31.

Month of the user’s birth; 1-12.

Optional. Year of the user’s birth.

Return the birthdate as a date object.

Changed in version 21.2: Now returns a datetime.date object instead of a datetime.datetime object, as was originally intended.

year (int, optional) – The year to use. Required, if the year was not present.

The birthdate as a date object.

---

## Animation¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.animation.html

**Contents:**
- Animation¶

Bases: telegram.TelegramObject

This object represents an animation file (GIF or H.264/MPEG-4 AVC video without sound).

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their file_unique_id is equal.

telegram.Bot.get_file()

telegram.Bot.send_animation()

telegram.ExternalReplyInfo.animation

telegram.Game.animation

telegram.InputMediaAnimation.media

telegram.Message.animation

telegram.Message.effective_attachment

Changed in version 20.5: Removed the deprecated argument and attribute thumb.

file_id (str) – Identifier for this file, which can be used to download or reuse the file.

file_unique_id (str) – Unique identifier for this file, which is supposed to be the same over time and for different bots. Can’t be used to download or reuse the file.

width (int) – Video width as defined by the sender.

height (int) – Video height as defined by the sender.

duration (int | datetime.timedelta, optional) – Duration of the video in seconds as defined by the sender. Changed in version v22.2: datetime.timedelta objects are accepted in addition to plain int values.

Duration of the video in seconds as defined by the sender.

Changed in version v22.2: datetime.timedelta objects are accepted in addition to plain int values.

file_name (str, optional) – Original animation filename as defined by the sender.

mime_type (str, optional) – MIME type of the file as defined by the sender.

file_size (int, optional) – File size in bytes.

thumbnail (telegram.PhotoSize, optional) – Animation thumbnail as defined by sender. Added in version 20.2.

Animation thumbnail as defined by sender.

Added in version 20.2.

Identifier for this file, which can be used to download or reuse the file.

Unique identifier for this file, which is supposed to be the same over time and for different bots. Can’t be used to download or reuse the file.

Video width as defined by the sender.

Video height as defined by the sender.

Duration of the video in seconds as defined by the sender.

Deprecated since version v22.2: In a future major version this attribute will be of type datetime.timedelta. You can opt-in early by setting PTB_TIMEDELTA=true or PTB_TIMEDELTA=1 as an environment variable.

int | datetime.timedelta

Optional. Original animation filename as defined by the sender.

Optional. MIME type of the file as defined by the sender.

Optional. File size in bytes.

Optional. Animation thumbnail as defined by sender.

Added in version 20.2.

See telegram.TelegramObject.de_json().

Convenience wrapper over telegram.Bot.get_file()

For the documentation of the arguments, please see telegram.Bot.get_file().

telegram.error.TelegramError –

---

## DirectMessagesTopic¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.directmessagestopic.html

**Contents:**
- DirectMessagesTopic¶

Bases: telegram.TelegramObject

This class represents a topic for direct messages in a chat.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their topic_id and user is equal.

telegram.Message.direct_messages_topic

Added in version 22.4.

topic_id (int) – Unique identifier of the topic. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier.

user (telegram.User, optional) – Information about the user that created the topic. Hint According to Telegram, this field is always present as of Bot API 9.2.

Information about the user that created the topic.

According to Telegram, this field is always present as of Bot API 9.2.

Unique identifier of the topic. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier.

Optional. Information about the user that created the topic.

According to Telegram, this field is always present as of Bot API 9.2.

See telegram.TelegramObject.de_json().

---

## BusinessMessagesDeleted¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.businessmessagesdeleted.html

**Contents:**
- BusinessMessagesDeleted¶

Bases: telegram.TelegramObject

This object is received when messages are deleted from a connected business account.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal if their business_connection_id, message_ids, and chat are equal.

telegram.Update.deleted_business_messages

Added in version 21.1.

business_connection_id (str) – Unique identifier of the business connection.

chat (telegram.Chat) – Information about a chat in the business account. The bot may not have access to the chat or the corresponding user.

message_ids (Sequence[int]) – A list of identifiers of the deleted messages in the chat of the business account.

Unique identifier of the business connection.

Information about a chat in the business account. The bot may not have access to the chat or the corresponding user.

A list of identifiers of the deleted messages in the chat of the business account.

See telegram.TelegramObject.de_json().

---

## InputMedia¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.inputmedia.html

**Contents:**
- InputMedia¶

Bases: telegram.TelegramObject

Base class for Telegram InputMedia Objects.

telegram.Bot.edit_message_media()

Changed in version 20.0: Added arguments and attributes type, media, caption, caption_entities, parse_mode.

Working with Files and Media

media_type (str) – Type of media that the instance represents.

media (str | InputFile) – File to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one. To upload a file, you can either pass a file object (e.g. open("filename", "rb")) or the file contents as bytes. If the bot is running in local_mode, passing the path of the file (as string or pathlib.Path object) is supported as well.

caption (str, optional) – Caption of the media to be sent, 0-1024 characters after entities parsing.

caption_entities (Sequence[telegram.MessageEntity], optional) – Sequence of special entities that appear in the caption, which can be specified instead of parse_mode. Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list. The input is converted to a tuple.

Sequence of special entities that appear in the caption, which can be specified instead of parse_mode.

Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list. The input is converted to a tuple.

parse_mode (str, optional) – Mode for parsing entities. See telegram.constants.ParseMode and formatting options for more details.

Type of the input media.

str | telegram.InputFile

Optional. Caption of the media to be sent, 0-1024 characters after entities parsing.

Optional. Mode for parsing entities. See telegram.constants.ParseMode and formatting options for more details.

Optional. Tuple of special entities that appear in the caption, which can be specified instead of parse_mode.

Changed in version 20.0:

This attribute is now an immutable tuple.

This attribute is now always a tuple, that may be empty.

tuple[telegram.MessageEntity]

---

## ChatPhoto¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.chatphoto.html

**Contents:**
- ChatPhoto¶

Bases: telegram.TelegramObject

This object represents a chat photo.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their small_file_unique_id and big_file_unique_id are equal.

telegram.Bot.get_file()

telegram.ChatFullInfo.photo

small_file_id (str) – File identifier of small (160 x 160) chat photo. This file_id can be used only for photo download and only for as long as the photo is not changed.

small_file_unique_id (str) – Unique file identifier of small (160 x 160) chat photo, which is supposed to be the same over time and for different bots. Can’t be used to download or reuse the file.

big_file_id (str) – File identifier of big (640 x 640) chat photo. This file_id can be used only for photo download and only for as long as the photo is not changed.

big_file_unique_id (str) – Unique file identifier of big (640 x 640) chat photo, which is supposed to be the same over time and for different bots. Can’t be used to download or reuse the file.

File identifier of small (160 x 160) chat photo. This file_id can be used only for photo download and only for as long as the photo is not changed.

Unique file identifier of small (160 x 160) chat photo, which is supposed to be the same over time and for different bots. Can’t be used to download or reuse the file.

File identifier of big (640 x 640) chat photo. This file_id can be used only for photo download and only for as long as the photo is not changed.

Unique file identifier of big (640 x 640) chat photo, which is supposed to be the same over time and for different bots. Can’t be used to download or reuse the file.

telegram.constants.ChatPhotoSize.BIG

Added in version 20.0.

telegram.constants.ChatPhotoSize.SMALL

Added in version 20.0.

Convenience wrapper over telegram.Bot.get_file() for getting the big (640 x 640) chat photo

For the documentation of the arguments, please see telegram.Bot.get_file().

telegram.error.TelegramError –

Convenience wrapper over telegram.Bot.get_file() for getting the small (160 x 160) chat photo

For the documentation of the arguments, please see telegram.Bot.get_file().

telegram.error.TelegramError –

---

## BotCommandScopeAllChatAdministrators¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.botcommandscopeallchatadministrators.html

**Contents:**
- BotCommandScopeAllChatAdministrators¶

Bases: telegram.BotCommandScope

Represents the scope of bot commands, covering all group and supergroup chat administrators.

telegram.Bot.delete_my_commands()

telegram.Bot.get_my_commands()

telegram.Bot.set_my_commands()

Added in version 13.7.

Scope type 'all_chat_administrators'.

---

## BackgroundTypeWallpaper¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.backgroundtypewallpaper.html

**Contents:**
- BackgroundTypeWallpaper¶

Added in version 21.2.

Bases: telegram.BackgroundType

The background is a wallpaper in the JPEG format.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their document and dark_theme_dimming are equal.

telegram.ChatBackground.type

Added in version 21.2.

document (telegram.Document) – Document with the wallpaper

dark_theme_dimming (int) – Dimming of the background in dark themes, as a percentage; 0-100.

is_blurred (bool, optional) – True, if the wallpaper is downscaled to fit in a 450x450 square and then box-blurred with radius 12

is_moving (bool, optional) – True, if the background moves slightly when the device is tilted

Type of the background. Always WALLPAPER.

Document with the wallpaper

Dimming of the background in dark themes, as a percentage; 0-100.

Optional. True, if the wallpaper is downscaled to fit in a 450x450 square and then box-blurred with radius 12

Optional. True, if the background moves slightly when the device is tilted

---

## ChatFullInfo¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.chatfullinfo.html

**Contents:**
- ChatFullInfo¶

Bases: telegram.TelegramObject

This object contains full information about a chat.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their id is equal.

telegram.Bot.get_chat()

Added in version 21.2.

Changed in version 21.3: Explicit support for all shortcut methods known from telegram.Chat on this object. Previously those were only available because this class inherited from telegram.Chat.

Removed in version 22.3: Removed argument and attribute can_send_gift deprecated by API 9.0.

id (int) – Unique identifier for this chat.

type (str) – Type of chat, can be either PRIVATE, GROUP, SUPERGROUP or CHANNEL.

accent_color_id (int, optional) – Identifier of the accent color for the chat name and backgrounds of the chat photo, reply header, and link preview. See accent colors for more details. Added in version 20.8.

Identifier of the accent color for the chat name and backgrounds of the chat photo, reply header, and link preview. See accent colors for more details.

Added in version 20.8.

max_reaction_count (int) – The maximum number of reactions that can be set on a message in the chat. Added in version 21.2.

The maximum number of reactions that can be set on a message in the chat.

Added in version 21.2.

accepted_gift_types (telegram.AcceptedGiftTypes) – Information about types of gifts that are accepted by the chat or by the corresponding user for private chats. Added in version 22.1.

Information about types of gifts that are accepted by the chat or by the corresponding user for private chats.

Added in version 22.1.

title (str, optional) – Title, for supergroups, channels and group chats.

username (str, optional) – Username, for private chats, supergroups and channels if available.

first_name (str, optional) – First name of the other party in a private chat.

last_name (str, optional) – Last name of the other party in a private chat.

is_forum (bool, optional) – True, if the supergroup chat is a forum (has topics enabled). Added in version 20.0.

True, if the supergroup chat is a forum (has topics enabled).

Added in version 20.0.

photo (telegram.ChatPhoto, optional) – Chat photo.

active_usernames (Sequence[str], optional) – If set, the list of all active chat usernames; for private chats, supergroups and channels. Added in version 20.0.

If set, the list of all active chat usernames; for private chats, supergroups and channels.

Added in version 20.0.

birthdate (telegram.Birthdate, optional) – For private chats, the date of birth of the user. Added in version 21.1.

For private chats, the date of birth of the user.

Added in version 21.1.

business_intro (telegram.BusinessIntro, optional) – For private chats with business accounts, the intro of the business. Added in version 21.1.

For private chats with business accounts, the intro of the business.

Added in version 21.1.

business_location (telegram.BusinessLocation, optional) – For private chats with business accounts, the location of the business. Added in version 21.1.

For private chats with business accounts, the location of the business.

Added in version 21.1.

business_opening_hours (telegram.BusinessOpeningHours, optional) – For private chats with business accounts, the opening hours of the business. Added in version 21.1.

For private chats with business accounts, the opening hours of the business.

Added in version 21.1.

personal_chat (telegram.Chat, optional) – For private chats, the personal channel of the user. Added in version 21.1.

For private chats, the personal channel of the user.

Added in version 21.1.

available_reactions (Sequence[telegram.ReactionType], optional) – List of available reactions allowed in the chat. If omitted, then all of telegram.constants.ReactionEmoji are allowed. Added in version 20.8.

List of available reactions allowed in the chat. If omitted, then all of telegram.constants.ReactionEmoji are allowed.

Added in version 20.8.

background_custom_emoji_id (str, optional) – Custom emoji identifier of emoji chosen by the chat for the reply header and link preview background. Added in version 20.8.

Custom emoji identifier of emoji chosen by the chat for the reply header and link preview background.

Added in version 20.8.

profile_accent_color_id (int, optional) – Identifier of the accent color for the chat’s profile background. See profile accent colors for more details. Added in version 20.8.

Identifier of the accent color for the chat’s profile background. See profile accent colors for more details.

Added in version 20.8.

profile_background_custom_emoji_id (str, optional) – Custom emoji identifier of the emoji chosen by the chat for its profile background. Added in version 20.8.

Custom emoji identifier of the emoji chosen by the chat for its profile background.

Added in version 20.8.

emoji_status_custom_emoji_id (str, optional) – Custom emoji identifier of emoji status of the chat or the other party in a private chat. Added in version 20.0.

Custom emoji identifier of emoji status of the chat or the other party in a private chat.

Added in version 20.0.

emoji_status_expiration_date (datetime.datetime, optional) – Expiration date of emoji status of the chat or the other party in a private chat, as a datetime object, if any. The default timezone of the bot is used for localization, which is UTC unless telegram.ext.Defaults.tzinfo is used. Added in version 20.5.

Expiration date of emoji status of the chat or the other party in a private chat, as a datetime object, if any.

The default timezone of the bot is used for localization, which is UTC unless telegram.ext.Defaults.tzinfo is used.

Added in version 20.5.

bio (str, optional) – Bio of the other party in a private chat.

has_private_forwards (bool, optional) – True, if privacy settings of the other party in the private chat allows to use tg://user?id=<user_id> links only in chats with the user. Added in version 13.9.

True, if privacy settings of the other party in the private chat allows to use tg://user?id=<user_id> links only in chats with the user.

Added in version 13.9.

has_restricted_voice_and_video_messages (bool, optional) – True, if the privacy settings of the other party restrict sending voice and video note messages in the private chat. Added in version 20.0.

True, if the privacy settings of the other party restrict sending voice and video note messages in the private chat.

Added in version 20.0.

join_to_send_messages (bool, optional) – True, if users need to join the supergroup before they can send messages. Added in version 20.0.

True, if users need to join the supergroup before they can send messages.

Added in version 20.0.

join_by_request (bool, optional) – True, if all users directly joining the supergroup without using an invite link need to be approved by supergroup administrators. Added in version 20.0.

True, if all users directly joining the supergroup without using an invite link need to be approved by supergroup administrators.

Added in version 20.0.

description (str, optional) – Description, for groups, supergroups and channel chats.

invite_link (str, optional) – Primary invite link, for groups, supergroups and channel.

pinned_message (telegram.Message, optional) – The most recent pinned message (by sending date).

permissions (telegram.ChatPermissions) – Optional. Default chat member permissions, for groups and supergroups.

slow_mode_delay (int | datetime.timedelta, optional) – For supergroups, the minimum allowed delay between consecutive messages sent by each unprivileged user. Changed in version v22.2: datetime.timedelta objects are accepted in addition to plain int values.

For supergroups, the minimum allowed delay between consecutive messages sent by each unprivileged user.

Changed in version v22.2: datetime.timedelta objects are accepted in addition to plain int values.

unrestrict_boost_count (int, optional) – For supergroups, the minimum number of boosts that a non-administrator user needs to add in order to ignore slow mode and chat permissions. Added in version 21.0.

For supergroups, the minimum number of boosts that a non-administrator user needs to add in order to ignore slow mode and chat permissions.

Added in version 21.0.

message_auto_delete_time (int | datetime.timedelta, optional) – The time after which all messages sent to the chat will be automatically deleted; in seconds. Added in version 13.4. Changed in version v22.2: datetime.timedelta objects are accepted in addition to plain int values.

The time after which all messages sent to the chat will be automatically deleted; in seconds.

Added in version 13.4.

Changed in version v22.2: datetime.timedelta objects are accepted in addition to plain int values.

has_aggressive_anti_spam_enabled (bool, optional) – True, if aggressive anti-spam checks are enabled in the supergroup. The field is only available to chat administrators. Added in version 20.0.

True, if aggressive anti-spam checks are enabled in the supergroup. The field is only available to chat administrators.

Added in version 20.0.

has_hidden_members (bool, optional) – True, if non-administrators can only get the list of bots and administrators in the chat. Added in version 20.0.

True, if non-administrators can only get the list of bots and administrators in the chat.

Added in version 20.0.

has_protected_content (bool, optional) – True, if messages from the chat can’t be forwarded to other chats. Added in version 13.9.

True, if messages from the chat can’t be forwarded to other chats.

Added in version 13.9.

has_visible_history (bool, optional) – True, if new chat members will have access to old messages; available only to chat administrators. Added in version 20.8.

True, if new chat members will have access to old messages; available only to chat administrators.

Added in version 20.8.

sticker_set_name (str, optional) – For supergroups, name of group sticker set.

can_set_sticker_set (bool, optional) – True, if the bot can change group the sticker set.

custom_emoji_sticker_set_name (str, optional) – For supergroups, the name of the group’s custom emoji sticker set. Custom emoji from this set can be used by all users and bots in the group. Added in version 21.0.

For supergroups, the name of the group’s custom emoji sticker set. Custom emoji from this set can be used by all users and bots in the group.

Added in version 21.0.

linked_chat_id (int, optional) – Unique identifier for the linked chat, i.e. the discussion group identifier for a channel and vice versa; for supergroups and channel chats.

location (telegram.ChatLocation, optional) – For supergroups, the location to which the supergroup is connected.

can_send_paid_media (bool, optional) – True, if paid media messages can be sent or forwarded to the channel chat. The field is available only for channel chats. Added in version 21.4.

True, if paid media messages can be sent or forwarded to the channel chat. The field is available only for channel chats.

Added in version 21.4.

is_direct_messages (bool, optional) – True, if the chat is the direct messages chat of a channel. Added in version 22.4.

True, if the chat is the direct messages chat of a channel.

Added in version 22.4.

parent_chat (telegram.Chat, optional) – Information about the corresponding channel chat; for direct messages chats only. Added in version 22.4.

Information about the corresponding channel chat; for direct messages chats only.

Added in version 22.4.

Unique identifier for this chat.

Type of chat, can be either PRIVATE, GROUP, SUPERGROUP or CHANNEL.

Optional. Identifier of the accent color for the chat name and backgrounds of the chat photo, reply header, and link preview. See accent colors for more details.

Added in version 20.8.

The maximum number of reactions that can be set on a message in the chat.

Added in version 21.2.

Information about types of gifts that are accepted by the chat or by the corresponding user for private chats.

Added in version 22.1.

telegram.AcceptedGiftTypes

Title, for supergroups, channels and group chats.

Username, for private chats, supergroups and channels if available.

First name of the other party in a private chat.

Last name of the other party in a private chat.

True, if the supergroup chat is a forum (has topics enabled).

Added in version 20.0.

Optional. Chat photo.

Optional. If set, the list of all active chat usernames; for private chats, supergroups and channels.

This list is empty if the chat has no active usernames or this chat instance was not obtained via get_chat().

Added in version 20.0.

Optional. For private chats, the date of birth of the user.

Added in version 21.1.

Optional. For private chats with business accounts, the intro of the business.

Added in version 21.1.

telegram.BusinessIntro

Optional. For private chats with business accounts, the location of the business.

Added in version 21.1.

telegram.BusinessLocation

Optional. For private chats with business accounts, the opening hours of the business.

Added in version 21.1.

telegram.BusinessOpeningHours

Optional. For private chats, the personal channel of the user.

Added in version 21.1.

Optional. List of available reactions allowed in the chat. If omitted, then all of telegram.constants.ReactionEmoji are allowed.

Added in version 20.8.

tuple[telegram.ReactionType]

Optional. Custom emoji identifier of emoji chosen by the chat for the reply header and link preview background.

Added in version 20.8.

Optional. Identifier of the accent color for the chat’s profile background. See profile accent colors for more details.

Added in version 20.8.

Optional. Custom emoji identifier of the emoji chosen by the chat for its profile background.

Added in version 20.8.

Optional. Custom emoji identifier of emoji status of the chat or the other party in a private chat.

Added in version 20.0.

Optional. Expiration date of emoji status of the chat or the other party in a private chat, as a datetime object, if any.

The default timezone of the bot is used for localization, which is UTC unless telegram.ext.Defaults.tzinfo is used.

Added in version 20.5.

Optional. Bio of the other party in a private chat.

Optional. True, if privacy settings of the other party in the private chat allows to use tg://user?id=<user_id> links only in chats with the user.

Added in version 13.9.

Optional. True, if the privacy settings of the other party restrict sending voice and video note messages in the private chat.

Added in version 20.0.

Optional. True, if users need to join the supergroup before they can send messages.

Added in version 20.0.

Optional. True, if all users directly joining the supergroup without using an invite link need to be approved by supergroup administrators.

Added in version 20.0.

Optional. Description, for groups, supergroups and channel chats.

Optional. Primary invite link, for groups, supergroups and channel.

Optional. The most recent pinned message (by sending date).

Optional. Default chat member permissions, for groups and supergroups.

telegram.ChatPermissions

Optional. For supergroups, the minimum allowed delay between consecutive messages sent by each unprivileged user.

Deprecated since version v22.2: In a future major version this attribute will be of type datetime.timedelta. You can opt-in early by setting PTB_TIMEDELTA=true or PTB_TIMEDELTA=1 as an environment variable.

int | datetime.timedelta

Optional. For supergroups, the minimum number of boosts that a non-administrator user needs to add in order to ignore slow mode and chat permissions.

Added in version 21.0.

Optional. The time after which all messages sent to the chat will be automatically deleted; in seconds.

Added in version 13.4.

Deprecated since version v22.2: In a future major version this attribute will be of type datetime.timedelta. You can opt-in early by setting PTB_TIMEDELTA=true or PTB_TIMEDELTA=1 as an environment variable.

int | datetime.timedelta

Optional. True, if aggressive anti-spam checks are enabled in the supergroup. The field is only available to chat administrators.

Added in version 20.0.

Optional. True, if non-administrators can only get the list of bots and administrators in the chat.

Added in version 20.0.

Optional. True, if messages from the chat can’t be forwarded to other chats.

Added in version 13.9.

Optional. True, if new chat members will have access to old messages; available only to chat administrators.

Added in version 20.8.

Optional. For supergroups, name of Group sticker set.

Optional. True, if the bot can change group the sticker set.

Optional. For supergroups, the name of the group’s custom emoji sticker set. Custom emoji from this set can be used by all users and bots in the group.

Added in version 21.0.

Optional. Unique identifier for the linked chat, i.e. the discussion group identifier for a channel and vice versa; for supergroups and channel chats.

Optional. For supergroups, the location to which the supergroup is connected.

telegram.ChatLocation

Optional. True, if paid media messages can be sent or forwarded to the channel chat. The field is available only for channel chats.

Added in version 21.4.

Optional. True, if the chat is the direct messages chat of a channel.

Added in version 22.4.

Optional. Information about the corresponding channel chat; for direct messages chats only.

Added in version 22.4.

telegram.constants.ChatType.CHANNEL

telegram.constants.ChatType.GROUP

telegram.constants.ChatType.PRIVATE

telegram.constants.ChatType.SENDER

Added in version 13.5.

telegram.constants.ChatType.SUPERGROUP

For the documentation of the arguments, please see telegram.Bot.approve_chat_join_request().

Added in version 13.8.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.approve_suggested_post().

Added in version 22.4.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.ban_chat_sender_chat().

Added in version 13.9.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.ban_chat_member().

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.ban_chat_sender_chat().

Added in version 13.9.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.close_forum_topic().

Added in version 20.0.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.close_general_forum_topic().

Added in version 20.0.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.copy_message().

send_copy(), send_copies(), copy_messages().

On success, returns the MessageId of the sent message.

For the documentation of the arguments, please see telegram.Bot.copy_messages().

copy_message(), send_copy(), send_copies().

Added in version 20.8.

On success, a tuple of MessageId of the sent messages is returned.

tuple[telegram.MessageId]

For the documentation of the arguments, please see telegram.Bot.create_forum_topic().

Added in version 20.0.

For the documentation of the arguments, please see telegram.Bot.create_chat_invite_link().

Added in version 13.4.

Changed in version 13.8: Edited signature according to the changes of telegram.Bot.create_chat_invite_link().

telegram.ChatInviteLink

For the documentation of the arguments, please see telegram.Bot.create_chat_subscription_invite_link().

Added in version 21.5.

telegram.ChatInviteLink

See telegram.TelegramObject.de_json().

For the documentation of the arguments, please see telegram.Bot.decline_chat_join_request().

Added in version 13.8.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.decline_suggested_post().

Added in version 22.4.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.delete_forum_topic().

Added in version 20.0.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.delete_message().

Added in version 20.8.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.delete_messages().

Added in version 20.8.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.delete_chat_photo().

Added in version 20.0.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.edit_forum_topic().

Added in version 20.0.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.edit_general_forum_topic().

Added in version 20.0.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.edit_chat_invite_link().

Added in version 13.4.

Changed in version 13.8: Edited signature according to the changes of telegram.Bot.edit_chat_invite_link().

telegram.ChatInviteLink

For the documentation of the arguments, please see telegram.Bot.edit_chat_subscription_invite_link().

Added in version 21.5.

telegram.ChatInviteLink

Convenience property. Gives title if not None, else full_name if not None.

Added in version 20.1.

For the documentation of the arguments, please see telegram.Bot.export_chat_invite_link().

Added in version 13.4.

New invite link on success.

For the documentation of the arguments, please see telegram.Bot.forward_message().

forward_to(), forward_messages_from(), forward_messages_to()

Added in version 20.0.

On success, instance representing the message posted.

For the documentation of the arguments, please see telegram.Bot.forward_messages().

forward_to(), forward_from(), forward_messages_to().

Added in version 20.8.

On success, a tuple of MessageId of sent messages is returned.

tuple[telegram.MessageId]

For the documentation of the arguments, please see telegram.Bot.forward_messages().

forward_from(), forward_to(), forward_messages_from().

Added in version 20.8.

On success, a tuple of MessageId of sent messages is returned.

tuple[telegram.MessageId]

For the documentation of the arguments, please see telegram.Bot.forward_message().

forward_from(), forward_messages_from(), forward_messages_to()

Added in version 20.0.

On success, instance representing the message posted.

Convenience property. If first_name is not None, gives first_name followed by (if available) last_name.

full_name will always be None, if the chat is a (super)group or channel.

Added in version 13.2.

For the documentation of the arguments, please see telegram.Bot.get_chat_administrators().

A tuple of administrators in a chat. An Array of telegram.ChatMember objects that contains information about all chat administrators except other bots. If the chat is a group or a supergroup and no administrators were appointed, only the creator will be returned.

tuple[telegram.ChatMember]

For the documentation of the arguments, please see telegram.Bot.get_chat_member().

For the documentation of the arguments, please see telegram.Bot.get_chat_member_count().

For the documentation of the arguments, please see telegram.Bot.get_chat_menu_button().

Can only work, if the chat is a private chat.

Added in version 20.0.

On success, the current menu button is returned.

For the documentation of the arguments, please see telegram.Bot.get_user_chat_boosts().

Added in version 20.8.

On success, returns the boosts applied in the chat.

telegram.UserChatBoosts

For the documentation of the arguments, please see telegram.Bot.hide_general_forum_topic().

Added in version 20.0.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.leave_chat().

On success, True is returned.

Convenience property. If the chat has a username, returns a t.me link of the chat.

Added in version 20.0.

name (str) – The name used as a link for the chat. Defaults to full_name.

The inline mention for the chat as HTML.

TypeError – If the chat is a private chat and neither the name nor the first_name is set, then throw an TypeError. If the chat is a public chat and neither the name nor the title is set, then throw an TypeError. If chat is a private group chat, then throw an TypeError.

'Markdown' is a legacy mode, retained by Telegram for backward compatibility. You should use mention_markdown_v2() instead.

Added in version 20.0.

name (str) – The name used as a link for the chat. Defaults to full_name.

The inline mention for the chat as markdown (version 1).

TypeError – If the chat is a private chat and neither the name nor the first_name is set, then throw an TypeError. If the chat is a public chat and neither the name nor the title is set, then throw an TypeError. If chat is a private group chat, then throw an TypeError.

Added in version 20.0.

name (str) – The name used as a link for the chat. Defaults to full_name.

The inline mention for the chat as markdown (version 2).

TypeError – If the chat is a private chat and neither the name nor the first_name is set, then throw an TypeError. If the chat is a public chat and neither the name nor the title is set, then throw an TypeError. If chat is a private group chat, then throw an TypeError.

For the documentation of the arguments, please see telegram.Bot.pin_chat_message().

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.promote_chat_member().

Added in version 13.2.

Changed in version 20.0: The argument can_manage_voice_chats was renamed to can_manage_video_chats in accordance to Bot API 6.0.

Changed in version 20.6: The arguments can_post_stories, can_edit_stories and can_delete_stories were added.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.read_business_message().

Added in version 22.1.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.remove_chat_verification().

Added in version 21.10.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.reopen_forum_topic().

Added in version 20.0.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.reopen_general_forum_topic().

Added in version 20.0.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.restrict_chat_member().

Added in version 13.2.

Added in version 20.1: Added use_independent_chat_permissions.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.revoke_chat_invite_link().

Added in version 13.4.

telegram.ChatInviteLink

For the documentation of the arguments, please see telegram.Bot.send_chat_action().

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.send_animation().

On success, instance representing the message posted.

For the documentation of the arguments, please see telegram.Bot.send_audio().

On success, instance representing the message posted.

For the documentation of the arguments, please see telegram.Bot.send_chat_action().

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.send_checklist().

Added in version 22.3.

On success, instance representing the message posted.

For the documentation of the arguments, please see telegram.Bot.send_contact().

On success, instance representing the message posted.

For the documentation of the arguments, please see telegram.Bot.copy_messages().

copy_message(), send_copy(), copy_messages().

Added in version 20.8.

On success, a tuple of MessageId of the sent messages is returned.

tuple[telegram.MessageId]

For the documentation of the arguments, please see telegram.Bot.copy_message().

copy_message(), send_copies(), copy_messages().

On success, instance representing the message posted.

For the documentation of the arguments, please see telegram.Bot.send_dice().

On success, instance representing the message posted.

For the documentation of the arguments, please see telegram.Bot.send_document().

On success, instance representing the message posted.

For the documentation of the arguments, please see telegram.Bot.send_game().

On success, instance representing the message posted.

For the documentation of the arguments, please see telegram.Bot.send_gift().

Will only work if the chat is a private or channel chat, see type.

Added in version 21.8.

Changed in version 21.11: Added support for channel chats.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.send_invoice().

As of API 5.2 start_parameter is an optional argument and therefore the order of the arguments had to be changed. Use keyword arguments to make sure that the arguments are passed correctly.

Changed in version 13.5: As of Bot API 5.2, the parameter start_parameter is optional.

On success, instance representing the message posted.

For the documentation of the arguments, please see telegram.Bot.send_location().

On success, instance representing the message posted.

For the documentation of the arguments, please see telegram.Bot.send_media_group().

On success, a tuple of Message instances that were sent is returned.

tuple[telegram.Message]

For the documentation of the arguments, please see telegram.Bot.send_message().

On success, instance representing the message posted.

For the documentation of the arguments, please see telegram.Bot.send_paid_media().

Added in version 21.4.

On success, instance representing the message posted.

For the documentation of the arguments, please see telegram.Bot.send_photo().

On success, instance representing the message posted.

For the documentation of the arguments, please see telegram.Bot.send_poll().

On success, instance representing the message posted.

For the documentation of the arguments, please see telegram.Bot.send_sticker().

On success, instance representing the message posted.

For the documentation of the arguments, please see telegram.Bot.send_venue().

On success, instance representing the message posted.

For the documentation of the arguments, please see telegram.Bot.send_video().

On success, instance representing the message posted.

For the documentation of the arguments, please see telegram.Bot.send_video_note().

On success, instance representing the message posted.

For the documentation of the arguments, please see telegram.Bot.send_voice().

On success, instance representing the message posted.

For the documentation of the arguments, please see telegram.Bot.set_chat_administrator_custom_title().

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.set_chat_description().

Added in version 20.0.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.set_chat_menu_button().

Can only work, if the chat is a private chat.

Added in version 20.0.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.set_message_reaction().

Added in version 20.8.

bool On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.set_chat_permissions().

Added in version 20.1: Added use_independent_chat_permissions.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.set_chat_photo().

Added in version 20.0.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.set_chat_title().

Added in version 20.0.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.transfer_gift().

Added in version 22.1.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.unban_chat_sender_chat().

Added in version 13.9.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.unban_chat_member().

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.unban_chat_sender_chat().

Added in version 13.9.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.unhide_general_forum_topic().

Added in version 20.0.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.unpin_all_forum_topic_messages().

Added in version 20.0.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.unpin_all_general_forum_topic_messages().

Added in version 20.5.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.unpin_all_chat_messages().

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.unpin_chat_message().

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.verify_chat().

Added in version 21.10.

On success, True is returned.

---

## GiveawayCompleted¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.giveawaycompleted.html

**Contents:**
- GiveawayCompleted¶

Bases: telegram.TelegramObject

This object represents a service message about the completion of a giveaway without public winners.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their winner_count and unclaimed_prize_count are equal.

telegram.Message.giveaway_completed

Added in version 20.8.

winner_count (int) – Number of winners in the giveaway

unclaimed_prize_count (int, optional) – Number of undistributed prizes

giveaway_message (telegram.Message, optional) – Message with the giveaway that was completed, if it wasn’t deleted

is_star_giveaway (bool, optional) – True, if the giveaway is a Telegram Star giveaway. Otherwise, currently, the giveaway is a Telegram Premium giveaway. Added in version 21.6.

True, if the giveaway is a Telegram Star giveaway. Otherwise, currently, the giveaway is a Telegram Premium giveaway.

Added in version 21.6.

Number of winners in the giveaway

Optional. Number of undistributed prizes

Optional. Message with the giveaway that was completed, if it wasn’t deleted

Optional. True, if the giveaway is a Telegram Star giveaway. Otherwise, currently, the giveaway is a Telegram Premium giveaway.

Added in version 21.6.

See telegram.TelegramObject.de_json().

---

## Document¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.document.html

**Contents:**
- Document¶

Bases: telegram.TelegramObject

This object represents a general file (as opposed to photos, voice messages and audio files).

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their file_unique_id is equal.

telegram.Bot.get_file()

telegram.Bot.send_document()

telegram.BackgroundTypePattern.document

telegram.BackgroundTypeWallpaper.document

telegram.ExternalReplyInfo.document

telegram.InputMediaDocument.media

telegram.Message.document

telegram.Message.effective_attachment

Changed in version 20.5: Removed the deprecated argument and attribute thumb.

file_id (str) – Identifier for this file, which can be used to download or reuse the file.

file_unique_id (str) – Unique identifier for this file, which is supposed to be the same over time and for different bots. Can’t be used to download or reuse the file.

file_name (str, optional) – Original filename as defined by the sender.

mime_type (str, optional) – MIME type of the file as defined by the sender.

file_size (int, optional) – File size in bytes.

thumbnail (telegram.PhotoSize, optional) – Document thumbnail as defined by the sender. Added in version 20.2.

Document thumbnail as defined by the sender.

Added in version 20.2.

Identifier for this file, which can be used to download or reuse the file.

Unique identifier for this file, which is supposed to be the same over time and for different bots. Can’t be used to download or reuse the file.

Optional. Original filename as defined by the sender.

Optional. MIME type of the file as defined by the sender.

Optional. File size in bytes.

Optional. Document thumbnail as defined by the sender.

Added in version 20.2.

See telegram.TelegramObject.de_json().

Convenience wrapper over telegram.Bot.get_file()

For the documentation of the arguments, please see telegram.Bot.get_file().

telegram.error.TelegramError –

---

## ChecklistTask¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.checklisttask.html

**Contents:**
- ChecklistTask¶

Bases: telegram.TelegramObject

Describes a task in a checklist.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their id is equal.

telegram.Checklist.tasks

telegram.ChecklistTasksAdded.tasks

Added in version 22.3.

id (int) – Unique identifier of the task.

text (str) – Text of the task.

text_entities (Sequence[telegram.MessageEntity], optional) – Special entities that appear in the task text.

completed_by_user (telegram.User, optional) – User that completed the task; omitted if the task wasn’t completed

completion_date (datetime.datetime, optional) – Point in time when the task was completed; ZERO_DATE if the task wasn’t completed The default timezone of the bot is used for localization, which is UTC unless telegram.ext.Defaults.tzinfo is used.

Point in time when the task was completed; ZERO_DATE if the task wasn’t completed

The default timezone of the bot is used for localization, which is UTC unless telegram.ext.Defaults.tzinfo is used.

Unique identifier of the task.

Optional. Special entities that appear in the task text.

Tuple[telegram.MessageEntity]

Optional. User that completed the task; omitted if the task wasn’t completed

Optional. Point in time when the task was completed; ZERO_DATE if the task wasn’t completed

The default timezone of the bot is used for localization, which is UTC unless telegram.ext.Defaults.tzinfo is used.

See telegram.TelegramObject.de_json().

Returns a dict that maps telegram.MessageEntity to str. It contains entities from this checklist task filtered by their type attribute as the key, and the text that each entity belongs to as the value of the dict.

This method should always be used instead of the text_entities attribute, since it calculates the correct substring from the message text based on UTF-16 codepoints. See parse_entity for more info.

types (list[str], optional) – List of MessageEntity types as strings. If the type attribute of an entity is contained in this list, it will be returned. Defaults to telegram.MessageEntity.ALL_TYPES.

A dictionary of entities mapped to the text that belongs to them, calculated based on UTF-16 codepoints.

dict[telegram.MessageEntity, str]

Returns the text in text from a given telegram.MessageEntity of text_entities.

This method is present because Telegram calculates the offset and length in UTF-16 codepoint pairs, which some versions of Python don’t handle automatically. (That is, you can’t just slice ChecklistTask.text with the offset and length.)

entity (telegram.MessageEntity) – The entity to extract the text from. It must be an entity that belongs to text_entities.

The text of the given entity.

---

## GeneralForumTopicHidden¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.generalforumtopichidden.html

**Contents:**
- GeneralForumTopicHidden¶

Bases: telegram.TelegramObject

This object represents a service message about General forum topic hidden in the chat. Currently holds no information.

telegram.Message.general_forum_topic_hidden

Added in version 20.0.

---

## DirectMessagePriceChanged¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.directmessagepricechanged.html

**Contents:**
- DirectMessagePriceChanged¶

Bases: telegram.TelegramObject

Describes a service message about a change in the price of direct messages sent to a channel chat.

telegram.Message.direct_message_price_changed

Added in version 22.3.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their are_direct_messages_enabled, and direct_message_star_count are equal.

are_direct_messages_enabled (bool) – True, if direct messages are enabled for the channel chat; False otherwise.

direct_message_star_count (int, optional) – The new number of Telegram Stars that must be paid by users for each direct message sent to the channel. Does not apply to users who have been exempted by administrators. Defaults to 0.

True, if direct messages are enabled for the channel chat; False otherwise.

Optional. The new number of Telegram Stars that must be paid by users for each direct message sent to the channel. Does not apply to users who have been exempted by administrators. Defaults to 0.

---

## Chat¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.chat.html

**Contents:**
- Chat¶

Bases: telegram.TelegramObject

This object represents a chat.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their id is equal.

telegram.AffiliateInfo.affiliate_chat

telegram.BusinessMessagesDeleted.chat

telegram.ChatBoostRemoved.chat

telegram.ChatBoostUpdated.chat

telegram.ChatFullInfo.parent_chat

telegram.ChatFullInfo.personal_chat

telegram.ChatJoinRequest.chat

telegram.ChatMemberUpdated.chat

telegram.ExternalReplyInfo.chat

telegram.Gift.publisher_chat

telegram.Giveaway.chats

telegram.GiveawayWinners.chat

telegram.InaccessibleMessage.chat

telegram.MaybeInaccessibleMessage.chat

telegram.Message.chat

telegram.Message.sender_chat

telegram.MessageOriginChannel.chat

telegram.MessageOriginChat.sender_chat

telegram.MessageReactionCountUpdated.chat

telegram.MessageReactionUpdated.actor_chat

telegram.MessageReactionUpdated.chat

telegram.PollAnswer.voter_chat

telegram.TransactionPartnerChat.chat

telegram.UniqueGift.publisher_chat

telegram.Update.effective_chat

telegram.Update.effective_sender

Changed in version 20.0:

Removed the deprecated methods kick_member and get_members_count.

The following are now keyword-only arguments in Bot methods: location, filename, contact, {read, write, connect, pool}_timeout, api_kwargs. Use a named argument for those, and notice that some positional arguments changed position as a result.

Changed in version 20.0: Removed the attribute all_members_are_administrators. As long as Telegram provides this field for backwards compatibility, it is available through api_kwargs.

Changed in version 21.3: As per Bot API 7.3, most of the arguments and attributes of this class have now moved to telegram.ChatFullInfo.

id (int) – Unique identifier for this chat.

type (str) – Type of chat, can be either PRIVATE, GROUP, SUPERGROUP or CHANNEL.

title (str, optional) – Title, for supergroups, channels and group chats.

username (str, optional) – Username, for private chats, supergroups and channels if available.

first_name (str, optional) – First name of the other party in a private chat.

last_name (str, optional) – Last name of the other party in a private chat.

is_forum (bool, optional) – True, if the supergroup chat is a forum (has topics enabled). Added in version 20.0.

True, if the supergroup chat is a forum (has topics enabled).

Added in version 20.0.

is_direct_messages (bool, optional) – True, if the chat is the direct messages chat of a channel. Added in version 22.4.

True, if the chat is the direct messages chat of a channel.

Added in version 22.4.

Unique identifier for this chat.

Type of chat, can be either PRIVATE, GROUP, SUPERGROUP or CHANNEL.

Optional. Title, for supergroups, channels and group chats.

Optional. Username, for private chats, supergroups and channels if available.

Optional. First name of the other party in a private chat.

Optional. Last name of the other party in a private chat.

Optional. True, if the supergroup chat is a forum (has topics enabled).

Added in version 20.0.

Optional. True, if the chat is the direct messages chat of a channel.

Added in version 22.4.

telegram.constants.ChatType.CHANNEL

telegram.constants.ChatType.GROUP

telegram.constants.ChatType.PRIVATE

telegram.constants.ChatType.SENDER

Added in version 13.5.

telegram.constants.ChatType.SUPERGROUP

For the documentation of the arguments, please see telegram.Bot.approve_chat_join_request().

Added in version 13.8.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.approve_suggested_post().

Added in version 22.4.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.ban_chat_sender_chat().

Added in version 13.9.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.ban_chat_member().

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.ban_chat_sender_chat().

Added in version 13.9.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.close_forum_topic().

Added in version 20.0.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.close_general_forum_topic().

Added in version 20.0.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.copy_message().

send_copy(), send_copies(), copy_messages().

On success, returns the MessageId of the sent message.

For the documentation of the arguments, please see telegram.Bot.copy_messages().

copy_message(), send_copy(), send_copies().

Added in version 20.8.

On success, a tuple of MessageId of the sent messages is returned.

tuple[telegram.MessageId]

For the documentation of the arguments, please see telegram.Bot.create_forum_topic().

Added in version 20.0.

For the documentation of the arguments, please see telegram.Bot.create_chat_invite_link().

Added in version 13.4.

Changed in version 13.8: Edited signature according to the changes of telegram.Bot.create_chat_invite_link().

telegram.ChatInviteLink

For the documentation of the arguments, please see telegram.Bot.create_chat_subscription_invite_link().

Added in version 21.5.

telegram.ChatInviteLink

For the documentation of the arguments, please see telegram.Bot.decline_chat_join_request().

Added in version 13.8.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.decline_suggested_post().

Added in version 22.4.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.delete_forum_topic().

Added in version 20.0.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.delete_message().

Added in version 20.8.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.delete_messages().

Added in version 20.8.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.delete_chat_photo().

Added in version 20.0.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.edit_forum_topic().

Added in version 20.0.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.edit_general_forum_topic().

Added in version 20.0.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.edit_chat_invite_link().

Added in version 13.4.

Changed in version 13.8: Edited signature according to the changes of telegram.Bot.edit_chat_invite_link().

telegram.ChatInviteLink

For the documentation of the arguments, please see telegram.Bot.edit_chat_subscription_invite_link().

Added in version 21.5.

telegram.ChatInviteLink

Convenience property. Gives title if not None, else full_name if not None.

Added in version 20.1.

For the documentation of the arguments, please see telegram.Bot.export_chat_invite_link().

Added in version 13.4.

New invite link on success.

For the documentation of the arguments, please see telegram.Bot.forward_message().

forward_to(), forward_messages_from(), forward_messages_to()

Added in version 20.0.

On success, instance representing the message posted.

For the documentation of the arguments, please see telegram.Bot.forward_messages().

forward_to(), forward_from(), forward_messages_to().

Added in version 20.8.

On success, a tuple of MessageId of sent messages is returned.

tuple[telegram.MessageId]

For the documentation of the arguments, please see telegram.Bot.forward_messages().

forward_from(), forward_to(), forward_messages_from().

Added in version 20.8.

On success, a tuple of MessageId of sent messages is returned.

tuple[telegram.MessageId]

For the documentation of the arguments, please see telegram.Bot.forward_message().

forward_from(), forward_messages_from(), forward_messages_to()

Added in version 20.0.

On success, instance representing the message posted.

Convenience property. If first_name is not None, gives first_name followed by (if available) last_name.

full_name will always be None, if the chat is a (super)group or channel.

Added in version 13.2.

For the documentation of the arguments, please see telegram.Bot.get_chat_administrators().

A tuple of administrators in a chat. An Array of telegram.ChatMember objects that contains information about all chat administrators except other bots. If the chat is a group or a supergroup and no administrators were appointed, only the creator will be returned.

tuple[telegram.ChatMember]

For the documentation of the arguments, please see telegram.Bot.get_chat_member().

For the documentation of the arguments, please see telegram.Bot.get_chat_member_count().

For the documentation of the arguments, please see telegram.Bot.get_chat_menu_button().

Can only work, if the chat is a private chat.

Added in version 20.0.

On success, the current menu button is returned.

For the documentation of the arguments, please see telegram.Bot.get_user_chat_boosts().

Added in version 20.8.

On success, returns the boosts applied in the chat.

telegram.UserChatBoosts

For the documentation of the arguments, please see telegram.Bot.hide_general_forum_topic().

Added in version 20.0.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.leave_chat().

On success, True is returned.

Convenience property. If the chat has a username, returns a t.me link of the chat.

Added in version 20.0.

name (str) – The name used as a link for the chat. Defaults to full_name.

The inline mention for the chat as HTML.

TypeError – If the chat is a private chat and neither the name nor the first_name is set, then throw an TypeError. If the chat is a public chat and neither the name nor the title is set, then throw an TypeError. If chat is a private group chat, then throw an TypeError.

'Markdown' is a legacy mode, retained by Telegram for backward compatibility. You should use mention_markdown_v2() instead.

Added in version 20.0.

name (str) – The name used as a link for the chat. Defaults to full_name.

The inline mention for the chat as markdown (version 1).

TypeError – If the chat is a private chat and neither the name nor the first_name is set, then throw an TypeError. If the chat is a public chat and neither the name nor the title is set, then throw an TypeError. If chat is a private group chat, then throw an TypeError.

Added in version 20.0.

name (str) – The name used as a link for the chat. Defaults to full_name.

The inline mention for the chat as markdown (version 2).

TypeError – If the chat is a private chat and neither the name nor the first_name is set, then throw an TypeError. If the chat is a public chat and neither the name nor the title is set, then throw an TypeError. If chat is a private group chat, then throw an TypeError.

For the documentation of the arguments, please see telegram.Bot.pin_chat_message().

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.promote_chat_member().

Added in version 13.2.

Changed in version 20.0: The argument can_manage_voice_chats was renamed to can_manage_video_chats in accordance to Bot API 6.0.

Changed in version 20.6: The arguments can_post_stories, can_edit_stories and can_delete_stories were added.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.read_business_message().

Added in version 22.1.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.remove_chat_verification().

Added in version 21.10.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.reopen_forum_topic().

Added in version 20.0.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.reopen_general_forum_topic().

Added in version 20.0.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.restrict_chat_member().

Added in version 13.2.

Added in version 20.1: Added use_independent_chat_permissions.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.revoke_chat_invite_link().

Added in version 13.4.

telegram.ChatInviteLink

For the documentation of the arguments, please see telegram.Bot.send_chat_action().

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.send_animation().

On success, instance representing the message posted.

For the documentation of the arguments, please see telegram.Bot.send_audio().

On success, instance representing the message posted.

For the documentation of the arguments, please see telegram.Bot.send_chat_action().

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.send_checklist().

Added in version 22.3.

On success, instance representing the message posted.

For the documentation of the arguments, please see telegram.Bot.send_contact().

On success, instance representing the message posted.

For the documentation of the arguments, please see telegram.Bot.copy_messages().

copy_message(), send_copy(), copy_messages().

Added in version 20.8.

On success, a tuple of MessageId of the sent messages is returned.

tuple[telegram.MessageId]

For the documentation of the arguments, please see telegram.Bot.copy_message().

copy_message(), send_copies(), copy_messages().

On success, instance representing the message posted.

For the documentation of the arguments, please see telegram.Bot.send_dice().

On success, instance representing the message posted.

For the documentation of the arguments, please see telegram.Bot.send_document().

On success, instance representing the message posted.

For the documentation of the arguments, please see telegram.Bot.send_game().

On success, instance representing the message posted.

For the documentation of the arguments, please see telegram.Bot.send_gift().

Will only work if the chat is a private or channel chat, see type.

Added in version 21.8.

Changed in version 21.11: Added support for channel chats.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.send_invoice().

As of API 5.2 start_parameter is an optional argument and therefore the order of the arguments had to be changed. Use keyword arguments to make sure that the arguments are passed correctly.

Changed in version 13.5: As of Bot API 5.2, the parameter start_parameter is optional.

On success, instance representing the message posted.

For the documentation of the arguments, please see telegram.Bot.send_location().

On success, instance representing the message posted.

For the documentation of the arguments, please see telegram.Bot.send_media_group().

On success, a tuple of Message instances that were sent is returned.

tuple[telegram.Message]

For the documentation of the arguments, please see telegram.Bot.send_message().

On success, instance representing the message posted.

For the documentation of the arguments, please see telegram.Bot.send_paid_media().

Added in version 21.4.

On success, instance representing the message posted.

For the documentation of the arguments, please see telegram.Bot.send_photo().

On success, instance representing the message posted.

For the documentation of the arguments, please see telegram.Bot.send_poll().

On success, instance representing the message posted.

For the documentation of the arguments, please see telegram.Bot.send_sticker().

On success, instance representing the message posted.

For the documentation of the arguments, please see telegram.Bot.send_venue().

On success, instance representing the message posted.

For the documentation of the arguments, please see telegram.Bot.send_video().

On success, instance representing the message posted.

For the documentation of the arguments, please see telegram.Bot.send_video_note().

On success, instance representing the message posted.

For the documentation of the arguments, please see telegram.Bot.send_voice().

On success, instance representing the message posted.

For the documentation of the arguments, please see telegram.Bot.set_chat_administrator_custom_title().

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.set_chat_description().

Added in version 20.0.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.set_chat_menu_button().

Can only work, if the chat is a private chat.

Added in version 20.0.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.set_message_reaction().

Added in version 20.8.

bool On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.set_chat_permissions().

Added in version 20.1: Added use_independent_chat_permissions.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.set_chat_photo().

Added in version 20.0.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.set_chat_title().

Added in version 20.0.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.transfer_gift().

Added in version 22.1.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.unban_chat_sender_chat().

Added in version 13.9.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.unban_chat_member().

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.unban_chat_sender_chat().

Added in version 13.9.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.unhide_general_forum_topic().

Added in version 20.0.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.unpin_all_forum_topic_messages().

Added in version 20.0.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.unpin_all_general_forum_topic_messages().

Added in version 20.5.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.unpin_all_chat_messages().

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.unpin_chat_message().

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.verify_chat().

Added in version 21.10.

On success, True is returned.

---

## ChatBoostSourceGiveaway¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.chatboostsourcegiveaway.html

**Contents:**
- ChatBoostSourceGiveaway¶

Added in version 20.8.

Bases: telegram.ChatBoostSource

The boost was obtained by the creation of a Telegram Premium giveaway or a Telegram Star. This boosts the chat 4 times for the duration of the corresponding Telegram Premium subscription for Telegram Premium giveaways and prize_star_count / 500 times for one year for Telegram Star giveaways.

telegram.ChatBoost.source

telegram.ChatBoostRemoved.source

Added in version 20.8.

giveaway_message_id (int) – Identifier of a message in the chat with the giveaway; the message could have been deleted already. May be 0 if the message isn’t sent yet.

user (telegram.User, optional) – User that won the prize in the giveaway if any; for Telegram Premium giveaways only.

prize_star_count (int, optional) – The number of Telegram Stars to be split between giveaway winners; for Telegram Star giveaways only. Added in version 21.6.

The number of Telegram Stars to be split between giveaway winners; for Telegram Star giveaways only.

Added in version 21.6.

is_unclaimed (bool, optional) – True, if the giveaway was completed, but there was no user to win the prize.

Source of the boost. Always GIVEAWAY.

Identifier of a message in the chat with the giveaway; the message could have been deleted already. May be 0 if the message isn’t sent yet.

Optional. User that won the prize in the giveaway if any.

Optional. The number of Telegram Stars to be split between giveaway winners; for Telegram Star giveaways only.

Added in version 21.6.

Optional. True, if the giveaway was completed, but there was no user to win the prize.

---

## ChatJoinRequest¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.chatjoinrequest.html

**Contents:**
- ChatJoinRequest¶

Bases: telegram.TelegramObject

This object represents a join request sent to a chat.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their chat, from_user and date are equal.

Since Bot API 5.5, bots are allowed to contact users who sent a join request to a chat where the bot is an administrator with the can_invite_users administrator right - even if the user never interacted with the bot before.

Telegram does not guarantee that from_user.id coincides with the chat_id of the user. Please use user_chat_id to contact the user in response to their join request.

telegram.Update.chat_join_request

Added in version 13.8.

Changed in version 20.1: In Bot API 6.5 the argument user_chat_id was added, which changes the position of the optional arguments bio and invite_link.

chat (telegram.Chat) – Chat to which the request was sent.

from_user (telegram.User) – User that sent the join request.

date (datetime.datetime) – Date the request was sent. Changed in version 20.3: The default timezone of the bot is used for localization, which is UTC unless telegram.ext.Defaults.tzinfo is used.

Date the request was sent.

Changed in version 20.3: The default timezone of the bot is used for localization, which is UTC unless telegram.ext.Defaults.tzinfo is used.

user_chat_id (int) – Identifier of a private chat with the user who sent the join request. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier. The bot can use this identifier for 5 minutes to send messages until the join request is processed, assuming no other administrator contacted the user. Added in version 20.1.

Identifier of a private chat with the user who sent the join request. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier. The bot can use this identifier for 5 minutes to send messages until the join request is processed, assuming no other administrator contacted the user.

Added in version 20.1.

bio (str, optional) – Bio of the user.

invite_link (telegram.ChatInviteLink, optional) – Chat invite link that was used by the user to send the join request.

Chat to which the request was sent.

User that sent the join request.

Date the request was sent.

Changed in version 20.3: The default timezone of the bot is used for localization, which is UTC unless telegram.ext.Defaults.tzinfo is used.

Identifier of a private chat with the user who sent the join request. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier. The bot can use this identifier for 24 hours to send messages until the join request is processed, assuming no other administrator contacted the user.

Added in version 20.1.

Optional. Bio of the user.

Optional. Chat invite link that was used by the user to send the join request.

When a user joins a public group via an invite link, this attribute may not be present. However, this behavior is undocument and may be subject to change. See this GitHub thread for some discussion.

telegram.ChatInviteLink

For the documentation of the arguments, please see telegram.Bot.approve_chat_join_request().

On success, True is returned.

See telegram.TelegramObject.de_json().

For the documentation of the arguments, please see telegram.Bot.decline_chat_join_request().

On success, True is returned.

---

## InputMediaVideo¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.inputmediavideo.html

**Contents:**
- InputMediaVideo¶

Bases: telegram.InputMedia

Represents a video to be sent.

Working with Files and Media

When using a telegram.Video for the media attribute, it will take the width, height and duration from that video, unless otherwise specified with the optional arguments.

easily generate thumbnails. However, this behaviour is undocumented and might be changed by Telegram.

telegram.Bot.edit_message_media()

telegram.Bot.send_media_group()

Changed in version 20.5: Removed the deprecated argument and attribute thumb.

media (str | file object | InputFile | bytes | pathlib.Path | telegram.Video) – File to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one. To upload a file, you can either pass a file object (e.g. open("filename", "rb")) or the file contents as bytes. If the bot is running in local_mode, passing the path of the file (as string or pathlib.Path object) is supported as well. Lastly you can pass an existing telegram.Video object to send. Changed in version 13.2: Accept bytes as input.

File to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one. To upload a file, you can either pass a file object (e.g. open("filename", "rb")) or the file contents as bytes. If the bot is running in local_mode, passing the path of the file (as string or pathlib.Path object) is supported as well. Lastly you can pass an existing telegram.Video object to send.

Changed in version 13.2: Accept bytes as input.

filename (str, optional) – Custom file name for the video, when uploading a new file. Convenience parameter, useful e.g. when sending files generated by the tempfile module. Added in version 13.1.

Custom file name for the video, when uploading a new file. Convenience parameter, useful e.g. when sending files generated by the tempfile module.

Added in version 13.1.

caption (str, optional) – Caption of the video to be sent, 0-1024 characters after entities parsing.

parse_mode (str, optional) – Mode for parsing entities. See telegram.constants.ParseMode and formatting options for more details.

caption_entities (Sequence[telegram.MessageEntity], optional) – Sequence of special entities that appear in the caption, which can be specified instead of parse_mode. Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list. The input is converted to a tuple.

Sequence of special entities that appear in the caption, which can be specified instead of parse_mode.

Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list. The input is converted to a tuple.

width (int, optional) – Video width.

height (int, optional) – Video height.

duration (int | datetime.timedelta, optional) – Video duration in seconds. Changed in version v22.2: datetime.timedelta objects are accepted in addition to plain int values.

Video duration in seconds.

Changed in version v22.2: datetime.timedelta objects are accepted in addition to plain int values.

supports_streaming (bool, optional) – Pass True, if the uploaded video is suitable for streaming.

has_spoiler (bool, optional) – Pass True, if the video needs to be covered with a spoiler animation. Added in version 20.0.

Pass True, if the video needs to be covered with a spoiler animation.

Added in version 20.0.

thumbnail (file object | bytes | pathlib.Path | str, optional) – Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail’s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file. To upload a file, you can either pass a file object (e.g. open("filename", "rb")) or the file contents as bytes. If the bot is running in local_mode, passing the path of the file (as string or pathlib.Path object) is supported as well. Added in version 20.2.

Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail’s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file. To upload a file, you can either pass a file object (e.g. open("filename", "rb")) or the file contents as bytes. If the bot is running in local_mode, passing the path of the file (as string or pathlib.Path object) is supported as well.

Added in version 20.2.

cover (file object | bytes | pathlib.Path | str, optional) – Cover for the video in the message. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one. To upload a file, you can either pass a file object (e.g. open("filename", "rb")) or the file contents as bytes. If the bot is running in local_mode, passing the path of the file (as string or pathlib.Path object) is supported as well. Changed in version 21.11.

Cover for the video in the message. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one. To upload a file, you can either pass a file object (e.g. open("filename", "rb")) or the file contents as bytes. If the bot is running in local_mode, passing the path of the file (as string or pathlib.Path object) is supported as well.

Changed in version 21.11.

start_timestamp (int, optional) – Start timestamp for the video in the message Changed in version 21.11.

Start timestamp for the video in the message

Changed in version 21.11.

show_caption_above_media (bool, optional) – Pass True, if the caption must be shown above the message media. Added in version 21.3.

Pass True, if the caption must be shown above the message media.

Added in version 21.3.

str | telegram.InputFile

Optional. Caption of the video to be sent, 0-1024 characters after entities parsing.

Optional. Mode for parsing entities. See telegram.constants.ParseMode and formatting options for more details.

Optional. Tuple of special entities that appear in the caption, which can be specified instead of parse_mode.

Changed in version 20.0:

This attribute is now an immutable tuple.

This attribute is now always a tuple, that may be empty.

tuple[telegram.MessageEntity]

Optional. Video width.

Optional. Video height.

Optional. Video duration in seconds.

Deprecated since version v22.2: In a future major version this attribute will be of type datetime.timedelta. You can opt-in early by setting PTB_TIMEDELTA=true or PTB_TIMEDELTA=1 as an environment variable.

int | datetime.timedelta

Optional. True, if the uploaded video is suitable for streaming.

Optional. True, if the video is covered with a spoiler animation.

Added in version 20.0.

Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail’s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file.

Added in version 20.2.

Optional. True, if the caption must be shown above the message media.

Added in version 21.3.

Optional. Cover for the video in the message. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one. To upload a file, you can either pass a file object (e.g. open("filename", "rb")) or the file contents as bytes. If the bot is running in local_mode, passing the path of the file (as string or pathlib.Path object) is supported as well.

Changed in version 21.11.

Optional. Start timestamp for the video in the message

Changed in version 21.11.

---

## ChatMemberRestricted¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.chatmemberrestricted.html

**Contents:**
- ChatMemberRestricted¶

Bases: telegram.ChatMember

Represents a chat member that is under certain restrictions in the chat. Supergroups only.

telegram.ChatMemberUpdated.new_chat_member

telegram.ChatMemberUpdated.old_chat_member

telegram.Bot.get_chat_administrators()

telegram.Bot.get_chat_member()

Added in version 13.7.

Changed in version 20.0: All arguments were made positional and their order was changed. The argument can_manage_topics was added.

Changed in version 20.5: Removed deprecated argument and attribute can_send_media_messages.

user (telegram.User) – Information about the user.

is_member (bool) – True, if the user is a member of the chat at the moment of the request.

can_change_info (bool) – True, if the user can change the chat title, photo and other settings.

can_invite_users (bool) – True, if the user can invite new users to the chat.

can_pin_messages (bool) – True, if the user is allowed to pin messages; groups and supergroups only.

can_send_messages (bool) – True, if the user is allowed to send text messages, contacts, invoices, locations and venues.

can_send_polls (bool) – True, if the user is allowed to send polls.

can_send_other_messages (bool) – True, if the user is allowed to send animations, games, stickers and use inline bots.

can_add_web_page_previews (bool) – True, if the user is allowed to add web page previews to their messages.

can_manage_topics (bool) – True, if the user is allowed to create forum topics. Added in version 20.0.

True, if the user is allowed to create forum topics.

Added in version 20.0.

until_date (datetime.datetime) – Date when restrictions will be lifted for this user. Changed in version 20.3: The default timezone of the bot is used for localization, which is UTC unless telegram.ext.Defaults.tzinfo is used.

Date when restrictions will be lifted for this user.

Changed in version 20.3: The default timezone of the bot is used for localization, which is UTC unless telegram.ext.Defaults.tzinfo is used.

can_send_audios (bool) – True, if the user is allowed to send audios. Added in version 20.1.

True, if the user is allowed to send audios.

Added in version 20.1.

can_send_documents (bool) – True, if the user is allowed to send documents. Added in version 20.1.

True, if the user is allowed to send documents.

Added in version 20.1.

can_send_photos (bool) – True, if the user is allowed to send photos. Added in version 20.1.

True, if the user is allowed to send photos.

Added in version 20.1.

can_send_videos (bool) – True, if the user is allowed to send videos. Added in version 20.1.

True, if the user is allowed to send videos.

Added in version 20.1.

can_send_video_notes (bool) – True, if the user is allowed to send video notes. Added in version 20.1.

True, if the user is allowed to send video notes.

Added in version 20.1.

can_send_voice_notes (bool) – True, if the user is allowed to send voice notes. Added in version 20.1.

True, if the user is allowed to send voice notes.

Added in version 20.1.

The member’s status in the chat, always 'restricted'.

Information about the user.

True, if the user is a member of the chat at the moment of the request.

True, if the user can change the chat title, photo and other settings.

True, if the user can invite new users to the chat.

True, if the user is allowed to pin messages; groups and supergroups only.

True, if the user is allowed to send text messages, contacts, locations and venues.

True, if the user is allowed to send polls.

True, if the user is allowed to send animations, games, stickers and use inline bots.

True, if the user is allowed to add web page previews to their messages.

True, if the user is allowed to create forum topics.

Added in version 20.0.

Date when restrictions will be lifted for this user.

Changed in version 20.3: The default timezone of the bot is used for localization, which is UTC unless telegram.ext.Defaults.tzinfo is used.

True, if the user is allowed to send audios.

Added in version 20.1.

True, if the user is allowed to send documents.

Added in version 20.1.

True, if the user is allowed to send photos.

Added in version 20.1.

True, if the user is allowed to send videos.

Added in version 20.1.

True, if the user is allowed to send video notes.

Added in version 20.1.

True, if the user is allowed to send voice notes.

Added in version 20.1.

---

## ForceReply¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.forcereply.html

**Contents:**
- ForceReply¶

Bases: telegram.TelegramObject

Upon receiving a message with this object, Telegram clients will display a reply interface to the user (act as if the user has selected the bot’s message and tapped ‘Reply’). This can be extremely useful if you want to create user-friendly step-by-step interfaces without having to sacrifice privacy mode. Not supported in channels and for messages sent on behalf of a Telegram Business account.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their selective is equal.

telegram.Bot.copy_message()

telegram.Bot.send_animation()

telegram.Bot.send_audio()

telegram.Bot.send_contact()

telegram.Bot.send_dice()

telegram.Bot.send_document()

telegram.Bot.send_location()

telegram.Bot.send_message()

telegram.Bot.send_paid_media()

telegram.Bot.send_photo()

telegram.Bot.send_poll()

telegram.Bot.send_sticker()

telegram.Bot.send_venue()

telegram.Bot.send_video_note()

telegram.Bot.send_video()

telegram.Bot.send_voice()

Changed in version 20.0: The (undocumented) argument force_reply was removed and instead force_reply is now always set to True as expected by the Bot API.

selective (bool, optional) – Use this parameter if you want to force reply from specific users only. Targets: Users that are @mentioned in the text of the telegram.Message object. If the bot’s message is a reply to a message in the same chat and forum topic, sender of the original message.

Use this parameter if you want to force reply from specific users only. Targets:

Users that are @mentioned in the text of the telegram.Message object.

If the bot’s message is a reply to a message in the same chat and forum topic, sender of the original message.

input_field_placeholder (str, optional) – The placeholder to be shown in the input field when the reply is active; 1- 64 characters. Added in version 13.7.

The placeholder to be shown in the input field when the reply is active; 1- 64 characters.

Added in version 13.7.

Shows reply interface to the user, as if they manually selected the bots message and tapped ‘Reply’.

Optional. Force reply from specific users only. Targets:

Users that are @mentioned in the text of the telegram.Message object.

sender of the original message.

Optional. The placeholder to be shown in the input field when the reply is active; 1- 64 characters.

Added in version 13.7.

telegram.constants.ReplyLimit.MAX_INPUT_FIELD_PLACEHOLDER

Added in version 20.0.

telegram.constants.ReplyLimit.MIN_INPUT_FIELD_PLACEHOLDER

Added in version 20.0.

---

## ChatAdministratorRights¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.chatadministratorrights.html

**Contents:**
- ChatAdministratorRights¶

Added in version 20.0.

Bases: telegram.TelegramObject

Represents the rights of an administrator in a chat.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their is_anonymous, can_manage_chat, can_delete_messages, can_manage_video_chats, can_restrict_members, can_promote_members, can_change_info, can_invite_users, can_post_messages, can_edit_messages, can_pin_messages, can_manage_topics, can_post_stories, can_delete_stories, can_edit_stories and can_manage_direct_messages are equal.

telegram.Bot.set_my_default_administrator_rights()

telegram.KeyboardButtonRequestChat.bot_administrator_rights

telegram.KeyboardButtonRequestChat.user_administrator_rights

telegram.Bot.get_my_default_administrator_rights()

Added in version 20.0.

Changed in version 20.0: can_manage_topics is considered as well when comparing objects of this type in terms of equality.

Changed in version 20.6: can_post_stories, can_edit_stories, and can_delete_stories are considered as well when comparing objects of this type in terms of equality.

Changed in version 21.1: As of this version, can_post_stories, can_edit_stories, and can_delete_stories is now required. Thus, the order of arguments had to be changed.

Changed in version 22.4: can_manage_direct_messages is considered as well when comparing objects of this type in terms of equality.

is_anonymous (bool) – True, if the user’s presence in the chat is hidden.

can_manage_chat (bool) – True, if the administrator can access the chat event log, get boost list, see hidden supergroup and channel members, report spam messages and ignore slow mode. Implied by any other administrator privilege.

can_delete_messages (bool) – True, if the administrator can delete messages of other users.

can_manage_video_chats (bool) – True, if the administrator can manage video chats.

can_restrict_members (bool) – True, if the administrator can restrict, ban or unban chat members, or access supergroup statistics.

can_promote_members (bool) – True, if the administrator can add new administrators with a subset of their own privileges or demote administrators that they have promoted, directly or indirectly (promoted by administrators that were appointed by the user).

can_change_info (bool) – True, if the user is allowed to change the chat title , photo and other settings.

can_invite_users (bool) – True, if the user is allowed to invite new users to the chat.

can_post_messages (bool, optional) – True, if the administrator can post messages in the channel, or access channel statistics; for channels only.

can_edit_messages (bool, optional) – True, if the administrator can edit messages of other users and can pin messages; for channels only.

can_pin_messages (bool, optional) – True, if the user is allowed to pin messages; for groups and supergroups only.

can_post_stories (bool) – True, if the administrator can post stories to the chat. Added in version 20.6. Changed in version 21.0: As of this version, this argument is now required. In accordance with our stability policy, the signature will be kept as optional for now, though they are mandatory and an error will be raised if you don’t pass it.

True, if the administrator can post stories to the chat.

Added in version 20.6.

Changed in version 21.0: As of this version, this argument is now required. In accordance with our stability policy, the signature will be kept as optional for now, though they are mandatory and an error will be raised if you don’t pass it.

can_edit_stories (bool) – True, if the administrator can edit stories posted by other users, post stories to the chat page, pin chat stories, and access the chat’s story archive Added in version 20.6. Changed in version 21.0: As of this version, this argument is now required. In accordance with our stability policy, the signature will be kept as optional for now, though they are mandatory and an error will be raised if you don’t pass it.

True, if the administrator can edit stories posted by other users, post stories to the chat page, pin chat stories, and access the chat’s story archive

Added in version 20.6.

Changed in version 21.0: As of this version, this argument is now required. In accordance with our stability policy, the signature will be kept as optional for now, though they are mandatory and an error will be raised if you don’t pass it.

can_delete_stories (bool) – True, if the administrator can delete stories posted by other users. Added in version 20.6. Changed in version 21.0: As of this version, this argument is now required. In accordance with our stability policy, the signature will be kept as optional for now, though they are mandatory and an error will be raised if you don’t pass it.

True, if the administrator can delete stories posted by other users.

Added in version 20.6.

Changed in version 21.0: As of this version, this argument is now required. In accordance with our stability policy, the signature will be kept as optional for now, though they are mandatory and an error will be raised if you don’t pass it.

can_manage_topics (bool, optional) – True, if the user is allowed to create, rename, close, and reopen forum topics; for supergroups only. Added in version 20.0.

True, if the user is allowed to create, rename, close, and reopen forum topics; for supergroups only.

Added in version 20.0.

can_manage_direct_messages (bool, optional) – True, if the administrator can manage direct messages of the channel and decline suggested posts; for channels only. Added in version 22.4.

True, if the administrator can manage direct messages of the channel and decline suggested posts; for channels only.

Added in version 22.4.

True, if the user’s presence in the chat is hidden.

True, if the administrator can access the chat event log, get boost list, see hidden supergroup and channel members, report spam messages and ignore slow mode. Implied by any other administrator privilege.

True, if the administrator can delete messages of other users.

True, if the administrator can manage video chats.

True, if the administrator can restrict, ban or unban chat members, or access supergroup statistics.

True, if the administrator can add new administrators with a subset of their own privileges or demote administrators that he has promoted, directly or indirectly (promoted by administrators that were appointed by the user.)

True, if the user is allowed to change the chat title ,photo and other settings.

True, if the user is allowed to invite new users to the chat.

Optional. True, if the administrator can post messages in the channel, or access channel statistics; for channels only.

Optional. True, if the administrator can edit messages of other users and can pin messages; for channels only.

Optional. True, if the user is allowed to pin messages; for groups and supergroups only.

True, if the administrator can post stories to the chat.

Added in version 20.6.

Changed in version 21.0: As of this version, this argument is now required. In accordance with our stability policy, the signature will be kept as optional for now, though they are mandatory and an error will be raised if you don’t pass it.

True, if the administrator can edit stories posted by other users, post stories to the chat page, pin chat stories, and access the chat’s story archive

Added in version 20.6.

Changed in version 21.0: As of this version, this argument is now required. In accordance with our stability policy, the signature will be kept as optional for now, though they are mandatory and an error will be raised if you don’t pass it.

True, if the administrator can delete stories posted by other users.

Added in version 20.6.

Changed in version 21.0: As of this version, this argument is now required. In accordance with our stability policy, the signature will be kept as optional for now, though they are mandatory and an error will be raised if you don’t pass it.

Optional. True, if the user is allowed to create, rename, close, and reopen forum topics; for supergroups only.

Added in version 20.0.

Optional. True, if the administrator can manage direct messages of the channel and decline suggested posts; for channels only.

Added in version 22.4.

This method returns the ChatAdministratorRights object with all attributes set to True. This is e.g. useful when changing the bot’s default administrator rights with telegram.Bot.set_my_default_administrator_rights().

Added in version 20.0.

This method returns the ChatAdministratorRights object with all attributes set to False.

Added in version 20.0.

---

## BusinessBotRights¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.businessbotrights.html

**Contents:**
- BusinessBotRights¶

Bases: telegram.TelegramObject

This object represents the rights of a business bot.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if all their attributes are equal.

telegram.BusinessConnection.rights

Added in version 22.1.

can_reply (bool, optional) – True, if the bot can send and edit messages in the private chats that had incoming messages in the last 24 hours.

can_read_messages (bool, optional) – True, if the bot can mark incoming private messages as read.

can_delete_sent_messages (bool, optional) – True, if the bot can delete messages sent by the bot.

can_delete_all_messages (bool, optional) – True, if the bot can delete all private messages in managed chats.

can_edit_name (bool, optional) – True, if the bot can edit the first and last name of the business account.

can_edit_bio (bool, optional) – True, if the bot can edit the bio of the business account.

can_edit_profile_photo (bool, optional) – True, if the bot can edit the profile photo of the business account.

can_edit_username (bool, optional) – True, if the bot can edit the username of the business account.

can_change_gift_settings (bool, optional) – True, if the bot can change the privacy settings pertaining to gifts for the business account.

can_view_gifts_and_stars (bool, optional) – True, if the bot can view gifts and the amount of Telegram Stars owned by the business account.

can_convert_gifts_to_stars (bool, optional) – True, if the bot can convert regular gifts owned by the business account to Telegram Stars.

can_transfer_and_upgrade_gifts (bool, optional) – True, if the bot can transfer and upgrade gifts owned by the business account.

can_transfer_stars (bool, optional) – True, if the bot can transfer Telegram Stars received by the business account to its own account, or use them to upgrade and transfer gifts.

can_manage_stories (bool, optional) – True, if the bot can post, edit and delete stories on behalf of the business account.

Optional. True, if the bot can send and edit messages in the private chats that had incoming messages in the last 24 hours.

Optional. True, if the bot can mark incoming private messages as read.

Optional. True, if the bot can delete messages sent by the bot.

Optional. True, if the bot can delete all private messages in managed chats.

Optional. True, if the bot can edit the first and last name of the business account.

Optional. True, if the bot can edit the bio of the business account.

Optional. True, if the bot can edit the profile photo of the business account.

Optional. True, if the bot can edit the username of the business account.

Optional. True, if the bot can change the privacy settings pertaining to gifts for the business account.

Optional. True, if the bot can view gifts and the amount of Telegram Stars owned by the business account.

Optional. True, if the bot can convert regular gifts owned by the business account to Telegram Stars.

Optional. True, if the bot can transfer and upgrade gifts owned by the business account.

Optional. True, if the bot can transfer Telegram Stars received by the business account to its own account, or use them to upgrade and transfer gifts.

Optional. True, if the bot can post, edit and delete stories on behalf of the business account.

---

## BusinessOpeningHours¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.businessopeninghours.html

**Contents:**
- BusinessOpeningHours¶

Bases: telegram.TelegramObject

This object describes the opening hours of a business.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their time_zone_name and opening_hours are equal.

telegram.ChatFullInfo.business_opening_hours

Added in version 21.1.

time_zone_name (str) – Unique name of the time zone for which the opening hours are defined.

opening_hours (Sequence[telegram.BusinessOpeningHoursInterval]) – List of time intervals describing business opening hours.

Unique name of the time zone for which the opening hours are defined.

List of time intervals describing business opening hours.

Sequence[telegram.BusinessOpeningHoursInterval]

See telegram.TelegramObject.de_json().

Returns the opening hours intervals for a specific day as datetime objects.

Added in version 22.5.

date (datetime.date) – The date to get opening hours for.

time_zone (datetime.tzinfo | str, optional) – Timezone to use for the returned datetime objects. If not specified, then time_zone_name be used.

A tuple of datetime pairs representing opening and closing times for the specified day. Each pair consists of (opening_time, closing_time). Returns an empty tuple if there are no opening hours for the given day.

tuple[tuple[datetime.datetime, datetime.datetime], …]

Check if the business is open at the specified datetime.

Added in version 22.5.

datetime (datetime.datetime) – The datetime to check. If the object is timezone-naive, it is assumed to be in the timezone specified by time_zone_name.

True if the business is open at the specified time, False otherwise.

---

## BackgroundFillFreeformGradient¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.backgroundfillfreeformgradient.html

**Contents:**
- BackgroundFillFreeformGradient¶

Added in version 21.2.

Bases: telegram.BackgroundFill

The background is a freeform gradient that rotates after every message in the chat.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their colors is equal.

telegram.BackgroundTypeFill.fill

telegram.BackgroundTypePattern.fill

Added in version 21.2.

colors (Sequence[int]) – A list of the 3 or 4 base colors that are used to generate the freeform gradient in the RGB24 format

Type of the background fill. Always FREEFORM_GRADIENT.

A list of the 3 or 4 base colors that are used to generate the freeform gradient in the RGB24 format

---

## BotCommandScopeAllPrivateChats¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.botcommandscopeallprivatechats.html

**Contents:**
- BotCommandScopeAllPrivateChats¶

Bases: telegram.BotCommandScope

Represents the scope of bot commands, covering all private chats.

telegram.Bot.delete_my_commands()

telegram.Bot.get_my_commands()

telegram.Bot.set_my_commands()

Added in version 13.7.

Scope type 'all_private_chats'.

---

## ChatLocation¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.chatlocation.html

**Contents:**
- ChatLocation¶

Bases: telegram.TelegramObject

This object represents a location to which a chat is connected.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their location is equal.

telegram.ChatFullInfo.location

location (telegram.Location) – The location to which the supergroup is connected. Can’t be a live location.

address (str) – Location address; 1- 64 characters, as defined by the chat owner.

The location to which the supergroup is connected. Can’t be a live location.

Location address; 1- 64 characters, as defined by the chat owner.

telegram.constants.LocationLimit.MAX_CHAT_LOCATION_ADDRESS

Added in version 20.0.

telegram.constants.LocationLimit.MIN_CHAT_LOCATION_ADDRESS

Added in version 20.0.

See telegram.TelegramObject.de_json().

---

## ChecklistTasksDone¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.checklisttasksdone.html

**Contents:**
- ChecklistTasksDone¶

Bases: telegram.TelegramObject

Describes a service message about checklist tasks marked as done or not done.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their marked_as_done_task_ids and marked_as_not_done_task_ids are equal.

telegram.Message.checklist_tasks_done

Added in version 22.3.

checklist_message (telegram.Message, optional) – Message containing the checklist whose tasks were marked as done or not done. Note that the ~:class:telegram.Message object in this field will not contain the reply_to_message field even if it itself is a reply.

marked_as_done_task_ids (Sequence[int], optional) – Identifiers of the tasks that were marked as done

marked_as_not_done_task_ids (Sequence[int], optional) – Identifiers of the tasks that were marked as not done

Optional. Message containing the checklist whose tasks were marked as done or not done. Note that the ~:class:telegram.Message object in this field will not contain the reply_to_message field even if it itself is a reply.

Optional. Identifiers of the tasks that were marked as done

Optional. Identifiers of the tasks that were marked as not done

See telegram.TelegramObject.de_json().

---

## Hidden Headline¶

**URL:** https://docs.python-telegram-bot.org/en/stable/

**Contents:**
- Hidden Headline¶
- Introduction¶
  - Telegram API support¶
  - Notable Features¶
- Installing¶
  - Verifying Releases¶
  - Dependencies & Their Versions¶
    - Optional Dependencies¶
- Working with PTB¶
  - Quick Start¶

This is just here to get furo to display the right sidebar.

We have made you a wrapper you can’t refuse

We have a vibrant community of developers helping each other in our Telegram group. Join us!

Stay tuned for library updates and new releases on our Telegram Channel.

This library provides a pure Python, asynchronous interface for the Telegram Bot API. It’s compatible with Python versions 3.9+.

In addition to the pure API implementation, this library features several convenience methods and shortcuts as well as a number of high-level classes to make the development of bots easy and straightforward. These classes are contained in the telegram.ext submodule.

After installing the library, be sure to check out the section on working with PTB.

All types and methods of the Telegram Bot API 9.2 are natively supported by this library. In addition, Bot API functionality not yet natively included can still be used as described in our wiki.

Convenient shortcut methods, e.g. Message.reply_text

Fully annotated with static type hints

Customizable and extendable interface

Seamless integration with webhooks and polling

Comprehensive documentation and examples

You can install or upgrade python-telegram-bot via

To install a pre-release, use the --pre flag in addition.

You can also install python-telegram-bot from source, though this is usually not necessary.

You can also use your favored package manager (such as uv, hatch, poetry, etc.) instead of pip.

To enable you to verify that a release file that you downloaded was indeed provided by the python-telegram-bot team, we have taken the following measures.

Starting with v21.4, all releases are signed via sigstore. The corresponding signature files are uploaded to the GitHub releases page. To verify the signature, please install the sigstore Python client and follow the instructions for verifying signatures from GitHub Actions. As input for the --repository parameter, please use the value python-telegram-bot/python-telegram-bot.

Earlier releases are signed with a GPG key. The signatures are uploaded to both the GitHub releases page and the PyPI project and end with a suffix .asc. Please find the public keys here. The keys are named in the format <first_version>-<last_version>.gpg.

In addition, the GitHub release page also contains the sha1 hashes of the release files in the files with the suffix .sha1.

python-telegram-bot tries to use as few 3rd party dependencies as possible. However, for some features using a 3rd party library is more sane than implementing the functionality again. As these features are optional, the corresponding 3rd party dependencies are not installed by default. Instead, they are listed as optional dependencies. This allows to avoid unnecessary dependency conflicts for users who don’t need the optional features.

The only required dependency is httpx >=0.27,<0.29 for telegram.request.HTTPXRequest, the default networking backend.

python-telegram-bot is most useful when used along with additional libraries. To minimize dependency conflicts, we try to be liberal in terms of version requirements on the (optional) dependencies. On the other hand, we have to ensure stability of python-telegram-bot, which is why we do apply version bounds. If you encounter dependency conflicts due to these bounds, feel free to reach out.

PTB can be installed with optional dependencies:

pip install "python-telegram-bot[passport]" installs the cryptography>=39.0.1 library. Use this, if you want to use Telegram Passport related functionality.

pip install "python-telegram-bot[socks]" installs httpx[socks]. Use this, if you want to work behind a Socks5 server.

pip install "python-telegram-bot[http2]" installs httpx[http2]. Use this, if you want to use HTTP/2.

pip install "python-telegram-bot[rate-limiter]" installs aiolimiter~=1.1,<1.3. Use this, if you want to use telegram.ext.AIORateLimiter.

pip install "python-telegram-bot[webhooks]" installs the tornado~=6.4 library. Use this, if you want to use telegram.ext.Updater.start_webhook/telegram.ext.Application.run_webhook.

pip install "python-telegram-bot[callback-data]" installs the cachetools>=5.3.3,<6.3.0 library. Use this, if you want to use arbitrary callback_data.

pip install "python-telegram-bot[job-queue]" installs the APScheduler>=3.10.4,<3.12.0 library. Use this, if you want to use the telegram.ext.JobQueue.

To install multiple optional dependencies, separate them by commas, e.g. pip install "python-telegram-bot[socks,webhooks]".

Additionally, two shortcuts are provided:

pip install "python-telegram-bot[all]" installs all optional dependencies.

pip install "python-telegram-bot[ext]" installs all optional dependencies that are related to telegram.ext, i.e. [rate-limiter, webhooks, callback-data, job-queue].

Once you have installed the library, you can begin working with it - so let’s get started!

Our Wiki contains an Introduction to the API explaining how the pure Bot API can be accessed via python-telegram-bot. Moreover, the Tutorial: Your first Bot gives an introduction on how chatbots can be easily programmed with the help of the telegram.ext module.

The package documentation is the technical reference for python-telegram-bot. It contains descriptions of all available classes, modules, methods and arguments as well as the changelog.

The wiki is home to number of more elaborate introductions of the different features of python-telegram-bot and other useful resources that go beyond the technical documentation.

Our examples section contains several examples that showcase the different features of both the Bot API and python-telegram-bot. Even if it is not your approach for learning, please take a look at echobot.py. It is the de facto base for most of the bots out there. The code for these examples is released to the public domain, so you can start by grabbing the code and building on top of it.

The official Telegram Bot API documentation is of course always worth a read.

If the resources mentioned above don’t answer your questions or simply overwhelm you, there are several ways of getting help.

We have a vibrant community of developers helping each other in our Telegram group. Join us! Asking a question here is often the quickest way to get a pointer in the right direction.

Ask questions by opening a discussion.

You can even ask for help on Stack Overflow using the python-telegram-bot tag.

Since v20.0, python-telegram-bot is built on top of Pythons asyncio module. Because asyncio is in general single-threaded, python-telegram-bot currently does not aim to be thread-safe. Noteworthy parts of python-telegram-bots API that are likely to cause issues (e.g. race conditions) when used in a multi-threaded setting include:

telegram.ext.Application/Updater.update_queue

telegram.ext.ConversationHandler.check/handle_update

telegram.ext.CallbackDataCache

telegram.ext.BasePersistence

all classes in the telegram.ext.filters module that allow to add/remove allowed users/chats at runtime

Contributions of all sizes are welcome. Please review our contribution guidelines to get started. You can also help by reporting bugs or feature requests.

Occasionally we are asked if we accept donations to support the development. While we appreciate the thought, maintaining PTB is our hobby, and we have almost no running costs for it. We therefore have nothing set up to accept donations. If you still want to donate, we kindly ask you to donate to another open source project/initiative of your choice instead.

You may copy, distribute and modify the software provided that modifications are described and licensed for free under LGPL-3. Derivative works (including modifications or anything statically linked to the library) can only be redistributed under LGPL-3, but applications that use the library don’t have to be.

---

## GiveawayCreated¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.giveawaycreated.html

**Contents:**
- GiveawayCreated¶

Bases: telegram.TelegramObject

This object represents a service message about the creation of a scheduled giveaway.

telegram.Message.giveaway_created

prize_star_count (int, optional) – The number of Telegram Stars to be split between giveaway winners; for Telegram Star giveaways only. Added in version 21.6.

The number of Telegram Stars to be split between giveaway winners; for Telegram Star giveaways only.

Added in version 21.6.

Optional. The number of Telegram Stars to be split between giveaway winners; for Telegram Star giveaways only.

Added in version 21.6.

---

## InputFile¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.inputfile.html

**Contents:**
- InputFile¶

This object represents a Telegram InputFile.

telegram.Bot.send_animation()

telegram.Bot.send_audio()

telegram.Bot.send_document()

telegram.Bot.send_photo()

telegram.Bot.send_sticker()

telegram.Bot.send_video_note()

telegram.Bot.send_video()

telegram.Bot.send_voice()

telegram.Bot.set_chat_photo()

telegram.Bot.set_sticker_set_thumbnail()

telegram.Bot.set_webhook()

telegram.Bot.upload_sticker_file()

telegram.InputMedia.media

telegram.InputMediaAnimation.media

telegram.InputMediaAnimation.thumbnail

telegram.InputMediaAudio.media

telegram.InputMediaAudio.thumbnail

telegram.InputMediaDocument.media

telegram.InputMediaDocument.thumbnail

telegram.InputMediaPhoto.media

telegram.InputMediaVideo.cover

telegram.InputMediaVideo.media

telegram.InputMediaVideo.thumbnail

telegram.InputPaidMedia.media

telegram.InputPaidMediaPhoto.media

telegram.InputPaidMediaVideo.cover

telegram.InputPaidMediaVideo.media

telegram.InputPaidMediaVideo.thumbnail

telegram.InputProfilePhotoAnimated.animation

telegram.InputProfilePhotoStatic.photo

telegram.InputSticker.sticker

telegram.InputStoryContentPhoto.photo

telegram.InputStoryContentVideo.video

Changed in version 20.0:

The former attribute attach was renamed to attach_name.

Method is_image was removed. If you pass bytes to obj and would like to have the mime type automatically guessed, please pass filename in addition.

obj (file object | bytes | str) – An open file descriptor or the files content as bytes or string. Note If obj is a string, it will be encoded as bytes via obj.encode('utf-8'). Changed in version 20.0: Accept string input.

An open file descriptor or the files content as bytes or string.

If obj is a string, it will be encoded as bytes via obj.encode('utf-8').

Changed in version 20.0: Accept string input.

filename (str, optional) – Filename for this InputFile.

attach (bool, optional) – Pass True if the parameter this file belongs to in the request to Telegram should point to the multipart data via an attach:// URI. Defaults to False.

read_file_handle (bool, optional) – If True and obj is a file handle, the data will be read from the file handle on initialization of this object. If False, the file handle will be passed on to the networking backend which will have to handle the reading. Defaults to True. Tip If you upload extremely large files, you may want to set this to False to avoid reading the complete file into memory. Additionally, this may be supported better by the networking backend (in particular it is handled better by the default HTTPXRequest). Important If you set this to False, you have to ensure that the file handle is still open when the request is made. In particular, the following snippet can not work as expected. with open('file.txt', 'rb') as file: input_file = InputFile(file, read_file_handle=False) # here the file handle is already closed and the upload will fail await bot.send_document(chat_id, input_file) Added in version 21.5.

If True and obj is a file handle, the data will be read from the file handle on initialization of this object. If False, the file handle will be passed on to the networking backend which will have to handle the reading. Defaults to True.

If you upload extremely large files, you may want to set this to False to avoid reading the complete file into memory. Additionally, this may be supported better by the networking backend (in particular it is handled better by the default HTTPXRequest).

If you set this to False, you have to ensure that the file handle is still open when the request is made. In particular, the following snippet can not work as expected.

Added in version 21.5.

The binary content of the file to send.

Optional. If present, the parameter this file belongs to in the request to Telegram should point to the multipart data via a an URI of the form attach://<attach_name> URI.

Filename for the file to be sent.

The mimetype inferred from the file to be sent.

URI to insert into the JSON data for uploading the file. Returns None, if attach_name is None.

Field tuple representing the contents of the file for upload to the Telegram servers.

Changed in version 21.5: Content may now be a file handle.

tuple[str, bytes | IO, str]

---

## CallbackQuery¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.callbackquery.html

**Contents:**
- CallbackQuery¶

Bases: telegram.TelegramObject

This object represents an incoming callback query from a callback button in an inline keyboard.

If the button that originated the query was attached to a message sent by the bot, the field message will be present. If the button was attached to a message sent via the bot (in inline mode), the field inline_message_id will be present.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their id is equal.

In Python from is a reserved word. Use from_user instead.

Exactly one of the fields data or game_short_name will be present.

After the user presses an inline button, Telegram clients will display a progress bar until you call answer. It is, therefore, necessary to react by calling telegram.Bot.answer_callback_query even if no notification to the user is needed (e.g., without specifying any of the optional parameters).

If you’re using telegram.ext.ExtBot.callback_data_cache, data may be an instance of telegram.ext.InvalidCallbackData. This will be the case, if the data associated with the button triggering the telegram.CallbackQuery was already deleted or if data was manipulated by a malicious client.

Added in version 13.6.

telegram.Update.callback_query

id (str) – Unique identifier for this query.

from_user (telegram.User) – Sender.

chat_instance (str) – Global identifier, uniquely corresponding to the chat to which the message with the callback button was sent. Useful for high scores in games.

message (telegram.MaybeInaccessibleMessage, optional) – Message sent by the bot with the callback button that originated the query. Changed in version 20.8: Accept objects of type telegram.MaybeInaccessibleMessage since Bot API 7.0.

Message sent by the bot with the callback button that originated the query.

Changed in version 20.8: Accept objects of type telegram.MaybeInaccessibleMessage since Bot API 7.0.

data (str, optional) – Data associated with the callback button. Be aware that the message, which originated the query, can contain no callback buttons with this data.

inline_message_id (str, optional) – Identifier of the message sent via the bot in inline mode, that originated the query.

game_short_name (str, optional) – Short name of a Game to be returned, serves as the unique identifier for the game.

Unique identifier for this query.

Global identifier, uniquely corresponding to the chat to which the message with the callback button was sent. Useful for high scores in games.

Optional. Message sent by the bot with the callback button that originated the query.

Changed in version 20.8: Objects may be of type telegram.MaybeInaccessibleMessage since Bot API 7.0.

telegram.MaybeInaccessibleMessage

Optional. Data associated with the callback button. Be aware that the message, which originated the query, can contain no callback buttons with this data.

The value here is the same as the value passed in telegram.InlineKeyboardButton.callback_data.

Optional. Identifier of the message sent via the bot in inline mode, that originated the query.

Optional. Short name of a Game to be returned, serves as the unique identifier for the game.

telegram.constants.CallbackQueryLimit.ANSWER_CALLBACK_QUERY_TEXT_LENGTH

Added in version 13.2.

For the documentation of the arguments, please see telegram.Bot.answer_callback_query().

On success, True is returned.

For the documentation of the arguments, please see telegram.Message.copy().

Changed in version 20.8: Raises TypeError if message is not accessible.

On success, returns the MessageId of the sent message.

See telegram.TelegramObject.de_json().

For the documentation of the arguments, please see telegram.Message.delete().

Changed in version 20.8: Raises TypeError if message is not accessible.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.edit_message_caption() and telegram.Message.edit_caption().

Changed in version 20.8: Raises TypeError if message is not accessible.

On success, if edited message is sent by the bot, the edited Message is returned, otherwise True is returned.

For the documentation of the arguments, please see telegram.Message.edit_checklist().

Added in version 22.3.

On success, the edited Message is returned.

For the documentation of the arguments, please see telegram.Bot.edit_message_live_location() and telegram.Message.edit_live_location().

Changed in version 20.8: Raises TypeError if message is not accessible.

On success, if edited message is sent by the bot, the edited Message is returned, otherwise True is returned.

For the documentation of the arguments, please see telegram.Bot.edit_message_media() and telegram.Message.edit_media().

Changed in version 20.8: Raises TypeError if message is not accessible.

On success, if edited message is not an inline message, the edited Message is returned, otherwise True is returned.

For the documentation of the arguments, please see telegram.Bot.edit_message_reply_markup() and telegram.Message.edit_reply_markup().

Changed in version 20.8: Raises TypeError if message is not accessible.

On success, if edited message is sent by the bot, the edited Message is returned, otherwise True is returned.

For the documentation of the arguments, please see telegram.Bot.edit_message_text() and telegram.Message.edit_text().

Changed in version 20.8: Raises TypeError if message is not accessible.

On success, if edited message is sent by the bot, the edited Message is returned, otherwise True is returned.

For the documentation of the arguments, please see telegram.Bot.get_game_high_scores() and telegram.Message.get_game_high_scores().

Changed in version 20.8: Raises TypeError if message is not accessible.

tuple[telegram.GameHighScore]

For the documentation of the arguments, please see telegram.Message.pin().

Changed in version 20.8: Raises TypeError if message is not accessible.

On success, True is returned.

For the documentation of the arguments, please see telegram.Bot.set_game_score() and telegram.Message.set_game_score().

Changed in version 20.8: Raises TypeError if message is not accessible.

On success, if edited message is sent by the bot, the edited Message is returned, otherwise True is returned.

For the documentation of the arguments, please see telegram.Bot.stop_message_live_location() and telegram.Message.stop_live_location().

Changed in version 20.8: Raises TypeError if message is not accessible.

On success, if edited message is sent by the bot, the edited Message is returned, otherwise True is returned.

For the documentation of the arguments, please see telegram.Message.unpin().

Changed in version 20.8: Raises TypeError if message is not accessible.

On success, True is returned.

---

## InputChecklist¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.inputchecklist.html

**Contents:**
- InputChecklist¶

Bases: telegram.TelegramObject

Describes a checklist to create.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal if their tasks is equal.

telegram.Bot.edit_message_checklist()

telegram.Bot.send_checklist()

Added in version 22.3.

title (str) – Title of the checklist; 1-255 characters after entities parsing.

parse_mode (str, optional) – Mode for parsing entities. See telegram.constants.ParseMode and formatting options for more details.

title_entities (Sequence[telegram.MessageEntity], optional) – List of special entities that appear in the title, which can be specified instead of parse_mode. Currently, only bold, italic, underline, strikethrough, spoiler, and custom_emoji entities are allowed.

tasks (Sequence[telegram.InputChecklistTask]) – List of 1-30 tasks in the checklist.

others_can_add_tasks (bool, optional) – Pass True if other users can add tasks to the checklist.

others_can_mark_tasks_as_done (bool, optional) – Pass True if other users can mark tasks as done or not done in the checklist.

Title of the checklist; 1-255 characters after entities parsing.

Optional. Mode for parsing entities. See telegram.constants.ParseMode and formatting options for more details.

Optional. List of special entities that appear in the title, which can be specified instead of parse_mode. Currently, only bold, italic, underline, strikethrough, spoiler, and custom_emoji entities are allowed.

Sequence[telegram.MessageEntity]

List of 1-30 tasks in the checklist.

Sequence[telegram.InputChecklistTask]

Optional. Pass True if other users can add tasks to the checklist.

Optional. Pass True if other users can mark tasks as done or not done in the checklist.

---

## BackgroundTypeChatTheme¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.backgroundtypechattheme.html

**Contents:**
- BackgroundTypeChatTheme¶

Added in version 21.2.

Bases: telegram.BackgroundType

The background is taken directly from a built-in chat theme.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their theme_name is equal.

telegram.ChatBackground.type

Added in version 21.2.

theme_name (str) – Name of the chat theme, which is usually an emoji.

Type of the background. Always CHAT_THEME.

Name of the chat theme, which is usually an emoji.

---

## BackgroundType¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.backgroundtype.html

**Contents:**
- BackgroundType¶

Added in version 21.2.

Bases: telegram.TelegramObject

Base class for Telegram BackgroundType Objects. It can be one of:

telegram.BackgroundTypeFill

telegram.BackgroundTypeWallpaper

telegram.BackgroundTypePattern

telegram.BackgroundTypeChatTheme.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their type is equal.

telegram.ChatBackground.type

Added in version 21.2.

type (str) – Type of the background. Can be one of: FILL, WALLPAPER PATTERN or CHAT_THEME.

Type of the background. Can be one of: FILL, WALLPAPER PATTERN or CHAT_THEME.

telegram.constants.BackgroundTypeType.CHAT_THEME

telegram.constants.BackgroundTypeType.FILL

telegram.constants.BackgroundTypeType.PATTERN

telegram.constants.BackgroundTypeType.WALLPAPER

See telegram.TelegramObject.de_json().

---

## BotCommandScopeChatMember¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.botcommandscopechatmember.html

**Contents:**
- BotCommandScopeChatMember¶

Bases: telegram.BotCommandScope

Represents the scope of bot commands, covering a specific member of a group or supergroup chat.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their type, chat_id and user_id are equal.

telegram.Bot.delete_my_commands()

telegram.Bot.get_my_commands()

telegram.Bot.set_my_commands()

Added in version 13.7.

chat_id (str | int) – Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername).

user_id (int) – Unique identifier of the target user.

Scope type 'chat_member'.

Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername).

Unique identifier of the target user.

---

## ForumTopicReopened¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.forumtopicreopened.html

**Contents:**
- ForumTopicReopened¶

Bases: telegram.TelegramObject

This object represents a service message about a forum topic reopened in the chat. Currently holds no information.

telegram.Message.forum_topic_reopened

Added in version 20.0.

---

## InputMediaPhoto¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.inputmediaphoto.html

**Contents:**
- InputMediaPhoto¶

Bases: telegram.InputMedia

Represents a photo to be sent.

Working with Files and Media

telegram.Bot.edit_message_media()

telegram.Bot.send_media_group()

media (str | file object | InputFile | bytes | pathlib.Path | telegram.PhotoSize) – File to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one. To upload a file, you can either pass a file object (e.g. open("filename", "rb")) or the file contents as bytes. If the bot is running in local_mode, passing the path of the file (as string or pathlib.Path object) is supported as well. Lastly you can pass an existing telegram.PhotoSize object to send. Changed in version 13.2: Accept bytes as input.

File to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one. To upload a file, you can either pass a file object (e.g. open("filename", "rb")) or the file contents as bytes. If the bot is running in local_mode, passing the path of the file (as string or pathlib.Path object) is supported as well. Lastly you can pass an existing telegram.PhotoSize object to send.

Changed in version 13.2: Accept bytes as input.

filename (str, optional) – Custom file name for the photo, when uploading a new file. Convenience parameter, useful e.g. when sending files generated by the tempfile module. Added in version 13.1.

Custom file name for the photo, when uploading a new file. Convenience parameter, useful e.g. when sending files generated by the tempfile module.

Added in version 13.1.

caption (str, optional) – Caption of the photo to be sent, 0-1024 characters after entities parsing.

parse_mode (str, optional) – Mode for parsing entities. See telegram.constants.ParseMode and formatting options for more details.

caption_entities (Sequence[telegram.MessageEntity], optional) – Sequence of special entities that appear in the caption, which can be specified instead of parse_mode. Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list. The input is converted to a tuple.

Sequence of special entities that appear in the caption, which can be specified instead of parse_mode.

Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list. The input is converted to a tuple.

has_spoiler (bool, optional) – Pass True, if the photo needs to be covered with a spoiler animation. Added in version 20.0.

Pass True, if the photo needs to be covered with a spoiler animation.

Added in version 20.0.

show_caption_above_media (bool, optional) – Pass True, if the caption must be shown above the message media. Added in version 21.3.

Pass True, if the caption must be shown above the message media.

Added in version 21.3.

str | telegram.InputFile

Optional. Caption of the photo to be sent, 0-1024 characters after entities parsing.

Optional. Mode for parsing entities. See telegram.constants.ParseMode and formatting options for more details.

Optional. Tuple of special entities that appear in the caption, which can be specified instead of parse_mode.

Changed in version 20.0:

This attribute is now an immutable tuple.

This attribute is now always a tuple, that may be empty.

tuple[telegram.MessageEntity]

Optional. True, if the photo is covered with a spoiler animation.

Added in version 20.0.

Optional. True, if the caption must be shown above the message media.

Added in version 21.3.

---

## ChatBackground¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.chatbackground.html

**Contents:**
- ChatBackground¶

Added in version 21.2.

Bases: telegram.TelegramObject

This object represents a chat background.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their type is equal.

telegram.Message.chat_background_set

Added in version 21.2.

type (telegram.BackgroundType) – Type of the background.

Type of the background.

telegram.BackgroundType

See telegram.TelegramObject.de_json().

---

## ChatInviteLink¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.chatinvitelink.html

**Contents:**
- ChatInviteLink¶

Bases: telegram.TelegramObject

This object represents an invite link for a chat.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their invite_link, creator, creates_join_request, is_primary and is_revoked are equal.

telegram.Bot.edit_chat_invite_link()

telegram.Bot.edit_chat_subscription_invite_link()

telegram.Bot.revoke_chat_invite_link()

telegram.ChatJoinRequest.invite_link

telegram.ChatMemberUpdated.invite_link

telegram.Bot.create_chat_invite_link()

telegram.Bot.create_chat_subscription_invite_link()

telegram.Bot.edit_chat_invite_link()

telegram.Bot.edit_chat_subscription_invite_link()

telegram.Bot.revoke_chat_invite_link()

Added in version 13.4.

Changed in version 20.0:

The argument & attribute creates_join_request is now required to comply with the Bot API.

Comparing objects of this class now also takes creates_join_request into account.

invite_link (str) – The invite link.

creator (telegram.User) – Creator of the link.

creates_join_request (bool) – True, if users joining the chat via the link need to be approved by chat administrators. Added in version 13.8.

True, if users joining the chat via the link need to be approved by chat administrators.

Added in version 13.8.

is_primary (bool) – True, if the link is primary.

is_revoked (bool) – True, if the link is revoked.

expire_date (datetime.datetime, optional) – Date when the link will expire or has been expired. Changed in version 20.3: The default timezone of the bot is used for localization, which is UTC unless telegram.ext.Defaults.tzinfo is used.

Date when the link will expire or has been expired.

Changed in version 20.3: The default timezone of the bot is used for localization, which is UTC unless telegram.ext.Defaults.tzinfo is used.

member_limit (int, optional) – Maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1- 99999.

name (str, optional) – Invite link name. 0-32 characters. Added in version 13.8.

Invite link name. 0-32 characters.

Added in version 13.8.

pending_join_request_count (int, optional) – Number of pending join requests created using this link. Added in version 13.8.

Number of pending join requests created using this link.

Added in version 13.8.

subscription_period (int | datetime.timedelta, optional) – The number of seconds the subscription will be active for before the next payment. Added in version 21.5. Changed in version v22.2: datetime.timedelta objects are accepted in addition to plain int values.

The number of seconds the subscription will be active for before the next payment.

Added in version 21.5.

Changed in version v22.2: datetime.timedelta objects are accepted in addition to plain int values.

subscription_price (int, optional) – The amount of Telegram Stars a user must pay initially and after each subsequent subscription period to be a member of the chat using the link. Added in version 21.5.

The amount of Telegram Stars a user must pay initially and after each subsequent subscription period to be a member of the chat using the link.

Added in version 21.5.

The invite link. If the link was created by another chat administrator, then the second part of the link will be replaced with '…'.

True, if users joining the chat via the link need to be approved by chat administrators.

Added in version 13.8.

True, if the link is primary.

True, if the link is revoked.

Optional. Date when the link will expire or has been expired.

Changed in version 20.3: The default timezone of the bot is used for localization, which is UTC unless telegram.ext.Defaults.tzinfo is used.

Optional. Maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1- 99999.

Optional. Invite link name. 0-32 characters.

Added in version 13.8.

Optional. Number of pending join requests created using this link.

Added in version 13.8.

Optional. The number of seconds the subscription will be active for before the next payment.

Added in version 21.5.

Deprecated since version v22.2: In a future major version this attribute will be of type datetime.timedelta. You can opt-in early by setting PTB_TIMEDELTA=true or PTB_TIMEDELTA=1 as an environment variable.

int | datetime.timedelta

Optional. The amount of Telegram Stars a user must pay initially and after each subsequent subscription period to be a member of the chat using the link.

Added in version 21.5.

See telegram.TelegramObject.de_json().

---

## ChatBoostSourcePremium¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.chatboostsourcepremium.html

**Contents:**
- ChatBoostSourcePremium¶

Added in version 20.8.

Bases: telegram.ChatBoostSource

The boost was obtained by subscribing to Telegram Premium or by gifting a Telegram Premium subscription to another user.

telegram.ChatBoost.source

telegram.ChatBoostRemoved.source

Added in version 20.8.

user (telegram.User) – User that boosted the chat.

The source of the chat boost. Always PREMIUM.

User that boosted the chat.

---

## InputMediaDocument¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.inputmediadocument.html

**Contents:**
- InputMediaDocument¶

Bases: telegram.InputMedia

Represents a general file to be sent.

Working with Files and Media

telegram.Bot.edit_message_media()

telegram.Bot.send_media_group()

Changed in version 20.5: Removed the deprecated argument and attribute thumb.

media (str | file object | InputFile | bytes | pathlib.Path | telegram.Document) – File to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one. To upload a file, you can either pass a file object (e.g. open("filename", "rb")) or the file contents as bytes. If the bot is running in local_mode, passing the path of the file (as string or pathlib.Path object) is supported as well. Lastly you can pass an existing telegram.Document object to send. Changed in version 13.2: Accept bytes as input.

File to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one. To upload a file, you can either pass a file object (e.g. open("filename", "rb")) or the file contents as bytes. If the bot is running in local_mode, passing the path of the file (as string or pathlib.Path object) is supported as well. Lastly you can pass an existing telegram.Document object to send.

Changed in version 13.2: Accept bytes as input.

filename (str, optional) – Custom file name for the document, when uploading a new file. Convenience parameter, useful e.g. when sending files generated by the tempfile module. Added in version 13.1.

Custom file name for the document, when uploading a new file. Convenience parameter, useful e.g. when sending files generated by the tempfile module.

Added in version 13.1.

caption (str, optional) – Caption of the document to be sent, 0-1024 characters after entities parsing.

parse_mode (str, optional) – Mode for parsing entities. See telegram.constants.ParseMode and formatting options for more details.

caption_entities (Sequence[telegram.MessageEntity], optional) – Sequence of special entities that appear in the caption, which can be specified instead of parse_mode. Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list. The input is converted to a tuple.

Sequence of special entities that appear in the caption, which can be specified instead of parse_mode.

Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list. The input is converted to a tuple.

disable_content_type_detection (bool, optional) – Disables automatic server-side content type detection for files uploaded using multipart/form-data. Always True, if the document is sent as part of an album.

thumbnail (file object | bytes | pathlib.Path | str, optional) – Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail’s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file. To upload a file, you can either pass a file object (e.g. open("filename", "rb")) or the file contents as bytes. If the bot is running in local_mode, passing the path of the file (as string or pathlib.Path object) is supported as well. Added in version 20.2.

Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail’s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file. To upload a file, you can either pass a file object (e.g. open("filename", "rb")) or the file contents as bytes. If the bot is running in local_mode, passing the path of the file (as string or pathlib.Path object) is supported as well.

Added in version 20.2.

str | telegram.InputFile

Optional. Caption of the document to be sent, 0-1024 characters after entities parsing.

Optional. Mode for parsing entities. See telegram.constants.ParseMode and formatting options for more details.

Optional. Tuple of special entities that appear in the caption, which can be specified instead of parse_mode.

Changed in version 20.0:

This attribute is now an immutable tuple.

This attribute is now always a tuple, that may be empty.

tuple[telegram.MessageEntity]

Optional. Disables automatic server-side content type detection for files uploaded using multipart/form-data. Always True, if the document is sent as part of an album.

Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail’s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file.

Added in version 20.2.

---

## ChatMemberOwner¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.chatmemberowner.html

**Contents:**
- ChatMemberOwner¶

Bases: telegram.ChatMember

Represents a chat member that owns the chat and has all administrator privileges.

telegram.ChatMemberUpdated.new_chat_member

telegram.ChatMemberUpdated.old_chat_member

telegram.Bot.get_chat_administrators()

telegram.Bot.get_chat_member()

Added in version 13.7.

user (telegram.User) – Information about the user.

is_anonymous (bool) – True, if the user’s presence in the chat is hidden.

custom_title (str, optional) – Custom title for this user.

The member’s status in the chat, always 'creator'.

Information about the user.

True, if the user’s presence in the chat is hidden.

Optional. Custom title for this user.

---

## CopyTextButton¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.copytextbutton.html

**Contents:**
- CopyTextButton¶

Bases: telegram.TelegramObject

This object represents an inline keyboard button that copies specified text to the clipboard.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their text is equal.

telegram.InlineKeyboardButton.copy_text

Added in version 21.7.

text (str) – The text to be copied to the clipboard; 1- 256 characters

The text to be copied to the clipboard; 1- 256 characters

---

## ForumTopicCreated¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.forumtopiccreated.html

**Contents:**
- ForumTopicCreated¶

Bases: telegram.TelegramObject

This object represents the content of a service message about a new forum topic created in the chat.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their name and icon_color are equal.

telegram.Message.forum_topic_created

Added in version 20.0.

name (str) – Name of the topic

icon_color (int) – Color of the topic icon in RGB format

icon_custom_emoji_id (str, optional) – Unique identifier of the custom emoji shown as the topic icon.

Color of the topic icon in RGB format

Optional. Unique identifier of the custom emoji shown as the topic icon.

---

## ChatPermissions¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.chatpermissions.html

**Contents:**
- ChatPermissions¶

Bases: telegram.TelegramObject

Describes actions that a non-administrator user is allowed to take in a chat.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their can_send_messages, can_send_polls, can_send_other_messages, can_add_web_page_previews, can_change_info, can_invite_users, can_pin_messages, can_send_audios, can_send_documents, can_send_photos, can_send_videos, can_send_video_notes, can_send_voice_notes, and can_manage_topics are equal.

telegram.Bot.restrict_chat_member()

telegram.Bot.set_chat_permissions()

telegram.ChatFullInfo.permissions

Changed in version 20.0: can_manage_topics is considered as well when comparing objects of this type in terms of equality.

Changed in version 20.5:

can_send_audios, can_send_documents, can_send_photos, can_send_videos, can_send_video_notes and can_send_voice_notes are considered as well when comparing objects of this type in terms of equality.

Removed deprecated argument and attribute can_send_media_messages.

Though not stated explicitly in the official docs, Telegram changes not only the permissions that are set, but also sets all the others to False. However, since not documented, this behavior may change unbeknown to PTB.

can_send_messages (bool, optional) – True, if the user is allowed to send text messages, contacts, locations and venues.

can_send_polls (bool, optional) – True, if the user is allowed to send polls.

can_send_other_messages (bool, optional) – True, if the user is allowed to send animations, games, stickers and use inline bots.

can_add_web_page_previews (bool, optional) – True, if the user is allowed to add web page previews to their messages.

can_change_info (bool, optional) – True, if the user is allowed to change the chat title, photo and other settings. Ignored in public supergroups.

can_invite_users (bool, optional) – True, if the user is allowed to invite new users to the chat.

can_pin_messages (bool, optional) – True, if the user is allowed to pin messages. Ignored in public supergroups.

can_manage_topics (bool, optional) – True, if the user is allowed to create forum topics. If omitted defaults to the value of can_pin_messages. Added in version 20.0.

True, if the user is allowed to create forum topics. If omitted defaults to the value of can_pin_messages.

Added in version 20.0.

can_send_audios (bool) – True, if the user is allowed to send audios. Added in version 20.1.

True, if the user is allowed to send audios.

Added in version 20.1.

can_send_documents (bool) – True, if the user is allowed to send documents. Added in version 20.1.

True, if the user is allowed to send documents.

Added in version 20.1.

can_send_photos (bool) – True, if the user is allowed to send photos. Added in version 20.1.

True, if the user is allowed to send photos.

Added in version 20.1.

can_send_videos (bool) – True, if the user is allowed to send videos. Added in version 20.1.

True, if the user is allowed to send videos.

Added in version 20.1.

can_send_video_notes (bool) – True, if the user is allowed to send video notes. Added in version 20.1.

True, if the user is allowed to send video notes.

Added in version 20.1.

can_send_voice_notes (bool) – True, if the user is allowed to send voice notes. Added in version 20.1.

True, if the user is allowed to send voice notes.

Added in version 20.1.

Optional. True, if the user is allowed to send text messages, contacts, locations and venues.

Optional. True, if the user is allowed to send polls, implies can_send_messages.

Optional. True, if the user is allowed to send animations, games, stickers and use inline bots.

Optional. True, if the user is allowed to add web page previews to their messages.

Optional. True, if the user is allowed to change the chat title, photo and other settings. Ignored in public supergroups.

Optional. True, if the user is allowed to invite new users to the chat.

Optional. True, if the user is allowed to pin messages. Ignored in public supergroups.

Optional. True, if the user is allowed to create forum topics. If omitted defaults to the value of can_pin_messages.

Added in version 20.0.

True, if the user is allowed to send audios.

Added in version 20.1.

True, if the user is allowed to send documents.

Added in version 20.1.

True, if the user is allowed to send photos.

Added in version 20.1.

True, if the user is allowed to send videos.

Added in version 20.1.

True, if the user is allowed to send video notes.

Added in version 20.1.

True, if the user is allowed to send voice notes.

Added in version 20.1.

This method returns an ChatPermissions instance with all attributes set to True. This is e.g. useful when unrestricting a chat member with telegram.Bot.restrict_chat_member().

Added in version 20.0.

See telegram.TelegramObject.de_json().

This method returns an ChatPermissions instance with all attributes set to False.

Added in version 20.0.

---

## BotCommandScopeAllGroupChats¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.botcommandscopeallgroupchats.html

**Contents:**
- BotCommandScopeAllGroupChats¶

Bases: telegram.BotCommandScope

Represents the scope of bot commands, covering all group and supergroup chats.

telegram.Bot.delete_my_commands()

telegram.Bot.get_my_commands()

telegram.Bot.set_my_commands()

Added in version 13.7.

Scope type 'all_group_chats'.

---

## ChatBoost¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.chatboost.html

**Contents:**
- ChatBoost¶

Added in version 20.8.

Bases: telegram.TelegramObject

This object contains information about a chat boost.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their boost_id, add_date, expiration_date, and source are equal.

telegram.ChatBoostUpdated.boost

telegram.UserChatBoosts.boosts

Added in version 20.8.

boost_id (str) – Unique identifier of the boost.

add_date (datetime.datetime) – Point in time when the chat was boosted.

expiration_date (datetime.datetime) – Point in time when the boost will automatically expire, unless the booster’s Telegram Premium subscription is prolonged.

source (telegram.ChatBoostSource) – Source of the added boost.

Unique identifier of the boost.

Point in time when the chat was boosted. The default timezone of the bot is used for localization, which is UTC unless telegram.ext.Defaults.tzinfo is used.

Point in time when the boost will automatically expire, unless the booster’s Telegram Premium subscription is prolonged. The default timezone of the bot is used for localization, which is UTC unless telegram.ext.Defaults.tzinfo is used.

Source of the added boost.

telegram.ChatBoostSource

See telegram.TelegramObject.de_json().

---

## ForumTopicClosed¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.forumtopicclosed.html

**Contents:**
- ForumTopicClosed¶

Bases: telegram.TelegramObject

This object represents a service message about a forum topic closed in the chat. Currently holds no information.

telegram.Message.forum_topic_closed

Added in version 20.0.

---

## GiftInfo¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.giftinfo.html

**Contents:**
- GiftInfo¶

Bases: telegram.TelegramObject

Describes a service message about a regular gift that was sent or received.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal if their gift is equal.

telegram.Message.gift

Added in version 22.1.

gift (Gift) – Information about the gift.

owned_gift_id (str, optional) – Unique identifier of the received gift for the bot; only present for gifts received on behalf of business accounts.

convert_star_count (int, optional) – the receiver by converting the gift; omitted if conversion to Telegram Stars is impossible.

prepaid_upgrade_star_count (int, optional) – Number of Telegram Stars that were prepaid by the sender for the ability to upgrade the gift.

can_be_upgraded (bool, optional) – True, if the gift can be upgraded to a unique gift.

text (str, optional) – Text of the message that was added to the gift.

entities (Sequence[telegram.MessageEntity], optional) – Special entities that appear in the text.

is_private (bool, optional) – True, if the sender and gift text are shown only to the gift receiver; otherwise, everyone will be able to see them.

Information about the gift.

Optional. Unique identifier of the received gift for the bot; only present for gifts received on behalf of business accounts.

Optional. Number of Telegram Stars that can be claimed by the receiver by converting the gift; omitted if conversion to Telegram Stars is impossible.

Optional. Number of Telegram Stars that were prepaid by the sender for the ability to upgrade the gift.

Optional. True, if the gift can be upgraded to a unique gift.

Optional. Text of the message that was added to the gift.

Optional. Special entities that appear in the text.

Sequence[telegram.MessageEntity]

Optional. True, if the sender and gift text are shown only to the gift receiver; otherwise, everyone will be able to see them.

See telegram.TelegramObject.de_json().

Returns a dict that maps telegram.MessageEntity to str. It contains entities from this gift info’s text filtered by their type attribute as the key, and the text that each entity belongs to as the value of the dict.

This method should always be used instead of the entities attribute, since it calculates the correct substring from the message text based on UTF-16 codepoints. See parse_entity for more info.

types (list[str], optional) – List of MessageEntity types as strings. If the type attribute of an entity is contained in this list, it will be returned. Defaults to telegram.MessageEntity.ALL_TYPES.

A dictionary of entities mapped to the text that belongs to them, calculated based on UTF-16 codepoints.

dict[telegram.MessageEntity, str]

RuntimeError – If the gift info has no text.

Returns the text in text from a given telegram.MessageEntity of entities.

This method is present because Telegram calculates the offset and length in UTF-16 codepoint pairs, which some versions of Python don’t handle automatically. (That is, you can’t just slice Message.text with the offset and length.)

entity (telegram.MessageEntity) – The entity to extract the text from. It must be an entity that belongs to entities.

The text of the given entity.

RuntimeError – If the gift info has no text.

---

## BackgroundFill¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.backgroundfill.html

**Contents:**
- BackgroundFill¶

Added in version 21.2.

Bases: telegram.TelegramObject

Base class for Telegram BackgroundFill Objects. It can be one of:

telegram.BackgroundFillSolid

telegram.BackgroundFillGradient

telegram.BackgroundFillFreeformGradient

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their type is equal.

telegram.BackgroundTypeFill.fill

telegram.BackgroundTypePattern.fill

Added in version 21.2.

type (str) – Type of the background fill. Can be one of: SOLID, GRADIENT or FREEFORM_GRADIENT.

Type of the background fill. Can be one of: SOLID, GRADIENT or FREEFORM_GRADIENT.

telegram.constants.BackgroundFillType.FREEFORM_GRADIENT

telegram.constants.BackgroundFillType.GRADIENT

telegram.constants.BackgroundFillType.SOLID

See telegram.TelegramObject.de_json().

---

## BotName¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.botname.html

**Contents:**
- BotName¶

Bases: telegram.TelegramObject

This object represents the bot’s name.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their name is equal.

telegram.Bot.get_my_name()

Added in version 20.3.

name (str) – The bot’s name.

telegram.constants.BotNameLimit.MAX_NAME_LENGTH

---

## GeneralForumTopicUnhidden¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.generalforumtopicunhidden.html

**Contents:**
- GeneralForumTopicUnhidden¶

Bases: telegram.TelegramObject

This object represents a service message about General forum topic unhidden in the chat. Currently holds no information.

telegram.Message.general_forum_topic_unhidden

Added in version 20.0.

---

## InputChecklistTask¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.inputchecklisttask.html

**Contents:**
- InputChecklistTask¶

Bases: telegram.TelegramObject

Describes a task to add to a checklist.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal if their id is equal.

telegram.InputChecklist.tasks

Added in version 22.3.

id (int) – Unique identifier of the task; must be positive and unique among all task identifiers currently present in the checklist.

text (str) – Text of the task; 1-100 characters after entities parsing.

parse_mode (str, optional) – Mode for parsing entities. See telegram.constants.ParseMode and formatting options for more details.

text_entities (Sequence[telegram.MessageEntity], optional) – List of special entities that appear in the text, which can be specified instead of parse_mode. Currently, only bold, italic, underline, strikethrough, spoiler, and custom_emoji entities are allowed.

Unique identifier of the task; must be positive and unique among all task identifiers currently present in the checklist.

Text of the task; 1-100 characters after entities parsing.

Optional. Mode for parsing entities. See telegram.constants.ParseMode and formatting options for more details.

Optional. List of special entities that appear in the text, which can be specified instead of parse_mode. Currently, only bold, italic, underline, strikethrough, spoiler, and custom_emoji entities are allowed.

Sequence[telegram.MessageEntity]

---

## BusinessConnection¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.businessconnection.html

**Contents:**
- BusinessConnection¶

Bases: telegram.TelegramObject

Describes the connection of the bot with a business account.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal if their id, user, user_chat_id, date, rights, and is_enabled are equal.

telegram.Update.business_connection

telegram.Bot.get_business_connection()

Added in version 21.1.

Changed in version 22.1: Equality comparison now considers rights instead of can_reply.

Removed in version 22.3: Removed argument and attribute can_reply deprecated by API 9.0.

id (str) – Unique identifier of the business connection.

user (telegram.User) – Business account user that created the business connection.

user_chat_id (int) – Identifier of a private chat with the user who created the business connection.

date (datetime.datetime) – Date the connection was established in Unix time.

is_enabled (bool) – True, if the connection is active.

rights (BusinessBotRights, optional) – Rights of the business bot. Added in version 22.1.

Rights of the business bot.

Added in version 22.1.

Unique identifier of the business connection.

Business account user that created the business connection.

Identifier of a private chat with the user who created the business connection.

Date the connection was established in Unix time.

True, if the connection is active.

Optional. Rights of the business bot.

Added in version 22.1.

See telegram.TelegramObject.de_json().

---

## BotDescription¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.botdescription.html

**Contents:**
- BotDescription¶

Bases: telegram.TelegramObject

This object represents the bot’s description.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their description is equal.

telegram.Bot.get_my_description()

Added in version 20.2.

description (str) – The bot’s description.

The bot’s description.

---

## Available Types¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.at-tree.html

**Contents:**
- Available Types¶

---

## BotCommand¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.botcommand.html

**Contents:**
- BotCommand¶

Bases: telegram.TelegramObject

This object represents a bot command.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their command and description are equal.

telegram.Bot.set_my_commands()

telegram.Bot.get_my_commands()

command (str) – Text of the command; 1- 32 characters. Can contain only lowercase English letters, digits and underscores.

description (str) – Description of the command; 1- 256 characters.

Text of the command; 1- 32 characters. Can contain only lowercase English letters, digits and underscores.

Description of the command; 1- 256 characters.

telegram.constants.BotCommandLimit.MAX_COMMAND

Added in version 20.0.

telegram.constants.BotCommandLimit.MAX_DESCRIPTION

Added in version 20.0.

telegram.constants.BotCommandLimit.MIN_COMMAND

Added in version 20.0.

telegram.constants.BotCommandLimit.MIN_DESCRIPTION

Added in version 20.0.

---

## BackgroundFillGradient¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.backgroundfillgradient.html

**Contents:**
- BackgroundFillGradient¶

Added in version 21.2.

Bases: telegram.BackgroundFill

The background is a gradient fill.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their top_color, bottom_color and rotation_angle are equal.

telegram.BackgroundTypeFill.fill

telegram.BackgroundTypePattern.fill

Added in version 21.2.

top_color (int) – Top color of the gradient in the RGB24 format.

bottom_color (int) – Bottom color of the gradient in the RGB24 format.

rotation_angle (int) – Clockwise rotation angle of the background fill in degrees; 0-359.

Type of the background fill. Always GRADIENT.

Top color of the gradient in the RGB24 format.

Bottom color of the gradient in the RGB24 format.

Clockwise rotation angle of the background fill in degrees; 0-359.

---

## ExternalReplyInfo¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.externalreplyinfo.html

**Contents:**
- ExternalReplyInfo¶

Bases: telegram.TelegramObject

This object contains information about a message that is being replied to, which may come from another chat or forum topic.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their origin is equal.

telegram.Message.external_reply

Added in version 20.8.

origin (telegram.MessageOrigin) – Origin of the message replied to by the given message.

chat (telegram.Chat, optional) – Chat the original message belongs to. Available only if the chat is a supergroup or a channel.

message_id (int, optional) – Unique message identifier inside the original chat. Available only if the original chat is a supergroup or a channel.

link_preview_options (telegram.LinkPreviewOptions, optional) – Options used for link preview generation for the original message, if it is a text message

animation (telegram.Animation, optional) – Message is an animation, information about the animation.

audio (telegram.Audio, optional) – Message is an audio file, information about the file.

document (telegram.Document, optional) – Message is a general file, information about the file.

photo (Sequence[telegram.PhotoSize], optional) – Message is a photo, available sizes of the photo.

sticker (telegram.Sticker, optional) – Message is a sticker, information about the sticker.

story (telegram.Story, optional) – Message is a forwarded story.

video (telegram.Video, optional) – Message is a video, information about the video.

video_note (telegram.VideoNote, optional) – Message is a video note, information about the video message.

voice (telegram.Voice, optional) – Message is a voice message, information about the file.

has_media_spoiler (bool, optional) – True, if the message media is covered by a spoiler animation.

checklist (telegram.Checklist, optional) – Message is a checklist. Added in version 22.3.

Message is a checklist.

Added in version 22.3.

contact (telegram.Contact, optional) – Message is a shared contact, information about the contact.

dice (telegram.Dice, optional) – Message is a dice with random value.

game (telegram.Game. optional) – Message is a game, information about the game. More about games >>.

giveaway (telegram.Giveaway, optional) – Message is a scheduled giveaway, information about the giveaway.

giveaway_winners (telegram.GiveawayWinners, optional) – A giveaway with public winners was completed.

invoice (telegram.Invoice, optional) – Message is an invoice for a payment, information about the invoice. More about payments >>.

location (telegram.Location, optional) – Message is a shared location, information about the location.

poll (telegram.Poll, optional) – Message is a native poll, information about the poll.

venue (telegram.Venue, optional) – Message is a venue, information about the venue.

paid_media (telegram.PaidMedia, optional) – Message contains paid media; information about the paid media. Added in version 21.4.

Message contains paid media; information about the paid media.

Added in version 21.4.

Origin of the message replied to by the given message.

telegram.MessageOrigin

Optional. Chat the original message belongs to. Available only if the chat is a supergroup or a channel.

Optional. Unique message identifier inside the original chat. Available only if the original chat is a supergroup or a channel.

Optional. Options used for link preview generation for the original message, if it is a text message.

telegram.LinkPreviewOptions

Optional. Message is an animation, information about the animation.

Optional. Message is an audio file, information about the file.

Optional. Message is a general file, information about the file.

Optional. Message is a photo, available sizes of the photo.

tuple[telegram.PhotoSize]

Optional. Message is a sticker, information about the sticker.

Optional. Message is a forwarded story.

Optional. Message is a video, information about the video.

Optional. Message is a video note, information about the video message.

Optional. Message is a voice message, information about the file.

Optional. True, if the message media is covered by a spoiler animation.

Optional. Message is a checklist.

Added in version 22.3.

Optional. Message is a shared contact, information about the contact.

Optional. Message is a dice with random value.

Optional. Message is a game, information about the game. More about games >>.

Optional. Message is a scheduled giveaway, information about the giveaway.

Optional. A giveaway with public winners was completed.

telegram.GiveawayWinners

Optional. Message is an invoice for a payment, information about the invoice. More about payments >>.

Optional. Message is a shared location, information about the location.

Optional. Message is a native poll, information about the poll.

Optional. Message is a venue, information about the venue.

Optional. Message contains paid media; information about the paid media.

Added in version 21.4.

See telegram.TelegramObject.de_json().

---

## BotCommandScopeChatAdministrators¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.botcommandscopechatadministrators.html

**Contents:**
- BotCommandScopeChatAdministrators¶

Bases: telegram.BotCommandScope

Represents the scope of bot commands, covering all administrators of a specific group or supergroup chat.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their type and chat_id are equal.

telegram.Bot.delete_my_commands()

telegram.Bot.get_my_commands()

telegram.Bot.set_my_commands()

Added in version 13.7.

chat_id (str | int) – Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername).

Scope type 'chat_administrators'.

Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername).

---

## AcceptedGiftTypes¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.acceptedgifttypes.html

**Contents:**
- AcceptedGiftTypes¶

Bases: telegram.TelegramObject

This object describes the types of gifts that can be gifted to a user or a chat.

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal if their unlimited_gifts, limited_gifts, unique_gifts and premium_subscription are equal.

telegram.Bot.set_business_account_gift_settings()

telegram.ChatFullInfo.accepted_gift_types

Added in version 22.1.

unlimited_gifts (bool) – True, if unlimited regular gifts are accepted.

limited_gifts (bool) – True, if limited regular gifts are accepted.

unique_gifts (bool) – True, if unique gifts or gifts that can be upgraded to unique for free are accepted.

premium_subscription (bool) – True, if a Telegram Premium subscription is accepted.

True, if unlimited regular gifts are accepted.

True, if limited regular gifts are accepted.

True, if unique gifts or gifts that can be upgraded to unique for free are accepted.

True, if a Telegram Premium subscription is accepted.

---

## BotCommandScope¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.botcommandscope.html

**Contents:**
- BotCommandScope¶

Bases: telegram.TelegramObject

Base class for objects that represent the scope to which bot commands are applied. Currently, the following 7 scopes are supported:

telegram.BotCommandScopeDefault

telegram.BotCommandScopeAllPrivateChats

telegram.BotCommandScopeAllGroupChats

telegram.BotCommandScopeAllChatAdministrators

telegram.BotCommandScopeChat

telegram.BotCommandScopeChatAdministrators

telegram.BotCommandScopeChatMember

Objects of this class are comparable in terms of equality. Two objects of this class are considered equal, if their type is equal. For subclasses with additional attributes, the notion of equality is overridden.

Please see the official docs on how Telegram determines which commands to display.

telegram.Bot.delete_my_commands()

telegram.Bot.get_my_commands()

telegram.Bot.set_my_commands()

Added in version 13.7.

type (str) – Scope type.

telegram.constants.BotCommandScopeType.ALL_CHAT_ADMINISTRATORS

telegram.constants.BotCommandScopeType.ALL_GROUP_CHATS

telegram.constants.BotCommandScopeType.ALL_PRIVATE_CHATS

telegram.constants.BotCommandScopeType.CHAT

telegram.constants.BotCommandScopeType.CHAT_ADMINISTRATORS

telegram.constants.BotCommandScopeType.CHAT_MEMBER

telegram.constants.BotCommandScopeType.DEFAULT

Converts JSON data to the appropriate BotCommandScope object, i.e. takes care of selecting the correct subclass.

data (dict[str, …]) – The JSON data.

bot (telegram.Bot, optional) – The bot associated with this object. Defaults to None, in which case shortcut methods will not be available. Changed in version 21.4: bot is now optional and defaults to None

The bot associated with this object. Defaults to None, in which case shortcut methods will not be available.

Changed in version 21.4: bot is now optional and defaults to None

---

## InputMediaAudio¶

**URL:** https://docs.python-telegram-bot.org/en/stable/telegram.inputmediaaudio.html

**Contents:**
- InputMediaAudio¶

Bases: telegram.InputMedia

Represents an audio file to be treated as music to be sent.

Working with Files and Media

When using a telegram.Audio for the media attribute, it will take the duration, performer and title from that video, unless otherwise specified with the optional arguments.

telegram.Bot.edit_message_media()

telegram.Bot.send_media_group()

Changed in version 20.5: Removed the deprecated argument and attribute thumb.

media (str | file object | InputFile | bytes | pathlib.Path | telegram.Audio) – File to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one. To upload a file, you can either pass a file object (e.g. open("filename", "rb")) or the file contents as bytes. If the bot is running in local_mode, passing the path of the file (as string or pathlib.Path object) is supported as well. Lastly you can pass an existing telegram.Audio object to send. Changed in version 13.2: Accept bytes as input.

File to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one. To upload a file, you can either pass a file object (e.g. open("filename", "rb")) or the file contents as bytes. If the bot is running in local_mode, passing the path of the file (as string or pathlib.Path object) is supported as well. Lastly you can pass an existing telegram.Audio object to send.

Changed in version 13.2: Accept bytes as input.

filename (str, optional) – Custom file name for the audio, when uploading a new file. Convenience parameter, useful e.g. when sending files generated by the tempfile module. Added in version 13.1.

Custom file name for the audio, when uploading a new file. Convenience parameter, useful e.g. when sending files generated by the tempfile module.

Added in version 13.1.

caption (str, optional) – Caption of the audio to be sent, 0-1024 characters after entities parsing.

parse_mode (str, optional) – Mode for parsing entities. See telegram.constants.ParseMode and formatting options for more details.

caption_entities (Sequence[telegram.MessageEntity], optional) – Sequence of special entities that appear in the caption, which can be specified instead of parse_mode. Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list. The input is converted to a tuple.

Sequence of special entities that appear in the caption, which can be specified instead of parse_mode.

Changed in version 20.0: Accepts any collections.abc.Sequence as input instead of just a list. The input is converted to a tuple.

duration (int | datetime.timedelta, optional) – Duration of the audio in seconds as defined by the sender. Changed in version v22.2: datetime.timedelta objects are accepted in addition to plain int values.

Duration of the audio in seconds as defined by the sender.

Changed in version v22.2: datetime.timedelta objects are accepted in addition to plain int values.

performer (str, optional) – Performer of the audio as defined by the sender or by audio tags.

title (str, optional) – Title of the audio as defined by the sender or by audio tags.

thumbnail (file object | bytes | pathlib.Path | str, optional) – Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail’s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file. To upload a file, you can either pass a file object (e.g. open("filename", "rb")) or the file contents as bytes. If the bot is running in local_mode, passing the path of the file (as string or pathlib.Path object) is supported as well. Added in version 20.2.

Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail’s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file. To upload a file, you can either pass a file object (e.g. open("filename", "rb")) or the file contents as bytes. If the bot is running in local_mode, passing the path of the file (as string or pathlib.Path object) is supported as well.

Added in version 20.2.

str | telegram.InputFile

Optional. Caption of the audio to be sent, 0-1024 characters after entities parsing.

Optional. Mode for parsing entities. See telegram.constants.ParseMode and formatting options for more details.

Optional. Tuple of special entities that appear in the caption, which can be specified instead of parse_mode.

Changed in version 20.0:

This attribute is now an immutable tuple.

This attribute is now always a tuple, that may be empty.

tuple[telegram.MessageEntity]

Optional. Duration of the audio in seconds.

Deprecated since version v22.2: In a future major version this attribute will be of type datetime.timedelta. You can opt-in early by setting PTB_TIMEDELTA=true or PTB_TIMEDELTA=1 as an environment variable.

int | datetime.timedelta

Optional. Performer of the audio as defined by the sender or by audio tags.

Optional. Title of the audio as defined by the sender or by audio tags.

Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail’s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file.

Added in version 20.2.

---
