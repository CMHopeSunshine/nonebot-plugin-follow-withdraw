import asyncio
from typing import Any, List, Optional

from nonebot import on_notice
from nonebot.adapters import Bot
from nonebot.typing import T_State
from nonebot.plugin import PluginMetadata
from nonebot.internal.matcher import current_event

from . import adapters as adapters_module
from .config import Config, withdraw_config
from .model import FollowMessage, save_message
from .adapter import (
    check_event,
    get_message,
    check_allow_api,
    withdraw_message,
    get_origin_message,
)

__plugin_meta__ = PluginMetadata(
    name="follow_withdraw",
    description="当命令消息被撤回时，Bot跟随撤回命令结果",
    usage="被动跟随消息并撤回",
    type="application",
    homepage="https://github.com/CMHopeSunshine/nonebot-plugin-follow-withdraw",
    config=Config,
    supported_adapters={
        "~onebot.v11",
        "~onebot.v12",
        "~qqguild",
        "~discord",
        "~kaiheila",
    },
)


withdraw_notice = on_notice(rule=check_event)


@withdraw_notice.handle()
async def handle_withdraw(bot: Bot, state: T_State):
    messages: Optional[List[FollowMessage]] = state.get("follow_messages")
    print("messages", messages)
    if messages:
        for message in messages:
            await withdraw_message(bot.adapter.get_name(), bot, message)
            if not withdraw_config.folow_withdraw_all:
                return
            await asyncio.sleep(withdraw_config.folow_withdraw_interval)


@Bot.on_called_api
async def handle_save_message(
    bot: Bot, exception: Optional[Exception], api: str, data: Any, result: Any
):
    if exception:
        return
    if bot.self_id in withdraw_config.folow_withdraw_bot_blacklist:
        return False
    adapter_name = bot.adapter.get_name()
    if adapter_name not in withdraw_config.folow_withdraw_enable_adapters:
        return
    if not check_allow_api(adapter_name, api):
        return

    event = current_event.get()
    if (message := get_message(result, adapter_name)) and (
        origin_message := get_origin_message(event, adapter_name)
    ):
        await save_message(adapter_name, origin_message, message)
