import discord
from discord.ext import commands
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline, set_seed

TOKEN = "---YOUR TOKEN---"
CLIENT_SECRET = "---YOUR CLIENT TOKEN---"
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
bot = commands.Bot(
    command_prefix="$", # $コマンド名　でコマンドを実行できるようになる
    case_insensitive=True, # 大文字小文字を区別しない ($hello も $Hello も同じ!)
    intents=intents # 権限を設定
)
MNAME = "rinna/youri-7b"
tokenizer = AutoTokenizer.from_pretrained(MNAME, padding=True, truncation=True, max_length=50, add_special_tokens = True)
generator = pipeline(
    "text-generation", model=MNAME, tokenizer=tokenizer, device=0, max_new_tokens=1024, torch_dtype=torch.float16, temperature=0.3, repetition_penalty=1
)


@bot.command(name="chat", description="LLM return utterance")
async def chat(ctx: commands.Context, prompt:str) -> None:
    prompt = f"ユーザー: 「{prompt}」\nシステム: "
    ###ここにLLMの生成を書く
    generated = generator(prompt)
    await ctx.send(generated)

bot.run(TOKEN)