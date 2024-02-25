import discord
import random
import requests
import os
from discord.ext import commands
cevre_kirliligi_cozum = [
    '-Su, kâğıt ve elektrik tüketimini bilinçli olarak yapmak ve bu konuda çevremizdeki insanları da uyarmak.',
    '-Çöplerimizi doğaya atmamak ve geri dönüşüm yapmak için kağıt, cam, plastik gibi atıkları ayrı toplama kutularına koymak.',
    '-Ekolojik farkındalığı artırmak ve çevreye duyarlı olmak için çevre konularında eğitimlere katılmak.',
    '-Sürdürülebilir enerji kaynaklarına yönelmek ve enerji tasarrufu yapmak.',
    '-Çevre dostu ulaşım yöntemlerini tercih etmek, örneğin bisiklet kullanmak veya toplu taşıma araçlarını kullanmak'
    ]
cevre_kirliligi = 'Çevre kirliliği, hava, su, toprak, gürültü ve görüntü gibi farklı yollarla doğal yaşam alanlarının insan etkisiyle bozulmasıdır. Fabrika emisyonları, araç egzozları, atık sular, kimyasal gübreler ve gürültü gibi etkenler çevre kirliliğine neden olur. Bu durum doğal dengenin bozulmasına ve canlıların sağlığını olumsuz etkilemesine yol açabilir.'

cevre_kirliligi_sebep = [
    '-Nüfus artışı: Hızlı nüfus artışı, ihtiyaç ve taleplerin artmasına ve dolayısıyla çevre sorunlarının artmasına neden olabilir.',
    '-Düzensiz şehirleşme: Plansız ve düzensiz şehirleşme, doğal yaşam alanlarının tahrip edilmesine ve çevre kirliliğinin artmasına yol açabilir.',
    '-Endüstrileşme: Plansız ve kontrolsüz endüstrileşme, fabrika emisyonları ve atık sular gibi etkenlerle çevre kirliliğini artırabilir.',
    '-Doğal kaynakların ölçüsüzce kullanılması: Doğal kaynakların aşırı kullanımı, ormanların tahrip edilmesi, su kaynaklarının tükenmesi ve toprak erozyonu gibi çevre kirliliği sorunlarına yol açabilir.',
    '-Kimyasal kullanımı: Kimyasal gübreler, tarım ilaçları ve endüstriyel kimyasallar gibi zararlı maddelerin kullanımı, su ve toprak kirliliğine neden olabilir.'
    ]    
cevre_kirliligi_sonuc = [
    '-Doğal yaşam alanlarının tahrip olması: Kirlilik, ormanların yok olması, su kaynaklarının kirlenmesi, toprak erozyonu gibi etkilerle doğal yaşam alanlarının tahrip olmasına neden olabilir. Bu durum, birçok canlı türünün yaşamını tehdit edebilir.',
    '-Ekosistem dengesinin bozulması: Çevre kirliliği, ekosistemlerdeki doğal dengeyi bozabilir. Kirlilik, bitki ve hayvan türlerinin yok olmasına, besin zincirinin etkilenmesine ve ekosistemlerin işlevselliğinin azalmasına yol açabilir.',
    '-İnsan sağlığına etkileri: Kirlilik, hava, su ve toprak kirliliği yoluyla insan sağlığını olumsuz etkileyebilir. Hava kirliliği solunum yolu hastalıklarına, su kirliliği su kaynaklarından bulaşan hastalıklara ve toprak kirliliği tarım ürünlerinin kalitesini düşürebilir. Ayrıca, kimyasal atıklar ve zararlı maddelerin maruz kalınması uzun vadede ciddi sağlık sorunlarına yol açabilir.',
    '-Ekonomik etkiler: Çevre kirliliği, ekonomi üzerinde de olumsuz etkilere sahip olabilir. Kirlilik, tarım üretimini azaltabilir, su kaynaklarının kullanımını kısıtlayabilir ve turizm sektörünü olumsuz etkileyebilir. Ayrıca, çevre kirliliğiyle mücadele ve temizlik çalışmaları da maliyetli olabilir.',
    '-İklim değişikliği: Çevre kirliliği, sera gazı emisyonları ve küresel ısınma gibi etkilerle iklim değişikliğine katkıda bulunabilir. Bu da dünya genelinde iklim koşullarının değişmesine ve doğal afetlerin artmasına neden olabilir.'
    ]
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


 
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def cevrekirliligi(ctx):
    await ctx.send(f'{cevre_kirliligi}')

@bot.command()
async def cevrekirliligicozum(ctx):
    random_cevre_kirliligi_cozum = random.choice (cevre_kirliligi_cozum)
    await ctx.send(f'{random_cevre_kirliligi_cozum}')   

@bot.command()
async def cevrekirliligisebep(ctx):
    random_cevre_kirliligi_sebep = random.choice (cevre_kirliligi_sebep)
    await ctx.send(f'{random_cevre_kirliligi_sebep}')   

@bot.command()
async def cevrekirliligisonuc(ctx):
    random_cevre_kirliligi_sonuc = random.choice (cevre_kirliligi_sonuc)
    await ctx.send(f'{random_cevre_kirliligi_sonuc}')

bot.run("MTIwMzc1Mjc3NzM3MzcxNjUxMA.GeG7sM.kh7cRB-gUQtzRQ8Ew9-7j7hVOzWymN3w4QFOB8")
