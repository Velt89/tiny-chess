import json,os,urllib.request as u
V=dict(zip('PNBRQKpnbrqk',(100,320,330,500,1000,0)*2))
S=('::::FFFF@@AB==>@;;<?;::=','024426:;4;<=4:=>4;=>4:<=26::0244',
'::::<<<<'+':'*22+';;','<<;;'*8)
E={}
for p,t in zip('PNBRQK',S[:2]+S[1:3]+S[2:]):
 e=[0]*128
 for i,c in enumerate(t):j=i//4*16+i%4;e[j]=e[j^7]=ord(c)*5-290
 E[p]=e
BD=(15,17,-15,-17);RD=(1,16,-1,-16);KG=BD+RD;KN=(14,18,31,33,-14,-18,-31,-33)
RK={118:(119,117),114:(112,115),6:(7,5),2:(0,3)}
CR={112:2,119:1,0:8,7:4}
SQ=[s for s in range(128)if s&136<1];U=[]
def atk(s,w):
 pn,nt,kg=('pnk','PNK')[w]
 for ds,ws in((KN,nt),(KG,kg),(BD,('bq','BQ')[w]),(RD,('rq','RQ')[w]),(((-15,-17),(15,17))[w],pn)):
  for d in ds:
   t=s+d
   while t&136<1:
    p=B[t]
    if p!='.':
     if p in ws:return 1
     break
    if len(ws)<2:break
    t+=d
 return 0
def gen(caps=0):
 ms=[];A=ms.append
 def add(s,t,pr):
  for pc in((0,),(4,))[pr]:A(s|t<<7|pc<<14)
 for s in SQ:
  p=B[s]
  if p=='.'or p.isupper()!=W:continue
  u=p.upper()
  if u=='P':
   d=16-32*W;r=s>>4;pr=6-5*W;t=s+d
   if B[t]=='.':
    if r==pr or not caps:add(s,t,r==pr)
    if r==7-pr and not caps and B[s+2*d]=='.':add(s,s+2*d,0)
   for t in(s+d-1,s+d+1):
    q=B[t]if t&136<1 else''
    if q not in'.'and q.isupper()!=W:add(s,t,r==pr)
  else:
   for d in(KN,BD,RD,KG,KG)['NBRQK'.index(u)]:
    t=s+d
    while t&136<1:
     q=B[t]
     if q=='.'and not caps:add(s,t,0)
     if q!='.'and q.isupper()!=W:add(s,t,0)
     if q!='.'or u in'NK':break
     t+=d
   if u=='K'and not caps:
    for bit,emp in((1,(117,118)),(2,(115,114,113)),(4,(5,6)),(8,(3,2,1))):
     if C&bit and(s==116)==(bit<4)and all(B[x]=='.'for x in emp)and not any(atk(x,not W)for x in(s,emp[0])):add(s,emp[1],0)
 return ms
def mk(m):
 global W,C,U
 f=m&127;t=m>>7&127;pc=m>>14;p=B[f]
 U+=[(m,B[t],C)]
 B[t]='Qq'[p>'a']if pc else p
 B[f]='.'
 if p in'Kk':
  K[p>'Z']=t;C&=(12,3)[p=='k']
  if abs(t-f)==2:
   a,b=RK[t];B[b]=B[a];B[a]='.'
 C&=~CR.get(f,0)&~CR.get(t,0)
 W=not W
def un():
 global W,C
 m,cap,C=U.pop();f=m&127;t=m>>7&127;p=B[t]
 if m>>14:p='P'if p<'a'else'p'
 B[f]=p;B[t]=cap
 if p in'Kk':
  K[p>'Z']=f
  if abs(t-f)==2:
   a,b=RK[t];B[a]=B[b];B[b]='.'
 W=not W
chk=lambda:atk(K[W<1],not W)
def se(d,a,b,ply):
 global ND,TM,W
 ND+=1
 if ND>9e4:raise StopIteration
 cap=pv=0
 if d<=0:
  if chk():d=1
  else:
   s=0
   for q in SQ:
    p=B[q]
    if p!='.':
     u=p.upper();v=V[u]+E[u][q if p<'a'else q^112];s+=v if p<'a'else-v
   st=s*(2*W-1)
   if st>=b:return b
   a=max(a,st)
   cap=True
 if d>0:
  h=(str(B),C,W);e=TT.get(h);pv=e[3]if e else-1
  if e and e[0]>=d:
   if e[2]:a,b=(max(a,e[1]),b)if e[2]==1 else(a,min(b,e[1]))
   if a>=b:return e[1]
 if d>2 and not chk()and sum(map(B.count,'NBRQnbrq'))>2:
  W=not W;sc=-se(d-3,-b,-b+1,ply+1);W=not W
  if sc>=b:return b
 ms=sorted(gen(cap),key=lambda m:-((9e8 if m==pv else 0)+(16*V[x]-V[B[m&127]]//16 if (x:=B[m>>7&127])!='.'else 0)));best,bm=-1e9,0
 for m in ms:
  if cap and bm and not m>>14 and st+V[B[m>>7&127]]+150<a:continue
  mk(m)
  if atk(K[W],W):un();continue
  sc=-se(d-1,-b,-a,ply+1);un()
  if sc>best:best,bm=sc,m;TM=m if ply==0 else TM
  a=max(a,sc)
  if a>=b:break
 if bm and d>0:TT[h]=(d,best,1 if best>=b else 2,bm)
 return a if cap else best if bm else(-100000+ply if chk()else 0)
def bestmove(fen):
 global ND,BM,TM,B,W,C,K,TT
 ps=fen.split();B=['.']*128;K=[0]*2;s=0
 for ch in ps[0]:
  if ch=='/':s+=8
  elif ch<'A':s+=int(ch)
  else:
   B[s]=ch
   if ch in'Kk':K[ch>'Z']=s
   s+=1
 W=ps[1]=='w';C=sum(1<<'KQkq'.index(c)for c in ps[2]if c in'KQkq')
 ND=0;BM=gen()[0];TT={}
 for d in range(64):
  TM=None
  try:se(d,-1e9,1e9,0)
  except StopIteration:break
  BM=TM or BM
 m=BM;f=m&127;t=m>>7&127
 s=f"{chr(97+(f&7))}{8-f//16}{chr(97+(t&7))}{8-t//16}"
 return s+('q'if m>>14 else'')
def post(pa,bo):return json.load(u.urlopen(os.getenv('MAKEFUN_ENV_URL')+pa,json.dumps(bo).encode()))
if __name__=='__main__':
 while 1:
  g=post('/game',{})
  if g['status']=='done':break
  while g['status']=='your_move':
   mv=bestmove(g['fen']);lm=g['legal_moves']
   if mv not in lm:mv=lm[0]
   g=post('/move',{'game':g['game'],'move':mv})
