from pyrogram import Client, filters
import re

gas = Client(
  "justGASBot"
)

@gas.on_message(
  filters.command('check')
  )
def check(bot, ctx):
  try:
   msg = ctx
   if msg.chat.type == 'private':
       return False
   if msg.reply_to_message:
     if msg.reply_to_message.sender_chat != None:
       return ctx.reply_text("User yg anda ingin ketahui mungkin admin anonim atau apalah :v")
     hasil = msg.reply_to_message.from_user.id
     if bool(hasil)==True:
       init = ctx.chat.get_member(hasil)
       uname = init.user.username 
       if uname == None:
        uname = "Tidak ada"
       elif uname != None:
        uname = "@"+uname
       pesan = f"Username : {uname}"
       pesan += f"\nStatus : {init.status}"
       pesan += f"\nId : <code>{init.user.id}</code>"
       pesan += f"\nIs_bot : {init.user.is_bot}"
       pesan += f"\nDC Id : <code>{init.user.dc_id}</code>"
       ctx.reply_text(pesan, parse_mode="HTML")
  except Exception as err:
    ctx.reply_text(f"`{err}`", quote=True)

@gas.on_message(
  filters.command('debugs')
  )
def debugs(bot, ctx):
  try:
    msg = ctx
    if msg.reply_to_message:
      ctx.reply_text(msg.reply_to_message)
  except Exception as e:
    ctx.reply_text(f"`{e}`", quote=True)
    
@gas.on_message(
  filters.regex(r"(^\/eval)")
)
async def membuat_eval(bot, ctx):
  try:
    msg = ctx
    coba = re.search(r"(^\/eval)", msg.text)
    idku = msg.from_user.id
    ngeval = msg.text.replace(coba.group(1), '')
    if idku != 1349919799:
      return await ctx.reply_text("Anda tidak diijinkan menggunakan command ini", quote=True)
    meval = str(await eval(ngeval))
    if(meval != None):
      if isinstance(meval, str):
         await ctx.reply_text(f"`Eval berhasil dijalankan\nStatus : Success`")
      
  except Exception as err:
    await ctx.reply_text(f"`Eval berhasil dijalankan\nStatus : Error\nErr Msg : {err}`", quote=True)

gas.run()
