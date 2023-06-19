<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-follow-withdraw

_✨ NoneBot2跟随撤回插件 ✨_

<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/CMHopeSunshine/nonebot-plugin-follow-withdraw.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-follow-withdraw">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-follow-withdraw.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">

</div>

## 📖 介绍

当触发命令的消息被撤回时，让Bot跟随撤回命令消息结果。

以内置插件`echo`为例：

- 你：`@bot /echo hello world`
- Bot：`hello world`

如果消息`@bot /echo hello world`被撤回了，那Bot将自动撤回它发出的`hello world`

## 💿 安装

在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

```shell
nb plugin install nonebot-plugin-follow-withdraw
```

## ☀ ️适配

现已支持以下适配器：

| 名称             | 测试 | 说明                         |
| ---------------- | ---- | ---------------------------- |
| OneBot(V11、V12) | ✔️    | -                            |
| QQ Guild         | ✔️    | -                            |
| Discord          | ✔️    | -                            |
| Kaiheila         | ❌    | 暂只支持频道消息，不支持私聊 |

部分适配器不支持消息撤回或无法接收消息撤回事件通知，无法支持。

## 🔧 ️配置

| 配置名                         | 默认值                                                       | 说明                                                         |
| ------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| follow_withdraw_all             | True                                                         | 为True时撤回所有(如果有多条)与该消息相关的消息，为False则是只撤回第一条 |
| follow_withdraw_interval        | 0.5                                                          | 多条消息时的撤回间隔(单位秒)，以防止一瞬间撤回过多消息导致风控( |
| follow_withdraw_enable_adapters | ["OneBot V11", "OneBot V12", "QQ Guild", "Discord", "Kaiheila"] | 启用的适配器类型列表，默认为所有已支持的适配器，可选值请看默认值 |
| follow_withdraw_bot_blacklist   | []                                                           | 不启用跟随撤回的Bot列表，填写Bot的bot_id                     |
| follow_withdraw_plugin_blacklist | [] | 不启用跟随撤回的插件列表 |

此外，本插件还提供了一个仅超级用户可使用的命令`清除消息记录`，来清除本插件记录的消息ID数据。