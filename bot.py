import os
from dotenv import load_dotenv

import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.reactions = True  # ⚠️ 必須開啟反應意圖

load_dotenv()

bot = commands.Bot(command_prefix="!", intents=intents)

# 儲存 Stellar 成員警告次數的字典
warning_records = {}

# ==================== 🛠️ 車隊重要參數設定 ====================

GUILD_ID = 1514176525862305853
STELLAR_ROLE_ID = 1514181827986722826
STELLAR_COUNT_CHANNEL_ID = 1514290979497050265


# 1. 請填入你複製的 Stellar 隊員身分組 ID
STELLAR_ROLE_ID = 1514181827986722826

# 2. 請填入你希望隊員點擊的 Emoji（可以是內建 Emoji 像是 "⭐"、"✅"、"👍"）
TRIGGER_EMOJI = "⭐"

SEPARATOR_ROLES = {
    "🌟": 1514300231079035121,
    "🎭": 1514283082545631463,
    "💖": 1514283156100874331,
}

SEPARATOR_NAMES = {
    "🌟": "功能身分組分隔線",
    "🎭": "推團身分組分隔線",
    "💖": "推角身分組分隔線",
}

FACTION_ROLES = {
    "<:leo_need:1514195080649511004>": 1514214161570332774,  # Leo/need 推 的身分組 ID
    "<:More_More_Jump:1514195322434359336>": 1514214345427652659,  # MORE MORE JUMP! 推 的身分組 ID
    "<:Vivid_Bad_Squad:1514195717122428979>": 1514214450045911161,  # Vivid BAD SQUAD 推 的身分組 ID
    "<:Wonderlands_Showtime:1514195470782562355>": 1514214636608688168,  # Wonderlands×Showtime 推 的身分組 ID
    "<:25_Nightcord:1514196473334595595>": 1514214716237414411,  # 25點，Nightcord見。 推 的身分組 ID
    "<:Visual_Singer:1514196119452909630>": 1514214955057152010,  # VIRTUAL SINGER 推 的身分組 ID
}

FACTION_NAMES = {
    "<:leo_need:1514195080649511004>": "Leo/need",
    "<:More_More_Jump:1514195322434359336>": "MORE MORE JUMP!",
    "<:Vivid_Bad_Squad:1514195717122428979>": "Vivid BAD Squad",
    "<:Wonderlands_Showtime:1514195470782562355>": "Wonderlands×Showtime",
    "<:25_Nightcord:1514196473334595595>": "25時，在Nightcord。",
    "<:Visual_Singer:1514196119452909630>": "Virtual Singer",
}

LEO_NEED_ROLES = {
    "<:Leo_Need_ichika:1514235952225325176>": 1514257393179955312,
    "<:Leo_Need_saki:1514236452517707796>": 1514257170693230672,
    "<:Leo_Need_honami:1514236064292798524>": 1514257706372825198,
    "<:Leo_Need_shiho:1514237806858207444>": 1514257975693410475,
}

MMJ_ROLES = {
    "<:minori:1514242015167250462>": 1514258158594560092,
    "<:haruka:1514272091904671764>": 1514258364832415906,
    "<:airi:1514241550798815344>": 1514258595657814169,
    "<:shizuku:1514272448286031872>": 1514259208022003752,
}

VBS_ROLES = {
    "<:kohane:1514242951629373522>": 1514260667731935323,
    "<:An:1514243084253134929>": 1514260666872107118,
    "<:Akito:1514242815586992250>": 1514260668482584638,
    "<:toya:1514242855260917860>": 1514260669233500371,
}

WS_ROLES = {
    "<:Tsukasa:1514242391169830962>": 1514259210433462493,
    "<:emu:1514242462707879957>": 1514260219914621072,
    "<:Nene:1514242539320774827>": 1514260323635564635,
    "<:rei:1514242692136173664>": 1514260496973430964,
}

NightAt25_ROLES = {
    "<:kanade:1514243311777484961>": 1514260802453115011,
    "<:mafuyu:1514243493831245904>": 1514260825441829019,
    "<:Ena:1514243608545329224>": 1514260825626640445,
    "<:mizuki:1514243684164435973>": 1514260825832161350,
}

VS_ROLES = {
    "<:Miku:1514244024427483327>": 1514262161361207366,
    "<:Rin:1514244112478638160>": 1514262162431021066,
    "<:Len:1514244067607842916>": 1514262162695127140,
    "<:luka:1514244212806127766>": 1514262164364464139,
    "<:meiko:1514244257152630965>": 1514262165086015518,
    "<:KAITO:1514244167042072636>": 1514262166348501002,
}

ALL_GROUPS = [
    LEO_NEED_ROLES,
    MMJ_ROLES,
    VBS_ROLES,
    WS_ROLES,
    NightAt25_ROLES,
    VS_ROLES,
]

# ==========================================================
@bot.event
async def on_ready():
    print(f"========================================")
    print(f"🌟 【Stellar】車隊中控機器人已成功啟動！")
    print(f"========================================")
    await bot.change_presence(
        activity=discord.Game(name="✨ 巡邏中 | 守護 Stellar 車隊秩序")
    )
    # 同步斜線指令
    await bot.tree.sync()


# ------------------ 指令：發送精美規章卡片 ------------------
@bot.tree.command(name="發送車隊規章", description="在當前頻道發送 Stellar 車隊規範")
@app_commands.checks.has_permissions(administrator=True)
async def send_rules(interaction: discord.Interaction):

    embed = discord.Embed(
        title="🌟 Stellar 車隊｜團隊規範 🌟",
        description=(
            "歡迎來到 **Stellar**！\n"
            "為了維持良好的交流環境、穩定的推車品質與公平的衝榜秩序，"
            "請所有成員、跑者與推車手務必遵守以下規範。"
        ),
        color=0xF1C40F,
    )

    embed.add_field(
        name="📌 一、社交與言論規範",
        value=(
            "1. 禁止辱罵、人身攻擊、引戰言論，以及惡意批評遊戲角色。\n"
            "2. 成員之間若發生糾紛，請尋求管理員協助，或私下理性溝通處理。\n"
            "3. 討論任何話題請保持理性；若爭議話題演變為罵戰，勸導無效者將記警告一次。\n"
            "4. 禁止歧視、貼標籤，或以有色眼光對待其他成員。\n"
            "5. 禁止未經允許宣傳頻道、要求贊助、發布商業廣告；如有需求請先詢問管理員。\n"
            "6. 禁止在群組內討論其他車隊或其他私人群組，官方或大群相關討論不在此限。"
        ),
        inline=False,
    )

    embed.add_field(
        name="💬 二、頻道使用與防雷規範",
        value=(
            "7. 禁止在刷屏區以外的頻道重複發送無意義或大量相同訊息；違者視為刷屏，記警告一次。\n"
            "8. 禁止開黃腔或討論 18 禁話題。\n"
            "9. 拆包／洩漏資訊請在領取對應身分組後，於專屬區域討論；禁止在指定區域外提及相關內容。\n"
            "10. 曬卡請至指定的【曬卡頻道】。\n"
            "11. 在指定的【劇情頻道】以外提及劇情內容時，請使用防雷標記；主線劇情與區域對話不在此限。"
        ),
        inline=False,
    )

    embed.add_field(
        name="🚨 三、官方違規與誠信條款",
        value=(
            "12. 嚴禁騷擾其他成員，包括但不限於私訊轟炸、性騷擾、惡意暱稱或任何使他人感到不適的行為；"
            "經投訴並查證屬實者，將立即移出群組。\n"
            "13. 本群嚴禁代打、輪班、共用帳號、外掛、腳本等官方明確禁止的行為；經查證屬實者，將直接移出群組。"
        ),
        inline=False,
    )

    embed.add_field(
        name="🔥 四、Stellar 衝榜士氣維護",
        value=(
            "14. 活動期間請勿做出損害車隊士氣的行為或言論，包括但不限於：辱罵跑者、辱罵推車手、"
            "刻意貶低本車隊、公開鼓吹他人選擇對面陣營、公開要求他人支援群外跑者等。\n"
            "⚠️ **處分**：初犯口頭警告；累犯可能禁言1~3天；情節嚴重者記警告一次。"
        ),
        inline=False,
    )

    embed.add_field(
        name="📎 五、處分規則",
        value=(
            "15. 違反以上規範者，將依情節輕重給予提醒、警告、禁言或移出群組等處分。\n"
            "16. 累積三次警告者，將直接移出群組。"
        ),
        inline=False,
    )

    embed.set_footer(text="Stellar 管理團隊保留規範解釋與最終處分權。")

    await interaction.response.send_message(content="@everyone", embed=embed)


# ------------------ 指令：發送推團卡片 ------------------
@bot.tree.command(name="發送推團選擇", description="在當前頻道發送推團身分組領取訊息")
@app_commands.checks.has_permissions(administrator=True)
async def send_faction_msg(interaction: discord.Interaction):
    await interaction.response.defer(ephemeral=True)

    description_text = (
        "請點擊下方對應的團體貼圖，領取你的推團身分組！\n"
        "可以同時選擇多個推團，也可以取消反應來移除身分組。\n\n"
    )

    for emoji_code in FACTION_ROLES.keys():
        faction_name = FACTION_NAMES[emoji_code]
        description_text += f"{emoji_code} ┃ 點擊領取 {faction_name} 身分組\n"

    embed = discord.Embed(
        title="🎭 【Stellar】成員推團認領 🎭",
        description=description_text,
        color=0x9B59B6,
    )

    msg = await interaction.channel.send(embed=embed)

    for emoji_code in FACTION_ROLES.keys():
        try:
            emoji = discord.PartialEmoji.from_str(emoji_code)
            await msg.add_reaction(emoji)
        except Exception as e:
            print(f"貼反應失敗: {emoji_code}, 錯誤: {e}")

    await interaction.followup.send("推團選擇訊息已建立完成。", ephemeral=True)
# ------------------ 指令：車隊成員 ------------------
@bot.tree.command(name="發送車隊成員領取", description="在當前頻道發送車隊成員身分組領取訊息")
@app_commands.checks.has_permissions(administrator=True)
async def send_member_role_msg(interaction: discord.Interaction):
    embed = discord.Embed(
        title="⭐ 【Stellar】車隊成員認證 ⭐",
        description=(
            "請點擊下方 ⭐ 反應，領取 Stellar 車隊成員身分組。\n"
            "領取後即可查看車隊成員專屬頻道。"
        ),
        color=0xF1C40F,
    )

    await interaction.response.send_message(embed=embed)
    original_msg = await interaction.original_response()
    await original_msg.add_reaction(TRIGGER_EMOJI)

# ------------------ 監聽：玩家「按」Emoji ------------------
@bot.event
async def on_raw_reaction_add(payload):
    if payload.user_id == bot.user.id:
        return

    guild = bot.get_guild(payload.guild_id)
    if guild is None:
        return

    member = guild.get_member(payload.user_id)
    if member is None:
        member = await guild.fetch_member(payload.user_id)

    emoji_name = payload.emoji.name

    # ⭐ 車隊成員身分組：只給，不管移除
    if emoji_name == TRIGGER_EMOJI:
        role = guild.get_role(STELLAR_ROLE_ID)
        if role and role not in member.roles:
            await member.add_roles(role)
            await update_stellar_count(guild)
            print(f"🟢 [身分組發放] 已為 {member.name} 加上 {role.name}")
        return

    # ✨ 分隔線身分組
    for emoji_code, role_id in SEPARATOR_ROLES.items():
        if emoji_name == emoji_code:
            role = guild.get_role(role_id)
            if role and role not in member.roles:
                await member.add_roles(role)
                print(f"✨ 已為 {member.name} 加上分隔線：{role.name}")
            return

    # 推團身分組
    for emoji_code, role_id in FACTION_ROLES.items():
        if f":{emoji_name}:" in emoji_code:
            role = guild.get_role(role_id)
            if role and role not in member.roles:
                await member.add_roles(role)
                print(f"🔮 已為 {member.name} 加上推團：{role.name}")
            return
        
    # 💖 推角身分組
    for role_dict in ALL_GROUPS:
        for emoji_code, role_id in role_dict.items():
            if f":{emoji_name}:" in emoji_code:
                role = guild.get_role(role_id)
                if role and role not in member.roles:
                    await member.add_roles(role)
                    print(f"💖 [推角] 已為 {member.name} 加上 {role.name}")
                return


# ------------------ 監聽：玩家「取消」Emoji ------------------
@bot.event
async def on_raw_reaction_remove(payload):
    guild = bot.get_guild(payload.guild_id)
    if guild is None:
        return

    member = guild.get_member(payload.user_id)
    if member is None:
        member = await guild.fetch_member(payload.user_id)

    # ✨ 分隔線身分組：取消反應就移除
    for emoji_code, role_id in SEPARATOR_ROLES.items():
        if emoji_name == emoji_code:
            role = guild.get_role(role_id)
            if role and role in member.roles:
                await member.remove_roles(role)
                print(f"✨ 已為 {member.name} 移除分隔線：{role.name}")
            return

    # 推團身份組移除
    emoji_name = payload.emoji.name

    # ⭐ 取消星星時，不移除車隊成員
    if emoji_name == TRIGGER_EMOJI:
        return

    # 推團身分組：取消反應就移除
    for emoji_code, role_id in FACTION_ROLES.items():
        if f":{emoji_name}:" in emoji_code:
            role = guild.get_role(role_id)
            if role and role in member.roles:
                await member.remove_roles(role)
                print(f"🔮 已為 {member.name} 移除推團：{role.name}")
            return
        
    # 💖 推角身分組：取消反應就移除
    for role_dict in ALL_GROUPS:
        for emoji_code, role_id in role_dict.items():
            if f":{emoji_name}:" in emoji_code:
                role = guild.get_role(role_id)
                if role and role in member.roles:
                    await member.remove_roles(role)
                    print(f"💖 [推角] 已為 {member.name} 移除 {role.name}")
                return
# ------------------ 功能三：管理員警告系統 (維持不變) ------------------
@bot.command(name="警告")
@commands.has_permissions(manage_messages=True)
async def give_warning(ctx, member: discord.Member):
    member_id = member.id
    warning_records[member_id] = warning_records.get(member_id, 0) + 1
    current_warns = warning_records[member_id]

    if current_warns >= 3:
        await ctx.send(
            f"🚨 {member.mention} 已累積第 **{current_warns}** 次警告！已達規章上限，請管理員立即執行剔除處分。"
        )
    else:
        await ctx.send(
            f"⚠️ {member.mention} 違反了 【Stellar】 車隊規範，已被記一次警告！當前累計警告：**{current_warns}/3** 次。"
        )

# ------------------ 指令：發送推團卡片 ------------------
@bot.tree.command(name="setup_character_roles", description="建立推角反應身分組")
async def setup_character_roles(interaction: discord.Interaction):
    await interaction.response.send_message("正在建立推角面板", ephemeral=True)

    panels = {
        "🎸 Leo/need 推角領取": LEO_NEED_ROLES,
        "🍀 MORE MORE JUMP! 推角領取": MMJ_ROLES,
        "🔥 Vivid BAD SQUAD 推角領取": VBS_ROLES,
        "🎪 Wonderlands×Showtime 推角領取": WS_ROLES,
        "🌙 25時，在Nightcord。推角領取": NightAt25_ROLES,
        "🎤 Virtual Singer 推角領取": VS_ROLES,
    }

    for title, role_dict in panels.items():
        msg = await interaction.channel.send(
            f"{title}\n請點擊下方表符領取推角身分組。"
        )

        for emoji in role_dict.keys():
            await msg.add_reaction(emoji)

@bot.tree.command(name="clear", description="清除指定數量的訊息")
async def clear(interaction: discord.Interaction, amount: int):
    if not interaction.user.guild_permissions.manage_messages:
        await interaction.response.send_message("你沒有管理訊息權限。", ephemeral=True)
        return

    await interaction.response.defer(ephemeral=True)

    deleted = await interaction.channel.purge(limit=amount)

    await interaction.followup.send(f"已清除 {len(deleted)} 則訊息。", ephemeral=True)

# =========================
# 歡迎頻道 ID
# =========================

WELCOME_CHANNEL_ID = 1514288972250222683  # 換成你的歡迎頻道 ID


# =========================
# 新成員加入通知
# =========================

@bot.event
async def on_member_join(member):

    channel = member.guild.get_channel(WELCOME_CHANNEL_ID)

    if channel is None:
        print("❌ 找不到歡迎頻道")
        return

    member_count = member.guild.member_count

    embed = discord.Embed(
        title="🌟 歡迎加入 Stellar！",
        description=(
            f"歡迎 {member.mention} 加入 **Stellar 車隊** ✨\n\n"
            "很高興你選擇加入我們！\n"
            "無論是聊天、推車、跑榜，還是單純享受《世界計畫》，"
            "都希望你能在這裡找到屬於自己的位置。"
        ),
        color=0xF1C40F
    )

    embed.add_field(
        name="📖 新成員必看",
        value=(
            "• 閱讀車隊規章\n"
            "• 領取車隊成員身分組\n"
            "• 領取推團身分組\n"
            "• 領取推角身分組"
        ),
        inline=False
    )

    embed.add_field(
        name="📊 目前伺服器成員數",
        value=f"**{member_count}** 人",
        inline=True
    )

    embed.add_field(
        name="🎵 關於 Stellar",
        value=(
            "一起推車、一起跑榜、一起享受世界計畫的樂趣！"
        ),
        inline=True
    )

    embed.set_thumbnail(url=member.display_avatar.url)

    embed.set_footer(
        text="願群星指引你的道路 ✨｜Stellar 管理團隊"
    )

    await channel.send(embed=embed)

async def update_stellar_count(guild):
    role = guild.get_role(STELLAR_ROLE_ID)
    channel = guild.get_channel(STELLAR_COUNT_CHANNEL_ID)

    if role is None:
        print("❌ 找不到車隊成員身分組")
        return

    if channel is None:
        print("❌ 找不到車隊成員統計頻道")
        return

    await channel.edit(
        name=f"🌟｜車隊成員：{len(role.members)}"
    )

    print(f"📊 車隊成員統計已更新：{len(role.members)} 人")

@bot.tree.command(name="發送分隔線領取", description="在當前頻道發送分隔線身分組領取訊息")
@app_commands.checks.has_permissions(administrator=True)
async def send_separator_roles(interaction: discord.Interaction):
    await interaction.response.defer(ephemeral=True)

    description_text = (
        "請點擊下方表符，領取對應的分隔線身分組。\n"
        "通常建議三個都領取，這樣個人身分組列表會比較整齊。\n\n"
    )

    for emoji_code in SEPARATOR_ROLES.keys():
        separator_name = SEPARATOR_NAMES[emoji_code]
        description_text += f"{emoji_code} ┃ 點擊領取 {separator_name}\n"

    embed = discord.Embed(
        title="✨ 【Stellar】分隔線身分組領取 ✨",
        description=description_text,
        color=0xFFFFFF,
    )

    msg = await interaction.channel.send(embed=embed)

    for emoji_code in SEPARATOR_ROLES.keys():
        await msg.add_reaction(emoji_code)

    await interaction.followup.send("分隔線領取訊息已建立完成。", ephemeral=True)

TOKEN = os.getenv("DISCORD_TOKEN")

bot.run(TOKEN)