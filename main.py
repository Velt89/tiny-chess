import json,os,urllib.request as u
V={'P':100,'N':320,'B':330,'R':500,'Q':1000,'K':0}
S=('::::FFFF@@AB==>@;;<?;::=','024426:;4;<=4:=>4;=>4:<=26::0244',
'::::<<<<'+':'*22+';;','4220'*3+'64428666:<:8>><:>@<')
E={}
for p,t in zip('PNRK',S):
 e=[0]*128
 for i,c in enumerate(t):j=i//4*16+i%4;e[j]=e[j^7]=ord(c)*5-290
 E[p]=e
E['B']=E['N'];E['Q']=E['R']
BD=(15,17,-15,-17);RD=(1,16,-1,-16);KG=BD+RD;KN=(14,18,31,33,-14,-18,-31,-33)
D=dict(N=KN,K=KG,Q=KG,B=BD,R=RD)
CT=((116,1,(117,118)),(116,2,(115,114,113)),(4,4,(5,6)),(4,8,(3,2,1)))
RK={118:(119,117),114:(112,115),6:(7,5),2:(0,3)}
CR={112:2,119:1,0:8,7:4}
SQ=[s for s in range(128)if not s&136]
def atk(s,w):
 pn,nt,kg='PNK'if w else'pnk'
 for ds,ws,sl in((KN,nt,0),(KG,kg,0),(BD,'BQ'if w else'bq',1),(RD,'RQ'if w else'rq',1)):
  for d in ds:
   t=s+d
   while not t&136:
    p=B[t]
    if p!='.':
     if p in ws or(p==pn and d in(BD[:2]if w else BD[2:])and t==s+d):return 1
     break
    if not sl:break
    t+=d
 return 0
def gen(caps=False):
 ms=[];w=W;A=ms.append
 def add(s,t,pr):
  for pc in(range(1,5)if pr else(0,)):A(s|t<<7|pc<<14)
 for s in SQ:
  p=B[s]
  if p=='.'or p.isupper()!=w:continue
  u=p.upper()
  if u=='P':
   d=-16 if w else 16;r=s>>4;pr,sr=(1,6)if w else(6,1);t=s+d
   if B[t]=='.':
    if r==pr or not caps:add(s,t,r==pr)
    if r==sr and not caps and B[s+2*d]=='.':add(s,s+2*d,False)
   for t in(s+d-1,s+d+1):
    if t&136:continue
    q=B[t]
    if q!='.'and q.isupper()!=w:add(s,t,r==pr)
  else:
   for d in D[u]:
    t=s+d
    while not t&136:
     q=B[t]
     if q!='.':
      if q.isupper()!=w:add(s,t,False)
      break
     if not caps:add(s,t,False)
     if u in'NK':break
     t+=d
   if u=='K'and not caps:
    for home,bit,emp in CT:
     if s==home and C&bit and all(B[x]=='.'for x in emp)and not any(atk(x,not w)for x in(home,emp[0])):add(s,emp[1],False)
 return ms
def mk(m):
 global W,C
 f=m&127;t=m>>7&127;pc=m>>14;p=B[f]
 U.append((m,B[t],C))
 B[t]='NBRQnbrq'[pc-1+4*(p>'a')]if pc else p
 B[f]='.'
 if p in'Kk':
  K[p>'Z']=t;C&=12 if p=='K'else 3
  if abs(t-f)==2:
   a,b=RK[t];B[b]=B[a];B[a]='.'
 C&=~CR.get(f,0);C&=~CR.get(t,0)
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
def chk():return atk(K[0]if W else K[1],not W)
def se(d,a,b,ply):
 global ND,TM
 ND+=1
 if ND>4e4:raise StopIteration
 cap=False;pv=-1
 if d<=0:
  if chk():d=1
  else:
   s=0
   for q in SQ:
    p=B[q];u=p.upper()
    if p!='.':
     v=V[u]+E[u][q if p<'a'else q^112]
     s+=v if p<'a'else -v
   st=s if W else -s
   if st>=b:return b
   a=max(a,st)
   cap=True
 if d>0:
  h=''.join(B)+chr(C*2+W);pv=TT.get(h,-1)
 ms=sorted(gen(cap),key=lambda m:(9e8 if m==pv else 0)+(16*V[B[m>>7&127].upper()]-V[B[m&127].upper()]//16 if B[m>>7&127]!='.'else(9e5 if m>>14 else 0)),reverse=True);best=-1e9;bm=0
 for m in ms:
  mk(m)
  if atk(K[0]if not W else K[1],W):un();continue
  sc=-se(d-1,-b,-a,ply+1);un()
  if sc>best:
   best,bm=sc,m
   if ply==0:TM=m
  a=max(a,sc)
  if a>=b:break
 if cap:return a
 r=best if best>-1e8 else(-100000+ply if chk()else 0)
 if bm and d>0:TT[h]=bm
 return r
def bestmove(fen):
 global ND,BM,TM,B,W,C,K,U,TT
 ps=fen.split();B=['.']*128;K=[0,0];U=[];s=0
 for ch in ps[0]:
  if ch=='/':s+=8
  elif ch<'A':s+=int(ch)
  else:
   B[s]=ch
   if ch in'Kk':K[ch>'Z']=s
   s+=1
 W=ps[1]=='w';C=sum(1<<i for i,c in enumerate('KQkq')if c in ps[2])
 ND=0;BM=gen()[0];TT={}
 for d in range(64):
  TM=None
  try:se(d,-1e9,1e9,0)
  except StopIteration:break
  if TM:BM=TM
 m=BM;f=m&127;t=m>>7&127
 s=chr(97+(f&7))+str(8-f//16)+chr(97+(t&7))+str(8-t//16)
 return s+'nbrq'[(m>>14)-1]if m>>14 else s
def post(pa,bo):return json.load(u.urlopen(u.Request(os.getenv('MAKEFUN_ENV_URL')+pa,data=json.dumps(bo).encode())))
if __name__=='__main__':
 while 1:
  g=post('/game',{})
  if g['status']=='done':break
  while g['status']=='your_move':
   mv=bestmove(g['fen']);lm=g['legal_moves']
   if mv not in lm:mv=lm[0]
   g=post('/move',{'game':g['game'],'move':mv})