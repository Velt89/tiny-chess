import json,urllib.request as u
V=dict(zip('PNBRQKpnbrqk',(100,320,330,500,1000,0)*2))
S=('::::DDDD@@@@=>>=<==<;<<;;;;;::::','468668:88:<<8;=<8;=<8:<;69::2667','68888:::8:;:9;<;9<<;9;;98;:86888','::::<==<:;;::;;::::::::::;;:::;:','89999:::9:;:::;::;;:9:;:9:::8999','022222224444666688889999<=:=>@:@')
E={}
for p,t in zip('PNBRQK',S):
 e=[0]*128
 for i,c in enumerate(t):j=i//4*16+i%4;e[j]=e[j^7]=ord(c)*5-290
 E[p]=e
BD=(15,17,-15,-17);RD=(1,16,-1,-16);KG=BD+RD;KN=(14,18,31,33,-14,-18,-31,-33)
RK={118:(119,117),114:(112,115),6:(7,5),2:(0,3)}
CR={112:2,119:1,0:8,7:4,116:3,4:12}
U=[];TT={}
def atk(s,w):
 pn,nt,kg=('pnk','PNK')[w]
 for ds,ws in((KN,nt),(KG,kg),(BD,('bq','BQ')[w]),(RD,('rq','RQ')[w]),(((-15,-17),(15,17))[w],pn)):
  for d in ds:
   t=s
   while 1:
    t+=d
    if t&136 or B[t]!='.'or len(ws)<2:break
   if not t&136 and B[t]in ws:return 1
def gen(c=0):
 ms=[];A=ms.append
 for s in range(128):
  p=B[s]
  if p=='.'or p.isupper()!=W:continue
  v=p.upper()
  if v=='P':
   d=16-32*W;r=s>>4;pr=6-5*W;t=s+d
   if B[t]=='.':
    if r==pr or not c:A(s|t<<7|(r==pr)<<16)
    if r==7-pr and not c and B[s+2*d]=='.':A(s|s+2*d<<7)
   for t in(s+d-1,s+d+1):
    if not t&136 and B[t]!='.'and B[t].isupper()!=W:A(s|t<<7|(r==pr)<<16)
  else:
   for d in(KN,BD,RD,KG,KG)['NBRQK'.index(v)]:
    t=s+d
    while not t&136:
     q=B[t]
     if q!='.':
      if q.isupper()!=W:A(s|t<<7)
      break
     if not c:A(s|t<<7)
     if v in'NK':break
     t+=d
   if v=='K'and not c:
    h=116 if W else 4
    for bit,emp in((1,(h+1,h+2)),(2,(h-1,h-2,h-3))):
     if s==h and C&bit<<(2-2*W)and all(B[x]=='.'for x in emp)and not any(atk(x,not W)for x in(s,emp[0])):A(s|emp[1]<<7)
 return ms
def mk(m):
 global W,C,U
 f=m&127;t=m>>7&127;p=B[f]
 U+=[(m,B[t],C)]
 B[t]='Qq'[p>'a']if m>>14 else p
 B[f]='.'
 if p in'Kk':
  K[p>'Z']=t
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
def se(d,a,b,y):
 global ND,TM,W
 ND+=1
 if ND>9e4:raise StopIteration
 if d<=0:
  if chk():d=1
  else:
   st=0
   for q in range(128):
    p=B[q]
    if p!='.':
     v=p.upper();x=V[v]+E[v][q^(p>'a')*112];st+=x if p<'a'else-x
   st*=2*W-1
   if st>=b:return b
   a=max(a,st)
 pv=-1
 if d>0:
  h=(str(B),C,W);e=TT.get(h)
  if e:
   pv=e[3]
   if e[0]>=d:
    if e[2]==1:a=max(a,e[1])
    else:b=min(b,e[1])
    if a>=b:return e[1]
 if d>2 and not chk()and sum(map(B.count,'NBRQnbrq'))>2:
  W=not W;sc=-se(d-3,-b,-b+1,y+1);W=not W
  if sc>=b:return b
 ms=sorted(gen(d<=0),key=lambda m:(m!=pv,-(16*V[x]-V[B[m&127]]//16)if(x:=B[m>>7&127])!='.'else 0))
 best=-1e9;bm=0
 for m in ms:
  if d<=0 and bm and st+V.get(B[m>>7&127],900)+150<a:continue
  mk(m)
  if atk(K[W],W):un();continue
  if d<=0 or not bm:sc=-se(d-1,-b,-a,y+1)
  else:
   sc=-se(d-1,-a-1,-a,y+1)
   if a<sc<b:sc=-se(d-1,-b,-a,y+1)
  un()
  if sc>best:best,bm=sc,m;TM=m if y==0 else TM
  a=max(a,sc)
  if a>=b:break
 if bm and d>0:TT[h]=(d,best,1 if best>=b else 2,bm)
 return a if d<=0 else best if bm else(-10**5+y if chk()else 0)
def bestmove(fen):
 global ND,BM,TM,B,W,C,K
 ps=fen.split();B=['.']*128;K=[0]*2;s=0
 for ch in ps[0]:
  if ch=='/':s+=8
  elif ch<'A':s+=int(ch)
  else:
   B[s]=ch
   if ch in'Kk':K[ch>'Z']=s
   s+=1
 W=ps[1]=='w';C=sum(1<<'KQkq'.index(c)for c in ps[2]if c in'KQkq')
 ND=0;TM=0;BM=gen()[0]
 if len(TT)>2e5:TT.clear()
 for d in range(64):
  try:se(d,-1e9,1e9,0)
  except StopIteration:break
  BM=TM or BM
 return chr(97+(BM&7))+str(8-(BM&127)//16)+chr(97+(BM>>7&7))+str(8-(BM>>7&127)//16)+('q'if BM>>14 else'')
post=lambda pa,bo:json.load(u.urlopen(u.os.getenv('MAKEFUN_ENV_URL')+pa,json.dumps(bo).encode()))
if __name__=='__main__':
 while 1:
  g=post('/game',{})
  if g['status']=='done':break
  while g['status']=='your_move':
   mv=bestmove(g['fen']);lm=g['legal_moves']
   if mv not in lm:mv=lm[0]
   g=post('/move',{'game':g['game'],'move':mv})
